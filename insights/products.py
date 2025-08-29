import pandas as pd

def _ok(df, cols):
    return all(c and c in df for c in cols)

def top_products(df: pd.DataFrame, mapping) -> dict:
    prod, amt = mapping.product, mapping.amount
    if not _ok(df, [prod, amt]):
        return {"error": "Need product and amount"}
    g = df.groupby(prod)[amt].sum().sort_values(ascending=False).head(15).reset_index()
    g.columns = ["product", "revenue"]
    return {"table": g}

def bottom_products(df: pd.DataFrame, mapping) -> dict:
    prod, amt = mapping.product, mapping.amount
    if not _ok(df, [prod, amt]):
        return {"error": "Need product and amount"}
    g = df.groupby(prod)[amt].sum().sort_values(ascending=True).head(15).reset_index()
    g.columns = ["product", "revenue"]
    return {"table": g}
