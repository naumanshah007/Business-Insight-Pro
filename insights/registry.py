# insights/registry.py
from typing import Dict
import pandas as pd
from . import kpis, trend, products, customers, cohorts, rfm, forecast

AVAILABLE = {
    "kpis": kpis.compute_kpis,
    "trend": trend.monthly_revenue_trend,
    "top_products": products.top_products,
    "bottom_products": products.bottom_products,
    "repeat_rate": customers.repeat_rate,
    "cohorts": cohorts.monthly_retention_cohort,
    "rfm": rfm.rfm_segments,
    "forecast": forecast.naive_forecast,
}

def run_all(df: pd.DataFrame, mapping) -> Dict[str, dict]:
    results = {}
    for qid, fn in AVAILABLE.items():
        try:
            results[qid] = fn(df, mapping=mapping)
        except Exception as e:
            results[qid] = {"error": str(e)}
    return results
