import pandas as pd

def repeat_rate(df: pd.DataFrame, mapping) -> dict:
    cid, oid = mapping.customer_id, mapping.order_id
    if not cid or cid not in df:
        return {"error": "Need customer_id"}
    orders_per = df.groupby(cid)[oid].nunique() if oid and oid in df else df.groupby(cid).size()
    if hasattr(orders_per, "reset_index"):
        repeaters = (orders_per > 1).mean() if len(orders_per) else 0.0
        return {"repeat_rate": float(repeaters), "table": orders_per.reset_index(name="num_orders")}
    return {"repeat_rate": 0.0, "table": None}
