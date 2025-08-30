import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from core.ai_google import ask_ai, is_configured as ai_ready

def _safe_df(obj):
    if isinstance(obj, pd.DataFrame):
        return obj
    if isinstance(obj, dict):
        try:
            return pd.DataFrame(obj)
        except Exception:
            return None
    return None

def _nonempty(df):
    return isinstance(df, pd.DataFrame) and (len(df.index) > 0)

def _explain(text):
    st.caption(str(text))

def _fmt(val, numfmt="{:,}", fallback="—"):
    if val is None:
        return fallback
    try:
        return numfmt.format(val)
    except Exception:
        return str(val)

def render_overview_tab(df, results, mapping, flt):
    st.subheader("Overview")
    _explain("Quick summary of sales and customers. All visuals respect the filters at the top.")

    k_container = results.get("kpis", {}) if isinstance(results, dict) else {}
    k = k_container.get("kpis", {}) if isinstance(k_container, dict) else {}

    cols = st.columns(4)
    cols[0].markdown(f"<div class='kpi'><h3>Total Sales</h3><div class='v'>{_fmt(k.get('total_sales'))}</div></div>", unsafe_allow_html=True)
    cols[1].markdown(f"<div class='kpi'><h3>Orders</h3><div class='v'>{_fmt(k.get('num_orders'))}</div></div>", unsafe_allow_html=True)
    cols[2].markdown(f"<div class='kpi'><h3>Customers</h3><div class='v'>{_fmt(k.get('num_customers'))}</div></div>", unsafe_allow_html=True)
    cols[3].markdown(f"<div class='kpi'><h3>Avg Order Value</h3><div class='v'>{_fmt(k.get('avg_order_value'), numfmt='{:.2f}')}</div></div>", unsafe_allow_html=True)

    tr_container = results.get("trend", {}) if isinstance(results, dict) else {}
    tr = _safe_df(tr_container.get("table") if isinstance(tr_container, dict) else None)
    if _nonempty(tr):
        xcol = "month" if "month" in tr.columns else tr.columns[0]
        ycol = "revenue" if "revenue" in tr.columns else tr.columns[1]
        fig = px.line(tr, x=xcol, y=ycol, markers=True, title="Monthly Sales")
        fig.update_layout(height=380, margin=dict(l=10,r=10,t=60,b=10), hovermode="x unified", template="plotly_white",
                          xaxis_title="Month", yaxis_title="Revenue")
        st.plotly_chart(fig, use_container_width=True)
        _explain("Shows how total sales evolve each month.")

def render_products_tab(df, results, mapping, flt):
    st.subheader("Products")
    _explain("Top and bottom performers by total sales.")
    top = _safe_df(results.get("top_products", {}).get("table") if isinstance(results.get("top_products", {}), dict) else None)
    bot = _safe_df(results.get("bottom_products", {}).get("table") if isinstance(results.get("bottom_products", {}), dict) else None)
    c1, c2 = st.columns(2)
    with c1:
        st.write("Top products by revenue")
        if _nonempty(top):
            st.dataframe(top, use_container_width=True, hide_index=True)
            xcol, ycol = top.columns[0], top.columns[1]
            fig = px.bar(top, x=xcol, y=ycol, labels={xcol:"Product", ycol:"Revenue"})
            fig.update_layout(height=360, margin=dict(l=10,r=10,t=30,b=10), template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)
            _explain("Focus inventory and marketing on these items.")
    with c2:
        st.write("Bottom products by revenue")
        if _nonempty(bot):
            st.dataframe(bot, use_container_width=True, hide_index=True)
            _explain("Consider discounts, bundling, or retiring these items.")

