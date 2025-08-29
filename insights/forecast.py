import pandas as pd

def naive_forecast(df: pd.DataFrame, mapping) -> dict:
    date, amt = mapping.date, mapping.amount
    if not date or not amt or date not in df or amt not in df:
        return {"error": "Need date and amount"}
    tmp = df[[date, amt]].dropna()
    tmp[date] = pd.to_datetime(tmp[date], errors="coerce")
    tmp = tmp.dropna(subset=[date])
    g = tmp.groupby(pd.Grouper(key=date, freq="M"))[amt].sum().reset_index()
    g.columns = ["month", "revenue"]
    # simple 3-month moving average forecast for next 3 months
    g['ma3'] = g['revenue'].rolling(3).mean()
    if len(g) >= 3:
        last_ma = g['ma3'].iloc[-1]
    else:
        last_ma = g['revenue'].mean() if len(g) else 0.0
    last_month = g['month'].max() if len(g) else pd.Timestamp.today().floor("M")
    future = pd.date_range(last_month + pd.offsets.MonthBegin(1), periods=3, freq="MS")
    fdf = pd.DataFrame({"month": future, "forecast": [float(last_ma)]*3})
    return {"history": g, "forecast": fdf}
