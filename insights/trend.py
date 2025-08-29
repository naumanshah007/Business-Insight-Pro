import pandas as pd

def monthly_revenue_trend(df: pd.DataFrame, mapping) -> dict:
    date, amt = mapping.date, mapping.amount
    if not date or not amt or date not in df or amt not in df:
        return {"error": "Need date and amount"}
    tmp = df[[date, amt]].dropna()
    tmp[date] = pd.to_datetime(tmp[date], errors="coerce")
    tmp = tmp.dropna(subset=[date])
    g = tmp.groupby(pd.Grouper(key=date, freq="M"))[amt].sum().reset_index()
    g.columns = ["month", "revenue"]
    return {"table": g}
