"""
core/config.py
Lightweight configuration loader for OmniInsights.
"""

import os
import yaml

DEFAULT_CONFIG = {
    "app_name": "OmniInsights",
    "version": "1.0",
    "theme": {
        "primary_color": "#2563eb",
        "secondary_color": "#64748b",
    },
    "limits": {
        "max_rows": 500000,
        "max_file_size_mb": 50,
    },
}


def load_config(path: str = None) -> dict:
    """
    Load configuration from YAML file if provided, else return defaults.
    If path is not given, checks environment variable OMNI_CONFIG.
    """
    config_path = path or os.environ.get("OMNI_CONFIG")
    if not config_path:
        return DEFAULT_CONFIG

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict):
            return DEFAULT_CONFIG
        # Merge with defaults
        merged = {**DEFAULT_CONFIG, **data}
        return merged
    except FileNotFoundError:
        return DEFAULT_CONFIG
    except Exception as e:
        print(f"[config] Failed to load config from {config_path}: {e}")
        return DEFAULT_CONFIG
