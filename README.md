# OmniInsights — Full Folder (AI Enabled)

## 🚀 **What's New in v2.1**
- **🤖 Smart Questions System**: No more external API calls! Get instant, intelligent business insights
- **📊 25+ Pre-crafted Questions**: Categorized by business function (Performance, Customers, Products, Operations, Strategy)
- **💡 Context-Aware Answers**: Intelligent responses based on your actual data
- **🎯 Beautiful UI**: Organized tabs and intuitive question selection
- **⚡ Instant Results**: No waiting for API responses or rate limits

## 1) Install dependencies
```bash
pip install -r requirements.txt
```

## 2) Run the app
```bash
streamlit run app.py
```

## 🎯 **Smart Questions Categories**

### 📊 Performance & Growth
- How is our revenue performing?
- What's our month-over-month growth rate?
- Do we see any seasonal patterns?
- Are there any unusual trends or anomalies?

### 👥 Customer Insights
- How fast are we acquiring new customers?
- What's our customer retention rate?
- What's the average customer lifetime value?
- How should we segment our customers?

### 📦 Product Performance
- Which products are our best performers?
- How diverse is our product portfolio?
- Should we adjust our inventory strategy?

### ⚙️ Operations & Efficiency
- How efficient are our order operations?
- Which sales channels perform best?
- What can we expect in the next 3 months?

### 🎯 Strategic Insights
- Where are our biggest growth opportunities?
- What risks should we be aware of?
- How do we compare to industry standards?
- What are the top 3 actions we should take?

## 🔧 **How It Works**
1. **Upload Data**: CSV, Excel, or Parquet files
2. **Map Columns**: Automatic suggestions for business concepts
3. **Select Questions**: Choose from curated business intelligence questions
4. **Get Insights**: Instant, contextual answers based on your data
5. **Export Reports**: Generate beautiful HTML reports

## 💡 **Why This Approach is Better**
- ✅ **No API Keys**: Works offline, no external dependencies
- ✅ **Instant Results**: No waiting for API responses
- ✅ **Context-Aware**: Answers based on your actual business data
- ✅ **Professional Quality**: Pre-crafted, business-focused responses
- ✅ **Scalable**: No rate limits or usage costs
- ✅ **Reliable**: Consistent quality regardless of external service status

## 📁 **Project Structure**
```
omni_insights_full_ai/
├── app.py                 # Main Streamlit application
├── core/                  # Core business logic
│   ├── smart_questions.py # 🤖 NEW: Smart questions system
│   ├── context.py         # Data context building
│   ├── mapping.py         # Column mapping logic
│   └── ...
├── ui/                    # User interface components
├── insights/              # Business analytics modules
└── reports/               # Report generation
```

## 🎉 **Ready to Use**
Your OmniInsights app is now powered by intelligent, context-aware business intelligence that works instantly without any external dependencies!
