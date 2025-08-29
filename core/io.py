"""
core/io.py
Safe file readers for OmniInsights (CSV, Excel, Parquet).
"""

import pandas as pd


def infer_sep(sample: bytes) -> str:
    """
    Try to infer the delimiter from the first chunk of bytes in a CSV file.
    Returns "," if unsure.
    """
    text = sample.decode("utf-8", errors="ignore")
    first_line = text.splitlines()[0] if text else ""
    # Common delimiters
    for sep in [",", ";", "\t", "|"]:
        if sep in first_line:
            return sep
    return ","


def read_any(uploaded_file) -> pd.DataFrame:
    """
    Read a file uploaded via Streamlit (UploadedFile).
    Supports CSV, Excel (xls/xlsx), and Parquet.
    """
    name = uploaded_file.name.lower()

    try:
        if name.endswith(".csv"):
            # Peek first 2KB to guess separator
            sample = uploaded_file.read(2048)
            uploaded_file.seek(0)
            sep = infer_sep(sample)
            df = pd.read_csv(uploaded_file, sep=sep)
            return df

        elif name.endswith(".xlsx") or name.endswith(".xls"):
            return pd.read_excel(uploaded_file)

        elif name.endswith(".parquet"):
            return pd.read_parquet(uploaded_file)

        else:
            raise ValueError(f"Unsupported file type: {name}")

    except Exception as e:
        raise RuntimeError(f"Failed to read file {name}: {e}")
