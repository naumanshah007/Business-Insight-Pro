"""
core/mapping.py
Streamlit widget for mapping dataset columns to OmniInsights semantics.
"""

import streamlit as st
import pandas as pd
from typing import Dict, Optional
from core.semantics import ColumnMapping


FIELDS = [
    ("date", "Date"),
    ("amount", "Amount / Revenue"),
    ("order_id", "Order ID / Invoice"),
    ("customer_id", "Customer ID"),
    ("product", "Product / SKU"),
    ("channel", "Channel / Source"),
]


def mapping_widget(df: pd.DataFrame, suggestions: Dict[str, Optional[str]]) -> Optional[dict]:
    """
    Render Streamlit widgets to let the user map dataset columns to standard fields.
    Always returns a dict (safe for ColumnMapping(**dict)).
    """
    cols = list(df.columns)
    values = {}

    st.caption("👉 Map your dataset columns to standard fields used by the app:")

    scols = st.columns(len(FIELDS))
    for i, (key, label) in enumerate(FIELDS):
        default_val = suggestions.get(key)
        idx = (cols.index(default_val) + 1) if default_val in cols else 0
        with scols[i]:
            sel = st.selectbox(label, ["—"] + cols, index=idx)
            values[key] = None if sel == "—" else sel

    st.caption("At least a Date and Amount column are recommended for insights.")

    if st.button("Save Mapping", type="primary"):
        st.session_state["mapping"] = values
        st.success("Mapping saved.")
        return values

    # If mapping already exists in session, return it
    if "mapping" in st.session_state:
        return st.session_state["mapping"]

    # Otherwise return current suggestions
    return suggestions
