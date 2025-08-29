import pandas as pd

def compute_kpis(df: pd.DataFrame, mapping) -> dict:
    date, amt, oid, cid = mapping.date, mapping.amount, mapping.order_id, mapping.customer_id
    total_sales = float(df[amt].sum()) if amt and amt in df else None
    num_orders = int(df[oid].nunique()) if oid and oid in df else len(df)
    num_customers = int(df[cid].nunique()) if cid and cid in df else None
    aov = None
    if amt and oid and amt in df and oid in df:
        aov = float(df.groupby(oid)[amt].sum().mean())
    return {"kpis": {"total_sales": total_sales, "num_orders": num_orders, "num_customers": num_customers, "avg_order_value": aov}}
