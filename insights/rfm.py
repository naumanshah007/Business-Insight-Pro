import pandas as pd
import numpy as np

def rfm_segments(df: pd.DataFrame, mapping) -> dict:
    date, cid, amt = mapping.date, mapping.customer_id, mapping.amount
    if not date or not cid or not amt or date not in df or cid not in df or amt not in df:
        return {"error": "Need date, customer_id, amount"}
    tbl = df[[date, cid, amt]].dropna()
    tbl[date] = pd.to_datetime(tbl[date], errors="coerce")
    tbl = tbl.dropna(subset=[date])
    snapshot = tbl[date].max() + pd.Timedelta(days=1)
    r = tbl.groupby(cid)[date].max().apply(lambda d: (snapshot - d).days)
    f = tbl.groupby(cid).size()
    m = tbl.groupby(cid)[amt].sum()
    rfm = pd.DataFrame({"CustomerID": r.index, "Recency": r.values, "Frequency": f.values, "Monetary": m.values})
    # tertiles
    r_score = pd.qcut(rfm['Recency'].rank(method='first'), 3, labels=[3,2,1])
    f_score = pd.qcut(rfm['Frequency'].rank(method='first'), 3, labels=[1,2,3])
    m_score = pd.qcut(rfm['Monetary'].rank(method='first'), 3, labels=[1,2,3])
    rfm['RFM_Score'] = r_score.astype(int)*100 + f_score.astype(int)*10 + m_score.astype(int)
    return {"table": rfm}
