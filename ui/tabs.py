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

    st.subheader("🤖 Smart Business Intelligence")
    st.caption("Get instant, intelligent answers to your business questions without external APIs.")
    
    # Add a navigation helper to ensure users can always get back to AI Assistant
    if st.button("🔄 Refresh AI Assistant", help="Click if you're having navigation issues"):
        st.session_state.selected_question = None
        st.rerun()

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
    
    # Show industry context with more detailed information
    if industry != "generic":
        industry_icons = {"retail": "🏪", "saas": "☁️", "marketplace": "🛒"}
        industry_names = {"retail": "Retail", "saas": "SaaS", "marketplace": "Marketplace"}
        
        # Get industry-specific question count
        industry_questions = {
            "retail": 4,  # store_performance, inventory_turnover, seasonal_planning, promotional_effectiveness
            "saas": 5,    # mrr_growth, churn_analysis, feature_adoption, pricing_optimization, customer_success
            "marketplace": 5  # seller_performance, buyer_behavior, network_effects, commission_optimization, liquidity_analysis
        }
        
        question_count = industry_questions.get(industry, 0)
        
        st.success(f"""
        {industry_icons.get(industry, '🏢')} **{industry_names.get(industry, 'Business')} Industry Mode Active**
        
        You have access to **{question_count} additional industry-specific questions** plus all standard business intelligence questions.
        
        **Industry-specific insights include:**
        {self._get_industry_question_preview(industry)}
        """)
    else:
        st.info("🏢 **Generic Mode**: You're using standard business intelligence questions. Switch to a specific industry for tailored insights!")
    
    # Create a beautiful question selector
    st.markdown("### 📋 Select Your Question")
    
    # Show question availability stats
    total_available = sum(cat["available_count"] for cat in available_questions.values())
    total_questions = sum(cat["total_count"] for cat in available_questions.values())
    st.success(f"🎯 **{total_available} out of {total_questions} questions available** based on your data context")
    
    # Create tabs for each category that has available questions
    if available_questions:
        category_tabs = st.tabs([f"{cat['title']} ({cat['available_count']}/{cat['total_count']})" for cat in available_questions.values()])
        
        # Use session state to remember selected question
        if "selected_question" not in st.session_state:
            st.session_state.selected_question = None
        
        # Render each category tab
        for i, (category_key, category) in enumerate(available_questions.items()):
            with category_tabs[i]:
                st.markdown(f"**{category['title']}**")
                st.caption(f"Click on any question to get an intelligent analysis. {category['available_count']} questions available.")
                
                # Create columns for better layout
                cols = st.columns(2)
                for j, (q_id, question) in enumerate(category["questions"].items()):
                    col_idx = j % 2
                    with cols[col_idx]:
                        if question.get("available", True):
                            # Available question - show as clickable button
                            button_key = f"q_{category_key}_{q_id}"
                            
                            # Use a simple button approach that works reliably
                            if st.button(
                                f"{question['icon']} {question['text']}", 
                                key=button_key,
                                use_container_width=True,
                                help=f"Get detailed analysis for: {question['text']}",
                                type="secondary"
                            ):
                                # Store the selected question
                                st.session_state.selected_question = q_id
                                st.rerun()
                        else:
                            # Unavailable question - show as disabled with reason
                            st.markdown(f"~~{question['icon']} {question['text']}~~")
                            st.caption(f"❌ **Unavailable**: {question.get('unavailable_reason', 'Data not available')}")
    else:
        st.warning("⚠️ **No questions available** with your current data context.")
        st.markdown("**To enable questions, ensure you have:**")
        st.markdown("- 📅 Date column mapped for trend analysis")
        st.markdown("- 💰 Amount column mapped for financial metrics")
        st.markdown("- 👥 Customer column mapped for customer insights")
        st.markdown("- 📦 Product column mapped for product analysis")
        st.markdown("- 🛣️ Channel column mapped for channel performance")

    # Display the answer if a question is selected
    if st.session_state.selected_question:
        st.markdown("---")
        st.markdown("### 💡 **Intelligent Analysis**")
        
        # Get the selected question details
        selected_question = st.session_state.selected_question
        question_details = None
        
        # Find the question details
        for category in available_questions.values():
            if selected_question in category["questions"]:
                question_details = category["questions"][selected_question]
                break
        
        if question_details:
            st.markdown(f"**🎯 Question**: {question_details['icon']} {question_details['text']}")
        
        # Generate answer instantly using pre-built context
        with st.spinner("🔍 Generating intelligent analysis..."):
            answer = smart_questions.generate_answer(selected_question, context_data, results)
        
        # Display the answer in a beautiful container
        st.markdown(answer)
        
        # Add action buttons
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("🔄 Ask Another Question", type="secondary"):
                st.session_state.selected_question = None
                st.rerun()
        with col2:
            if st.button("📊 Show Data Context", type="secondary"):
                st.session_state.show_context = not st.session_state.get("show_context", False)
                st.rerun()
        with col3:
            if st.button("💾 Save Answer", type="secondary"):
                # Save answer to session state for potential export
                if "saved_answers" not in st.session_state:
                    st.session_state.saved_answers = []
                st.session_state.saved_answers.append({
                    "question": question_details["text"] if question_details else selected_question,
                    "answer": answer,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                st.success("Answer saved! 📝")
    
    # Show context information in an expander (only when requested)
    if st.session_state.get("show_context", False):
        st.markdown("---")
        st.markdown("### 📊 **Data Context Available**")
        st.markdown("**Business Context:**")
        st.markdown(context_data["context_md"])
        st.markdown("**Recent Activity Summary:**")
        st.markdown(context_data["sql_md"])
        
        # Add a button to hide context
        if st.button("👁️ Hide Context"):
            st.session_state.show_context = False
            st.rerun()
    
    # Show saved answers if any
    if st.session_state.get("saved_answers"):
        st.markdown("---")
        st.markdown("### 💾 **Saved Answers**")
        for i, saved in enumerate(st.session_state.saved_answers):
            with st.expander(f"📝 {saved['question']} ({saved['timestamp']})", expanded=False):
                st.markdown(saved['answer'])
                if st.button(f"🗑️ Delete", key=f"delete_{i}"):
                    st.session_state.saved_answers.pop(i)
                    st.rerun()