def render_customers_tab(df, results, mapping, flt):
    st.subheader("Customers")
    _explain("Repeat customers drive growth.")
    rr = results.get("repeat_rate", {}) if isinstance(results.get("repeat_rate", {}), dict) else {}
    if isinstance(rr, dict) and ("repeat_rate" in rr) and (rr["repeat_rate"] is not None):
        st.metric("Repeat Customer Share", f"{float(rr['repeat_rate']) * 100:.1f}%")
        _explain("The percentage of customers who placed more than one order.")
    tbl = _safe_df(rr.get("table") if isinstance(rr, dict) else None)
    if _nonempty(tbl):
        st.dataframe(tbl.head(200), use_container_width=True, hide_index=True)

def render_cohorts_tab(df, results, mapping, flt):
    st.subheader("Customer Cohorts")
    _explain("Groups customers by their first purchase month and tracks how many return over time.")
    ret = _safe_df(results.get("cohorts", {}).get("retention") if isinstance(results.get("cohorts", {}), dict) else None)
    if _nonempty(ret):
        st.dataframe(ret, use_container_width=True, hide_index=True)
        _explain("Each row is a cohort (first purchase month). Columns show return rates in later months.")
    else:
        st.info("Not enough data to compute cohorts.")

def render_rfm_tab(df, results, mapping, flt):
    st.subheader("Customer Segments (RFM)")
    _explain("RFM = Recency, Frequency, Monetary. Higher scores indicate more valuable customers.")
    tbl = _safe_df(results.get("rfm", {}).get("table") if isinstance(results.get("rfm", {}), dict) else None)
    if _nonempty(tbl):
        st.dataframe(tbl.head(200), use_container_width=True, hide_index=True)

def render_forecast_tab(df, results, mapping, flt):
    st.subheader("Forecast")
    _explain("We project the next 3 months using a simple **Moving Average (MA)** baseline. MA(3) means the average of the last three months.")
    f_res = results.get("forecast", {}) if isinstance(results.get("forecast", {}), dict) else {}
    hist = _safe_df(f_res.get("history"))
    fdf  = _safe_df(f_res.get("forecast"))
    if _nonempty(hist) and _nonempty(fdf):
        fig = go.Figure()
        x = hist["month"] if "month" in hist.columns else hist.iloc[:, 0]
        y = hist["revenue"] if "revenue" in hist.columns else hist.iloc[:, 1]
        fig.add_trace(go.Scatter(x=x, y=y, mode="lines+markers", name="History"))
        if "ma3" in hist.columns:
            fig.add_trace(go.Scatter(x=x, y=hist["ma3"], mode="lines", name="MA(3) — 3-month Moving Average"))
        fx = fdf["month"] if "month" in fdf.columns else fdf.iloc[:, 0]
        fy = fdf["forecast"] if "forecast" in fdf.columns else fdf.iloc[:, 1]
        fig.add_trace(go.Scatter(x=fx, y=fy, mode="lines+markers", name="Forecast"))
        fig.update_layout(height=380, margin=dict(l=10,r=10,t=40,b=10), template="plotly_white",
                          hovermode="x unified", xaxis_title="Month", yaxis_title="Revenue")
        st.plotly_chart(fig, use_container_width=True)
        _explain("MA smooths short-term fluctuations to show the underlying trend.")

