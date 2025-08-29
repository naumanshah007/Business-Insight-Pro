"""
core/sqlctx.py
Tiny SQL-like aggregator for compact context. Prefer duckdb if installed.
"""

from __future__ import annotations
from typing import Optional, Tuple
import pandas as pd

try:
    import duckdb  # type: ignore
except Exception:
    duckdb = None


def _mk_view(df: pd.DataFrame, mapping) -> pd.DataFrame:
    d = df.copy()
    if mapping.date and mapping.date in d.columns:
        d[mapping.date] = pd.to_datetime(d[mapping.date], errors="coerce")
        d["month"] = d[mapping.date].dt.to_period("M").astype(str)
        d["date"]  = d[mapping.date].dt.date
    amt = mapping.amount
    if amt and amt in d.columns:
        d["_amount"] = pd.to_numeric(d[amt], errors="coerce").fillna(0.0)
    return d


def _markdown_table(df: pd.DataFrame, max_rows: int = 10) -> str:
    if not isinstance(df, pd.DataFrame) or df.empty:
        return "_n/a_"
    view = df.head(max_rows)
    cols = list(view.columns)
    lines = ["|" + "|".join(cols) + "|", "|" + "|".join(["---"] * len(cols)) + "|"]
    for _, r in view.iterrows():
        lines.append("|" + "|".join([str(r[c]) for c in cols]) + "|")
    return "\n".join(lines)


def reasons_pack(df: pd.DataFrame, mapping, recent_months: int = 3) -> str:
    """
    Build a tiny SQL-style pack: last-month vs prev-month, and top movers.
    Keeps strict bounds on size.
    """
    if df is None or df.empty or not mapping.amount:
        return "### SQL Pack\n- n/a"

    d = _mk_view(df, mapping)
    amt = "_amount"
    prod = mapping.product if mapping.product in d.columns else None
    ch   = mapping.channel if mapping.channel in d.columns else None

    # Prefer duckdb for speed; otherwise pandas
    md_sections = ["### SQL Pack"]

    # 1) Month vs previous month totals
    try:
        if duckdb:
            con = duckdb.connect(database=":memory:")
            con.register("t", d)
            q = """
              WITH m AS (
                SELECT month, SUM({amt}) AS revenue
                FROM t
                WHERE month IS NOT NULL
                GROUP BY 1
                ORDER BY 1
              )
              SELECT month, revenue
              FROM m
              ORDER BY month DESC
              LIMIT 6
            """.format(amt=amt)
            mv = con.execute(q).df().sort_values("month")
        else:
            mv = d.groupby("month", as_index=False)[amt].sum().rename(columns={amt: "revenue"}).sort_values("month").tail(6)
        md_sections.append("**Recent Months (Revenue)**")
        md_sections.append(_markdown_table(mv))
    except Exception:
        pass

    # 2) Last-month breakdown by product / channel
    try:
        if "month" in d.columns and d["month"].notna().any():
            last_m = d["month"].dropna().iloc[-1]
            dd = d[d["month"] == last_m]
            if prod:
                g = dd.groupby(prod, as_index=False)[amt].sum().rename(columns={amt: "revenue"}).sort_values("revenue", ascending=False).head(10)
                md_sections.append(f"**{last_m} Top Products**")
                md_sections.append(_markdown_table(g))
            if ch:
                g2 = dd.groupby(ch, as_index=False)[amt].sum().rename(columns={amt: "revenue"}).sort_values("revenue", ascending=False).head(10)
                md_sections.append(f"**{last_m} Top Channels**")
                md_sections.append(_markdown_table(g2))
    except Exception:
        pass

    return "\n\n".join(md_sections)
