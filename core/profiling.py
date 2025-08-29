"""
core/profiling.py
Quick dataset profiling helpers for OmniInsights.
"""

import pandas as pd


def quick_profile(df: pd.DataFrame) -> dict:
    """
    Return a lightweight profile of the DataFrame as a dict.
    Useful for display in Streamlit as JSON.
    """
    if df is None or df.empty:
        return {"rows": 0, "columns": 0, "message": "No data loaded"}

    profile = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_types": {},
        "missing_values": {},
    }

    for col in df.columns:
        profile["column_types"][col] = str(df[col].dtype)
        na_count = int(df[col].isna().sum())
        if na_count > 0:
            profile["missing_values"][col] = na_count

    return profile
