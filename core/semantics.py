"""
core/semantics.py
Column mapping helpers for OmniInsights.
"""

from dataclasses import dataclass
from typing import Optional, Dict
import pandas as pd


@dataclass
class ColumnMapping:
    """Standardized mapping between user dataset and app semantics."""
    date: Optional[str] = None
    amount: Optional[str] = None
    order_id: Optional[str] = None
    customer_id: Optional[str] = None
    product: Optional[str] = None
    channel: Optional[str] = None

    def to_dict(self) -> Dict[str, Optional[str]]:
        return {
            "date": self.date,
            "amount": self.amount,
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "product": self.product,
            "channel": self.channel,
        }


def suggest_mappings(df: pd.DataFrame, industry: str = "generic") -> Dict[str, Optional[str]]:
    """
    Try to suggest column mappings based on column names.
    """
    cols = [c.lower() for c in df.columns]

    def find(*keywords):
        for i, c in enumerate(cols):
            if any(k in c for k in keywords):
                return df.columns[i]
        return None

    return {
        "date": find("date", "order_date", "timestamp"),
        "amount": find("amount", "revenue", "sales", "price", "total"),
        "order_id": find("order_id", "invoice", "transaction"),
        "customer_id": find("customer", "cust_id", "client"),
        "product": find("product", "sku", "item"),
        "channel": find("channel", "source", "platform"),
    }
