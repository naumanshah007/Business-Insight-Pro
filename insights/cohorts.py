import pandas as pd

def monthly_retention_cohort(df: pd.DataFrame, mapping) -> dict:
    date, cid = mapping.date, mapping.customer_id
    if not date or not cid or date not in df or cid not in df:
        return {"error": "Need date and customer_id"}
    tmp = df[[date, cid]].dropna()
    tmp[date] = pd.to_datetime(tmp[date], errors="coerce")
    tmp = tmp.dropna(subset=[date])
    tmp['order_month'] = tmp[date].values.astype('datetime64[M]')
    first = tmp.groupby(cid)['order_month'].min().rename('cohort')
    tmp = tmp.join(first, on=cid)
    pivot = tmp.pivot_table(index='cohort', columns='order_month', values=cid, aggfunc='nunique')
    retention = pivot.divide(pivot.iloc[:,0], axis=0).fillna(0.0)
    return {"retention": retention.reset_index()}
