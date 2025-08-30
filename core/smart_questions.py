"""
Smart question system with pre-crafted, intelligent answers based on business analytics context.
Replaces external API calls with beautiful, contextual responses.
"""

from typing import Dict, List, Optional, Tuple
import pandas as pd
from datetime import datetime
import numpy as np

class SmartQuestionSystem:
    """Intelligent question answering system for business analytics."""
    
    def __init__(self, industry: str = "generic"):
        self.industry = industry.lower()
        self.questions = self._build_question_catalog()
    
    def _build_question_catalog(self) -> Dict[str, Dict]:
        """Build the comprehensive question catalog with categories."""
        return {
            "performance": {
                "title": "📊 Performance & Growth",
                "questions": {
                    "revenue_trend": {
                        "text": "How is our revenue performing?",
                        "icon": "📈",
                        "category": "performance"
                    },
                    "growth_rate": {
                        "text": "What's our month-over-month growth rate?",
                        "icon": "🚀",
                        "category": "performance"
                    },
                    "seasonality": {
                        "text": "Do we see any seasonal patterns?",
                        "icon": "🌦️",
                        "category": "performance"
                    },
                    "anomalies": {
                        "text": "Are there any unusual trends or anomalies?",
                        "icon": "⚠️",
                        "category": "performance"
                    }
                }
            },
            "customers": {
                "title": "👥 Customer Insights",
                "questions": {
                    "customer_growth": {
                        "text": "How fast are we acquiring new customers?",
                        "icon": "👤",
                        "category": "customers"
                    },
                    "retention": {
                        "text": "What's our customer retention rate?",
                        "icon": "🔄",
                        "category": "customers"
                    },
                    "lifetime_value": {
                        "text": "What's the average customer lifetime value?",
                        "icon": "💰",
                        "category": "customers"
                    },
                    "segments": {
                        "text": "How should we segment our customers?",
                        "icon": "🏷️",
                        "category": "customers"
                    }
                }
            },
            "products": {
                "title": "📦 Product Performance",
                "questions": {
                    "top_products": {
                        "text": "Which products are our best performers?",
                        "icon": "⭐",
                        "category": "products"
                    },
                    "product_mix": {
                        "text": "How diverse is our product portfolio?",
                        "icon": "🎯",
                        "category": "products"
                    },
                    "inventory": {
                        "text": "Should we adjust our inventory strategy?",
                        "icon": "📦",
                        "category": "products"
                    }
                }
            },
            "operations": {
                "title": "⚙️ Operations & Efficiency",
                "questions": {
                    "order_efficiency": {
                        "text": "How efficient are our order operations?",
                        "icon": "⚡",
                        "category": "operations"
                    },
                    "channel_performance": {
                        "text": "Which sales channels perform best?",
                        "icon": "🛣️",
                        "category": "operations"
                    },
                    "forecasting": {
                        "text": "What can we expect in the next 3 months?",
                        "icon": "🔮",
                        "category": "operations"
                    }
                }
            },
            "strategy": {
                "title": "🎯 Strategic Insights",
                "questions": {
                    "opportunities": {
                        "text": "Where are our biggest growth opportunities?",
                        "icon": "💡",
                        "category": "strategy"
                    },
                    "risks": {
                        "text": "What risks should we be aware of?",
                        "icon": "🚨",
                        "category": "strategy"
                    },
                    "benchmarks": {
                        "text": "How do we compare to industry standards?",
                        "icon": "📊",
                        "category": "strategy"
                    },
                    "recommendations": {
                        "text": "What are the top 3 actions we should take?",
                        "icon": "✅",
                        "category": "strategy"
                    }
                }
            },
            "retail_specific": {
                "title": "🏪 Retail-Specific Insights",
                "questions": {
                    "store_performance": {
                        "text": "How are our physical stores performing?",
                        "icon": "🏪",
                        "category": "retail_specific"
                    },
                    "inventory_turnover": {
                        "text": "What's our inventory turnover rate?",
                        "icon": "🔄",
                        "category": "retail_specific"
                    },
                    "seasonal_planning": {
                        "text": "How should we plan for seasonal demand?",
                        "icon": "📅",
                        "category": "retail_specific"
                    },
                    "promotional_effectiveness": {
                        "text": "How effective are our promotions?",
                        "icon": "🎯",
                        "category": "retail_specific"
                    }
                }
            },
            "saas_specific": {
                "title": "☁️ SaaS-Specific Insights",
                "questions": {
                    "mrr_growth": {
                        "text": "How is our Monthly Recurring Revenue growing?",
                        "icon": "📈",
                        "category": "saas_specific"
                    },
                    "churn_analysis": {
                        "text": "What's causing customer churn?",
                        "icon": "📉",
                        "category": "saas_specific"
                    },
                    "feature_adoption": {
                        "text": "Which features drive the most engagement?",
                        "icon": "🔧",
                        "category": "saas_specific"
                    },
                    "pricing_optimization": {
                        "text": "How can we optimize our pricing strategy?",
                        "icon": "💰",
                        "category": "saas_specific"
                    },
                    "customer_success": {
                        "text": "How effective is our customer success program?",
                        "icon": "🎯",
                        "category": "saas_specific"
                    }
                }
            },
            "marketplace_specific": {
                "title": "🛒 Marketplace-Specific Insights",
                "questions": {
                    "seller_performance": {
                        "text": "How are our sellers performing?",
                        "icon": "👥",
                        "category": "marketplace_specific"
                    },
                    "buyer_behavior": {
                        "text": "What drives buyer purchasing decisions?",
                        "icon": "🛍️",
                        "category": "marketplace_specific"
                    },
                    "network_effects": {
                        "text": "Are we experiencing network effects?",
                        "icon": "🌐",
                        "category": "marketplace_specific"
                    },
                    "commission_optimization": {
                        "text": "How can we optimize our commission structure?",
                        "icon": "💸",
                        "category": "marketplace_specific"
                    },
                    "liquidity_analysis": {
                        "text": "How liquid is our marketplace?",
                        "icon": "💧",
                        "category": "marketplace_specific"
                    }
                }
            }
        }
    
    def get_all_questions(self) -> Dict[str, Dict]:
        """Get the complete question catalog."""
        return self.questions
    
    def get_question_by_id(self, question_id: str) -> Optional[Dict]:
        """Get a specific question by its ID."""
        for category in self.questions.values():
            if question_id in category["questions"]:
                return category["questions"][question_id]
        return None
    
    def generate_answer(self, question_id: str, context_data: Dict, results: Dict) -> str:
        """Generate an intelligent answer based on the question and context data."""
        question = self.get_question_by_id(question_id)
        if not question:
            return "❌ Question not found."
        
        # Get the appropriate answer generator
        answer_generator = getattr(self, f"_answer_{question_id}", None)
        if answer_generator:
            return answer_generator(context_data, results)
        else:
            return self._generate_generic_answer(question, context_data, results)
    
    def _answer_revenue_trend(self, context: Dict, results: Dict) -> str:
        """Generate revenue trend analysis."""
        # Handle nested KPI structure
        kpis_data = results.get("kpis", {})
        if isinstance(kpis_data, dict) and "kpis" in kpis_data:
            kpis = kpis_data["kpis"]
        else:
            kpis = kpis_data
        
        trend_data = results.get("trend", {})
        
        # Handle different trend data structures
        if "table" in trend_data:
            trend_df = trend_data["table"]
            if isinstance(trend_df, pd.DataFrame) and not trend_df.empty:
                trend_points = trend_df.to_dict('records')
            else:
                trend_points = []
        else:
            trend_points = trend_data.get("trend", [])
        
        total_revenue = kpis.get("total_sales", 0) if kpis else 0
        
        if not trend_points or len(trend_points) < 2:
            # Get context info to help debug
            context_shape = context.get("shape", "Unknown")
            context_kpis = context.get("context_md", "")
            
            return f"""📊 **Revenue Trend Analysis**

**Data Status**: *Insufficient data to analyze revenue trends*

**Available Trend Points**: {len(trend_points) if trend_points else 0}
**Required**: At least 2 months of data
**Dataset Shape**: {context_shape}

**Possible Causes**:
1. **Column Mapping**: Amount column may be mapped incorrectly
2. **Data Processing**: Trend data may not be aggregating properly
3. **Date Format**: Date column may not be recognized correctly

**Troubleshooting**:
- **Amount Column**: Should be mapped to "Total Amount" not "Price per Unit"
- **Date Column**: Ensure dates are in a recognized format
- **Data Range**: Verify your data spans multiple months

**Current Context**: {context_kpis[:300]}...

**Note**: Your dataset shows 12 months of data in the context, but the trend analysis isn't receiving it properly. Check your column mapping."""
        
        # Calculate growth metrics
        recent = trend_points[-1] if trend_points else None
        previous = trend_points[-2] if len(trend_points) > 1 else None
        
        if recent and previous:
            try:
                growth_pct = ((recent["revenue"] - previous["revenue"]) / previous["revenue"]) * 100
                growth_direction = "📈" if growth_pct > 0 else "📉"
                growth_text = f"{growth_direction} **{growth_pct:.1f}%** month-over-month"
            except:
                growth_text = "📊 *Growth calculation unavailable*"
        else:
            growth_text = "📊 *Growth calculation unavailable*"
        
        return f"""📊 **Revenue Trend Analysis**

**Current Status**: {growth_text}

**Key Metrics**:
- Total Revenue: **${total_revenue:,.0f}**
- Trend Points: **{len(trend_points)}** months of data
- Latest Month: **{recent['month'] if recent else 'N/A'}**

**Insight**: {self._get_trend_insight(trend_points)}"""
    
    def _answer_growth_rate(self, context: Dict, results: Dict) -> str:
        """Generate growth rate analysis."""
        trend_data = results.get("trend", {})
        
        # Handle different trend data structures
        if "table" in trend_data:
            trend_df = trend_data["table"]
            if isinstance(trend_df, pd.DataFrame) and not trend_df.empty:
                trend_points = trend_df.to_dict('records')
            else:
                trend_points = []
        else:
            trend_points = trend_data.get("trend", [])
        
        # Debug info for troubleshooting
        debug_info = f"""
**Debug Information**:
- Trend data type: {type(trend_data)}
- Trend table exists: {'table' in trend_data}
- Trend points count: {len(trend_points)}
- First few trend points: {trend_points[:3] if trend_points else 'None'}
"""
        
        if len(trend_points) < 3:
            # Get context info to help debug
            context_shape = context.get("shape", "Unknown")
            context_kpis = context.get("context_md", "")
            
            return f"""🚀 **Growth Rate Analysis**

**Data Status**: *Insufficient trend data for analysis*

**Available Trend Points**: {len(trend_points)} data points
**Required**: At least 3 months of data
**Dataset Shape**: {context_shape}

**Possible Causes**:
1. **Date Filtering**: Your global date filters may be too restrictive
2. **Data Aggregation**: Monthly data may not be aggregating properly
3. **Column Mapping**: Date or amount columns may have issues

**Troubleshooting Steps**:
1. **Expand Date Range**: Try widening your date filters
2. **Check Data**: Verify your date column contains valid dates
3. **Verify Mapping**: Ensure date and amount columns are correctly mapped

**Current Context**: {context_kpis[:200]}...

**Note**: Your dataset appears to have sufficient data, but the trend analysis requires monthly aggregated data with at least 3 distinct months.

{debug_info}"""
        
        # Calculate compound monthly growth rate
        try:
            first_month = trend_points[0]["revenue"]
            last_month = trend_points[-1]["revenue"]
            months = len(trend_points) - 1
            
            if first_month > 0:
                cmgr = ((last_month / first_month) ** (1/months) - 1) * 100
                growth_category = self._categorize_growth(cmgr)
            else:
                cmgr = 0
                growth_category = "📊 *Insufficient data*"
        except Exception as e:
            cmgr = 0
            growth_category = f"📊 *Calculation error: {str(e)}*"
        
        return f"""🚀 **Growth Rate Analysis**

**Compound Monthly Growth Rate**: **{cmgr:.1f}%**

**Growth Category**: {growth_category}

**Monthly Breakdown**:
{self._format_trend_summary(trend_points)}

**Recommendation**: {self._get_growth_recommendation(cmgr)}"""
    
    def _answer_customer_growth(self, context: Dict, results: Dict) -> str:
        """Generate customer growth analysis."""
        # Handle nested KPI structure
        kpis_data = results.get("kpis", {})
        if isinstance(kpis_data, dict) and "kpis" in kpis_data:
            kpis = kpis_data["kpis"]
        else:
            kpis = kpis_data
        
        customer_data = results.get("repeat_rate", {})
        
        total_customers = kpis.get("num_customers", 0) if kpis else 0
        repeat_rate = customer_data.get("repeat_rate", 0)
        
        return f"""👤 **Customer Growth Analysis**

**Current Metrics**:
- Total Customers: **{total_customers:,}**
- Repeat Customer Rate: **{repeat_rate*100:.1f}%**

**Customer Health Indicators**:
- 🟢 **Strong** if repeat rate > 30%
- 🟡 **Good** if repeat rate 15-30%
- 🔴 **Needs attention** if repeat rate < 15%

**Growth Insights**:
{self._get_customer_insights(repeat_rate, total_customers)}"""
    
    def _answer_top_products(self, context: Dict, results: Dict) -> str:
        """Generate top products analysis."""
        products_data = results.get("top_products", {})
        top_products = products_data.get("table", pd.DataFrame())
        
        if top_products.empty:
            return "⭐ **Top Products Analysis**\n\n*No product data available for analysis.*"
        
        return f"""⭐ **Top Products Analysis**

**Top Performers**:
{self._format_top_products(top_products)}

**Product Strategy Insights**:
- 🎯 **Focus** on top 20% of products (Pareto principle)
- 📦 **Inventory** optimization for high-demand items
- 🚀 **Marketing** emphasis on proven winners

**Recommendations**:
{self._get_product_recommendations(top_products)}"""
    
    def _answer_forecasting(self, context: Dict, results: Dict) -> str:
        """Generate forecasting analysis."""
        forecast_data = results.get("forecast", {})
        forecast_df = forecast_data.get("forecast", pd.DataFrame())
        
        if forecast_df.empty:
            return "🔮 **Forecasting Analysis**\n\n*Insufficient data for reliable forecasting.*"
        
        return f"""🔮 **Forecasting Analysis**

**Next 3 Months Projection**:
{self._format_forecast(forecast_df)}

**Forecast Confidence**: 
- 📊 Based on Moving Average (MA3) methodology
- ⚠️ Simple baseline - consider external factors
- 🔄 Update monthly for accuracy

**Planning Recommendations**:
- 📈 **Prepare** for projected growth
- 💰 **Budget** according to forecasts
- 📦 **Inventory** planning based on trends"""
    
    def _answer_opportunities(self, context: Dict, results: Dict) -> str:
        """Generate growth opportunities analysis."""
        kpis = results.get("kpis", {})
        trend_data = results.get("trend", {})
        customer_data = results.get("repeat_rate", {})
        
        total_revenue = kpis.get("total_revenue", 0)
        repeat_rate = customer_data.get("repeat_rate", 0)
        trend_points = trend_data.get("trend", [])
        
        opportunities = []
        
        # Revenue opportunities
        if total_revenue > 0:
            opportunities.append("💰 **Revenue Growth**: Focus on high-value customers and products")
        
        # Customer retention opportunities
        if repeat_rate < 0.3:
            opportunities.append("🔄 **Customer Retention**: Implement loyalty programs and engagement strategies")
        
        # Product opportunities
        products_data = results.get("top_products", {})
        if products_data.get("table") is not None and not products_data["table"].empty:
            opportunities.append("📦 **Product Optimization**: Expand successful product lines and improve underperformers")
        
        # Seasonal opportunities
        if len(trend_points) >= 12:
            opportunities.append("🌦️ **Seasonal Planning**: Leverage seasonal patterns for marketing and inventory")
        
        if not opportunities:
            opportunities = ["📊 **Data Analysis**: Continue monitoring key metrics for emerging opportunities"]
        
        return f"""💡 **Growth Opportunities Analysis**

**Top Opportunities Identified**:
{chr(10).join(f"- {opp}" for opp in opportunities[:3])}

**Priority Actions**:
1. 🎯 **Immediate** (Next 30 days): Focus on highest-impact opportunities
2. 📈 **Short-term** (Next 90 days): Implement systematic improvements
3. 🚀 **Long-term** (Next 6 months): Build sustainable growth foundations

**Success Metrics**:
- Revenue growth rate
- Customer retention improvement
- Product performance optimization"""
    
    def _answer_recommendations(self, context: Dict, results: Dict) -> str:
        """Generate top 3 strategic recommendations."""
        kpis = results.get("kpis", {})
        customer_data = results.get("repeat_rate", {})
        trend_data = results.get("trend", {})
        
        recommendations = []
        
        # Analyze data and generate recommendations
        if customer_data.get("repeat_rate", 0) < 0.25:
            recommendations.append("🔄 **Improve Customer Retention**\n   Implement customer success programs, personalized communication, and loyalty rewards to increase repeat purchase rate.")
        
        if trend_data.get("trend"):
            trend_points = trend_data["trend"]
            if len(trend_points) >= 2:
                recent_growth = self._calculate_recent_growth(trend_points)
                if recent_growth < 0.05:  # Less than 5% growth
                    recommendations.append("📈 **Boost Revenue Growth**\n   Focus on upselling, cross-selling, and optimizing pricing strategies to accelerate revenue growth.")
        
        # Add general recommendations if we don't have enough specific ones
        while len(recommendations) < 3:
            if len(recommendations) == 0:
                recommendations.append("📊 **Data-Driven Decision Making**\n   Establish regular reporting and monitoring systems to track KPIs and make informed business decisions.")
            elif len(recommendations) == 1:
                recommendations.append("🎯 **Customer Experience Optimization**\n   Analyze customer journey touchpoints and optimize for better conversion and satisfaction.")
            else:
                recommendations.append("🚀 **Operational Efficiency**\n   Streamline processes, reduce costs, and improve productivity across all business operations.")
        
        return f"""✅ **Top 3 Strategic Recommendations**

{chr(10).join(f"{i+1}. {rec}" for i, rec in enumerate(recommendations[:3]))}

**Implementation Timeline**:
- 🚀 **Week 1-2**: Planning and resource allocation
- 📋 **Week 3-8**: Implementation and testing
- 📊 **Week 9-12**: Monitoring and optimization

**Success Metrics**:
- Track progress against specific KPIs
- Regular review and adjustment
- Celebrate wins and learn from challenges"""
    
    def _answer_anomalies(self, context: Dict, results: Dict) -> str:
        """Generate anomalies analysis."""
        trend_data = results.get("trend", {})
        
        # Handle different trend data structures
        if "table" in trend_data:
            trend_df = trend_data["table"]
            if isinstance(trend_df, pd.DataFrame) and not trend_df.empty:
                trend_points = trend_df.to_dict('records')
            else:
                trend_points = []
        else:
            trend_points = trend_data.get("trend", [])
        
        if not trend_points or len(trend_points) < 3:
            return "⚠️ **Anomalies Analysis**\n\n*Need at least 3 months of data to detect anomalies.*"
        
        # Calculate statistical measures for anomaly detection
        revenues = [point.get("revenue", 0) for point in trend_points]
        mean_revenue = np.mean(revenues)
        std_revenue = np.std(revenues)
        
        anomalies = []
        for point in trend_points:
            revenue = point.get("revenue", 0)
            month = point.get("month", "Unknown")
            z_score = abs((revenue - mean_revenue) / std_revenue) if std_revenue > 0 else 0
            
            if z_score > 2.0:  # More than 2 standard deviations
                direction = "📈 Above average" if revenue > mean_revenue else "📉 Below average"
                anomalies.append(f"- **{month}**: ${revenue:,.0f} ({direction})")
        
        if not anomalies:
            return f"""⚠️ **Anomalies Analysis**

**Status**: No significant anomalies detected

**Statistical Summary**:
- Average Monthly Revenue: **${mean_revenue:,.0f}**
- Standard Deviation: **${std_revenue:,.0f}**
- Data Points Analyzed: **{len(trend_points)}** months

**Analysis**: Your revenue shows consistent patterns within normal statistical ranges. This indicates stable business operations."""
        
        return f"""⚠️ **Anomalies Analysis**

**Anomalies Detected**:
{chr(10).join(anomalies)}

**Statistical Context**:
- Average Monthly Revenue: **${mean_revenue:,.0f}**
- Standard Deviation: **${std_revenue:,.0f}**
- Anomaly Threshold: **2+ standard deviations**

**Recommendations**:
- 🔍 **Investigate** causes of unusual performance
- 📊 **Analyze** external factors (seasonality, market changes)
- 🎯 **Leverage** positive anomalies for growth strategies
- ⚠️ **Address** negative anomalies promptly"""
    
    def _answer_seasonality(self, context: Dict, results: Dict) -> str:
        """Generate seasonality analysis."""
        trend_data = results.get("trend", {})
        
        # Handle different trend data structures
        if "table" in trend_data:
            trend_df = trend_data["table"]
            if isinstance(trend_df, pd.DataFrame) and not trend_df.empty:
                trend_points = trend_df.to_dict('records')
            else:
                trend_points = []
        else:
            trend_points = trend_data.get("trend", [])
        
        if len(trend_points) < 12:
            # Add debugging information
            debug_info = f"""
**Debug Information**:
- Trend data type: {type(trend_data)}
- Trend table exists: {'table' in trend_data}
- Trend points count: {len(trend_points)}
- First few trend points: {trend_points[:3] if trend_points else 'None'}
- Data range: {trend_points[0].get('month', 'Start')} to {trend_points[-1].get('month', 'End') if trend_points else 'N/A'}
"""
            return f"🌦️ **Seasonality Analysis**\n\n*Need at least 12 months of data to detect seasonal patterns. Currently have {len(trend_points)} months of data.*\n\n{debug_info}"
        
        # Group by month to identify seasonal patterns
        monthly_avg = {}
        for point in trend_points:
            month = point.get("month", "")
            
            # Handle different month formats (Timestamp, string, etc.)
            if hasattr(month, 'month'):  # Pandas Timestamp object
                month_name = str(month.month).zfill(2)  # Get month as MM format
            elif isinstance(month, str) and len(month) >= 7:  # String format YYYY-MM
                month_name = month.split("-")[1]  # Extract MM
            else:
                continue  # Skip invalid month formats
            
            revenue = point.get("revenue", 0)
            if month_name not in monthly_avg:
                monthly_avg[month_name] = []
            monthly_avg[month_name].append(revenue)
        
        if not monthly_avg:
            return "🌦️ **Seasonality Analysis**\n\n*Unable to analyze seasonal patterns with current data format.*"
        
        # Calculate average revenue by month
        seasonal_pattern = {}
        for month, revenues in monthly_avg.items():
            seasonal_pattern[month] = np.mean(revenues)
        
        # Find high and low seasons
        avg_revenue = np.mean(list(seasonal_pattern.values()))
        high_season = max(seasonal_pattern.items(), key=lambda x: x[1])
        low_season = min(seasonal_pattern.items(), key=lambda x: x[1])
        
        # Determine seasonality strength
        seasonal_variance = np.var(list(seasonal_pattern.values()))
        total_variance = np.var([point.get("revenue", 0) for point in trend_points])
        seasonality_strength = seasonal_variance / total_variance if total_variance > 0 else 0
        
        if seasonality_strength < 0.1:
            strength_text = "📊 **Weak seasonality** - revenue is relatively consistent throughout the year"
        elif seasonality_strength < 0.3:
            strength_text = "🌤️ **Moderate seasonality** - some seasonal variation is present"
        else:
            strength_text = "🌦️ **Strong seasonality** - significant seasonal patterns detected"
        
        # Convert month numbers to month names
        month_names = {
            "01": "January", "02": "February", "03": "March", "04": "April",
            "05": "May", "06": "June", "07": "July", "08": "August",
            "09": "September", "10": "October", "11": "November", "12": "December"
        }
        
        peak_month = month_names.get(high_season[0], f"Month {high_season[0]}")
        low_month = month_names.get(low_season[0], f"Month {low_season[0]}")
        
        return f"""🌦️ **Seasonality Analysis**

**Seasonal Strength**: {strength_text}

**Peak Season**: **{peak_month}** - Average Revenue: **${high_season[1]:,.0f}**
**Low Season**: **{low_month}** - Average Revenue: **${low_season[1]:,.0f}**
**Overall Average**: **${avg_revenue:,.0f}**

**Seasonal Variation**: **{seasonality_strength:.1%}** of total variance

**Business Implications**:
- 📈 **Plan** inventory and marketing for peak seasons
- 💰 **Optimize** pricing during high-demand periods
- 📦 **Prepare** for low-season challenges
- 🎯 **Leverage** seasonal patterns for growth strategies"""
    
    def _answer_customer_lifetime_value(self, context: Dict, results: Dict) -> str:
        """Generate customer lifetime value analysis."""
        kpis = results.get("kpis", {})
        customer_data = results.get("repeat_rate", {})
        
        total_revenue = kpis.get("total_revenue", 0)
        total_customers = kpis.get("num_customers", 0)
        repeat_rate = customer_data.get("repeat_rate", 0)
        
        if total_customers == 0:
            return "💰 **Customer Lifetime Value Analysis**\n\n*No customer data available for analysis.*"
        
        # Calculate basic CLV metrics
        avg_revenue_per_customer = total_revenue / total_customers if total_customers > 0 else 0
        
        # Estimate CLV based on repeat rate
        if repeat_rate > 0:
            # Simple CLV calculation: avg_revenue * (1 + repeat_rate + repeat_rate^2 + ...)
            # This assumes customers who repeat will continue at similar rates
            clv_multiplier = 1 / (1 - repeat_rate) if repeat_rate < 1 else 5  # Cap at 5x
            estimated_clv = avg_revenue_per_customer * clv_multiplier
        else:
            estimated_clv = avg_revenue_per_customer
        
        # Categorize CLV
        if estimated_clv > 1000:
            clv_category = "🏆 **Premium** - High-value customer base"
        elif estimated_clv > 500:
            clv_category = "💎 **High** - Strong customer value"
        elif estimated_clv > 100:
            clv_category = "📊 **Good** - Solid customer value"
        else:
            clv_category = "📈 **Growth** - Opportunity to increase value"
        
        return f"""💰 **Customer Lifetime Value Analysis**

**Current Metrics**:
- Total Revenue: **${total_revenue:,.0f}**
- Total Customers: **{total_customers:,}**
- Average Revenue per Customer: **${avg_revenue_per_customer:,.0f}**
- Repeat Customer Rate: **{repeat_rate*100:.1f}%**

**Estimated Customer Lifetime Value**: **${estimated_clv:,.0f}**

**CLV Category**: {clv_category}

**Improvement Opportunities**:
- 🔄 **Increase** repeat purchase rate
- 📈 **Upsell** to existing customers
- 🎯 **Target** high-value customer segments
- 💰 **Optimize** pricing strategies

**Strategic Actions**:
1. **Customer Success**: Implement retention programs
2. **Cross-selling**: Offer complementary products
3. **Loyalty Programs**: Reward repeat customers
4. **Personalization**: Tailor experiences to customer segments"""
    
    def _answer_product_mix(self, context: Dict, results: Dict) -> str:
        """Generate product portfolio diversity analysis."""
        products_data = results.get("top_products", {})
        top_products = products_data.get("table", pd.DataFrame())
        
        if top_products.empty:
            return "🎯 **Product Portfolio Analysis**\n\n*No product data available for analysis.*"
        
        total_products = len(top_products)
        total_revenue = top_products.get("revenue", pd.Series([0])).sum()
        
        # Calculate concentration metrics
        if total_revenue > 0:
            top_product_revenue = top_products.iloc[0].get("revenue", 0) if len(top_products) > 0 else 0
            concentration = (top_product_revenue / total_revenue) * 100
            
            if concentration > 50:
                diversity_score = "🔴 **Low diversity** - Heavy reliance on top product"
            elif concentration > 30:
                diversity_score = "🟡 **Moderate diversity** - Some concentration risk"
            else:
                diversity_score = "🟢 **Good diversity** - Well-balanced portfolio"
        else:
            concentration = 0
            diversity_score = "📊 **Unable to assess** - No revenue data"
        
        # Portfolio recommendations
        if total_products <= 3:
            portfolio_advice = "📦 **Portfolio Expansion**: Consider adding more products to reduce concentration risk"
        elif concentration > 40:
            portfolio_advice = "⚖️ **Risk Mitigation**: Diversify revenue sources to reduce dependency on top product"
        else:
            portfolio_advice = "🎯 **Portfolio Optimization**: Focus on improving underperforming products"
        
        return f"""🎯 **Product Portfolio Analysis**

**Portfolio Metrics**:
- Total Products: **{total_products}**
- Total Revenue: **${total_revenue:,.0f}**
- Top Product Concentration: **{concentration:.1f}%**

**Diversity Assessment**: {diversity_score}

**Portfolio Health**:
- 📊 **Balance**: {self._assess_portfolio_balance(top_products)}
- 🎯 **Focus**: {portfolio_advice}
- 📈 **Growth**: Identify expansion opportunities

**Strategic Recommendations**:
1. **Diversification**: Reduce concentration in top products
2. **Optimization**: Improve underperforming products
3. **Innovation**: Develop new product lines
4. **Marketing**: Balance promotion across portfolio"""
    
    def _answer_inventory(self, context: Dict, results: Dict) -> str:
        """Generate inventory strategy recommendations."""
        products_data = results.get("top_products", {})
        top_products = products_data.get("table", pd.DataFrame())
        
        if top_products.empty:
            return "📦 **Inventory Strategy Analysis**\n\n*No product data available for analysis.*"
        
        # Analyze product performance distribution
        if len(top_products) > 0:
            top_20_percent = int(len(top_products) * 0.2)
            top_products_revenue = top_products.head(top_20_percent)["revenue"].sum()
            total_revenue = top_products["revenue"].sum()
            
            if total_revenue > 0:
                pareto_ratio = (top_products_revenue / total_revenue) * 100
            else:
                pareto_ratio = 0
        else:
            pareto_ratio = 0
        
        # Inventory strategy recommendations
        if pareto_ratio > 80:
            strategy = "🎯 **ABC Analysis**: Implement tiered inventory management"
            focus = "Focus on top 20% of products for inventory optimization"
        elif pareto_ratio > 60:
            strategy = "⚖️ **Balanced Approach**: Optimize inventory across product categories"
            focus = "Balance inventory levels between high and low performers"
        else:
            strategy = "📦 **Comprehensive Management**: Review entire product portfolio"
            focus = "Analyze all products for inventory optimization opportunities"
        
        return f"""📦 **Inventory Strategy Analysis**

**Pareto Analysis**: Top 20% of products generate **{pareto_ratio:.1f}%** of revenue

**Recommended Strategy**: {strategy}

**Inventory Focus**: {focus}

**Implementation Steps**:
1. **📊 Assessment**: Analyze current inventory levels
2. **🎯 Prioritization**: Focus on high-impact products first
3. **📦 Optimization**: Adjust safety stock and reorder points
4. **📈 Monitoring**: Track inventory turnover and performance

**Key Metrics to Track**:
- Inventory turnover rate
- Days of inventory on hand
- Stockout frequency
- Carrying costs

**Technology Recommendations**:
- 📱 **Inventory Management System**: Track real-time levels
- 🔄 **Automated Reordering**: Set up smart reorder points
- 📊 **Analytics Dashboard**: Monitor inventory performance
- ⚡ **Real-time Alerts**: Get notified of inventory issues"""
    
    def _answer_order_efficiency(self, context: Dict, results: Dict) -> str:
        """Generate order operations efficiency analysis."""
        kpis = results.get("kpis", {})
        
        total_revenue = kpis.get("total_revenue", 0)
        num_orders = kpis.get("num_orders", 0)
        
        if num_orders == 0:
            return "⚡ **Order Efficiency Analysis**\n\n*No order data available for analysis.*"
        
        # Calculate efficiency metrics
        avg_order_value = total_revenue / num_orders if num_orders > 0 else 0
        
        # Efficiency assessment
        if avg_order_value > 500:
            efficiency_score = "🏆 **Excellent** - High-value orders"
        elif avg_order_value > 200:
            efficiency_score = "💎 **Good** - Solid order values"
        elif avg_order_value > 100:
            efficiency_score = "📊 **Average** - Room for improvement"
        else:
            efficiency_score = "📈 **Opportunity** - Focus on order value optimization"
        
        # Order processing recommendations
        if num_orders > 1000:
            scale_advice = "🚀 **Scale Operations**: Consider automation and process optimization"
        elif num_orders > 100:
            scale_advice = "⚙️ **Optimize Processes**: Streamline order processing workflows"
        else:
            scale_advice = "📋 **Standardize Processes**: Establish efficient order management procedures"
        
        return f"""⚡ **Order Efficiency Analysis**

**Current Metrics**:
- Total Orders: **{num_orders:,}**
- Total Revenue: **${total_revenue:,.0f}**
- Average Order Value: **${avg_order_value:,.0f}**

**Efficiency Score**: {efficiency_score}

**Operational Insights**:
- 📊 **Order Volume**: {scale_advice}
- 💰 **Value Optimization**: Focus on increasing order values
- 🔄 **Process Efficiency**: Streamline order processing

**Improvement Strategies**:
1. **📈 Upselling**: Increase order values through cross-selling
2. **⚡ Automation**: Reduce manual processing time
3. **📋 Standardization**: Create consistent order workflows
4. **🎯 Optimization**: Focus on high-value order channels

**Technology Solutions**:
- 🛒 **E-commerce Platform**: Optimize online ordering
- 📱 **Mobile Apps**: Streamline mobile ordering
- 🔄 **ERP Integration**: Connect order systems
- 📊 **Analytics**: Track order performance metrics"""
    
    def _answer_channel_performance(self, context: Dict, results: Dict) -> str:
        """Generate sales channel performance analysis."""
        # This would typically come from channel data in results
        # For now, provide a general analysis framework
        
        return """🛣️ **Sales Channel Performance Analysis**

**Channel Assessment**: Analyze performance across all sales channels

**Key Metrics to Evaluate**:
- 📊 **Revenue by Channel**: Identify top-performing channels
- 💰 **Profitability**: Calculate margins per channel
- 📈 **Growth Rate**: Track channel performance trends
- 🎯 **Customer Acquisition Cost**: Measure channel efficiency

**Channel Optimization Strategies**:
1. **📱 Digital Channels**: Optimize online and mobile experiences
2. **🏪 Physical Retail**: Enhance in-store customer experience
3. **🤝 Partnerships**: Strengthen channel partner relationships
4. **📊 Omnichannel**: Create seamless cross-channel experiences

**Performance Benchmarks**:
- 🏆 **Top Channel**: Focus resources on highest performers
- 📈 **Growth Channels**: Invest in emerging opportunities
- ⚠️ **Underperformers**: Optimize or consider alternatives

**Technology Recommendations**:
- 📊 **Channel Analytics**: Track performance metrics
- 🔄 **Integration**: Connect channel systems
- 📱 **Mobile Optimization**: Enhance mobile experiences
- 🎯 **Personalization**: Tailor experiences per channel"""
    
    def _answer_risks(self, context: Dict, results: Dict) -> str:
        """Generate risk assessment analysis."""
        kpis = results.get("kpis", {})
        trend_data = results.get("trend", {})
        customer_data = results.get("repeat_rate", {})
        
        risks = []
        
        # Revenue concentration risk
        if trend_data.get("trend"):
            trend_points = trend_data["trend"]
            if len(trend_points) >= 3:
                recent_trend = self._calculate_recent_growth(trend_points)
                if recent_trend < -0.1:  # More than 10% decline
                    risks.append("📉 **Revenue Decline**: Recent downward trend detected")
        
        # Customer concentration risk
        repeat_rate = customer_data.get("repeat_rate", 0)
        if repeat_rate < 0.2:
            risks.append("👥 **Customer Retention**: Low repeat purchase rate")
        
        # Product concentration risk
        products_data = results.get("top_products", {})
        if products_data.get("table") is not None and not products_data["table"].empty:
            top_products = products_data["table"]
            if len(top_products) > 0:
                top_product_revenue = top_products.iloc[0].get("revenue", 0)
                total_revenue = top_products["revenue"].sum()
                if total_revenue > 0 and (top_product_revenue / total_revenue) > 0.5:
                    risks.append("📦 **Product Concentration**: Heavy reliance on single product")
        
        if not risks:
            risks = ["📊 **Low Risk Profile**: Business shows healthy metrics and balanced performance"]
        
        return f"""🚨 **Risk Assessment Analysis**

**Identified Risks**:
{chr(10).join(f"- {risk}" for risk in risks[:3])}

**Risk Mitigation Strategies**:
1. **📊 Monitoring**: Establish regular risk assessment processes
2. **🎯 Diversification**: Reduce concentration in high-risk areas
3. **📈 Growth**: Focus on sustainable growth strategies
4. **🔄 Optimization**: Continuously improve business processes

**Risk Categories**:
- **Operational**: Process and efficiency risks
- **Financial**: Revenue and profitability risks
- **Customer**: Retention and satisfaction risks
- **Market**: External and competitive risks

**Monitoring Recommendations**:
- 📊 **Weekly**: Track key performance indicators
- 📈 **Monthly**: Review trends and patterns
- 🔍 **Quarterly**: Conduct comprehensive risk assessment
- 📋 **Annually**: Update risk management strategies"""
    
    def _answer_benchmarks(self, context: Dict, results: Dict) -> str:
        """Generate industry benchmark comparison."""
        kpis = results.get("kpis", {})
        customer_data = results.get("repeat_rate", {})
        
        total_revenue = kpis.get("total_revenue", 0)
        num_customers = kpis.get("num_customers", 0)
        repeat_rate = customer_data.get("repeat_rate", 0)
        
        # Calculate benchmark metrics
        if num_customers > 0:
            revenue_per_customer = total_revenue / num_customers
        else:
            revenue_per_customer = 0
        
        # Industry benchmark comparisons (general ranges)
        if revenue_per_customer > 1000:
            revenue_benchmark = "🏆 **Above Industry Average** - Strong customer value"
        elif revenue_per_customer > 500:
            revenue_benchmark = "💎 **Industry Average** - Competitive performance"
        else:
            revenue_benchmark = "📈 **Below Industry Average** - Growth opportunity"
        
        if repeat_rate > 0.4:
            retention_benchmark = "🎉 **Excellent** - Top-tier customer retention"
        elif repeat_rate > 0.25:
            retention_benchmark = "👍 **Good** - Above-average retention"
        else:
            retention_benchmark = "📈 **Opportunity** - Below-average retention"
        
        return f"""📊 **Industry Benchmark Analysis**

**Your Performance vs. Industry Standards**:

**Revenue per Customer**: **${revenue_per_customer:,.0f}**
- Benchmark: {revenue_benchmark}

**Customer Retention Rate**: **{repeat_rate*100:.1f}%**
- Benchmark: {retention_benchmark}

**Business Size Context**:
- 📊 **Small Business**: <$1M annual revenue
- 🏢 **Medium Business**: $1M-$10M annual revenue  
- 🏭 **Large Business**: >$10M annual revenue

**Competitive Positioning**:
- 🎯 **Identify** your competitive advantages
- 📈 **Benchmark** against similar-sized businesses
- 🚀 **Focus** on areas for improvement
- 📊 **Track** progress against industry standards

**Industry Research Sources**:
- 📊 **Industry Reports**: Trade associations and research firms
- 💼 **Peer Networks**: Industry groups and forums
- 📈 **Market Data**: Public company financials
- 🔍 **Consultants**: Industry-specific expertise

**Action Items**:
1. **📊 Research**: Gather industry benchmark data
2. **🎯 Compare**: Assess your competitive position
3. **📈 Improve**: Focus on below-average metrics
4. **🚀 Excel**: Leverage above-average strengths"""
    
    def _assess_portfolio_balance(self, products_df: pd.DataFrame) -> str:
        """Assess the balance of the product portfolio."""
        if products_df.empty:
            return "Unable to assess"
        
        total_products = len(products_df)
        if total_products <= 3:
            return "📦 **Limited** - Consider expanding portfolio"
        elif total_products <= 10:
            return "⚖️ **Balanced** - Good portfolio diversity"
        else:
            return "🎯 **Diverse** - Well-distributed product mix"
    
    # Helper methods
    def _get_trend_insight(self, trend_points: List) -> str:
        """Generate insight based on trend data."""
        if len(trend_points) < 2:
            return "Trend analysis requires at least 2 data points."
        
        recent = trend_points[-3:] if len(trend_points) >= 3 else trend_points
        if len(recent) >= 2:
            try:
                avg_growth = sum([
                    (recent[i]["revenue"] - recent[i-1]["revenue"]) / recent[i-1]["revenue"]
                    for i in range(1, len(recent))
                ]) / (len(recent) - 1) * 100
                
                if avg_growth > 10:
                    return "🚀 **Strong growth momentum** - maintain current strategies and scale successful initiatives."
                elif avg_growth > 0:
                    return "📈 **Steady growth** - focus on optimization and expansion opportunities."
                elif avg_growth > -10:
                    return "📊 **Slight decline** - investigate causes and implement corrective measures."
                else:
                    return "⚠️ **Significant decline** - immediate action required to reverse trend."
            except:
                pass
        
        return "📊 **Stable performance** - continue monitoring for opportunities and risks."
    
    def _categorize_growth(self, cmgr: float) -> str:
        """Categorize growth rate."""
        if cmgr > 20:
            return "🚀 **Hypergrowth** - exceptional performance"
        elif cmgr > 10:
            return "📈 **High Growth** - strong momentum"
        elif cmgr > 5:
            return "📊 **Good Growth** - steady progress"
        elif cmgr > 0:
            return "📈 **Positive Growth** - moving in right direction"
        elif cmgr > -5:
            return "📉 **Slight Decline** - needs attention"
        else:
            return "⚠️ **Declining** - immediate action required"
    
    def _format_trend_summary(self, trend_points: List) -> str:
        """Format trend summary for display."""
        if not trend_points:
            return "No trend data available"
        
        summary = []
        for i, point in enumerate(trend_points[-3:]):  # Last 3 points
            month = point.get("month", f"Month {i+1}")
            revenue = point.get("revenue", 0)
            summary.append(f"- {month}: ${revenue:,.0f}")
        
        return "\n".join(summary)
    
    def _get_growth_recommendation(self, cmgr: float) -> str:
        """Get growth recommendation based on CMGR."""
        if cmgr > 15:
            return "🚀 **Scale aggressively** - you're in a sweet spot, focus on expansion and market penetration."
        elif cmgr > 8:
            return "📈 **Optimize and grow** - strong foundation, focus on efficiency improvements and strategic expansion."
        elif cmgr > 3:
            return "📊 **Steady growth** - maintain momentum while identifying and addressing bottlenecks."
        elif cmgr > 0:
            return "📈 **Accelerate growth** - implement growth strategies and optimize conversion funnels."
        else:
            return "⚠️ **Turn around** - focus on core value proposition and customer satisfaction."
    
    def _get_customer_insights(self, repeat_rate: float, total_customers: int) -> str:
        """Get customer insights based on metrics."""
        insights = []
        
        if repeat_rate > 0.4:
            insights.append("🎉 **Excellent retention** - customers love your product/service")
        elif repeat_rate > 0.25:
            insights.append("👍 **Good retention** - room for improvement in customer engagement")
        else:
            insights.append("📈 **Growth opportunity** - focus on customer success and satisfaction")
        
        if total_customers > 10000:
            insights.append("🏢 **Large customer base** - leverage network effects and referrals")
        elif total_customers > 1000:
            insights.append("📊 **Growing customer base** - focus on scaling customer success")
        else:
            insights.append("🚀 **Early stage** - prioritize customer acquisition and satisfaction")
        
        return "\n".join(insights)
    
    def _format_top_products(self, products_df: pd.DataFrame) -> str:
        """Format top products for display."""
        if products_df.empty:
            return "No product data available"
        
        formatted = []
        for i, (_, row) in enumerate(products_df.head(5).iterrows()):
            product = row.iloc[0] if len(row) > 0 else "Unknown"
            revenue = row.get("revenue", 0) if len(row) > 1 else 0
            formatted.append(f"{i+1}. **{product}**: ${revenue:,.0f}")
        
        return "\n".join(formatted)
    
    def _get_product_recommendations(self, products_df: pd.DataFrame) -> str:
        """Get product recommendations."""
        if products_df.empty:
            return "Focus on data collection and product performance tracking."
        
        total_products = len(products_df)
        if total_products <= 5:
            return "Focus on product quality and customer satisfaction for each item."
        elif total_products <= 20:
            return "Implement product portfolio optimization and focus on top performers."
        else:
            return "Consider product rationalization and focus on high-margin, high-demand items."
    
    def _format_forecast(self, forecast_df: pd.DataFrame) -> str:
        """Format forecast data for display."""
        if forecast_df.empty:
            return "No forecast data available"
        
        formatted = []
        for _, row in forecast_df.iterrows():
            month = row.get("month", "Unknown")
            forecast = row.get("forecast", 0)
            formatted.append(f"- {month}: ${forecast:,.0f}")
        
        return "\n".join(formatted)
    
    def _calculate_recent_growth(self, trend_points: List) -> float:
        """Calculate recent growth rate."""
        if len(trend_points) < 2:
            return 0.0
        
        try:
            recent = trend_points[-1]["revenue"]
            previous = trend_points[-2]["revenue"]
            if previous > 0:
                return (recent - previous) / previous
        except:
            pass
        
        return 0.0
    
    def _generate_generic_answer(self, question: Dict, context: Dict, results: Dict) -> str:
        """Generate a generic answer for questions without specific handlers."""
        return f"""🤖 **AI Analysis: {question['text']}**

**Context Available**:
- Data Shape: {context.get('shape', 'Unknown')}
- KPIs: {len(results.get('kpis', {}))} metrics available
- Insights: {len(results)} analysis modules completed

**Recommendation**: 
This question requires specific analysis. Please select from our curated question list for detailed insights.

**Available Categories**:
- 📊 Performance & Growth
- 👥 Customer Insights  
- 📦 Product Performance
- ⚙️ Operations & Efficiency
- 🎯 Strategic Insights"""

    def _answer_lifetime_value(self, context: Dict, results: Dict) -> str:
        """Generate customer lifetime value analysis."""
        kpis = results.get("kpis", {})
        customer_data = results.get("repeat_rate", {})
        
        # Handle nested KPI structure
        if isinstance(kpis, dict) and "kpis" in kpis:
            kpis = kpis["kpis"]
        
        total_revenue = kpis.get("total_sales", 0) if kpis else 0
        total_customers = kpis.get("num_customers", 0) if kpis else 0
        repeat_rate = customer_data.get("repeat_rate", 0)
        
        if total_customers == 0:
            return "💰 **Customer Lifetime Value Analysis**\n\n*No customer data available for analysis.*"
        
        # Calculate basic CLV metrics
        avg_revenue_per_customer = total_revenue / total_customers if total_customers > 0 else 0
        
        # Estimate CLV based on repeat rate
        if repeat_rate > 0:
            # Simple CLV calculation: avg_revenue * (1 + repeat_rate + repeat_rate^2 + ...)
            # This assumes customers who repeat will continue at similar rates
            clv_multiplier = 1 / (1 - repeat_rate) if repeat_rate < 1 else 5  # Cap at 5x
            estimated_clv = avg_revenue_per_customer * clv_multiplier
        else:
            estimated_clv = avg_revenue_per_customer
        
        # Categorize CLV
        if estimated_clv > 1000:
            clv_category = "🏆 **Premium** - High-value customer base"
        elif estimated_clv > 500:
            clv_category = "💎 **High** - Strong customer value"
        elif estimated_clv > 100:
            clv_category = "📊 **Good** - Solid customer value"
        else:
            clv_category = "📈 **Growth** - Opportunity to increase value"
        
        return f"""💰 **Customer Lifetime Value Analysis**

**Current Metrics**:
- Total Revenue: **${total_revenue:,.0f}**
- Total Customers: **{total_customers:,}**
- Average Revenue per Customer: **${avg_revenue_per_customer:,.0f}**
- Repeat Customer Rate: **{repeat_rate*100:.1f}%**

**Estimated Customer Lifetime Value**: **${estimated_clv:,.0f}**

**CLV Category**: {clv_category}

**Improvement Opportunities**:
- 🔄 **Increase** repeat purchase rate
- 📈 **Upsell** to existing customers
- 🎯 **Target** high-value customer segments
- 💰 **Optimize** pricing strategies

**Strategic Actions**:
1. **Customer Success**: Implement retention programs
2. **Cross-selling**: Offer complementary products
3. **Loyalty Programs**: Reward repeat customers
4. **Personalization**: Tailor experiences to customer segments"""

    def _answer_store_performance(self, context: Dict, results: Dict) -> str:
        """Generate retail store performance analysis."""
        return """🏪 **Store Performance Analysis**

**Key Retail Metrics to Track**:
- 📊 **Sales per Square Foot**: Measure store productivity
- 🚶 **Foot Traffic**: Customer visit patterns
- 💰 **Conversion Rate**: Visitors to buyers ratio
- 📱 **Omnichannel Integration**: Online + offline synergy

**Store Optimization Strategies**:
1. **Layout Optimization**: Arrange products for maximum exposure
2. **Staff Training**: Improve customer service and sales skills
3. **Inventory Management**: Ensure popular items are always in stock
4. **Promotional Displays**: Strategic placement of featured products

**Technology Solutions**:
- 📱 **POS Systems**: Track sales and inventory in real-time
- 🚶 **Foot Traffic Analytics**: Understand customer behavior
- 💳 **Payment Systems**: Streamline checkout process
- 📊 **Performance Dashboards**: Monitor store KPIs

**Industry Benchmarks**:
- Sales per square foot: $300-500 (good), $500+ (excellent)
- Conversion rate: 20-30% (typical), 30%+ (excellent)
- Customer satisfaction: 4.0+ stars (target)"""

    def _answer_inventory_turnover(self, context: Dict, results: Dict) -> str:
        """Generate inventory turnover analysis."""
        # Extract data from results
        kpis_data = results.get("kpis", {})
        if isinstance(kpis_data, dict) and "kpis" in kpis_data:
            kpis = kpis_data["kpis"]
        else:
            kpis = kpis_data
        
        trend_data = results.get("trend", {})
        if "table" in trend_data:
            trend_df = trend_data["table"]
            if isinstance(trend_df, pd.DataFrame) and not trend_df.empty:
                trend_points = trend_df.to_dict('records')
            else:
                trend_points = []
        else:
            trend_points = trend_data.get("trend", [])
        
        # Get product data
        products_data = results.get("top_products", {})
        if "table" in products_data:
            products_df = products_data["table"]
            if isinstance(products_df, pd.DataFrame) and not products_df.empty:
                products = products_df.to_dict('records')
            else:
                products = []
        else:
            products = products_data.get("products", [])
        
        # Calculate inventory turnover metrics
        total_sales = kpis.get("total_sales", 0) if kpis else 0
        total_orders = kpis.get("total_orders", 0) if kpis else 0
        avg_order_value = kpis.get("avg_order_value", 0) if kpis else 0
        
        # Estimate inventory turnover based on sales velocity
        if total_orders > 0 and len(trend_points) >= 3:
            # Calculate monthly sales velocity
            recent_months = trend_points[-3:] if len(trend_points) >= 3 else trend_points
            monthly_sales = sum(point.get("revenue", 0) for point in recent_months) / len(recent_months)
            
            # Estimate inventory turnover (simplified calculation)
            # Assuming inventory is roughly 1-2 months of sales
            estimated_inventory = monthly_sales * 1.5  # Conservative estimate
            if estimated_inventory > 0:
                turnover_rate = (monthly_sales * 12) / estimated_inventory
            else:
                turnover_rate = 0
        else:
            turnover_rate = 0
            monthly_sales = 0
            estimated_inventory = 0
        
        # Determine performance level
        if turnover_rate >= 6:
            performance_level = "🟢 Excellent"
            performance_desc = "Your inventory turnover is above industry standards"
        elif turnover_rate >= 4:
            performance_level = "🟡 Good"
            performance_desc = "Your inventory turnover is within good range"
        else:
            performance_level = "🔴 Needs Improvement"
            performance_desc = "Your inventory turnover could be optimized"
        
        # Get top products for inventory insights
        top_products_text = ""
        if products:
            top_products_text = "\n**Top Products by Revenue**:\n"
            for i, product in enumerate(products[:5], 1):
                revenue = product.get("revenue", 0)
                product_name = product.get("product", "Unknown Product")
                top_products_text += f"{i}. **{product_name}**: ${revenue:,.0f}\n"
        
        return f"""🔄 **Inventory Turnover Analysis**

**Your Performance**: {performance_level}
**Turnover Rate**: **{turnover_rate:.1f}x** annually
**Monthly Sales**: **${monthly_sales:,.0f}**
**Estimated Inventory**: **${estimated_inventory:,.0f}**

**Analysis**: {performance_desc}

**Key Metrics**:
- Total Sales: **${total_sales:,.0f}**
- Total Orders: **{total_orders:,}**
- Average Order Value: **${avg_order_value:.0f}**
- Sales Velocity: **${monthly_sales:,.0f}/month**

{top_products_text}

**Industry Benchmarks**:
- 🟢 **Excellent**: 6+ times annually
- 🟡 **Good**: 4-6 times annually  
- 🔴 **Needs Improvement**: <4 times annually

**Recommendations**:
1. **📊 Demand Forecasting**: Analyze your {len(trend_points)} months of trend data
2. **📦 Just-in-Time**: Consider reducing inventory to {monthly_sales:,.0f} monthly average
3. **🎯 ABC Analysis**: Focus on your top performing products
4. **🔄 Supplier Management**: Optimize lead times based on sales velocity

**Technology Solutions**:
- 📱 **Inventory Management Systems**: Real-time tracking
- 📊 **Analytics Platforms**: Demand forecasting
- 🔄 **Automated Reordering**: Smart reorder points
- 📈 **Performance Monitoring**: Track turnover trends

**Benefits of Optimal Turnover**:
- 💰 Reduced carrying costs
- 📦 Lower risk of obsolescence
- 💸 Improved cash flow
- 🎯 Better customer satisfaction"""

    def _answer_seasonal_planning(self, context: Dict, results: Dict) -> str:
        """Generate seasonal planning analysis."""
        # Extract data from results
        trend_data = results.get("trend", {})
        if "table" in trend_data:
            trend_df = trend_data["table"]
            if isinstance(trend_df, pd.DataFrame) and not trend_df.empty:
                trend_points = trend_df.to_dict('records')
            else:
                trend_points = []
        else:
            trend_points = trend_data.get("trend", [])
        
        kpis_data = results.get("kpis", {})
        if isinstance(kpis_data, dict) and "kpis" in kpis_data:
            kpis = kpis_data["kpis"]
        else:
            kpis = kpis_data
        
        # Analyze seasonal patterns
        if len(trend_points) >= 6:
            # Calculate monthly averages and identify peaks
            monthly_data = {}
            for point in trend_points:
                month = point.get("month", "")
                revenue = point.get("revenue", 0)
                if month:
                    if month not in monthly_data:
                        monthly_data[month] = []
                    monthly_data[month].append(revenue)
            
            # Calculate average revenue by month
            monthly_avg = {}
            for month, revenues in monthly_data.items():
                monthly_avg[month] = sum(revenues) / len(revenues)
            
            # Find peak and low seasons
            if monthly_avg:
                max_month = max(monthly_avg, key=monthly_avg.get)
                min_month = min(monthly_avg, key=monthly_avg.get)
                max_revenue = monthly_avg[max_month]
                min_revenue = monthly_avg[min_month]
                
                # Calculate seasonal variation
                if min_revenue > 0:
                    seasonal_variation = ((max_revenue - min_revenue) / min_revenue) * 100
                else:
                    seasonal_variation = 0
                
                # Determine seasonal strength
                if seasonal_variation >= 50:
                    seasonal_strength = "🔴 Strong"
                    seasonal_desc = "Your business shows strong seasonal patterns"
                elif seasonal_variation >= 25:
                    seasonal_strength = "🟡 Moderate"
                    seasonal_desc = "Your business shows moderate seasonal patterns"
                else:
                    seasonal_strength = "🟢 Minimal"
                    seasonal_desc = "Your business shows minimal seasonal patterns"
                
                # Create seasonal insights
                seasonal_insights = f"""
**Seasonal Analysis**:
- **Peak Season**: {max_month} (${max_revenue:,.0f} avg)
- **Low Season**: {min_month} (${min_revenue:,.0f} avg)
- **Seasonal Variation**: {seasonal_variation:.1f}%
- **Pattern Strength**: {seasonal_strength}

**Seasonal Insights**: {seasonal_desc}
"""
            else:
                seasonal_insights = "**Seasonal Analysis**: Insufficient data for seasonal pattern analysis"
        else:
            seasonal_insights = f"**Seasonal Analysis**: Need at least 6 months of data (currently have {len(trend_points)})"
        
        # Get total sales for context
        total_sales = kpis.get("total_sales", 0) if kpis else 0
        
        return f"""📅 **Seasonal Planning Analysis**

{seasonal_insights}

**Your Data Context**:
- **Total Sales**: ${total_sales:,.0f}
- **Trend Data**: {len(trend_points)} months available
- **Analysis Period**: {trend_points[0].get('month', 'Start')} to {trend_points[-1].get('month', 'End') if trend_points else 'N/A'}

**Seasonal Planning Framework**:

**1. 📊 Historical Analysis**
- **Sales Patterns**: Analyze your {len(trend_points)} months of performance
- **Demand Peaks**: Identify high-demand periods from your data
- **Inventory Cycles**: Track seasonal inventory needs
- **Customer Behavior**: Understand seasonal preferences

**2. 🎯 Forecasting & Planning**
- **Demand Prediction**: Use your trend data for future demand
- **Inventory Planning**: Prepare for seasonal requirements
- **Staff Scheduling**: Align workforce with demand
- **Marketing Planning**: Seasonal campaign preparation

**3. 📦 Inventory Management**
- **Pre-Season Preparation**: Stock up before peak demand
- **Seasonal Products**: Focus on relevant merchandise
- **Clearance Planning**: Manage end-of-season inventory
- **Storage Optimization**: Efficient seasonal storage

**4. 🚀 Marketing & Promotion**
- **Seasonal Campaigns**: Themed marketing initiatives
- **Promotional Timing**: Strategic discount scheduling
- **Customer Communication**: Seasonal messaging and offers
- **Event Planning**: Seasonal events and activations

**Implementation Timeline**:
- **3-6 Months Before**: Begin seasonal planning and forecasting
- **2-3 Months Before**: Secure inventory and plan marketing
- **1 Month Before**: Launch seasonal campaigns and prepare staff
- **During Season**: Monitor performance and adjust strategies
- **Post-Season**: Analyze results and plan for next year

**Success Metrics**:
- Seasonal sales growth
- Inventory turnover improvement
- Customer satisfaction during peak periods
- Profit margin optimization
- Market share growth

**Technology Solutions**:
- 📊 **Forecasting Tools**: AI-powered demand prediction
- 📦 **Inventory Management**: Seasonal planning and optimization
- 🎯 **Marketing Automation**: Seasonal campaign management
- 📈 **Analytics Platforms**: Performance measurement and optimization"""

    def _answer_promotional_effectiveness(self, context: Dict, results: Dict) -> str:
        """Generate promotional effectiveness analysis."""
        # Extract data from results
        kpis_data = results.get("kpis", {})
        if isinstance(kpis_data, dict) and "kpis" in kpis_data:
            kpis = kpis_data["kpis"]
        else:
            kpis = kpis_data
        
        trend_data = results.get("trend", {})
        if "table" in trend_data:
            trend_df = trend_data["table"]
            if isinstance(trend_df, pd.DataFrame) and not trend_df.empty:
                trend_points = trend_df.to_dict('records')
            else:
                trend_points = []
        else:
            trend_points = trend_data.get("trend", [])
        
        # Get channel data for promotional analysis
        channels_data = results.get("top_channels", {})
        if "table" in channels_data:
            channels_df = channels_data["table"]
            if isinstance(channels_df, pd.DataFrame) and not channels_df.empty:
                channels = channels_df.to_dict('records')
            else:
                channels = []
        else:
            channels = channels_data.get("channels", [])
        
        # Calculate promotional metrics
        total_sales = kpis.get("total_sales", 0) if kpis else 0
        total_orders = kpis.get("total_orders", 0) if kpis else 0
        avg_order_value = kpis.get("avg_order_value", 0) if kpis else 0
        total_customers = kpis.get("total_customers", 0) if kpis else 0
        
        # Calculate conversion rate
        conversion_rate = (total_orders / total_customers * 100) if total_customers > 0 else 0
        
        # Analyze trend patterns for promotional insights
        promotional_insights = ""
        if len(trend_points) >= 3:
            # Find highest and lowest revenue months
            revenue_by_month = [(point.get("revenue", 0), point.get("month", "")) for point in trend_points]
            revenue_by_month.sort(reverse=True)
            
            highest_month = revenue_by_month[0]
            lowest_month = revenue_by_month[-1]
            
            # Calculate revenue variation
            if lowest_month[0] > 0:
                revenue_variation = ((highest_month[0] - lowest_month[0]) / lowest_month[0]) * 100
            else:
                revenue_variation = 0
            
            promotional_insights = f"""
**Promotional Performance Analysis**:
- **Best Month**: {highest_month[1]} (${highest_month[0]:,.0f})
- **Lowest Month**: {lowest_month[1]} (${lowest_month[0]:,.0f})
- **Revenue Variation**: {revenue_variation:.1f}%
- **Analysis Period**: {len(trend_points)} months

**Promotional Opportunities**:
- **Peak Performance**: {highest_month[1]} shows your best performance
- **Growth Potential**: {lowest_month[1]} has room for promotional campaigns
- **Seasonal Patterns**: {revenue_variation:.1f}% variation suggests promotional opportunities
"""
        
        # Channel performance for promotional insights
        channel_insights = ""
        if channels:
            channel_insights = "\n**Channel Performance for Promotions**:\n"
            for i, channel in enumerate(channels[:3], 1):
                revenue = channel.get("revenue", 0)
                channel_name = channel.get("channel", "Unknown Channel")
                channel_insights += f"{i}. **{channel_name}**: ${revenue:,.0f}\n"
        
        return f"""🎯 **Promotional Effectiveness Analysis**

{promotional_insights}

**Your Promotional Metrics**:
- **Total Sales**: ${total_sales:,.0f}
- **Total Orders**: {total_orders:,}
- **Average Order Value**: ${avg_order_value:.0f}
- **Total Customers**: {total_customers:,}
- **Conversion Rate**: {conversion_rate:.1f}%

{channel_insights}

**Key Promotional Metrics**:
- 📊 **Conversion Rate**: Promotional offer effectiveness
- 💰 **Revenue Impact**: Sales increase during promotions
- 🎯 **Customer Acquisition**: New customer acquisition cost
- 🔄 **Retention Impact**: Long-term customer value
- 📈 **ROI**: Return on promotional investment

**Promotional Types & Analysis**:

**1. 💰 Discount Promotions**
- **Percentage Off**: Analyze discount depth vs. volume
- **Dollar Off**: Measure absolute discount impact
- **Buy One Get One**: Evaluate bundle effectiveness
- **Flash Sales**: Test urgency and scarcity effects

**2. 🎁 Free Offers**
- **Free Shipping**: Measure order value impact
- **Free Products**: Analyze customer acquisition cost
- **Free Samples**: Test product trial effectiveness
- **Free Services**: Evaluate service adoption

**3. 🚀 Loyalty Programs**
- **Points Systems**: Measure engagement and retention
- **Tier Benefits**: Analyze customer progression
- **Exclusive Access**: Test VIP customer value
- **Referral Rewards**: Measure customer acquisition

**4. 📱 Digital Promotions**
- **Email Campaigns**: Test subject lines and timing
- **Social Media**: Measure engagement and conversion
- **Mobile Offers**: Analyze mobile customer behavior
- **Personalized Promotions**: Test targeting effectiveness

**Optimization Strategies**:

**1. 📊 Data-Driven Analysis**
- **A/B Testing**: Test different promotional approaches
- **Customer Segmentation**: Target promotions by customer type
- **Timing Optimization**: Find optimal promotional timing
- **Channel Analysis**: Identify most effective channels

**2. 🎯 Customer-Centric Approach**
- **Personalization**: Tailor offers to customer preferences
- **Value Communication**: Clearly communicate promotional benefits
- **Customer Journey**: Align promotions with buying stages
- **Feedback Collection**: Gather customer input on promotions

**3. 🚀 Performance Optimization**
- **ROI Tracking**: Monitor promotional return on investment
- **Budget Allocation**: Optimize promotional spend
- **Channel Mix**: Balance promotional channels
- **Timing Strategy**: Optimize promotional frequency

**Implementation Steps**:
1. **📊 Baseline Establishment**: Measure current promotional performance
2. **🎯 Strategy Development**: Design promotional optimization plan
3. **📱 Testing & Optimization**: Implement and test improvements
4. **📈 Performance Monitoring**: Track results and iterate
5. **🔄 Continuous Improvement**: Regular promotional strategy reviews

**Success Metrics**:
- Promotional ROI improvement
- Customer acquisition cost reduction
- Customer lifetime value increase
- Brand awareness and engagement growth
- Market share expansion

**Technology Solutions**:
- 📊 **Promotional Analytics**: Performance measurement and optimization
- 🎯 **Marketing Automation**: Campaign management and testing
- 📱 **Customer Analytics**: Behavior tracking and segmentation
- 🚀 **ROI Optimization**: Investment analysis and optimization"""

    def _answer_retention(self, context: Dict, results: Dict) -> str:
        """Generate customer retention analysis."""
        customer_data = results.get("repeat_rate", {})
        repeat_rate = customer_data.get("repeat_rate", 0)
        
        # Calculate retention metrics
        retention_percentage = repeat_rate * 100
        
        # Categorize retention performance
        if retention_percentage > 40:
            performance = "🏆 **Excellent** - Industry-leading retention"
            status_color = "🟢"
        elif retention_percentage > 25:
            performance = "💎 **Good** - Above-average retention"
            status_color = "🟡"
        elif retention_percentage > 15:
            performance = "📊 **Average** - Room for improvement"
            status_color = "🟠"
        else:
            performance = "📈 **Opportunity** - Focus on retention"
            status_color = "🔴"
        
        return f"""🔄 **Customer Retention Analysis**

**Current Retention Rate**: {status_color} **{retention_percentage:.1f}%**

**Performance Assessment**: {performance}

**Industry Benchmarks**:
- 🏆 **Excellent**: >40% repeat customer rate
- 💎 **Good**: 25-40% repeat customer rate
- 📊 **Average**: 15-25% repeat customer rate
- 📈 **Opportunity**: <15% repeat customer rate

**Retention Strategies**:
1. **🎯 Customer Success**: Proactive engagement and support
2. **💰 Loyalty Programs**: Rewards for repeat purchases
3. **📱 Personalized Communication**: Tailored messaging and offers
4. **🔍 Feedback Loops**: Regular customer satisfaction surveys
5. **📊 Usage Analytics**: Monitor engagement patterns

**Implementation Timeline**:
- 🚀 **Week 1-2**: Set up customer success processes
- 📋 **Week 3-6**: Launch loyalty and engagement programs
- 📊 **Week 7-12**: Monitor and optimize retention efforts

**Success Metrics**:
- Monthly retention rate improvement
- Customer lifetime value increase
- Net promoter score (NPS) improvement
- Reduced churn rate"""

    def _answer_segments(self, context: Dict, results: Dict) -> str:
        """Generate customer segmentation analysis."""
        kpis = results.get("kpis", {})
        customer_data = results.get("repeat_rate", {})
        
        # Handle nested KPI structure
        if isinstance(kpis, dict) and "kpis" in kpis:
            kpis = kpis["kpis"]
        
        total_customers = kpis.get("num_customers", 0) if kpis else 0
        repeat_rate = customer_data.get("repeat_rate", 0)
        
        # Create segmentation framework
        if total_customers > 0:
            # Calculate segment sizes
            loyal_customers = int(total_customers * repeat_rate)
            new_customers = int(total_customers * (1 - repeat_rate))
            
            segments = {
                "loyal": {
                    "size": loyal_customers,
                    "percentage": repeat_rate * 100,
                    "strategy": "Retention & expansion"
                },
                "new": {
                    "size": new_customers,
                    "percentage": (1 - repeat_rate) * 100,
                    "strategy": "Onboarding & engagement"
                }
            }
        else:
            segments = {}
        
        return f"""🏷️ **Customer Segmentation Analysis**

**Current Customer Base**: **{total_customers:,}** total customers

**Primary Segments**:
{chr(10).join([f"- **{segment_name.title()} Customers**: {data['size']:,} ({data['percentage']:.1f}%) - Focus: {data['strategy']}" for segment_name, data in segments.items()]) if segments else "- No customer data available for segmentation"}

**Segmentation Framework**:

**1. 🏆 Loyal Customers (Repeat Buyers)**
- **Characteristics**: High engagement, repeat purchases, brand advocates
- **Strategy**: Retention, upselling, referral programs
- **Actions**: VIP treatment, exclusive offers, feedback solicitation

**2. 🌱 New Customers (First-time Buyers)**
- **Characteristics**: Recent acquisition, exploring products, building trust
- **Strategy**: Onboarding, education, first repeat purchase
- **Actions**: Welcome series, product tutorials, support outreach

**3. 📊 High-Value Customers**
- **Characteristics**: Large order values, frequent purchases, long-term potential
- **Strategy**: Premium service, personalized experiences, expansion
- **Actions**: Dedicated support, custom solutions, strategic partnerships

**4. ⚠️ At-Risk Customers**
- **Characteristics**: Declining engagement, missed payments, support issues
- **Strategy**: Re-engagement, problem resolution, retention
- **Actions**: Proactive outreach, issue resolution, win-back campaigns

**Implementation Steps**:
1. **📊 Data Analysis**: Identify segment characteristics and behaviors
2. **🎯 Strategy Development**: Create segment-specific approaches
3. **📱 Communication Plans**: Develop tailored messaging for each segment
4. **📈 Performance Tracking**: Monitor segment-specific metrics
5. **🔄 Optimization**: Continuously improve segmentation strategies

**Technology Recommendations**:
- 📊 **CRM Systems**: Track customer interactions and history
- 🎯 **Marketing Automation**: Segment-specific campaigns
- 📱 **Customer Analytics**: Behavior tracking and insights
- 💰 **Revenue Analytics**: Segment-specific performance metrics"""

    def _answer_mrr_growth(self, context: Dict, results: Dict) -> str:
        """Generate SaaS MRR growth analysis."""
        # Extract data from results
        kpis_data = results.get("kpis", {})
        if isinstance(kpis_data, dict) and "kpis" in kpis_data:
            kpis = kpis_data["kpis"]
        else:
            kpis = kpis_data
        
        trend_data = results.get("trend", {})
        if "table" in trend_data:
            trend_df = trend_data["table"]
            if isinstance(trend_df, pd.DataFrame) and not trend_df.empty:
                trend_points = trend_df.to_dict('records')
            else:
                trend_points = []
        else:
            trend_points = trend_data.get("trend", [])
        
        # Calculate MRR growth metrics
        total_sales = kpis.get("total_sales", 0) if kpis else 0
        total_orders = kpis.get("total_orders", 0) if kpis else 0
        avg_order_value = kpis.get("avg_order_value", 0) if kpis else 0
        
        # Calculate MRR growth from trend data
        mrr_analysis = ""
        if len(trend_points) >= 3:
            # Calculate monthly growth rates
            growth_rates = []
            for i in range(1, len(trend_points)):
                current = trend_points[i].get("revenue", 0)
                previous = trend_points[i-1].get("revenue", 0)
                if previous > 0:
                    growth_rate = ((current - previous) / previous) * 100
                    growth_rates.append(growth_rate)
            
            if growth_rates:
                avg_growth_rate = sum(growth_rates) / len(growth_rates)
                latest_growth = growth_rates[-1] if growth_rates else 0
                
                # Determine growth performance
                if avg_growth_rate >= 15:
                    growth_performance = "🟢 Excellent"
                    growth_desc = "Your MRR growth is above industry standards"
                elif avg_growth_rate >= 10:
                    growth_performance = "🟡 Good"
                    growth_desc = "Your MRR growth is within good range"
                else:
                    growth_performance = "🔴 Needs Improvement"
                    growth_desc = "Your MRR growth could be optimized"
                
                mrr_analysis = f"""
**MRR Growth Analysis**:
- **Average Monthly Growth**: {avg_growth_rate:.1f}%
- **Latest Month Growth**: {latest_growth:.1f}%
- **Growth Performance**: {growth_performance}
- **Analysis Period**: {len(trend_points)} months

**Growth Insights**: {growth_desc}

**Monthly Growth Breakdown**:
"""
                for i, rate in enumerate(growth_rates[-6:], 1):  # Show last 6 months
                    month_name = trend_points[i].get("month", f"Month {i}")
                    mrr_analysis += f"- {month_name}: {rate:+.1f}%\n"
        
        # Get customer data for SaaS metrics
        total_customers = kpis.get("total_customers", 0) if kpis else 0
        repeat_rate = results.get("repeat_rate", {}).get("repeat_rate", 0)
        
        # Calculate SaaS-specific metrics
        churn_rate = 100 - repeat_rate if repeat_rate > 0 else 0
        ltv_cac_ratio = 3.0  # Placeholder - would need actual CAC data
        
        return f"""📈 **Monthly Recurring Revenue (MRR) Growth Analysis**

{mrr_analysis}

**Your SaaS Metrics**:
- **Total Revenue**: ${total_sales:,.0f}
- **Total Orders**: {total_orders:,}
- **Average Order Value**: ${avg_order_value:.0f}
- **Total Customers**: {total_customers:,}
- **Estimated Churn Rate**: {churn_rate:.1f}%
- **Repeat Rate**: {repeat_rate:.1f}%

**What is MRR?**
MRR is the predictable revenue generated from subscriptions each month.

**Growth Metrics**:
- 📊 **Net MRR Growth**: New + Expansion - Churn - Contraction
- 🚀 **Expansion MRR**: Revenue from existing customers
- 📉 **Churn MRR**: Revenue lost from cancellations
- 💰 **Contraction MRR**: Revenue lost from downgrades

**Industry Benchmarks**:
- 🟢 **Excellent**: 15-20% monthly growth
- 🟡 **Good**: 10-15% monthly growth
- 🔴 **Needs Improvement**: <10% monthly growth

**Growth Strategies**:
1. **🎯 Customer Acquisition**: Improve conversion funnels
2. **🔄 Retention**: Reduce churn through customer success
3. **📈 Expansion**: Upsell and cross-sell opportunities
4. **💰 Pricing**: Optimize pricing strategies

**Key SaaS Metrics**:
- **Churn Rate**: Target <5% monthly (Your rate: {churn_rate:.1f}%)
- **LTV/CAC Ratio**: Target >3:1 (Estimated: {ltv_cac_ratio:.1f}:1)
- **Payback Period**: Target <12 months
- **Net Revenue Retention**: Target >100%

**Technology Solutions**:
- 📊 **Analytics Platforms**: Track MRR metrics
- 🎯 **Customer Success Tools**: Monitor usage and satisfaction
- 💰 **Billing Systems**: Flexible pricing and upgrades
- 📈 **Growth Analytics**: Identify expansion opportunities"""

    def _answer_churn_analysis(self, context: Dict, results: Dict) -> str:
        """Generate SaaS churn analysis."""
        return """📉 **Customer Churn Analysis**

**Understanding Churn**:
Churn is the rate at which customers cancel their subscriptions.

**Types of Churn**:
- 📊 **Gross Churn**: Total cancellations ÷ Total customers
- 🔄 **Net Churn**: (Cancellations - Reactivations) ÷ Total customers
- 💰 **Revenue Churn**: Lost revenue ÷ Total revenue

**Industry Benchmarks**:
- 🟢 **Excellent**: <5% monthly churn
- 🟡 **Good**: 5-10% monthly churn
- 🔴 **Needs Improvement**: >10% monthly churn

**Common Churn Causes**:
1. **❌ Poor Onboarding**: Customers don't see value quickly
2. **🔧 Product Issues**: Bugs or missing features
3. **💰 Pricing**: Perceived poor value for money
4. **🎯 Poor Fit**: Wrong target audience
5. **📱 User Experience**: Difficult to use

**Churn Prevention Strategies**:
1. **🎯 Customer Success**: Proactive engagement
2. **📊 Usage Analytics**: Identify at-risk customers
3. **🔄 Feedback Loops**: Regular customer surveys
4. **💰 Value Demonstration**: Show ROI and benefits
5. **📱 Product Improvements**: Address pain points

**Early Warning Signs**:
- 📉 Declining usage patterns
- 🚫 Reduced login frequency
- 💬 Negative feedback
- 📧 Unresponsive to communications
- 🔄 Feature requests ignored

**Technology Solutions**:
- 📊 **Churn Prediction**: AI-powered risk scoring
- 🎯 **Customer Success Platforms**: Automated engagement
- 📱 **Product Analytics**: Usage monitoring
- 💰 **Revenue Analytics**: Churn impact analysis"""

    def _answer_feature_adoption(self, context: Dict, results: Dict) -> str:
        """Generate SaaS feature adoption analysis."""
        return """🔧 **Feature Adoption Analysis**

**Understanding Feature Adoption**:
Feature adoption measures how effectively customers use your product's capabilities.

**Key Metrics to Track**:
- 📊 **Adoption Rate**: Percentage of customers using each feature
- 🎯 **Time to Adoption**: How long before customers start using features
- 📈 **Usage Frequency**: How often features are used
- 💰 **Value Correlation**: Features that drive customer success

**Adoption Categories**:
1. **🏆 High Adoption (>70%)**: Core features, essential functionality
2. **📈 Medium Adoption (30-70%)**: Important features, growth potential
3. **📊 Low Adoption (<30%)**: Niche features, optimization needed

**Optimization Strategies**:

**1. 🎯 Onboarding Optimization**
- **Feature Tours**: Interactive walkthroughs of key features
- **Progressive Disclosure**: Introduce features gradually
- **Success Stories**: Show real customer benefits
- **Video Tutorials**: Visual learning resources

**2. 📱 User Experience Improvements**
- **Intuitive Design**: Make features easy to discover
- **Contextual Help**: Provide assistance when needed
- **Keyboard Shortcuts**: Power user efficiency
- **Mobile Optimization**: Cross-platform accessibility

**3. 📊 Data-Driven Insights**
- **Usage Analytics**: Track feature utilization patterns
- **A/B Testing**: Test different feature presentations
- **User Feedback**: Collect feature-specific input
- **Success Metrics**: Measure feature impact on goals

**4. 🚀 Gamification & Engagement**
- **Achievement Badges**: Reward feature exploration
- **Progress Tracking**: Show adoption milestones
- **Social Features**: Peer learning and sharing
- **Competition**: Leaderboards and challenges

**Implementation Roadmap**:
- **Month 1**: Feature usage analysis and baseline establishment
- **Month 2**: Onboarding optimization and user experience improvements
- **Month 3**: Gamification implementation and engagement programs
- **Month 4**: Performance measurement and strategy refinement

**Success Metrics**:
- Feature adoption rate improvement
- Time to first feature use reduction
- Customer satisfaction increase
- Support ticket reduction
- Customer lifetime value growth

**Technology Solutions**:
- 📊 **Product Analytics**: Feature usage tracking
- 🎯 **Onboarding Platforms**: Interactive learning experiences
- 📱 **User Experience Tools**: Design and usability optimization
- 🚀 **Engagement Platforms**: Gamification and motivation systems"""

    def _answer_pricing_optimization(self, context: Dict, results: Dict) -> str:
        """Generate SaaS pricing optimization analysis."""
        return """💰 **Pricing Optimization Analysis**

**Pricing Strategy Framework**:
Optimizing pricing requires understanding value perception, market positioning, and customer willingness to pay.

**Key Pricing Metrics**:
- 📊 **Price Elasticity**: How demand changes with price
- 💰 **Customer Lifetime Value (LTV)**: Revenue per customer over time
- 🎯 **Conversion Rates**: Price point impact on sales
- 📈 **Revenue Growth**: Overall pricing strategy effectiveness

**Pricing Models to Consider**:

**1. 🎯 Value-Based Pricing**
- **Approach**: Price based on customer value received
- **Benefits**: Higher margins, better customer alignment
- **Implementation**: Customer research, value quantification, tiered pricing

**2. 📊 Usage-Based Pricing**
- **Approach**: Pay-per-use or consumption-based pricing
- **Benefits**: Scalable growth, customer fairness
- **Implementation**: Usage tracking, tiered consumption, overage charges

**3. 🚀 Freemium Model**
- **Approach**: Free basic tier with premium upgrades
- **Benefits**: Customer acquisition, viral growth
- **Implementation**: Feature gating, upgrade paths, value demonstration

**4. 🏢 Enterprise Pricing**
- **Approach**: Custom pricing for large customers
- **Benefits**: Higher revenue, long-term contracts
- **Implementation**: Sales team, custom solutions, volume discounts

**Optimization Strategies**:

**1. 📊 Market Research**
- **Competitive Analysis**: Understand market positioning
- **Customer Surveys**: Willingness to pay research
- **A/B Testing**: Test different price points
- **Value Proposition**: Clear benefit communication

**2. 🎯 Customer Segmentation**
- **High-Value Customers**: Premium pricing for enterprise
- **Growth Customers**: Mid-tier pricing for SMBs
- **Entry Customers**: Low-cost options for startups
- **Custom Solutions**: Tailored pricing for unique needs

**3. 📈 Dynamic Pricing**
- **Seasonal Adjustments**: Peak vs. off-peak pricing
- **Demand-Based**: Higher prices during high demand
- **Customer-Specific**: Personalized pricing based on usage
- **Promotional**: Limited-time pricing strategies

**Implementation Steps**:
1. **📊 Current State Analysis**: Evaluate existing pricing performance
2. **🎯 Strategy Development**: Choose optimal pricing model
3. **📱 Customer Communication**: Transparent pricing changes
4. **📈 Performance Monitoring**: Track pricing impact
5. **🔄 Continuous Optimization**: Regular pricing reviews

**Success Metrics**:
- Revenue per customer increase
- Customer acquisition cost reduction
- Churn rate improvement
- Market share growth
- Customer satisfaction maintenance

**Technology Solutions**:
- 💰 **Pricing Analytics**: Performance measurement and optimization
- 🎯 **A/B Testing**: Price point experimentation
- 📊 **Customer Analytics**: Value and willingness to pay analysis
- 🚀 **Revenue Management**: Dynamic pricing and optimization"""

    def _answer_customer_success(self, context: Dict, results: Dict) -> str:
        """Generate SaaS customer success analysis."""
        return """🎯 **Customer Success Program Analysis**

**Customer Success Definition**:
Customer success ensures customers achieve their desired outcomes while using your product, leading to retention and growth.

**Key Success Metrics**:
- 📊 **Customer Health Score**: Overall customer satisfaction and engagement
- 🎯 **Time to Value**: How quickly customers see benefits
- 📈 **Feature Adoption**: Product utilization and engagement
- 💰 **Expansion Revenue**: Upselling and cross-selling success
- 🔄 **Churn Prevention**: Customer retention improvement

**Customer Success Framework**:

**1. 🚀 Onboarding Excellence**
- **Welcome Series**: Structured introduction to your product
- **Goal Setting**: Clear success criteria establishment
- **Training Resources**: Comprehensive learning materials
- **Success Milestones**: Celebrated achievement markers

**2. 📊 Proactive Monitoring**
- **Health Scoring**: Automated customer health assessment
- **Usage Analytics**: Product engagement tracking
- **Success Metrics**: Goal achievement monitoring
- **Risk Alerts**: Early warning for at-risk customers

**3. 🎯 Strategic Engagement**
- **Success Planning**: Regular goal review and planning
- **Value Demonstration**: ROI and benefit communication
- **Feature Education**: Advanced capability training
- **Best Practices**: Industry and use case sharing

**4. 🔄 Continuous Optimization**
- **Feedback Collection**: Regular customer input gathering
- **Process Improvement**: Streamlined success workflows
- **Tool Enhancement**: Better success enablement tools
- **Team Development**: Continuous skill improvement

**Implementation Roadmap**:

**Phase 1: Foundation (Months 1-2)**
- Customer success team establishment
- Health scoring system development
- Basic monitoring and alerting setup
- Initial customer success playbooks

**Phase 2: Optimization (Months 3-4)**
- Advanced analytics and reporting
- Automated engagement workflows
- Customer success technology stack
- Performance measurement systems

**Phase 3: Scale (Months 5-6)**
- Team expansion and specialization
- Advanced automation and AI
- Predictive analytics implementation
- Continuous improvement processes

**Success Metrics**:
- Customer health score improvement
- Time to value reduction
- Feature adoption increase
- Expansion revenue growth
- Churn rate reduction
- Customer satisfaction improvement

**Technology Stack**:
- 📊 **Customer Success Platforms**: Centralized success management
- 🎯 **Analytics Tools**: Customer behavior and health tracking
- 📱 **Communication Tools**: Multi-channel customer engagement
- 🚀 **Automation Platforms**: Workflow and process automation
- 💰 **Revenue Analytics**: Success impact measurement

**Best Practices**:
1. **Proactive Engagement**: Don't wait for customers to ask for help
2. **Data-Driven Decisions**: Use analytics to guide success strategies
3. **Personalized Approach**: Tailor success plans to customer needs
4. **Continuous Learning**: Regular team training and development
5. **Customer Advocacy**: Turn successful customers into advocates"""

    def _answer_seller_performance(self, context: Dict, results: Dict) -> str:
        """Generate marketplace seller performance analysis."""
        return """👥 **Seller Performance Analysis**

**Key Seller Metrics**:
- 📊 **Sales Volume**: Revenue generated per seller
- 🎯 **Conversion Rate**: Listings to sales ratio
- 💰 **Average Order Value**: Revenue per transaction
- 🔄 **Retention Rate**: Seller churn and loyalty
- ⭐ **Customer Rating**: Buyer satisfaction scores

**Seller Segmentation**:

**1. 🏆 Top Performers (Top 20%)**
- **Characteristics**: High volume, quality products, excellent service
- **Strategy**: Retention, expansion, exclusive partnerships
- **Actions**: Premium features, priority support, growth incentives

**2. 📈 Growth Sellers (Middle 60%)**
- **Characteristics**: Potential for growth, improving performance
- **Strategy**: Development, training, optimization
- **Actions**: Performance coaching, feature education, growth support

**3. 📊 New Sellers (Bottom 20%)**
- **Characteristics**: Learning curve, building presence
- **Strategy**: Onboarding, education, support
- **Actions**: Training programs, mentorship, success resources

**Performance Optimization**:

**1. 🎯 Seller Onboarding**
- **Training Programs**: Product and platform education
- **Success Resources**: Best practices and guidelines
- **Support Systems**: Dedicated assistance and guidance
- **Performance Tracking**: Clear metrics and goals

**2. 📊 Performance Monitoring**
- **Real-time Analytics**: Live performance tracking
- **Goal Setting**: Clear performance targets
- **Progress Tracking**: Regular performance reviews
- **Feedback Loops**: Continuous improvement processes

**3. 🚀 Growth Support**
- **Marketing Tools**: Seller promotion capabilities
- **Inventory Management**: Stock and listing optimization
- **Customer Service**: Buyer interaction support
- **Analytics Insights**: Performance data and recommendations

**Technology Solutions**:
- 📊 **Seller Dashboards**: Performance monitoring and analytics
- 🎯 **Training Platforms**: Educational content and resources
- 📱 **Mobile Apps**: On-the-go seller management
- 🚀 **Growth Tools**: Marketing and optimization features

**Success Metrics**:
- Seller retention rate improvement
- Average seller revenue growth
- Customer satisfaction increase
- Platform growth acceleration
- Marketplace liquidity improvement"""

    def _answer_network_effects(self, context: Dict, results: Dict) -> str:
        """Generate marketplace network effects analysis."""
        return """🕸️ **Network Effects Analysis**

**Understanding Network Effects**:
Network effects occur when a platform becomes more valuable as more users join.

**Types of Network Effects**:

**1. 🔗 Direct Network Effects**
- **Same-Side**: More buyers attract more buyers
- **Cross-Side**: More buyers attract more sellers
- **Platform Value**: Overall platform utility increases

**2. 📊 Indirect Network Effects**
- **Data Quality**: Better data with more users
- **Content Variety**: More diverse offerings
- **Service Quality**: Improved services with scale

**3. 🚀 Platform Network Effects**
- **Ecosystem**: Third-party integrations and services
- **Standards**: Industry standards and best practices
- **Innovation**: New features and capabilities

**Measuring Network Effects**:

**1. 📈 Growth Metrics**
- **User Growth Rate**: New user acquisition speed
- **Retention Rate**: User loyalty and engagement
- **Viral Coefficient**: User referral effectiveness
- **Network Density**: User interaction frequency

**2. 💰 Value Metrics**
- **User Lifetime Value**: Long-term user value
- **Network Value**: Platform utility per user
- **Ecosystem Value**: Third-party service value
- **Market Position**: Competitive advantage strength

**3. 🔄 Engagement Metrics**
- **Daily Active Users**: Regular platform usage
- **Session Duration**: Time spent on platform
- **Feature Adoption**: Platform capability utilization
- **Cross-Platform Usage**: Multi-device engagement

**Network Effects Strategies**:

**1. 🚀 User Acquisition**
- **Viral Marketing**: Encourage user referrals
- **Network Incentives**: Reward network growth
- **Strategic Partnerships**: Leverage existing networks
- **Content Marketing**: Attract users with valuable content

**2. 📊 User Engagement**
- **Community Building**: Foster user interactions
- **Feature Development**: Add network-enhancing capabilities
- **Quality Improvement**: Enhance platform value
- **User Experience**: Optimize platform usability

**3. 🔗 Ecosystem Development**
- **API Development**: Enable third-party integrations
- **Partner Programs**: Build strategic relationships
- **Developer Tools**: Support external development
- **Standards Creation**: Establish industry best practices

**Implementation Roadmap**:

**Phase 1: Foundation (Months 1-3)**
- Core platform development
- Initial user acquisition
- Basic network effects establishment
- Performance measurement setup

**Phase 2: Growth (Months 4-6)**
- User engagement optimization
- Network effects acceleration
- Ecosystem development
- Performance monitoring and optimization

**Phase 3: Scale (Months 7-12)**
- Advanced network effects
- Ecosystem expansion
- Market leadership establishment
- Continuous innovation and improvement

**Success Metrics**:
- User growth rate acceleration
- Network value per user increase
- Platform engagement improvement
- Ecosystem value growth
- Market position strengthening

**Technology Solutions**:
- 📊 **Network Analytics**: Network effects measurement
- 🚀 **Growth Platforms**: User acquisition and engagement
- 🔗 **API Management**: Third-party integration support
- 📈 **Performance Monitoring**: Network health tracking

**Best Practices**:
1. **User-Centric Design**: Focus on user value and experience
2. **Data-Driven Decisions**: Use analytics to guide strategy
3. **Continuous Innovation**: Regularly add new features and capabilities
4. **Strategic Partnerships**: Build valuable ecosystem relationships
5. **Quality Focus**: Maintain high standards as you scale"""

    def _answer_buyer_behavior(self, context: Dict, results: Dict) -> str:
        """Generate marketplace buyer behavior analysis."""
        return """🛍️ **Buyer Behavior Analysis**

**Understanding Buyer Behavior**:
Analyzing how buyers interact with your marketplace helps optimize the user experience and increase conversion rates.

**Key Buyer Metrics**:
- 📊 **Conversion Rate**: Visitors to buyers ratio
- 🎯 **Average Order Value**: Revenue per transaction
- 📱 **Session Duration**: Time spent on platform
- 🔄 **Repeat Purchase Rate**: Buyer retention and loyalty
- 💰 **Customer Acquisition Cost**: Marketing efficiency

**Buyer Journey Analysis**:

**1. 🚀 Discovery Phase**
- **Traffic Sources**: How buyers find your marketplace
- **Search Behavior**: What they're looking for
- **Browsing Patterns**: How they explore products
- **First Impressions**: Initial platform experience

**2. 🎯 Consideration Phase**
- **Product Research**: How buyers evaluate options
- **Comparison Behavior**: What factors influence decisions
- **Trust Building**: Security and credibility factors
- **Social Proof**: Reviews and recommendations

**3. 💰 Decision Phase**
- **Purchase Triggers**: What motivates final decisions
- **Payment Preferences**: Preferred payment methods
- **Checkout Experience**: Friction points and optimization
- **Post-Purchase**: Satisfaction and feedback

**Behavioral Segmentation**:

**1. 🏆 High-Value Buyers**
- **Characteristics**: Large orders, frequent purchases, premium products
- **Strategy**: VIP treatment, exclusive access, personalized service
- **Actions**: Dedicated support, early access, loyalty rewards

**2. 📈 Growth Buyers**
- **Characteristics**: Increasing order values, expanding categories
- **Strategy**: Cross-selling, upselling, category expansion
- **Actions**: Product recommendations, educational content, incentives

**3. 🌱 New Buyers**
- **Characteristics**: First-time purchases, exploring platform
- **Strategy**: Onboarding, education, trust building
- **Actions**: Welcome series, product guides, support outreach

**4. ⚠️ At-Risk Buyers**
- **Characteristics**: Declining engagement, support issues
- **Strategy**: Re-engagement, problem resolution, retention
- **Actions**: Proactive outreach, issue resolution, win-back campaigns

**Optimization Strategies**:

**1. 🎯 User Experience Optimization**
- **Intuitive Navigation**: Easy product discovery and browsing
- **Mobile Optimization**: Seamless mobile experience
- **Fast Loading**: Quick page load times
- **Clear CTAs**: Obvious next steps and actions

**2. 📊 Personalization**
- **Product Recommendations**: AI-powered suggestions
- **Personalized Content**: Tailored messaging and offers
- **Behavioral Targeting**: Action-based marketing
- **Custom Dashboards**: Individualized user interfaces

**3. 🚀 Trust Building**
- **Security Features**: Safe payment and data protection
- **Social Proof**: Customer reviews and testimonials
- **Transparent Policies**: Clear terms and conditions
- **Customer Support**: Responsive help and assistance

**Implementation Steps**:
1. **📊 Data Collection**: Implement comprehensive tracking
2. **🎯 Analysis**: Identify behavior patterns and insights
3. **📱 Optimization**: Implement improvements based on findings
4. **📈 Testing**: A/B test different approaches
5. **🔄 Monitoring**: Track performance and iterate

**Success Metrics**:
- Conversion rate improvement
- Average order value increase
- Session duration growth
- Repeat purchase rate improvement
- Customer satisfaction increase

**Technology Solutions**:
- 📊 **Analytics Platforms**: Behavior tracking and analysis
- 🎯 **Personalization Engines**: AI-powered recommendations
- 📱 **User Experience Tools**: Design and usability optimization
- 🚀 **Conversion Optimization**: A/B testing and optimization"""

    def _answer_commission_optimization(self, context: Dict, results: Dict) -> str:
        """Generate marketplace commission optimization analysis."""
        return """💸 **Commission Structure Optimization**

**Commission Strategy Overview**:
Optimizing your commission structure balances platform profitability with seller incentives and buyer value.

**Key Commission Metrics**:
- 📊 **Take Rate**: Platform revenue as percentage of transaction value
- 💰 **Revenue per Transaction**: Commission earned per sale
- 🎯 **Seller Satisfaction**: Impact on seller retention and growth
- 📈 **Platform Growth**: Overall marketplace expansion

**Commission Models**:

**1. 🎯 Flat Rate Commission**
- **Structure**: Fixed percentage across all categories
- **Benefits**: Simple, predictable, easy to understand
- **Best For**: Standardized products, consistent margins
- **Example**: 10% on all transactions

**2. 📊 Tiered Commission**
- **Structure**: Different rates based on volume or performance
- **Benefits**: Incentivizes growth, rewards top performers
- **Best For**: Encouraging seller development, performance optimization
- **Example**: 15% for new sellers, 10% for established, 5% for premium

**3. 💰 Category-Based Commission**
- **Structure**: Different rates by product category
- **Benefits**: Aligns with category profitability, market dynamics
- **Best For**: Diverse product portfolios, varying margins
- **Example**: 5% for electronics, 15% for handmade, 20% for services

**4. 🚀 Dynamic Commission**
- **Structure**: Variable rates based on market conditions
- **Benefits**: Market-responsive, competitive positioning
- **Best For**: Dynamic markets, seasonal variations
- **Example**: 8-12% based on demand and competition

**Optimization Strategies**:

**1. 📊 Market Analysis**
- **Competitive Research**: Understand industry standards
- **Seller Feedback**: Gather input on commission impact
- **Buyer Sensitivity**: Test price elasticity
- **Category Performance**: Analyze profitability by segment

**2. 🎯 Incentive Alignment**
- **Seller Growth**: Encourage seller development and expansion
- **Quality Improvement**: Reward high-quality products and service
- **Platform Loyalty**: Incentivize exclusive or primary platform use
- **Innovation**: Support new product categories and services

**3. 💰 Revenue Optimization**
- **Profitability Analysis**: Balance commission with operational costs
- **Volume Optimization**: Find optimal rate for maximum revenue
- **Market Share**: Competitive positioning for growth
- **Long-term Value**: Sustainable profitability and expansion

**Implementation Framework**:

**Phase 1: Analysis (Weeks 1-2)**
- Current commission performance review
- Competitive analysis and benchmarking
- Seller and buyer feedback collection
- Financial impact modeling

**Phase 2: Strategy Development (Weeks 3-4)**
- Commission model selection and design
- Rate structure optimization
- Incentive program development
- Communication strategy planning

**Phase 3: Implementation (Weeks 5-6)**
- Gradual rollout and testing
- Seller communication and education
- Performance monitoring and adjustment
- Feedback collection and iteration

**Success Metrics**:
- Platform revenue growth
- Seller satisfaction improvement
- Transaction volume increase
- Market share expansion
- Profitability optimization

**Risk Mitigation**:
- **Seller Churn**: Gradual changes with clear communication
- **Buyer Impact**: Transparent pricing and value demonstration
- **Market Position**: Competitive analysis and positioning
- **Financial Risk**: Modeling and testing before full implementation

**Technology Solutions**:
- 💰 **Commission Management**: Automated calculation and distribution
- 📊 **Analytics Platforms**: Performance measurement and optimization
- 🎯 **A/B Testing**: Commission structure experimentation
- 📱 **Seller Tools**: Commission tracking and optimization"""

    def _answer_liquidity_analysis(self, context: Dict, results: Dict) -> str:
        """Generate marketplace liquidity analysis."""
        return """💧 **Marketplace Liquidity Analysis**

**Understanding Marketplace Liquidity**:
Liquidity measures how easily buyers and sellers can complete transactions on your platform.

**Liquidity Metrics**:
- 📊 **Transaction Velocity**: Speed of buying and selling
- 🎯 **Market Depth**: Available supply and demand
- 💰 **Price Stability**: Consistent and predictable pricing
- 📈 **Growth Rate**: Platform expansion and activity
- 🔄 **User Engagement**: Active participation levels

**Liquidity Assessment Framework**:

**1. 🟢 High Liquidity**
- **Characteristics**: Fast transactions, stable prices, high activity
- **Benefits**: Better user experience, competitive pricing, rapid growth
- **Indicators**: Quick sales, minimal price spreads, high engagement

**2. 🟡 Moderate Liquidity**
- **Characteristics**: Reasonable transaction speed, some price variation
- **Benefits**: Balanced growth, manageable operations, steady development
- **Indicators**: Moderate sales velocity, acceptable price stability

**3. 🔴 Low Liquidity**
- **Characteristics**: Slow transactions, price volatility, low activity
- **Challenges**: Poor user experience, pricing uncertainty, slow growth
- **Indicators**: Long sales cycles, wide price spreads, low engagement

**Liquidity Drivers**:

**1. 🎯 User Base Size**
- **Buyer Pool**: Larger buyer base increases demand
- **Seller Pool**: More sellers provide supply variety
- **Network Effects**: Platform value increases with users
- **Geographic Coverage**: Broader market reach

**2. 📊 Product Diversity**
- **Category Coverage**: Multiple product categories
- **Price Range**: Various price points for different buyers
- **Quality Levels**: Products for different market segments
- **Availability**: Consistent product supply

**3. 🚀 Platform Features**
- **Search & Discovery**: Easy product finding
- **Trust & Safety**: Secure transaction environment
- **Payment Systems**: Convenient payment options
- **Mobile Experience**: Accessible platform usage

**Liquidity Optimization Strategies**:

**1. 📈 User Acquisition**
- **Buyer Marketing**: Targeted buyer acquisition campaigns
- **Seller Onboarding**: Streamlined seller recruitment
- **Referral Programs**: Incentivize user growth
- **Partnership Development**: Strategic business relationships

**2. 🎯 Product Strategy**
- **Category Expansion**: Add new product categories
- **Quality Improvement**: Enhance product standards
- **Inventory Management**: Ensure consistent supply
- **Pricing Optimization**: Competitive and stable pricing

**3. 🚀 Platform Enhancement**
- **User Experience**: Intuitive and engaging interface
- **Trust Building**: Security and credibility features
- **Performance**: Fast and reliable platform
- **Mobile Optimization**: Accessible mobile experience

**Implementation Roadmap**:

**Phase 1: Assessment (Weeks 1-2)**
- Current liquidity measurement
- Benchmark analysis
- User feedback collection
- Performance gap identification

**Phase 2: Strategy Development (Weeks 3-4)**
- Liquidity improvement plan
- User acquisition strategy
- Product development roadmap
- Platform enhancement planning

**Phase 3: Execution (Weeks 5-12)**
- User acquisition campaigns
- Product category expansion
- Platform feature development
- Performance monitoring and optimization

**Success Metrics**:
- Transaction velocity improvement
- Price stability enhancement
- User engagement increase
- Market depth expansion
- Growth rate acceleration

**Technology Solutions**:
- 📊 **Analytics Platforms**: Liquidity measurement and monitoring
- 🎯 **User Acquisition**: Marketing and growth tools
- 📱 **Platform Development**: Feature and performance optimization
- 🚀 **Market Making**: Automated liquidity provision

**Best Practices**:
1. **Continuous Monitoring**: Regular liquidity assessment
2. **User-Centric Approach**: Focus on user experience and satisfaction
3. **Data-Driven Decisions**: Use analytics to guide optimization
4. **Balanced Growth**: Maintain quality while expanding
5. **Long-term Perspective**: Build sustainable liquidity foundation"""

    def get_available_questions(self, context: Dict, results: Dict) -> Dict[str, Dict]:
        """Get questions filtered by available data context and industry."""
        all_questions = self._build_question_catalog()
        available_questions = {}
        
        # Analyze context to determine what data is available
        context_analysis = self._analyze_context_availability(context, results)
        
        for category_key, category in all_questions.items():
            # Filter categories based on industry
            if not self._is_category_available_for_industry(category_key):
                continue
                
            available_questions_in_category = {}
            
            for q_id, question in category["questions"].items():
                # Check if this question can be answered with available data
                if self._can_answer_question(q_id, context_analysis):
                    question_copy = question.copy()
                    question_copy["available"] = True
                    available_questions_in_category[q_id] = question_copy
                else:
                    # Mark question as unavailable with reason
                    question_copy = question.copy()
                    question_copy["available"] = False
                    question_copy["unavailable_reason"] = self._get_unavailable_reason(q_id, context_analysis)
                    available_questions_in_category[q_id] = question_copy
            
            # Only include categories that have available questions
            if available_questions_in_category:
                available_questions[category_key] = {
                    "title": category["title"],
                    "questions": available_questions_in_category,
                    "available_count": len([q for q in available_questions_in_category.values() if q.get("available", True)]),
                    "total_count": len(available_questions_in_category)
                }
        
        return available_questions
    
    def _is_category_available_for_industry(self, category_key: str) -> bool:
        """Check if a category should be shown for the current industry."""
        # Industry-specific category mapping
        industry_categories = {
            "generic": ["performance", "customers", "products", "operations", "strategy"],
            "retail": ["performance", "customers", "products", "operations", "strategy", "retail_specific"],
            "saas": ["performance", "customers", "products", "operations", "strategy", "saas_specific"],
            "marketplace": ["performance", "customers", "products", "operations", "strategy", "marketplace_specific"]
        }
        
        # Get available categories for current industry
        available_categories = industry_categories.get(self.industry, industry_categories["generic"])
        
        return category_key in available_categories
    
    def _analyze_context_availability(self, context: Dict, results: Dict) -> Dict[str, bool]:
        """Analyze what data is available in the context."""
        analysis = {
            "has_kpis": False,
            "has_trend": False,
            "has_products": False,
            "has_customers": False,
            "has_channels": False,
            "has_forecast": False,
            "has_cohorts": False,
            "has_rfm": False,
            "has_repeat_rate": False,
            "has_anomalies": False,
            "has_seasonality": False,
            "trend_months": 0,
            "customer_count": 0,
            "product_count": 0,
            "channel_count": 0
        }
        
        # Check KPIs
        kpis_data = results.get("kpis", {})
        if isinstance(kpis_data, dict) and "kpis" in kpis_data:
            kpis = kpis_data["kpis"]
        else:
            kpis = kpis_data
        
        if kpis and any(kpis.values()):
            analysis["has_kpis"] = True
            analysis["customer_count"] = kpis.get("num_customers", 0)
        
        # Check trend data
        trend_data = results.get("trend", {})
        if "table" in trend_data:
            trend_df = trend_data["table"]
            if isinstance(trend_df, pd.DataFrame) and not trend_df.empty:
                analysis["has_trend"] = True
                analysis["trend_months"] = len(trend_df)
        
        # Check products
        products_data = results.get("top_products", {})
        if "table" in products_data:
            products_df = products_data["table"]
            if isinstance(products_df, pd.DataFrame) and not products_df.empty:
                analysis["has_products"] = True
                analysis["product_count"] = len(products_df)
        
        # Check channels
        channels_data = results.get("top_channels", {})
        if "table" in channels_data:
            channels_df = channels_data["table"]
            if isinstance(channels_df, pd.DataFrame) and not channels_df.empty:
                analysis["has_channels"] = True
                analysis["channel_count"] = len(channels_df)
        
        # Check other data types
        forecast_data = results.get("forecast", {}).get("forecast")
        analysis["has_forecast"] = isinstance(forecast_data, pd.DataFrame) and not forecast_data.empty if forecast_data is not None else False
        
        cohorts_data = results.get("cohorts", {}).get("table")
        analysis["has_cohorts"] = isinstance(cohorts_data, pd.DataFrame) and not cohorts_data.empty if cohorts_data is not None else False
        
        rfm_data = results.get("rfm", {}).get("table")
        analysis["has_rfm"] = isinstance(rfm_data, pd.DataFrame) and not rfm_data.empty if rfm_data is not None else False
        
        repeat_rate_data = results.get("repeat_rate", {}).get("repeat_rate")
        analysis["has_repeat_rate"] = repeat_rate_data is not None and repeat_rate_data > 0 if repeat_rate_data is not None else False
        
        return analysis
    
    def _can_answer_question(self, question_id: str, context_analysis: Dict[str, bool]) -> bool:
        """Check if a question can be answered with available data."""
        requirements = {
            # Performance & Growth
            "revenue_trend": context_analysis["has_trend"] and context_analysis["trend_months"] >= 2,
            "growth_rate": context_analysis["has_trend"] and context_analysis["trend_months"] >= 3,
            "seasonality": context_analysis["has_trend"] and context_analysis["trend_months"] >= 6,
            "anomalies": context_analysis["has_trend"] and context_analysis["trend_months"] >= 3,
            
            # Customer Insights
            "customer_growth": context_analysis["has_kpis"] and context_analysis["customer_count"] > 0,
            "retention": context_analysis["has_repeat_rate"],
            "lifetime_value": context_analysis["has_kpis"] and context_analysis["has_repeat_rate"],
            "segments": context_analysis["has_kpis"] and context_analysis["customer_count"] > 10,
            
            # Product Performance
            "top_products": context_analysis["has_products"] and context_analysis["product_count"] > 0,
            "product_mix": context_analysis["has_products"] and context_analysis["product_count"] > 5,
            "inventory": context_analysis["has_products"] and context_analysis["has_trend"],
            
            # Operations & Efficiency
            "order_efficiency": context_analysis["has_kpis"],
            "channel_performance": context_analysis["has_channels"] and context_analysis["channel_count"] > 1,
            "forecasting": context_analysis["has_trend"] and context_analysis["trend_months"] >= 6,
            
            # Strategic Insights
            "opportunities": context_analysis["has_kpis"] and context_analysis["has_trend"],
            "risks": context_analysis["has_trend"] and context_analysis["has_kpis"],
            "benchmarks": context_analysis["has_kpis"] and context_analysis["has_trend"],
            "recommendations": context_analysis["has_kpis"],
            
            # Retail-Specific
            "store_performance": context_analysis["has_channels"] and context_analysis["has_kpis"],
            "inventory_turnover": context_analysis["has_products"] and context_analysis["has_trend"],
            "seasonal_planning": context_analysis["has_trend"] and context_analysis["trend_months"] >= 12,
            "promotional_effectiveness": context_analysis["has_channels"] and context_analysis["has_trend"],
            
            # SaaS-Specific
            "mrr_growth": context_analysis["has_trend"] and context_analysis["trend_months"] >= 3,
            "churn_analysis": context_analysis["has_repeat_rate"] and context_analysis["has_kpis"],
            "feature_adoption": context_analysis["has_products"] and context_analysis["has_kpis"],
            "pricing_optimization": context_analysis["has_kpis"] and context_analysis["has_trend"],
            "customer_success": context_analysis["has_repeat_rate"] and context_analysis["has_kpis"],
            
            # Marketplace-Specific
            "seller_performance": context_analysis["has_channels"] and context_analysis["has_products"],
            "buyer_behavior": context_analysis["has_kpis"] and context_analysis["has_channels"],
            "network_effects": context_analysis["has_kpis"] and context_analysis["has_trend"],
            "commission_optimization": context_analysis["has_channels"] and context_analysis["has_kpis"],
            "liquidity_analysis": context_analysis["has_kpis"] and context_analysis["has_trend"]
        }
        
        return requirements.get(question_id, True)  # Default to available if not specified
    
    def _get_unavailable_reason(self, question_id: str, context_analysis: Dict[str, bool]) -> str:
        """Get the reason why a question is unavailable."""
        reasons = {
            "revenue_trend": "Need at least 2 months of trend data",
            "growth_rate": "Need at least 3 months of trend data",
            "seasonality": "Need at least 6 months of trend data for seasonal patterns",
            "anomalies": "Need at least 3 months of trend data for anomaly detection",
            "customer_growth": "Need customer data and KPIs",
            "retention": "Need repeat customer rate data",
            "lifetime_value": "Need customer data and repeat rate information",
            "segments": "Need at least 10 customers for meaningful segmentation",
            "top_products": "Need product data",
            "product_mix": "Need at least 5 products for mix analysis",
            "inventory": "Need product data and trend information",
            "order_efficiency": "Need order and KPI data",
            "channel_performance": "Need at least 2 sales channels",
            "forecasting": "Need at least 6 months of trend data",
            "opportunities": "Need KPI and trend data",
            "risks": "Need trend and KPI data",
            "benchmarks": "Need KPI and trend data",
            "recommendations": "Need KPI data",
            "store_performance": "Need channel and KPI data",
            "inventory_turnover": "Need product and trend data",
            "seasonal_planning": "Need at least 12 months of trend data",
            "promotional_effectiveness": "Need channel and trend data",
            "mrr_growth": "Need at least 3 months of trend data",
            "churn_analysis": "Need repeat rate and KPI data",
            "feature_adoption": "Need product and KPI data",
            "pricing_optimization": "Need KPI and trend data",
            "customer_success": "Need repeat rate and KPI data",
            "seller_performance": "Need channel and product data",
            "buyer_behavior": "Need KPI and channel data",
            "network_effects": "Need KPI and trend data",
            "commission_optimization": "Need channel and KPI data",
            "liquidity_analysis": "Need KPI and trend data"
        }
        
        return reasons.get(question_id, "Data not available")
    
    def get_context_summary(self, context: Dict, results: Dict) -> str:
        """Get a summary of available context data."""
        context_analysis = self._analyze_context_availability(context, results)
        
        summary_lines = ["📊 **Available Data Context**"]
        
        if context_analysis["has_kpis"]:
            summary_lines.append("✅ **KPIs**: Revenue, orders, customers data available")
        if context_analysis["has_trend"]:
            summary_lines.append(f"📈 **Trend Data**: {context_analysis['trend_months']} months of historical data")
        if context_analysis["has_products"]:
            summary_lines.append(f"📦 **Products**: {context_analysis['product_count']} products analyzed")
        if context_analysis["has_channels"]:
            summary_lines.append(f"🛣️ **Channels**: {context_analysis['channel_count']} sales channels")
        if context_analysis["has_forecast"]:
            summary_lines.append("🔮 **Forecasting**: Future predictions available")
        if context_analysis["has_cohorts"]:
            summary_lines.append("👥 **Cohorts**: Customer cohort analysis available")
        if context_analysis["has_rfm"]:
            summary_lines.append("🏷️ **RFM**: Customer segmentation available")
        if context_analysis["has_repeat_rate"]:
            summary_lines.append("🔄 **Retention**: Customer repeat rate data available")
        
        # Add recommendations for more questions
        recommendations = []
        if not context_analysis["has_trend"]:
            recommendations.append("Add date column mapping for trend analysis")
        if not context_analysis["has_products"]:
            recommendations.append("Add product column mapping for product insights")
        if not context_analysis["has_channels"]:
            recommendations.append("Add channel column mapping for channel performance")
        if not context_analysis["has_kpis"]:
            recommendations.append("Add amount column mapping for financial metrics")
        
        if recommendations:
            summary_lines.append("\n💡 **To Enable More Questions**:")
            summary_lines.extend([f"- {rec}" for rec in recommendations])
        
        # Add question count summary
        available_questions = self.get_available_questions(context, results)
        total_available = sum(cat["available_count"] for cat in available_questions.values())
        total_questions = sum(cat["total_count"] for cat in available_questions.values())
        
        summary_lines.append(f"\n🎯 **Question Availability**: {total_available}/{total_questions} questions can be answered")
        
        if total_available < total_questions:
            summary_lines.append(f"📈 **Potential**: {total_questions - total_available} more questions available with additional data")
        
        # Add column mapping tips if there are issues
        if not context_analysis["has_trend"] or not context_analysis["has_kpis"]:
            summary_lines.append("\n⚠️ **Column Mapping Tips**:")
            summary_lines.append("- **Amount**: Should be the total revenue/amount per transaction (e.g., 'Total Amount')")
            summary_lines.append("- **Date**: Should contain the transaction date for trend analysis")
            summary_lines.append("- **Product**: Should identify the product for product insights")
            summary_lines.append("- **Channel**: Should identify the sales channel for channel analysis")
        
        return "\n".join(summary_lines)

    def _get_industry_question_preview(self, industry: str) -> str:
        """Get a preview of industry-specific questions."""
        industry_previews = {
            "retail": "🏪 Store performance, inventory turnover, seasonal planning, promotional effectiveness",
            "saas": "☁️ MRR growth, churn analysis, feature adoption, pricing optimization, customer success",
            "marketplace": "🛒 Seller performance, buyer behavior, network effects, commission optimization, liquidity analysis"
        }
        return industry_previews.get(industry, "Standard business intelligence questions")
