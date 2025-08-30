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
/* Enhanced page layout */
.block-container{padding-top:2rem;padding-bottom:2rem}

/* Beautiful KPI cards */
.kpi{background:linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);border:1px solid #cbd5e1;border-radius:16px;padding:20px;box-shadow:0 4px 6px rgba(0,0,0,0.05);transition:all 0.3s ease}
.kpi:hover{transform:translateY(-2px);box-shadow:0 8px 25px rgba(0,0,0,0.1)}
.kpi h3{font-size:14px;margin:0;color:#475569;font-weight:600}
.kpi .v{font-size:28px;font-weight:700;margin-top:8px;color:#1e293b;background:linear-gradient(135deg, #3b82f6, #1d4ed8);-webkit-background-clip:text;-webkit-text-fill-color:transparent}

/* Enhanced typography */
.caption{color:#64748b;font-weight:500}
hr{border:none;border-top:2px solid #e2e8f0;margin:1.5rem 0;border-radius:1px}

/* Beautiful dataframes */
div[data-testid="stDataFrame"] { font-size:13px;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.1) }
div[data-testid="stDataFrame"] div[role="row"] { min-height:32px;transition:background-color 0.2s ease }
div[data-testid="stDataFrame"] div[role="gridcell"] { padding:8px 12px;border-bottom:1px solid #f1f5f9 }
div[data-testid="stDataFrame"] div[role="row"]:hover { background-color:#f8fafc }

/* Enhanced buttons */
.stButton > button {
    border-radius: 12px !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.15) !important;
}

/* Beautiful sidebar */
.css-1d391kg {
    background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%) !important;
}

/* Enhanced file uploader */
.stFileUploader {
    border-radius: 15px !important;
    border: 2px dashed #cbd5e1 !important;
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%) !important;
    transition: all 0.3s ease !important;
}
.stFileUploader:hover {
    border-color: #3b82f6 !important;
    background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%) !important;
}

/* Success messages */
.stSuccess {
    background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%) !important;
    border-radius: 12px !important;
    border: 1px solid #22c55e !important;
    box-shadow: 0 2px 8px rgba(34, 197, 94, 0.1) !important;
}

/* Info messages */
.stInfo {
    background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%) !important;
    border-radius: 12px !important;
    border: 1px solid #3b82f6 !important;
    box-shadow: 0 2px 8px rgba(59, 130, 246, 0.1) !important;
}

/* Mobile responsive */
@media (max-width: 768px) {
    .kpi { padding: 16px; }
    .kpi .v { font-size: 24px; }
    .stButton > button { font-size: 14px !important; padding: 8px 16px !important; }
}

