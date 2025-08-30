from pathlib import Path
import time
import pandas as pd

HTML = """
<html><head><meta charset="utf-8"><title>OmniInsights Report</title>
<style>
body{{font-family:"Inter","ui-sans-serif","system-ui","Segoe UI","Roboto","Helvetica","Arial",sans-serif;margin:40px;color:#0f172a}}
h1{{margin:0 0 6px 0}} .sec{{margin-top:24px}}
.card{{border:1px solid #e5e7eb;border-radius:12px;padding:16px;margin:8px 0;background:#fff}}
small{{color:#6b7280}}
</style></head><body>
<h1>OmniInsights — Executive Report</h1>
<small>Generated: {ts}</small>

<div class="sec card"><h2>KPIs</h2><pre>{kpis}</pre></div>
<div class="sec card"><h2>Monthly Revenue Trend (first rows)</h2>{trend}</div>
<div class="sec card"><h2>Top Products</h2>{top}</div>
<div class="sec card"><h2>RFM (sample)</h2>{rfm}</div>
</body></html>
"""

def _html(tbl):
    if isinstance(tbl, pd.DataFrame):
        return tbl.head(50).to_html(index=False)
    return "<i>No data</i>"

def export_html_report(df: pd.DataFrame, results: dict, mapping, filters: dict) -> str:
    ts = time.strftime("%Y-%m-%d %H:%M")
    
    # Safely extract data with fallbacks
    kpis_data = results.get("kpis", {})
    if isinstance(kpis_data, dict) and "kpis" in kpis_data:
        k = kpis_data["kpis"]
    else:
        k = kpis_data
    
    trend_tbl = results.get("trend", {}).get("table")
    top_tbl = results.get("top_products", {}).get("table")
    rfm_tbl = results.get("rfm", {}).get("table")
    
    # Format KPIs for display
    if isinstance(k, dict):
        kpis_formatted = "\n".join([f"{key}: {value}" for key, value in k.items()])
    else:
        kpis_formatted = str(k) if k else "No KPI data available"
    
    html = HTML.format(
        ts=ts, 
        kpis=kpis_formatted, 
        trend=_html(trend_tbl), 
        top=_html(top_tbl), 
        rfm=_html(rfm_tbl)
    )
    
    out = Path("omniinsights_report.html")
    out.write_text(html, encoding="utf-8")
    return str(out)
