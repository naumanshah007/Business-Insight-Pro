"""
core/filters.py
Global filtering widgets for OmniInsights.
"""

import streamlit as st
import pandas as pd
from core.semantics import ColumnMapping


def render_global_filters(df: pd.DataFrame, mapping: ColumnMapping):
    """
    Render global filters in the sidebar.
    Returns (filtered_df, active_filters_dict).
    """
    active_filters = {}

    # Work on a copy
    fdf = df.copy()

    st.sidebar.header("Filters")

    # Date filter
    if mapping.date and mapping.date in fdf.columns:
        try:
            fdf[mapping.date] = pd.to_datetime(fdf[mapping.date], errors="coerce")
            min_date, max_date = fdf[mapping.date].min(), fdf[mapping.date].max()
            start, end = st.sidebar.date_input(
                "Date range",
                [min_date, max_date] if min_date and max_date else None,
            )
            if start and end:
                mask = (fdf[mapping.date] >= pd.to_datetime(start)) & (
                    fdf[mapping.date] <= pd.to_datetime(end)
                )
                fdf = fdf.loc[mask]
                active_filters["date_range"] = (str(start), str(end))
        except Exception:
            st.sidebar.warning("Could not parse date column properly.")

    # Product filter
    if mapping.product and mapping.product in fdf.columns:
        options = sorted(fdf[mapping.product].dropna().unique().tolist())
        sel = st.sidebar.multiselect("Products", options)
        if sel:
            fdf = fdf[fdf[mapping.product].isin(sel)]
            active_filters["products"] = sel

    # Channel filter
    if mapping.channel and mapping.channel in fdf.columns:
        options = sorted(fdf[mapping.channel].dropna().unique().tolist())
        sel = st.sidebar.multiselect("Channels", options)
        if sel:
            fdf = fdf[fdf[mapping.channel].isin(sel)]
            active_filters["channels"] = sel

    # Customer filter
    if mapping.customer_id and mapping.customer_id in fdf.columns:
        options = sorted(fdf[mapping.customer_id].dropna().unique().tolist())
        sel = st.sidebar.multiselect("Customers", options)
        if sel:
            fdf = fdf[fdf[mapping.customer_id].isin(sel)]
            active_filters["customers"] = sel

    return fdf, active_filters
