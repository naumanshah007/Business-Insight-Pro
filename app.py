import streamlit as st
import pandas as pd

from core.config import load_config
from core.io import read_any
from core.semantics import suggest_mappings, ColumnMapping
from core.mapping import mapping_widget
from core.filters import render_global_filters
from core.profiling import quick_profile

from insights.registry import run_all
from ui.tabs import (
    render_overview_tab,
    render_products_tab,
    render_customers_tab,
    render_cohorts_tab,
    render_rfm_tab,
    render_forecast_tab,
    render_ai_tab
)
from reports.exporter import export_html_report

st.set_page_config(page_title="OmniInsights — Growth Analytics", page_icon="📈", layout="wide")

st.markdown('''
<style>
.block-container{padding-top:2rem;padding-bottom:2rem}
.kpi{background:#fff;border:1px solid #e5e7eb;border-radius:16px;padding:16px;box-shadow:0 1px 2px rgba(0,0,0,0.04)}
.kpi h3{font-size:14px;margin:0;color:#64748b}
.kpi .v{font-size:24px;font-weight:700;margin-top:4px;color:#0f172a}
.caption{color:#6b7280}
hr{border:none;border-top:1px solid #e5e7eb;margin:1rem 0}
div[data-testid="stDataFrame"] { font-size:13px }
div[data-testid="stDataFrame"] div[role="row"] { min-height:28px }
div[data-testid="stDataFrame"] div[role="gridcell"] { padding:4px 8px }
</style>
''', unsafe_allow_html=True)

st.markdown("# 📈 OmniInsights")
st.caption("Upload a dataset → map columns → filter → explore insights → export a report. Clear, simple, and explainable.")

cfg = load_config()

with st.sidebar:
    st.header("Setup")
    upl = st.file_uploader("Upload CSV / Excel / Parquet", type=["csv","xlsx","xls","parquet"])
    st.caption("Tip: include: date • amount • order_id • customer_id • (product) • (channel)")
    st.subheader("Report")
    export_btn = st.button("📄 Export HTML Report")

# Load data
df = None
if upl is not None:
    try:
        df = read_any(upl)
        st.success(f"Loaded data: {df.shape[0]} rows, {df.shape[1]} columns.")
        
        # Industry Selection Section
        st.markdown("---")
        st.subheader("🏢 **Choose Your Industry Type**")
        st.caption("Select your industry to get tailored insights and recommendations")
        
        # Industry selection with detailed explanations
        col1, col2 = st.columns([1, 2])
        
        with col1:
            preset = st.selectbox(
                "Industry Type",
                ["Generic", "Retail", "SaaS", "Marketplace"],
                index=0,
                help="Choose the industry that best matches your business"
            )
            # Store industry preset in session state for smart questions
            st.session_state["industry_preset"] = preset
        
        with col2:
            # Show industry-specific information
            industry_info = {
                "Generic": {
                    "icon": "🏢",
                    "description": "General business analysis for any industry",
                    "features": ["Standard KPIs", "Basic trend analysis", "General insights"],
                    "best_for": "Any business type or mixed data"
                },
                "Retail": {
                    "icon": "🏪",
                    "description": "Specialized for physical and online retail businesses",
                    "features": ["Store performance", "Inventory turnover", "Seasonal planning", "Promotional effectiveness"],
                    "best_for": "E-commerce, brick-and-mortar stores, retail chains"
                },
                "SaaS": {
                    "icon": "☁️",
                    "description": "Optimized for software-as-a-service companies",
                    "features": ["MRR growth", "Churn analysis", "Feature adoption", "Customer success", "Pricing optimization"],
                    "best_for": "Software companies, subscription services, SaaS platforms"
                },
                "Marketplace": {
                    "icon": "🛒",
                    "description": "Designed for multi-sided marketplace platforms",
                    "features": ["Seller performance", "Buyer behavior", "Network effects", "Commission optimization", "Liquidity analysis"],
                    "best_for": "E-commerce marketplaces, service platforms, peer-to-peer platforms"
                }
            }
            
            selected_info = industry_info[preset]
            st.markdown(f"""
            **{selected_info['icon']} {preset} Industry**
            
            {selected_info['description']}
            
            **Key Features:**
            {chr(10).join([f"• {feature}" for feature in selected_info['features']])}
            
            **Best For:** {selected_info['best_for']}
            """)
        
        # Show what changes with industry selection
        st.info(f"💡 **Industry Mode Active**: Your analysis will now include {preset.lower()}-specific insights, questions, and recommendations.")
        
    except Exception as e:
        st.error(f"Failed to read file: {e}")