/* Beautiful main header */
.main-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2rem;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}
.main-header h1 {
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.main-header p {
    font-size: 1.2rem;
    margin: 0.5rem 0 0 0;
    opacity: 0.9;
}

/* Industry selection cards */
.industry-card {
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    padding: 1.5rem;
    border-radius: 15px;
    border: 1px solid #cbd5e1;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
}
.industry-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}
</style>
''', unsafe_allow_html=True)

# Beautiful main header
st.markdown("""
<div class="main-header">
    <h1>📈 OmniInsights</h1>
    <p>Advanced Business Intelligence & Analytics Platform</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <p style="font-size: 1.1rem; color: #64748b; font-weight: 500;">
        🚀 Upload a dataset → 🧭 Map columns → 🔍 Filter → 📊 Explore insights → 📄 Export reports
    </p>
    <p style="font-size: 0.9rem; color: #94a3b8; margin-top: 0.5rem;">
        Clear, simple, and explainable business intelligence
    </p>
</div>
""", unsafe_allow_html=True)

cfg = load_config()

with st.sidebar:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 15px; color: white; margin-bottom: 1.5rem;">
        <h2 style="margin: 0; color: white; font-size: 1.5rem;">⚙️ Setup</h2>
        <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;">Configure your analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); padding: 1.5rem; border-radius: 12px; border: 1px solid #cbd5e1; margin-bottom: 1.5rem;">
        <h3 style="margin: 0 0 1rem 0; color: #1e293b; font-size: 1.2rem;">📁 Data Upload</h3>
    """, unsafe_allow_html=True)
    
    upl = st.file_uploader(
        "Upload CSV / Excel / Parquet", 
        type=["csv","xlsx","xls","parquet"],
        help="Upload your business data file"
    )
    
    st.markdown("""
    <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; border-left: 4px solid #3b82f6; margin: 1rem 0;">
        <p style="margin: 0; color: #1e40af; font-size: 0.9rem; font-weight: 500;">
            💡 <strong>Tip:</strong> Include these columns for best results:
        </p>
        <ul style="margin: 0.5rem 0 0 0; color: #1e40af; font-size: 0.85rem;">
            <li>📅 date</li>
            <li>💰 amount</li>
            <li>🆔 order_id</li>
            <li>👥 customer_id</li>
            <li>📦 product (optional)</li>
            <li>🛣️ channel (optional)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); padding: 1.5rem; border-radius: 12px; border: 1px solid #f59e0b; margin-bottom: 1.5rem;">
        <h3 style="margin: 0 0 1rem 0; color: #92400e; font-size: 1.2rem;">📄 Report Generation</h3>
    """, unsafe_allow_html=True)
    
    export_btn = st.button(
        "📄 Export Executive Report", 
        use_container_width=True,
        help="Generate a comprehensive HTML report"
    )
    
    st.markdown("""
    <div style="background: #f0fdf4; padding: 1rem; border-radius: 8px; border-left: 4px solid #22c55e; margin: 1rem 0;">
        <p style="margin: 0; color: #166534; font-size: 0.9rem;">
            📊 <strong>Includes:</strong> KPIs, Trends, Products, Customers, RFM Analysis
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Load data
df = None
if upl is not None:
    try:
        df = read_any(upl)
        st.success(f"Loaded data: {df.shape[0]} rows, {df.shape[1]} columns.")
        
        # Beautiful Industry Selection Section
        st.markdown("---")
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); padding: 2rem; border-radius: 20px; border: 1px solid #cbd5e1; margin: 2rem 0;">
            <h2 style="margin: 0 0 1.5rem 0; color: #1e293b; text-align: center; font-size: 1.8rem;">🏢 Industry Configuration</h2>
            <p style="margin: 0 0 2rem 0; color: #64748b; text-align: center; font-size: 1.1rem;">Select your industry for tailored insights and recommendations</p>
        """, unsafe_allow_html=True)
        
        # Industry selection in a beautiful format
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            preset = st.selectbox(
                "🏢 Industry Type",
                ["Generic", "Retail", "SaaS", "Marketplace"],
                index=0,
                help="Choose your industry for tailored insights"
            )
            # Store industry preset in session state for smart questions
            st.session_state["industry_preset"] = preset
        
        with col2:
            # Beautiful industry info
            industry_icons = {"Generic": "🏢", "Retail": "🏪", "SaaS": "☁️", "Marketplace": "🛒"}
            industry_descriptions = {
                "Generic": "General business analysis for any industry",
                "Retail": "Store performance, inventory, seasonal planning",
                "SaaS": "MRR growth, churn analysis, feature adoption",
                "Marketplace": "Seller performance, buyer behavior, network effects"
            }
            
            industry_colors = {
                "Generic": "#64748b",
                "Retail": "#f59e0b", 
                "SaaS": "#3b82f6",
                "Marketplace": "#10b981"
            }
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%); padding: 1.5rem; border-radius: 15px; border: 2px solid {industry_colors[preset]}; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                <h3 style="margin: 0 0 0.5rem 0; color: {industry_colors[preset]}; font-size: 1.3rem;">{industry_icons[preset]} {preset} Industry</h3>
                <p style="margin: 0; color: #64748b; font-size: 1rem;">{industry_descriptions[preset]}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            # Status indicator
            if preset != "Generic":
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%); padding: 1.5rem; border-radius: 15px; border: 2px solid #22c55e; text-align: center;">
                    <h3 style="margin: 0 0 0.5rem 0; color: #166534; font-size: 1.2rem;">✅ Active</h3>
                    <p style="margin: 0; color: #166534; font-size: 0.9rem;">{preset} insights enabled</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%); padding: 1.5rem; border-radius: 15px; border: 2px solid #3b82f6; text-align: center;">
                    <h3 style="margin: 0 0 0.5rem 0; color: #1e40af; font-size: 1.2rem;">ℹ️ Standard</h3>
                    <p style="margin: 0; color: #1e40af; font-size: 0.9rem;">General analysis mode</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
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
        try:
            path = export_html_report(filtered_df, results, mapping, active_filters)
            
            # Read the generated file for download
            with open(path, "r", encoding="utf-8") as f:
                html_content = f.read()
            
            # Create a proper download button
            st.success("📄 Executive Report Generated Successfully!")
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.download_button(
                    label="📥 Download Executive Report",
                    data=html_content,
                    file_name="omniinsights_executive_report.html",
                    mime="text/html",
                    use_container_width=True,
                    type="primary"
                )
            
            st.info("💡 **Report includes**: KPIs, Revenue Trends, Top Products, RFM Analysis, and Executive Summary")
            
        except Exception as e:
            st.error(f"❌ Failed to generate report: {str(e)}")
            st.info("Please try again or contact support if the issue persists.")
else:
    st.info("Upload a dataset and confirm the mapping to continue.")