def render_ai_tab(df, results, mapping, flt):
    from core.context import build_context_pack
    from core.sqlctx import reasons_pack
    from core.smart_questions import SmartQuestionSystem
    from datetime import datetime

    # Add mobile-friendly CSS
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .stButton > button {
            font-size: 14px !important;
            padding: 8px 16px !important;
            height: auto !important;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px !important;
        }
        .stTabs [data-baseweb="tab"] {
            height: 40px !important;
            font-size: 12px !important;
        }
        .stMarkdown {
            font-size: 14px !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.subheader("🤖 Smart Business Intelligence")
    st.caption("Get instant, intelligent answers to your business questions without external APIs.")
    
    # Ensure we stay on the AI Assistant tab - More robust approach
    if "current_tab" not in st.session_state:
        st.session_state["current_tab"] = "AI Assistant"
    else:
        st.session_state["current_tab"] = "AI Assistant"
    
    # Initialize selected question if not exists
    if "selected_question" not in st.session_state:
        st.session_state.selected_question = None

    # Initialize the smart questions system with industry context
    # Get industry from session state or default to generic
    industry = st.session_state.get("industry_preset", "generic").lower()
    smart_questions = SmartQuestionSystem(industry=industry)
    
    # Pre-build and cache context data ONCE to avoid reprocessing
    @st.cache_data(show_spinner=False)
    def _build_context_once(sig: str):
        """Build context data once and cache it for all questions."""
        ctx_md = build_context_pack(df, mapping, max_trend_points=18, top_n=5)
        sql_md = reasons_pack(df, mapping, recent_months=3)
        return {
            "shape": df.shape,
            "context_md": ctx_md,
            "sql_md": sql_md
        }

    # Create a stable signature for caching
    context_signature = f"{df.shape}-{hash(str(flt))}-{hash(str(mapping))}"
    
    # Build context data once (this will be cached)
    context_data = _build_context_once(context_signature)
    
    # Get available questions based on data context
    available_questions = smart_questions.get_available_questions(context_data, results)
    
    # Show context summary
    st.markdown("### 📊 **Data Context Analysis**")
    context_summary = smart_questions.get_context_summary(context_data, results)
    st.markdown(context_summary)
    
    # Professional Header Section
    st.markdown("---")
    
    # Industry Status Banner - Mobile Responsive
    if industry != "generic":
        industry_icons = {"retail": "🏪", "saas": "☁️", "marketplace": "🛒"}
        industry_names = {"retail": "Retail", "saas": "SaaS", "marketplace": "Marketplace"}
        
        # Mobile responsive layout
        st.markdown(f"""
        <div style="background: linear-gradient(90deg, #f0f9ff 0%, #e0f2fe 100%); padding: 20px; border-radius: 15px; border-left: 4px solid #0284c7; margin-bottom: 15px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <h4 style="margin: 0; color: #0c4a6e; font-size: 18px;">{industry_icons.get(industry, '🏢')} {industry_names.get(industry, 'Business')} Industry Mode</h4>
            <div style="margin-left: auto; background: #ecfdf5; padding: 5px 10px; border-radius: 5px; border: 1px solid #a7f3d0;">
                <span style="color: #065f46; font-size: 12px; font-weight: bold;">✓ Active</span>
            </div>
        </div>
        <p style="margin: 0 0 10px 0; color: #0369a1; font-size: 14px;">Tailored insights for {industry.lower()} businesses</p>
        <div style="background: #f8fafc; padding: 10px; border-radius: 8px; border: 1px solid #e2e8f0;">
            <p style="margin: 0; color: #475569; font-size: 13px;"><strong>Available Insights:</strong> {smart_questions._get_industry_question_preview(industry)}</p>
        </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("🏢 **Standard Business Intelligence Mode** - Switch to a specific industry for tailored insights")
    
    # Question Availability Summary - Mobile Responsive
    total_available = sum(cat["available_count"] for cat in available_questions.values())
    total_questions = sum(cat["total_count"] for cat in available_questions.values())
    
    st.markdown(f"""
    <div style="background: linear-gradient(90deg, #fef3c7 0%, #fde68a 100%); padding: 25px; border-radius: 15px; text-align: center; border: 2px solid #f59e0b; margin: 20px 0;">
    <h3 style="margin: 0 0 15px 0; color: #92400e; font-size: 20px;">📊 Business Intelligence Dashboard</h3>
    <div style="background: rgba(255,255,255,0.3); padding: 15px; border-radius: 10px; margin: 10px 0;">
        <p style="margin: 0; color: #78350f; font-size: 18px; font-weight: bold;"><strong>{total_available} of {total_questions}</strong> insights available</p>
    </div>
    <p style="margin: 10px 0 0 0; color: #92400e; font-size: 14px;">Select a question below for detailed analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Professional Question Selection Interface
    st.markdown("---")
    
    if available_questions:
        # Create main tabs for available categories only
        available_categories = [cat for cat in available_questions.values() if cat["available_count"] > 0]
        category_tabs = st.tabs([f"{cat['title']} ({cat['available_count']})" for cat in available_categories])
        
        # Use session state to remember selected question
        if "selected_question" not in st.session_state:
            st.session_state.selected_question = None
        
        # Render each category tab
        for i, category in enumerate(available_categories):
            with category_tabs[i]:
                # Professional category header
                st.markdown(f"""
                <div style="background: #f8fafc; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                <h4 style="margin: 0 0 10px 0; color: #1e293b;">{category['title']}</h4>
                <p style="margin: 0; color: #64748b; font-size: 14px;">Click any question below for comprehensive analysis</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Mobile responsive question layout
                available_questions_list = [q for q in category["questions"].items() if q[1].get("available", True)]
                
                # Single column layout for mobile responsiveness
                for j, (q_id, question) in enumerate(available_questions_list):
                    # Professional question card with mobile-friendly styling
                    button_key = f"q_{category['title'].replace(' ', '_').lower()}_{q_id}"
                    
                    if st.button(
                        f"{question['icon']} {question['text']}", 
                        key=button_key,
                        use_container_width=True,
                        help=f"Get detailed analysis for: {question['text']}",
                        type="primary"
                    ):
                        st.session_state.selected_question = q_id
        
        # Show unavailable questions in a collapsible section
        all_unavailable = []
        for category in available_questions.values():
            for q_id, question in category["questions"].items():
                if not question.get("available", True):
                    all_unavailable.append((category['title'], question))
        
        if all_unavailable:
            with st.expander("🔍 View Unavailable Questions (Require Additional Data)", expanded=False):
                st.markdown("""
                <div style="background: #fef2f2; padding: 15px; border-radius: 8px; border-left: 4px solid #ef4444;">
                <p style="margin: 0; color: #991b1b; font-size: 14px;"><strong>Note:</strong> These questions require additional data mapping or more comprehensive datasets to provide meaningful insights.</p>
                </div>
                """, unsafe_allow_html=True)
                
                for category_title, question in all_unavailable:
                    st.markdown(f"""
                    <div style="background: #f9fafb; padding: 10px; border-radius: 5px; margin: 5px 0; border-left: 3px solid #d1d5db;">
                    <p style="margin: 0; color: #6b7280; font-size: 13px;"><strong>{category_title}:</strong> {question['icon']} {question['text']}</p>
                    <p style="margin: 2px 0 0 0; color: #9ca3af; font-size: 12px;">❌ {question.get('unavailable_reason', 'Data not available')}</p>
                    </div>
                    """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ **No questions available** with your current data context.")
        st.markdown("**To enable questions, ensure you have:**")
        st.markdown("- 📅 Date column mapped for trend analysis")
        st.markdown("- 💰 Amount column mapped for financial metrics")
        st.markdown("- 👥 Customer column mapped for customer insights")
        st.markdown("- 📦 Product column mapped for product analysis")
        st.markdown("- 🛣️ Channel column mapped for channel performance")

    # Professional Answer Display Section
    if st.session_state.selected_question:
        st.markdown("---")
        
        # Get the selected question details
        selected_question = st.session_state.selected_question
        question_details = None
        
        # Find the question details
        for category in available_questions.values():
            if selected_question in category["questions"]:
                question_details = category["questions"][selected_question]
                break
        
        # Professional Analysis Header - Mobile Responsive
        st.markdown(f"""
        <div style="background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%); padding: 25px; border-radius: 15px; color: white; margin-bottom: 20px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 15px;">
            <h2 style="margin: 0; color: white; font-size: 22px;">💡 Executive Intelligence Report</h2>
            <div style="background: rgba(255,255,255,0.2); padding: 8px 12px; border-radius: 8px;">
                <p style="margin: 0; color: white; font-size: 12px; font-weight: bold;">{datetime.now().strftime("%H:%M")}</p>
            </div>
        </div>
        <p style="margin: 0; font-size: 16px; opacity: 0.9;">{question_details['icon']} {question_details['text'] if question_details else selected_question}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Generate and display answer
        with st.spinner("🔍 Generating executive analysis..."):
            answer = smart_questions.generate_answer(selected_question, context_data, results)
        
        # Professional answer container
        st.markdown(f"""
        <div style="background: #ffffff; padding: 30px; border-radius: 15px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); margin: 20px 0;">
        {answer}
        </div>
        """, unsafe_allow_html=True)
        
        # Professional action buttons - Mobile Responsive
        st.markdown("---")
        
        # Mobile-friendly button layout
        if st.button("🔄 New Analysis", type="primary", use_container_width=True):
            st.session_state.selected_question = None
        
        # Secondary actions in a more compact layout
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📊 Data Context", type="secondary", use_container_width=True):
                st.session_state.show_context = not st.session_state.get("show_context", False)
        
        with col2:
            if st.button("💾 Save Report", type="secondary", use_container_width=True):
                # Save answer to session state for potential export
                if "saved_answers" not in st.session_state:
                    st.session_state.saved_answers = []
                st.session_state.saved_answers.append({
                    "question": question_details["text"] if question_details else selected_question,
                    "answer": answer,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                st.success("📝 Report saved to executive summary")
        
        # Export button in its own row for mobile
        if st.button("📋 Export Report", type="secondary", use_container_width=True):
            st.info("📄 Export functionality coming soon")
    
    # Professional Context Display (only when requested)
    if st.session_state.get("show_context", False):
        st.markdown("---")
        st.markdown(f"""
        <div style="background: linear-gradient(90deg, #f0fdf4 0%, #dcfce7 100%); padding: 25px; border-radius: 15px; border: 2px solid #22c55e;">
        <h3 style="margin: 0 0 15px 0; color: #166534;">📊 Data Foundation & Context</h3>
        <p style="margin: 0; color: #15803d; font-size: 14px;">This analysis is based on your business data and market context</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Mobile responsive context layout
        st.markdown("""
        <div style="background: #f8fafc; padding: 20px; border-radius: 10px; border: 1px solid #e2e8f0; margin-bottom: 15px;">
        <h4 style="margin: 0 0 15px 0; color: #1e293b;">Business Context</h4>
        """, unsafe_allow_html=True)
        st.markdown(context_data["context_md"])
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: #f8fafc; padding: 20px; border-radius: 10px; border: 1px solid #e2e8f0;">
        <h4 style="margin: 0 0 15px 0; color: #1e293b;">Recent Activity Summary</h4>
        """, unsafe_allow_html=True)
        st.markdown(context_data["sql_md"])
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Professional hide button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("👁️ Hide Data Context", type="secondary", use_container_width=True):
                st.session_state.show_context = False
    
    # Professional Saved Reports Section
    if st.session_state.get("saved_answers"):
        st.markdown("---")
        st.markdown(f"""
        <div style="background: linear-gradient(90deg, #fef3c7 0%, #fde68a 100%); padding: 25px; border-radius: 15px; border: 2px solid #f59e0b;">
        <h3 style="margin: 0 0 10px 0; color: #92400e;">💾 Executive Summary Reports</h3>
        <p style="margin: 0; color: #78350f; font-size: 14px;">Your saved intelligence reports for executive review</p>
        </div>
        """, unsafe_allow_html=True)
        
        for i, saved in enumerate(st.session_state.saved_answers):
            with st.expander(f"📋 {saved['question']} - {saved['timestamp']}", expanded=False):
                st.markdown(f"""
                <div style="background: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #e2e8f0; margin: 10px 0;">
                {saved['answer']}
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns([1, 1, 1])
                with col2:
                    if st.button(f"🗑️ Remove Report", key=f"delete_{i}", type="secondary", use_container_width=True):
                        st.session_state.saved_answers.pop(i)
