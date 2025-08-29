"""
core/context.py
Builds a tiny, cached "context pack" for the AI: schema, KPIs, trends, tops, anomalies.
Designed to be fast and bounded in size.
"""

from __future__ import annotations
import hashlib
from typing import Dict, Optional, Tuple, List
import pandas as pd

try:
    import streamlit as st
except Exception:  # streamlit optional for caching
    st = None


def _safe_cols(df: pd.DataFrame, *cols) -> List[str]:
    return [c for c in cols if c and c in df.columns]


def _df_signature(df: pd.DataFrame) -> str:
    """Stable signature to invalidate cache when data changes (shape + head bytes)."""
    try:
        head = df.head(50).to_csv(index=False).encode("utf-8", errors="ignore")
    except Exception:
        head = b""
    h = hashlib.sha256()
    h.update(str(df.shape).encode())
    h.update(head)
    return h.hexdigest()


def _format_money(x) -> str:
    try:
        return f"${float(x):,.0f}"
    except Exception:
        return str(x)


def _format_pct(x) -> str:
    try:
        return f"{float(x)*100:.1f}%"
    except Exception:
        return "—"


def _monthly(df: pd.DataFrame, date_col: str, amount_col: str) -> pd.DataFrame:
    d = df.copy()
    d[date_col] = pd.to_datetime(d[date_col], errors="coerce")
    d = d.dropna(subset=[date_col])
    d["month"] = d[date_col].dt.to_period("M").astype(str)
    g = d.groupby("month", as_index=False)[amount_col].sum().rename(columns={amount_col: "revenue"})
    return g.sort_values("month").reset_index(drop=True)


def _anomaly_last(trend: pd.DataFrame) -> Tuple[Optional[str], Optional[float]]:
    """Return (month, pct_change_vs_prev) for the last point (if possible)."""
    if not isinstance(trend, pd.DataFrame) or trend.shape[0] < 2:
        return None, None
    last = trend.iloc[-1]
    prev = trend.iloc[-2]
    m = str(last["month"])
    try:
        pc = (float(last["revenue"]) - float(prev["revenue"])) / max(1e-9, float(prev["revenue"]))
    except Exception:
        pc = None
    return m, pc


def _kv_line(k: str, v) -> str:
    return f"- {k}: **{v}**"


def _topn(df: pd.DataFrame, by_col: str, amount_col: str, n: int = 5) -> pd.DataFrame:
    g = df.groupby(by_col, as_index=False)[amount_col].sum().rename(columns={amount_col: "revenue"})
    return g.sort_values("revenue", ascending=False).head(n).reset_index(drop=True)


def _schema_snippet(df: pd.DataFrame, limit: int = 12) -> str:
    parts = []
    for i, c in enumerate(df.columns[:limit]):
        parts.append(f"- {c}: {str(df[c].dtype)}")
    if df.shape[1] > limit:
        parts.append(f"- … (+{df.shape[1]-limit} more)")
    return "\n".join(parts)


def _mk_context_markdown(
    kpis: Dict[str, float],
    trend_lines: List[str],
    top_products: Optional[pd.DataFrame],
    top_channels: Optional[pd.DataFrame],
    schema_md: str,
    anomaly_month: Optional[str],
    anomaly_pct: Optional[float],
    cap_lines: int = 12
) -> str:
    lines = []
    # KPIs
    lines.append("### KPIs")
    if kpis:
        if "total_sales" in kpis: lines.append(_kv_line("Total Sales", _format_money(kpis["total_sales"])))
        if "num_orders" in kpis: lines.append(_kv_line("Orders", f"{int(kpis['num_orders']):,}"))
        if "num_customers" in kpis: lines.append(_kv_line("Customers", f"{int(kpis['num_customers']):,}"))
        if "avg_order_value" in kpis and kpis["avg_order_value"] is not None:
            lines.append(_kv_line("Avg Order Value", _format_money(kpis["avg_order_value"])))
    else:
        lines.append("- No KPIs available")

    # Trend
    lines.append("\n### Monthly Trend (compact)")
    if trend_lines:
        for s in trend_lines[-cap_lines:]:
            lines.append(f"- {s}")
    else:
        lines.append("- n/a")

    # Anomaly
    if anomaly_month is not None and anomaly_pct is not None:
        arrow = "↑" if anomaly_pct > 0 else "↓"
        lines.append(f"\n**Latest change ({anomaly_month})**: {arrow} {_format_pct(abs(anomaly_pct))}")

    # Tops
    if isinstance(top_products, pd.DataFrame) and not top_products.empty:
        lines.append("\n### Top Products")
        for _, r in top_products.iterrows():
            lines.append(f"- {r.iloc[0]}: {_format_money(r['revenue'])}")
    if isinstance(top_channels, pd.DataFrame) and not top_channels.empty:
        lines.append("\n### Top Channels")
        for _, r in top_channels.iterrows():
            lines.append(f"- {r.iloc[0]}: {_format_money(r['revenue'])}")

    # Schema
    lines.append("\n### Schema")
    lines.append(schema_md or "- n/a")

    return "\n".join(lines)


def build_context_pack(
    df: pd.DataFrame,
    mapping,                      # core.semantics.ColumnMapping
    max_trend_points: int = 12,
    top_n: int = 5
) -> str:
    """
    Build a compact Markdown context for the AI.
    Uses only aggregated info; no raw rows. Fast & bounded.
    """
    if df is None or df.empty:
        return "### KPIs\n- No data\n\n### Monthly Trend (compact)\n- n/a\n\n### Schema\n- n/a"

    date_col, amt_col = mapping.date, mapping.amount
    cid, prod, ch = mapping.customer_id, mapping.product, mapping.channel

    # KPIs
    k = {}
    if amt_col and amt_col in df.columns:
        k["total_sales"] = float(pd.to_numeric(df[amt_col], errors="coerce").fillna(0).sum())
    if cid and cid in df.columns:
        try: k["num_customers"] = int(df[cid].nunique())
        except Exception: pass
    if prod and prod in df.columns:
        pass
    # Orders
    oid = getattr(mapping, "order_id", None)
    if oid and oid in df.columns:
        try:
            k["num_orders"] = int(df[oid].nunique())
        except Exception:
            k["num_orders"] = int(df.shape[0]) if amt_col else None
    else:
        k["num_orders"] = int(df.shape[0]) if amt_col else None

    if k.get("total_sales") is not None and k.get("num_orders"):
        try:
            k["avg_order_value"] = float(k["total_sales"]) / max(1, float(k["num_orders"]))
        except Exception:
            k["avg_order_value"] = None

    # Trend
    trend = None
    trend_lines: List[str] = []
    if date_col and amt_col and date_col in df.columns and amt_col in df.columns:
        trend = _monthly(df, date_col, amt_col)
        for _, r in trend.tail(max_trend_points).iterrows():
            trend_lines.append(f"{r['month']}: {_format_money(r['revenue'])}")

    # Anomaly
    m_anom, pc_anom = _anomaly_last(trend) if isinstance(trend, pd.DataFrame) else (None, None)

    # Tops
    top_prod = _topn(df, prod, amt_col, n=top_n) if prod and prod in df.columns and amt_col in df.columns else None
    top_chan = _topn(df, ch, amt_col, n=top_n) if ch and ch in df.columns and amt_col in df.columns else None

    # Schema
    schema_md = _schema_snippet(df)

    return _mk_context_markdown(k, trend_lines, top_prod, top_chan, schema_md, m_anom, pc_anom)