# Profile + Mapping
mapping = None
if df is not None:
    with st.expander("🔍 Data Preview & Quick Profile", expanded=False):
        st.dataframe(df.head(50), use_container_width=True)
        st.json(quick_profile(df))

    st.subheader("🧭 Column Mapping")
    
    # Show industry impact on mapping suggestions
    if preset != "Generic":
        industry_icons = {"Retail": "🏪", "SaaS": "☁️", "Marketplace": "🛒"}
        st.info(f"{industry_icons.get(preset, '🏢')} **{preset} Industry Mode**: Column mapping suggestions are optimized for {preset.lower()} businesses.")
    
    sugg = suggest_mappings(df, industry=preset.lower())
    selected = mapping_widget(df, suggestions=sugg)

    if selected:
        if isinstance(selected, dict):
            mapping = ColumnMapping(**selected)
        elif isinstance(selected, ColumnMapping):
            mapping = selected
        else:
            st.error("Unexpected mapping type returned.")
            mapping = None

        if mapping is not None:
            if hasattr(mapping, "to_dict"):
                st.session_state["mapping"] = mapping.to_dict()
            else:
                st.session_state["mapping"] = selected
            st.caption("✔ Mapping saved.")

# Insights - Cache results to avoid regeneration
if df is not None and mapping is not None:
    filtered_df, active_filters = render_global_filters(df, mapping)

    # Cache insights to avoid regeneration
    @st.cache_data(show_spinner=False)
    def _run_insights_cached(sig: str):
        return run_all(filtered_df, mapping)
    
    # Create stable signature for caching
    insights_signature = f"{df.shape}-{hash(str(mapping))}-{hash(str(active_filters))}"
    
    # Only show spinner if insights aren't cached yet
    if "insights" not in st.session_state or st.session_state.get("insights_signature") != insights_signature:
        with st.spinner("Running insights..."):
            results = _run_insights_cached(insights_signature)
        st.session_state["insights"] = results
        st.session_state["insights_signature"] = insights_signature
        st.success("✅ Insights generated successfully!")
    else:
        results = st.session_state["insights"]
        # Show subtle indicator that insights are loaded from cache
        st.caption("💡 Using cached insights - instant performance!")

    # Define tab names
    tab_names = ["Overview", "Products", "Customers", "Customer Cohorts", "Customer Segments", "Forecast", "AI Assistant"]
    
    tabs = st.tabs(tab_names)
    with tabs[0]:
        render_overview_tab(filtered_df, results, mapping, active_filters)
    with tabs[1]:
        render_products_tab(filtered_df, results, mapping, active_filters)
    with tabs[2]:
        render_customers_tab(filtered_df, results, mapping, active_filters)
    with tabs[3]:
        render_cohorts_tab(filtered_df, results, mapping, active_filters)
    with tabs[4]:
        render_rfm_tab(filtered_df, results, mapping, active_filters)
    with tabs[5]:
        render_forecast_tab(filtered_df, results, mapping, active_filters)
    with tabs[6]:
        render_ai_tab(filtered_df, results, mapping, active_filters)

    if export_btn:
        path = export_html_report(filtered_df, results, mapping, active_filters)
        st.success("Report generated.")
        st.markdown(f"[Download Executive Report]({path})")
else:
    st.info("Upload a dataset and confirm the mapping to continue.")
