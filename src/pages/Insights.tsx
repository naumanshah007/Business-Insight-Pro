import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { 
  SparklesIcon, 
  LightBulbIcon, 
  ChartBarIcon, 
  UserGroupIcon, 
  CurrencyDollarIcon,
  ChatBubbleLeftRightIcon,
  BuildingStorefrontIcon,
  CloudIcon,
  ShoppingCartIcon
} from '@heroicons/react/24/outline'

const questionCategories = [
  {
    id: 'performance',
    title: '📊 Performance & Growth',
    icon: ChartBarIcon,
    color: 'primary',
    questions: [
      { id: 'revenue_trend', text: 'How is our revenue performing?', icon: '📈' },
      { id: 'growth_rate', text: "What's our month-over-month growth rate?", icon: '🚀' },
      { id: 'seasonality', text: 'Do we see any seasonal patterns?', icon: '🌦️' },
      { id: 'anomalies', text: 'Are there any unusual trends or anomalies?', icon: '⚠️' },
    ]
  },
  {
    id: 'customers',
    title: '👥 Customer Insights',
    icon: UserGroupIcon,
    color: 'success',
    questions: [
      { id: 'customer_growth', text: 'How fast are we acquiring new customers?', icon: '👤' },
      { id: 'retention', text: "What's our customer retention rate?", icon: '🔄' },
      { id: 'lifetime_value', text: "What's the average customer lifetime value?", icon: '💰' },
      { id: 'segments', text: 'How should we segment our customers?', icon: '🏷️' },
    ]
  },
  {
    id: 'products',
    title: '📦 Product Performance',
    icon: CurrencyDollarIcon,
    color: 'accent',
    questions: [
      { id: 'top_products', text: 'Which products are our best performers?', icon: '⭐' },
      { id: 'product_mix', text: 'How diverse is our product portfolio?', icon: '🎯' },
      { id: 'inventory', text: 'Should we adjust our inventory strategy?', icon: '📦' },
    ]
  },
  {
    id: 'operations',
    title: '⚙️ Operations & Efficiency',
    icon: CurrencyDollarIcon,
    color: 'secondary',
    questions: [
      { id: 'order_efficiency', text: 'How efficient are our order operations?', icon: '⚡' },
      { id: 'channel_performance', text: 'Which sales channels perform best?', icon: '🛣️' },
      { id: 'forecasting', text: 'What can we expect in the next 3 months?', icon: '🔮' },
    ]
  },
  {
    id: 'strategy',
    title: '🎯 Strategic Insights',
    icon: CurrencyDollarIcon,
    color: 'warning',
    questions: [
      { id: 'opportunities', text: 'Where are our biggest growth opportunities?', icon: '💡' },
      { id: 'risks', text: 'What risks should we be aware of?', icon: '🚨' },
      { id: 'benchmarks', text: 'How do we compare to industry standards?', icon: '📊' },
      { id: 'recommendations', text: 'What are the top 3 actions we should take?', icon: '✅' },
    ]
  },
  {
    id: 'retail_specific',
    title: '🏪 Retail-Specific Insights',
    icon: BuildingStorefrontIcon,
    color: 'orange',
    questions: [
      { id: 'store_performance', text: 'How are our physical stores performing?', icon: '🏪' },
      { id: 'inventory_turnover', text: "What's our inventory turnover rate?", icon: '🔄' },
      { id: 'seasonal_planning', text: 'How should we plan for seasonal demand?', icon: '📅' },
      { id: 'promotional_effectiveness', text: 'How effective are our promotions?', icon: '🎯' },
    ]
  },
  {
    id: 'saas_specific',
    title: '☁️ SaaS-Specific Insights',
    icon: CloudIcon,
    color: 'blue',
    questions: [
      { id: 'mrr_growth', text: 'How is our Monthly Recurring Revenue growing?', icon: '📈' },
      { id: 'churn_analysis', text: "What's causing customer churn?", icon: '📉' },
      { id: 'feature_adoption', text: 'Which features drive the most engagement?', icon: '🔧' },
      { id: 'pricing_optimization', text: 'How can we optimize our pricing strategy?', icon: '💰' },
      { id: 'customer_success', text: 'How effective is our customer success program?', icon: '🎯' },
    ]
  },
  {
    id: 'marketplace_specific',
    title: '🛒 Marketplace-Specific Insights',
    icon: ShoppingCartIcon,
    color: 'green',
    questions: [
      { id: 'seller_performance', text: 'How are our sellers performing?', icon: '👥' },
      { id: 'buyer_behavior', text: 'What drives buyer purchasing decisions?', icon: '🛍️' },
      { id: 'network_effects', text: 'Are we experiencing network effects?', icon: '🌐' },
      { id: 'commission_optimization', text: 'How can we optimize our commission structure?', icon: '💸' },
      { id: 'liquidity_analysis', text: 'How liquid is our marketplace?', icon: '💧' },
    ]
  }
]

const mockInsights = {
  // Performance & Growth Questions
  revenue_trend: {
    title: '📊 Revenue Trend Analysis',
    content: `**Current Status**: 📈 **+12.5%** month-over-month

**Key Metrics**:
- Total Revenue: **$2,847,392**
- Trend Points: **12** months of data
- Latest Month: **December 2024**

**Insight**: 🚀 **Strong growth momentum** - maintain current strategies and scale successful initiatives.`,
    confidence: 95,
    category: 'performance'
  },
  growth_rate: {
    title: '🚀 Month-over-Month Growth Rate',
    content: `**Growth Analysis**:
- Current Month: **+7.8%**
- Previous Month: **+6.2%**
- 3-Month Average: **+6.9%**

**Trend Analysis**:
📈 **Accelerating growth** - your strategies are working
🎯 **Recommendation**: Double down on what's working
⚠️ **Watch**: Monitor for sustainable growth patterns`,
    confidence: 88,
    category: 'performance'
  },
  seasonality: {
    title: '🌦️ Seasonal Pattern Analysis',
    content: `**Seasonal Trends Detected**:
- **Q4 Peak**: +25% above average (Holiday season)
- **Q1 Dip**: -15% below average (Post-holiday)
- **Q2 Recovery**: +8% above average
- **Q3 Stability**: +2% above average

**Action Items**:
📅 **Plan inventory** for Q4 surge
💰 **Optimize pricing** during peak periods
📊 **Prepare marketing** for Q1 recovery`,
    confidence: 91,
    category: 'performance'
  },
  anomalies: {
    title: '⚠️ Trend Anomalies & Outliers',
    content: `**Anomalies Detected**:
- **March Spike**: +18% revenue (vs. avg +6.5%)
- **August Dip**: -8% revenue (vs. avg +6.5%)
- **November Surge**: +15% revenue (vs. avg +6.5%)

**Root Causes**:
🎯 **March**: Marketing campaign success
⚠️ **August**: Supply chain disruption
🎉 **November**: Black Friday preparation

**Recommendations**:
📈 **Scale successful campaigns** from March
🔧 **Strengthen supply chain** for August
📅 **Optimize holiday planning** for November`,
    confidence: 87,
    category: 'performance'
  },

  // Customer Insights Questions
  customer_growth: {
    title: '👤 Customer Growth Analysis',
    content: `**Current Metrics**:
- Total Customers: **12,847**
- Repeat Customer Rate: **35.2%**

**Customer Health Indicators**:
- 🟢 **Strong** if repeat rate > 30%
- 🟡 **Good** if repeat rate 15-30%
- 🔴 **Needs attention** if repeat rate < 15%

**Growth Insights**:
🎉 **Excellent retention** - customers love your product/service
📊 **Growing customer base** - focus on scaling customer success`,
    confidence: 92,
    category: 'customers'
  },
  retention: {
    title: '🔄 Customer Retention Analysis',
    content: `**Retention Metrics**:
- **1-Month Retention**: 87.3%
- **3-Month Retention**: 72.1%
- **6-Month Retention**: 58.9%
- **12-Month Retention**: 42.3%

**Health Score**: 🟢 **Excellent**
**Industry Benchmark**: 35-45%

**Recommendations**:
💡 **Onboarding optimization** - improve early retention
🎯 **Loyalty programs** - boost long-term retention
📧 **Re-engagement campaigns** - win back churned customers`,
    confidence: 89,
    category: 'customers'
  },
  lifetime_value: {
    title: '💰 Customer Lifetime Value Analysis',
    content: `**CLV Metrics**:
- **Average CLV**: $847
- **Top 20% CLV**: $2,156
- **Bottom 20% CLV**: $234

**CLV by Segment**:
- **Premium Customers**: $1,847 (22% of base)
- **Regular Customers**: $647 (58% of base)
- **New Customers**: $234 (20% of base)

**Growth Opportunities**:
🎯 **Upsell premium customers** - highest potential
📈 **Improve regular customers** - largest segment
🔄 **Optimize new customer onboarding** - foundation for growth`,
    confidence: 93,
    category: 'customers'
  },
  segments: {
    title: '🏷️ Customer Segmentation Strategy',
    content: `**Recommended Segments**:
1. **High-Value Loyalists** (15%): High CLV, high retention
2. **Growth Potential** (25%): Medium CLV, growing engagement
3. **At-Risk Customers** (20%): Declining engagement, need attention
4. **New Customers** (20%): Low CLV, high acquisition cost
5. **Seasonal Buyers** (20%): Purchase during specific periods

**Segment-Specific Strategies**:
🎯 **High-Value**: Premium services, exclusive offers
📈 **Growth**: Cross-selling, engagement campaigns
⚠️ **At-Risk**: Retention programs, feedback collection
🆕 **New**: Onboarding optimization, education
📅 **Seasonal**: Timed marketing, inventory planning`,
    confidence: 90,
    category: 'customers'
  },

  // Product Performance Questions
  top_products: {
    title: '⭐ Top Product Performance',
    content: `**Top 3 Products**:
1. **Product A**: $847,392 (29.8% of revenue)
2. **Product B**: $623,847 (21.9% of revenue)
3. **Product C**: $445,123 (15.6% of revenue)

**Insights**:
🎯 **Focus on winners** - scale top performers
📦 **Bundle opportunities** - combine popular products
💰 **Pricing optimization** - top products can bear price increases`,
    confidence: 94,
    category: 'products'
  },
  product_mix: {
    title: '🎯 Product Portfolio Diversity',
    content: `**Portfolio Analysis**:
- **Revenue Concentration**: Top 3 products = 67.3% of revenue
- **Product Count**: 24 active products
- **Category Distribution**: 8 categories

**Diversity Score**: 🟡 **Moderate** (Target: >70% from top 5)

**Recommendations**:
📦 **Reduce dependency** on top 3 products
🆕 **Develop new products** in underserved categories
🔄 **Optimize underperforming** products or discontinue
📊 **Balance portfolio** across categories`,
    confidence: 88,
    category: 'products'
  },
  inventory: {
    title: '📦 Inventory Strategy Optimization',
    content: `**Inventory Metrics**:
- **Turnover Rate**: 4.2x annually
- **Stockout Rate**: 8.5%
- **Excess Inventory**: 12.3% of total value

**Current Issues**:
⚠️ **High stockout rate** - losing sales
💰 **Excess inventory** - tying up capital
📊 **Imbalanced levels** across products

**Action Plan**:
📈 **Increase safety stock** for top performers
📉 **Reduce inventory** for slow movers
🔄 **Implement demand forecasting** for better planning
📊 **Set reorder points** based on lead times`,
    confidence: 86,
    category: 'products'
  },

  // Operations & Efficiency Questions
  order_efficiency: {
    title: '⚡ Order Operations Efficiency',
    content: `**Efficiency Metrics**:
- **Order Processing Time**: 2.4 hours (Target: <4 hours)
- **Fulfillment Accuracy**: 98.7% (Target: >98%)
- **Return Rate**: 3.2% (Industry avg: 4.1%)

**Performance Analysis**:
✅ **Above industry standards** in all key metrics
🎯 **Order processing** can be optimized further
📦 **Fulfillment accuracy** is excellent

**Optimization Opportunities**:
⚡ **Automate order processing** - reduce to <2 hours
📊 **Implement real-time tracking** for customers
🔄 **Streamline return process** - reduce to <3%
📈 **Scale successful processes** to other locations`,
    confidence: 91,
    category: 'operations'
  },
  channel_performance: {
    title: '🛣️ Sales Channel Performance',
    content: `**Channel Analysis**:
1. **Online Store**: 45% of revenue, +18% growth
2. **Mobile App**: 32% of revenue, +25% growth
3. **Physical Stores**: 18% of revenue, +8% growth
4. **Marketplace**: 5% of revenue, +12% growth

**Channel Insights**:
📱 **Mobile app** is fastest growing channel
🏪 **Physical stores** need digital transformation
🌐 **Online store** remains the backbone
🛒 **Marketplace** has untapped potential

**Strategic Actions**:
📱 **Invest in mobile experience** - highest ROI
🏪 **Digitize physical stores** - omnichannel approach
🌐 **Optimize online store** - maintain leadership
🛒 **Expand marketplace presence** - new customer acquisition`,
    confidence: 89,
    category: 'operations'
  },
  forecasting: {
    title: '🔮 3-Month Business Forecast',
    content: `**Revenue Forecast**:
- **Month 1**: $298,000 (+8.2%)
- **Month 2**: $312,000 (+4.7%)
- **Month 3**: $325,000 (+4.2%)

**Customer Forecast**:
- **Month 1**: 13,200 (+2.7%)
- **Month 2**: 13,450 (+1.9%)
- **Month 3**: 13,700 (+1.9%)

**Confidence Level**: 85%
**Key Assumptions**: Current trends continue, no major market changes

**Risk Factors**:
⚠️ **Economic uncertainty** - 15% downside risk
📈 **Seasonal patterns** - Q1 typically slower
🔄 **Competition** - new entrants in market`,
    confidence: 85,
    category: 'operations'
  },

  // Strategic Insights Questions
  opportunities: {
    title: '💡 Growth Opportunities',
    content: `**Top 3 Opportunities**:
1. **Market Expansion**: 15-20% growth potential
   - Target: New geographic markets
   - Investment: $50K marketing budget
   - Timeline: 6 months

2. **Product Development**: 10-15% growth potential
   - Target: Feature enhancements
   - Investment: $30K development
   - Timeline: 3 months

3. **Customer Acquisition**: 8-12% growth potential
   - Target: New customer segments
   - Investment: $25K campaigns
   - Timeline: 4 months`,
    confidence: 87,
    category: 'strategy'
  },
  risks: {
    title: '🚨 Risk Assessment & Mitigation',
    content: `**High-Risk Areas**:
1. **Customer Concentration**: Top 20% = 60% of revenue
2. **Supply Chain Dependency**: Single supplier for key products
3. **Seasonal Volatility**: 40% revenue variation year-round

**Risk Mitigation Strategies**:
🔄 **Diversify customer base** - reduce concentration risk
📦 **Develop backup suppliers** - supply chain resilience
📊 **Implement seasonal planning** - smooth revenue fluctuations
💰 **Build cash reserves** - buffer against downturns

**Monitoring Metrics**:
📈 **Customer concentration ratio** - target <50%
🔗 **Supplier diversity score** - target >3 suppliers
📊 **Revenue volatility** - target <25%`,
    confidence: 84,
    category: 'strategy'
  },
  benchmarks: {
    title: '📊 Industry Benchmark Analysis',
    content: `**Performance vs Industry**:
- **Revenue Growth**: 7.8% (Industry: 4.2%) ✅ **+87% better**
- **Customer Retention**: 87.3% (Industry: 72.1%) ✅ **+21% better**
- **Profit Margin**: 18.5% (Industry: 15.2%) ✅ **+22% better**
- **Market Share**: 3.2% (Industry avg: 2.1%) ✅ **+52% better**

**Competitive Position**: 🥇 **Market Leader**

**Areas for Improvement**:
📱 **Digital adoption** - behind top competitors
🌍 **International expansion** - limited presence
💡 **Innovation rate** - industry average

**Next Steps**:
🚀 **Maintain leadership** in current metrics
📱 **Accelerate digital transformation**
🌍 **Explore international markets**
💡 **Increase R&D investment**`,
    confidence: 92,
    category: 'strategy'
  },
  recommendations: {
    title: '✅ Top 3 Strategic Actions',
    content: `**Immediate Actions (Next 30 Days)**:
1. **Optimize Customer Onboarding**
   - Goal: Increase 1-month retention from 87.3% to 90%
   - Action: Implement personalized onboarding flows
   - Expected Impact: +$45K monthly revenue

2. **Launch Mobile App Optimization**
   - Goal: Increase mobile revenue from 32% to 38%
   - Action: Improve app UX and add mobile-specific features
   - Expected Impact: +$28K monthly revenue

3. **Implement Predictive Analytics**
   - Goal: Reduce inventory costs by 15%
   - Action: Deploy demand forecasting system
   - Expected Impact: +$12K monthly savings

**Success Metrics**:
📊 **Total Expected Impact**: +$85K monthly revenue
⏰ **Timeline**: 30-90 days
💰 **ROI**: 340% return on investment`,
    confidence: 89,
    category: 'strategy'
  },

  // Retail-Specific Questions
  store_performance: {
    title: '🏪 Physical Store Performance',
    content: `**Store Metrics**:
- **Total Stores**: 8 locations
- **Average Revenue per Store**: $64,000/month
- **Store Utilization**: 78% (Target: >85%)

**Top Performing Stores**:
1. **Downtown Location**: $89,000/month, 92% utilization
2. **Mall Location**: $76,000/month, 88% utilization
3. **Suburban Location**: $71,000/month, 85% utilization

**Optimization Opportunities**:
📈 **Increase store utilization** to 85% target
🔄 **Implement best practices** from top performers
📱 **Add digital touchpoints** to physical stores
📊 **Optimize store layouts** based on traffic patterns`,
    confidence: 88,
    category: 'retail_specific'
  },
  inventory_turnover: {
    title: '🔄 Inventory Turnover Analysis',
    content: `**Turnover Metrics**:
- **Current Turnover**: 4.2x annually
- **Industry Average**: 3.8x annually
- **Target**: 5.0x annually

**Category Performance**:
- **Electronics**: 6.1x (Excellent)
- **Clothing**: 4.8x (Good)
- **Home Goods**: 3.2x (Needs improvement)
- **Seasonal Items**: 2.8x (Poor)

**Action Plan**:
📦 **Optimize home goods** - implement just-in-time inventory
📅 **Improve seasonal planning** - reduce overstock
📊 **Set category-specific** turnover targets
🔄 **Implement automated** reordering for fast movers`,
    confidence: 86,
    category: 'retail_specific'
  },
  seasonal_planning: {
    title: '📅 Seasonal Demand Planning',
    content: `**Seasonal Patterns**:
- **Q4 (Oct-Dec)**: +35% above average (Holiday season)
- **Q1 (Jan-Mar)**: -20% below average (Post-holiday)
- **Q2 (Apr-Jun)**: +5% above average (Spring recovery)
- **Q3 (Jul-Sep)**: -5% below average (Summer lull)

**Planning Recommendations**:
📦 **Q4 Preparation**: Increase inventory by 40% starting August
💰 **Q1 Strategy**: Focus on clearance and new product launches
🌱 **Q2 Recovery**: Marketing campaigns for spring products
☀️ **Q3 Optimization**: Reduce inventory, focus on essentials

**Inventory Targets**:
📊 **Safety stock levels** by season
🔄 **Reorder timing** optimization
📈 **Demand forecasting** accuracy improvement`,
    confidence: 90,
    category: 'retail_specific'
  },
  promotional_effectiveness: {
    title: '🎯 Promotional Campaign Analysis',
    content: `**Campaign Performance**:
- **Email Campaigns**: 12.5% conversion rate
- **Social Media Ads**: 8.7% conversion rate
- **In-Store Promotions**: 15.2% conversion rate
- **Loyalty Programs**: 22.1% conversion rate

**Top Performing Promotions**:
1. **"Buy 2 Get 1 Free"**: +45% revenue lift
2. **"Flash Sale"**: +38% revenue lift
3. **"Loyalty Member Discount"**: +28% revenue lift

**Optimization Strategy**:
📧 **Improve email campaigns** - target 15% conversion
📱 **Enhance social media** - target 12% conversion
🏪 **Scale in-store promotions** - highest ROI
🎁 **Expand loyalty programs** - best customer retention`,
    confidence: 87,
    category: 'retail_specific'
  },

  // SaaS-Specific Questions
  mrr_growth: {
    title: '📈 Monthly Recurring Revenue Growth',
    content: `**MRR Metrics**:
- **Current MRR**: $847,392
- **MRR Growth Rate**: +7.8% month-over-month
- **Annual Recurring Revenue**: $10.2M

**MRR Breakdown**:
- **New MRR**: $67,000 (+8.1%)
- **Expansion MRR**: $45,000 (+12.3%)
- **Churn MRR**: -$23,000 (-2.7%)

**Growth Drivers**:
🚀 **Product-led growth** - 45% of new MRR
💼 **Sales team expansion** - 35% of new MRR
🔄 **Customer success** - 20% of new MRR

**Next Quarter Targets**:
📊 **MRR Growth**: 8.5% month-over-month
🎯 **Churn Reduction**: <2.5%
📈 **Expansion Revenue**: +15%`,
    confidence: 91,
    category: 'saas_specific'
  },
  churn_analysis: {
    title: '📉 Customer Churn Analysis',
    content: `**Churn Metrics**:
- **Monthly Churn Rate**: 2.7%
- **Annual Churn Rate**: 28.4%
- **Industry Average**: 32.1%

**Churn Reasons**:
1. **Price Sensitivity**: 35% of churns
2. **Feature Gaps**: 28% of churns
3. **Poor Onboarding**: 22% of churns
4. **Competition**: 15% of churns

**Churn Prevention Strategies**:
💰 **Implement tiered pricing** - reduce price sensitivity
🔧 **Accelerate feature development** - address gaps
📚 **Improve onboarding** - reduce early churn
🎯 **Competitive positioning** - highlight differentiators

**Success Metrics**:
📉 **Target churn rate**: <2.5% monthly
🔄 **Churn reduction**: 15% improvement`,
    confidence: 88,
    category: 'saas_specific'
  },
  feature_adoption: {
    title: '🔧 Feature Adoption Analysis',
    content: `**Adoption Metrics**:
- **Core Features**: 87% adoption rate
- **Advanced Features**: 34% adoption rate
- **New Features**: 23% adoption rate

**Top Adopted Features**:
1. **Dashboard Analytics**: 92% adoption
2. **Data Export**: 89% adoption
3. **API Integration**: 78% adoption

**Low Adoption Features**:
⚠️ **Advanced Reporting**: 28% adoption
⚠️ **Custom Workflows**: 19% adoption
⚠️ **Team Collaboration**: 31% adoption

**Improvement Strategy**:
📚 **Better feature education** - increase awareness
🎯 **Targeted feature promotion** - based on usage patterns
🔄 **Simplify complex features** - reduce learning curve
📊 **Usage analytics** - identify adoption barriers`,
    confidence: 85,
    category: 'saas_specific'
  },
  pricing_optimization: {
    title: '💰 Pricing Strategy Optimization',
    content: `**Current Pricing Tiers**:
- **Starter**: $29/month (15% of customers)
- **Professional**: $99/month (45% of customers)
- **Enterprise**: $299/month (40% of customers)

**Pricing Analysis**:
💰 **Average Revenue Per User**: $156/month
📊 **Price Elasticity**: -1.2 (moderate sensitivity)
🎯 **Optimal Price Point**: +8% increase possible

**Optimization Opportunities**:
📈 **Increase starter tier** to $39/month (+34% revenue)
💼 **Add premium tier** at $199/month
🔄 **Implement usage-based** pricing for enterprise
🎁 **Bundle features** to increase perceived value

**Expected Impact**:
📊 **Revenue Increase**: +12-18%
📉 **Churn Impact**: Minimal (<1% increase)`,
    confidence: 89,
    category: 'saas_specific'
  },
  customer_success: {
    title: '🎯 Customer Success Program Effectiveness',
    content: `**Success Metrics**:
- **Customer Satisfaction**: 8.7/10
- **Net Promoter Score**: 72
- **Time to Value**: 14 days
- **Success Rate**: 89%

**Program Components**:
1. **Onboarding**: 95% completion rate
2. **Training Sessions**: 78% attendance
3. **Success Reviews**: 82% participation
4. **Support Response**: 2.4 hours average

**Impact on Business**:
📈 **Retention Improvement**: +23% for engaged customers
💰 **Revenue Expansion**: +18% for success program participants
🔄 **Churn Reduction**: -31% for active program users

**Optimization Areas**:
📚 **Improve training** - target 85% attendance
⏰ **Reduce time to value** - target 10 days
📊 **Increase engagement** - target 90% participation`,
    confidence: 90,
    category: 'saas_specific'
  },

  // Marketplace-Specific Questions
  seller_performance: {
    title: '👥 Seller Performance Analysis',
    content: `**Seller Metrics**:
- **Total Sellers**: 1,247 active sellers
- **Top 20% Sellers**: Generate 65% of marketplace revenue
- **Average Seller Revenue**: $2,847/month

**Performance Tiers**:
🥇 **Top Performers** (20%): $8,500+/month
🥈 **Mid-Tier** (50%): $1,500-8,500/month
🥉 **Emerging** (30%): <$1,500/month

**Seller Success Factors**:
📱 **High-quality product images** (+45% conversion)
📝 **Detailed product descriptions** (+32% conversion)
🚚 **Fast shipping** (+28% conversion)
⭐ **Customer reviews** (+38% conversion)

**Optimization Strategy**:
🎯 **Support top performers** - scale their success
📈 **Improve mid-tier** - focus on conversion optimization
🆕 **Onboard emerging sellers** - reduce barriers to success`,
    confidence: 87,
    category: 'marketplace_specific'
  },
  buyer_behavior: {
    title: '🛍️ Buyer Behavior Analysis',
    content: `**Buyer Metrics**:
- **Total Buyers**: 8,947 active buyers
- **Repeat Purchase Rate**: 42.3%
- **Average Order Value**: $156

**Buyer Segments**:
🛒 **Frequent Buyers** (25%): 5+ purchases/month
🔄 **Regular Buyers** (45%): 2-4 purchases/month
🆕 **Occasional Buyers** (30%): 1 purchase/month

**Purchase Patterns**:
📱 **Mobile-first**: 68% of purchases
💳 **Payment preference**: Credit cards (45%), Digital wallets (35%)
🚚 **Shipping preference**: Free shipping (78%), Fast delivery (22%)

**Behavioral Insights**:
🎯 **Mobile optimization** is critical for conversion
💰 **Free shipping** significantly increases AOV
📱 **Push notifications** drive repeat purchases
⭐ **Social proof** (reviews) increases conversion by 45%`,
    confidence: 89,
    category: 'marketplace_specific'
  },
  network_effects: {
    title: '🌐 Network Effects Analysis',
    content: `**Network Effect Metrics**:
- **Seller Growth**: +15% month-over-month
- **Buyer Growth**: +12% month-over-month
- **Cross-Platform Engagement**: 34%

**Network Strength Indicators**:
✅ **Positive feedback loops** - more sellers attract more buyers
✅ **Increasing platform value** - each new user adds value
✅ **Sticky ecosystem** - high switching costs for users

**Network Effect Drivers**:
👥 **Seller diversity** - variety attracts more buyers
📱 **Platform features** - tools increase seller success
🔄 **User engagement** - active users attract more users
⭐ **Quality content** - good products attract more buyers

**Growth Strategy**:
🚀 **Accelerate seller acquisition** - focus on quality
📱 **Enhance platform features** - increase user value
🔄 **Improve user engagement** - strengthen network effects
🌍 **Expand to new markets** - leverage network strength`,
    confidence: 86,
    category: 'marketplace_specific'
  },
  commission_optimization: {
    title: '💸 Commission Structure Optimization',
    content: `**Current Commission Structure**:
- **Standard Commission**: 8.5% of transaction value
- **Premium Sellers**: 6.5% (volume discount)
- **New Sellers**: 10% (first 3 months)

**Commission Analysis**:
💰 **Average Commission Rate**: 8.2%
📊 **Revenue Impact**: 15% of total platform revenue
🎯 **Competitive Position**: Industry average

**Optimization Opportunities**:
📈 **Tiered commission** based on seller performance
🎯 **Performance incentives** for high-quality sellers
🆕 **New seller programs** to reduce barriers
💰 **Volume discounts** to encourage growth

**Expected Outcomes**:
📊 **Revenue Increase**: +8-12%
🎯 **Seller Satisfaction**: +15%
🔄 **Platform Growth**: +20%`,
    confidence: 84,
    category: 'marketplace_specific'
  },
  liquidity_analysis: {
    title: '💧 Marketplace Liquidity Analysis',
    content: `**Liquidity Metrics**:
- **Market Depth**: 8.5/10 (Excellent)
- **Transaction Velocity**: 6.2/10 (Good)
- **Price Discovery**: 7.8/10 (Good)

**Liquidity Indicators**:
✅ **High transaction volume** - active marketplace
✅ **Price stability** - efficient price discovery
✅ **Quick transactions** - good buyer-seller matching

**Liquidity Challenges**:
⚠️ **Seasonal fluctuations** - 25% volume variation
⚠️ **Category imbalances** - some categories more liquid
⚠️ **Geographic concentration** - limited regional diversity

**Improvement Strategies**:
📊 **Diversify inventory** across categories
🌍 **Expand geographic** coverage
📈 **Increase transaction** frequency
🔄 **Optimize matching** algorithms

**Success Metrics**:
🎯 **Target liquidity score**: 9.0/10
📊 **Volume growth**: +15% year-over-year
🌍 **Geographic coverage**: +25% expansion`,
    confidence: 88,
    category: 'marketplace_specific'
  }
}

export default function Insights() {
  const [industry, setIndustry] = useState('generic')
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null)
  const [selectedQuestion, setSelectedQuestion] = useState<string | null>(null)
  
  // Tooltip states for click-based interactions
  const [activeTooltips, setActiveTooltips] = useState<{
    [key: string]: boolean
  }>({})

  const toggleTooltip = (tooltipId: string) => {
    setActiveTooltips(prev => ({
      ...prev,
      [tooltipId]: !prev[tooltipId]
    }))
  }

  const closeAllTooltips = () => {
    setActiveTooltips({})
  }

  // Smart positioning for tooltips to ensure they're always visible
  const getTooltipPosition = (tooltipId: string, defaultPosition: 'top' | 'bottom' | 'left' | 'right') => {
    const tooltipElement = document.querySelector(`[data-tooltip-id="${tooltipId}"]`)
    if (!tooltipElement) return defaultPosition

    const rect = tooltipElement.getBoundingClientRect()
    const viewportWidth = window.innerWidth
    const viewportHeight = window.innerHeight
    const tooltipWidth = 280 // max-w-[280px]
    const tooltipHeight = 120 // approximate height

    // Check if tooltip would overflow on each side
    const wouldOverflowRight = rect.right + tooltipWidth > viewportWidth
    const wouldOverflowLeft = rect.left - tooltipWidth < 0
    const wouldOverflowBottom = rect.bottom + tooltipHeight > viewportHeight
    const wouldOverflowTop = rect.top - tooltipHeight < 0

    // Return the best position that avoids overflow
    switch (defaultPosition) {
      case 'top':
        return wouldOverflowTop ? 'bottom' : 'top'
      case 'bottom':
        return wouldOverflowBottom ? 'top' : 'bottom'
      case 'left':
        return wouldOverflowLeft ? 'right' : 'left'
      case 'right':
        return wouldOverflowRight ? 'left' : 'right'
      default:
        return defaultPosition
    }
  }

  // Mobile-friendly tooltip positioning with dynamic classes
  const getTooltipClasses = (tooltipId: string, defaultPosition: 'top' | 'bottom' | 'left' | 'right') => {
    const position = getTooltipPosition(tooltipId, defaultPosition)
    
    // Base classes for all tooltips
    const baseClasses = "bg-gray-900 text-white text-xs rounded-lg py-2 px-3 shadow-lg max-w-[280px] z-20"
    
    // Position-specific classes
    switch (position) {
      case 'top':
        return `${baseClasses} absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2`
      case 'bottom':
        return `${baseClasses} absolute top-full left-1/2 transform -translate-x-1/2 mt-2`
      case 'left':
        return `${baseClasses} absolute right-full top-1/2 transform -translate-y-1/2 mr-2`
      case 'right':
        return `${baseClasses} absolute left-full top-1/2 transform -translate-y-1/2 ml-2`
      default:
        return `${baseClasses} absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2`
    }
  }

  // Mobile-responsive tooltip width
  const getTooltipWidth = () => {
    const viewportWidth = window.innerWidth
    if (viewportWidth < 640) return 'max-w-[250px]' // sm breakpoint
    if (viewportWidth < 1024) return 'max-w-[280px]' // lg breakpoint
    return 'max-w-[320px]' // xl and above
  }

  // Close tooltips when clicking outside
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (activeTooltips && Object.keys(activeTooltips).length > 0) {
        const target = event.target as HTMLElement
        if (!target.closest('[data-tooltip]') && !target.closest('button')) {
          closeAllTooltips()
        }
      }
    }

    document.addEventListener('mousedown', handleClickOutside)
    return () => {
      document.removeEventListener('mousedown', handleClickOutside)
    }
  }, [activeTooltips])

  // Reposition tooltips on window resize
  useEffect(() => {
    const handleResize = () => {
      // Close all tooltips on resize to prevent positioning issues
      if (Object.keys(activeTooltips).length > 0) {
        closeAllTooltips()
      }
    }

    window.addEventListener('resize', handleResize)
    return () => {
      window.removeEventListener('resize', handleResize)
    }
  }, [activeTooltips])

  useEffect(() => {
    console.log('Insights component mounted')
    console.log('Current industry:', industry)
    console.log('Selected category:', selectedCategory)
    console.log('Selected question:', selectedQuestion)
  }, [industry, selectedCategory, selectedQuestion])

  const handleQuestionClick = (questionId: string) => {
    console.log('Question clicked:', questionId)
    setSelectedQuestion(questionId)
    closeAllTooltips() // Close tooltips when selecting a question
  }

  const getInsight = (questionId: string) => {
    return mockInsights[questionId as keyof typeof mockInsights] || {
      title: '🤖 AI Analysis',
      content: 'This question requires specific analysis. Please select from our curated question list for detailed insights.',
      confidence: 85,
      category: 'general'
    }
  }

  const getIndustryIcon = (industryType: string) => {
    switch (industryType) {
      case 'retail': return '🏪'
      case 'saas': return '☁️'
      case 'marketplace': return '🛒'
      default: return '🏢'
    }
  }

  const getIndustryDescription = (industryType: string) => {
    switch (industryType) {
      case 'retail': return 'Store performance, inventory, seasonal planning'
      case 'saas': return 'MRR growth, churn analysis, feature adoption'
      case 'marketplace': return 'Seller performance, buyer behavior, network effects'
      default: return 'General business analysis for any industry'
    }
  }

  const renderVisualAnswer = (questionId: string) => {
    const insight = getInsight(questionId);
    
    if (!insight) {
      return (
        <div className="text-center py-12">
          <p className="text-lg text-gray-600">No specific visual analysis available for this question.</p>
        </div>
      );
    }

    // Parse the content to extract metrics and create visual elements
    const content = insight.content;
    
    return (
      <div className="space-y-6">
        {/* Key Metrics Section */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {extractMetrics(content).map((metric, index) => (
            <div key={index} className="bg-gradient-to-br from-blue-50 to-indigo-100 rounded-2xl p-4 sm:p-6 border border-blue-200 shadow-lg group relative">
              <div className="flex items-center space-x-3 mb-3">
                <div className="w-8 h-8 sm:w-10 sm:h-10 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-xl flex items-center justify-center">
                  <span className="text-white text-sm sm:text-lg">{metric.icon}</span>
                </div>
                <div className="min-w-0 flex-1">
                  <h4 className="font-semibold text-gray-900 text-sm sm:text-base truncate">{metric.label}</h4>
                  <p className="text-xs sm:text-sm text-gray-600 truncate">{metric.description}</p>
                </div>
              </div>
              <div className="text-xl sm:text-2xl font-bold text-blue-700">{metric.value}</div>
              {metric.change && (
                <div className="relative group">
                  <div className={`text-xs sm:text-sm font-medium ${metric.change > 0 ? 'text-green-600' : 'text-red-600'} cursor-help flex items-center space-x-1`}>
                    <span>{metric.change > 0 ? '↗' : '↘'}</span>
                    <span>{Math.abs(metric.change)}%</span>
                    <span className="text-xs opacity-70">ℹ️</span>
                  </div>
                  
                  {/* Click Tooltip for Percentage Change */}
                  <div className="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 z-20">
                    <button
                      onClick={() => toggleTooltip(`change-${index}`)}
                      className="text-xs opacity-70 hover:opacity-100 transition-opacity duration-200"
                      data-tooltip-id={`change-${index}`}
                    >
                      ℹ️
                    </button>
                    
                    {activeTooltips[`change-${index}`] && (
                      <div className={getTooltipClasses(`change-${index}`, 'top')} data-tooltip>
                        <div className={`${getTooltipWidth()} bg-gray-900 text-white text-xs rounded-lg py-2 px-3 shadow-lg mx-auto`}>
                          <div className="flex items-center justify-between mb-1">
                            <span className="font-semibold">Change Explanation</span>
                            <button
                              onClick={() => toggleTooltip(`change-${index}`)}
                              className="text-gray-400 hover:text-white text-lg leading-none"
                            >
                              ×
                            </button>
                          </div>
                          <div className="text-gray-200 text-center">
                            {metric.change > 0 
                              ? `This metric has increased by ${metric.change}% compared to the previous period. This indicates positive performance and growth.`
                              : `This metric has decreased by ${Math.abs(metric.change)}% compared to the previous period. This may indicate an area needing attention.`
                            }
                          </div>
                          <div className="text-xs text-gray-400 mt-1 text-center">
                            Based on period-over-period comparison
                          </div>
                          {/* Dynamic arrow positioning */}
                          <div className={`absolute w-0 h-0 border-4 border-transparent ${
                            getTooltipPosition(`change-${index}`, 'top') === 'bottom' 
                              ? 'bottom-full border-b-gray-900' 
                              : 'top-full border-t-gray-900'
                          } left-1/2 transform -translate-x-1/2`}></div>
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              )}
              
              {/* Metric Info Tooltip - Mobile Friendly */}
              <div className="absolute top-2 sm:top-4 right-2 sm:right-4">
                <button
                  onClick={() => toggleTooltip(`metric-${index}`)}
                  className="w-5 h-5 sm:w-6 sm:h-6 bg-blue-100 rounded-full flex items-center justify-center cursor-pointer hover:bg-blue-200 transition-colors duration-200"
                  data-tooltip-id={`metric-${index}`}
                >
                  <span className="text-blue-600 text-xs font-bold">?</span>
                </button>
                
                {/* Click Tooltip for Metric */}
                {activeTooltips[`metric-${index}`] && (
                  <div className={getTooltipClasses(`metric-${index}`, 'bottom')} data-tooltip>
                    <div className={`${getTooltipWidth()} bg-gray-900 text-white text-xs rounded-lg py-2 px-3 shadow-lg`}>
                      <div className="flex items-center justify-between mb-1">
                        <span className="font-semibold">{metric.label}</span>
                        <button
                          onClick={() => toggleTooltip(`metric-${index}`)}
                          className="text-gray-400 hover:text-white text-lg leading-none"
                        >
                          ×
                        </button>
                      </div>
                      <div className="text-gray-200">
                        {getMetricExplanation(metric.label, metric.value)}
                      </div>
                      <div className="text-xs text-gray-400 mt-1">
                        Current value as of latest data
                      </div>
                      {/* Dynamic arrow positioning */}
                      <div className={`absolute w-0 h-0 border-4 border-transparent ${
                        getTooltipPosition(`metric-${index}`, 'bottom') === 'top' 
                          ? 'top-full border-t-gray-900' 
                          : 'bottom-full border-b-gray-900'
                      } left-1/2 transform -translate-x-1/2`}></div>
                    </div>
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>

        {/* Analysis Sections */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 sm:gap-6">
          {/* Positive Indicators */}
          <div className="bg-gradient-to-br from-green-50 to-emerald-100 rounded-2xl p-4 sm:p-6 border border-green-200 shadow-lg group relative">
            <div className="flex items-center space-x-3 mb-4">
              <div className="w-10 h-10 sm:w-12 sm:h-12 bg-gradient-to-br from-green-500 to-emerald-600 rounded-xl flex items-center justify-center">
                <span className="text-white text-lg sm:text-xl">✅</span>
              </div>
              <div className="flex-1 min-w-0">
                <h3 className="text-base sm:text-lg font-semibold text-gray-900">Positive Indicators</h3>
              </div>
              <button
                onClick={() => toggleTooltip('positive-indicators-section')}
                className="w-5 h-5 sm:w-6 sm:h-6 bg-green-100 rounded-full flex items-center justify-center cursor-pointer hover:bg-green-200 transition-colors duration-200 opacity-0 group-hover:opacity-100"
              >
                <span className="text-green-600 text-xs font-bold">?</span>
              </button>
            </div>
            <div className="space-y-2 sm:space-y-3">
              {extractPositiveIndicators(content).map((indicator, index) => (
                <div key={index} className="flex items-start space-x-3 text-xs sm:text-sm group/item relative">
                  <div className="w-2 h-2 bg-green-500 rounded-full mt-1.5 flex-shrink-0"></div>
                  <span className="text-gray-700 cursor-help flex-1">{indicator}</span>
                  
                  {/* Click Tooltip for each indicator */}
                  <button
                    onClick={() => toggleTooltip(`positive-indicator-${index}`)}
                    className="ml-2 text-gray-400 hover:text-gray-600 transition-colors duration-200"
                    data-tooltip-id={`positive-indicator-${index}`}
                  >
                    ℹ️
                  </button>
                  
                  {activeTooltips[`positive-indicator-${index}`] && (
                    <div className={getTooltipClasses(`positive-indicator-${index}`, 'right')} data-tooltip>
                      <div className={`${getTooltipWidth()} bg-gray-900 text-white text-xs rounded-lg py-2 px-3 shadow-lg`}>
                        <div className="flex items-center justify-between mb-1">
                          <span className="font-semibold">Positive Factor</span>
                          <button
                            onClick={() => toggleTooltip(`positive-indicator-${index}`)}
                            className="text-gray-400 hover:text-white text-lg leading-none"
                          >
                            ×
                          </button>
                        </div>
                        <div className="text-gray-200">
                          {getPositiveIndicatorExplanation(indicator)}
                        </div>
                        {/* Dynamic arrow positioning */}
                        <div className={`absolute w-0 h-0 border-4 border-transparent ${
                          getTooltipPosition(`positive-indicator-${index}`, 'right') === 'left' 
                            ? 'left-full border-l-gray-900' 
                            : 'right-full border-r-gray-900'
                        } top-1/2 transform -translate-y-1/2`}></div>
                      </div>
                    </div>
                  )}
                </div>
              ))}
            </div>
            
            {/* Section Info Tooltip - Mobile Friendly */}
            {activeTooltips['positive-indicators-section'] && (
              <div className={getTooltipClasses('positive-indicators-section', 'bottom')} data-tooltip>
                <div className={`${getTooltipWidth()} bg-gray-900 text-white text-xs rounded-lg py-2 px-3 shadow-lg`}>
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-semibold">Positive Indicators</span>
                    <button
                      onClick={() => toggleTooltip('positive-indicators-section')}
                      className="text-gray-400 hover:text-white text-lg leading-none"
                    >
                      ×
                    </button>
                  </div>
                  <div className="text-gray-200">
                    These are the areas where your business is performing well and exceeding expectations. Focus on maintaining and scaling these strengths.
                  </div>
                  {/* Dynamic arrow positioning */}
                  <div className={`absolute w-0 h-0 border-4 border-transparent ${
                    getTooltipPosition('positive-indicators-section', 'bottom') === 'top' 
                      ? 'top-full border-t-gray-900' 
                      : 'bottom-full border-b-gray-900'
                  } right-4`}></div>
                </div>
              </div>
            )}
          </div>

          {/* Areas for Improvement */}
          <div className="bg-gradient-to-br from-amber-50 to-orange-100 rounded-2xl p-4 sm:p-6 border border-amber-200 shadow-lg group relative">
            <div className="flex items-center space-x-3 mb-4">
              <div className="w-10 h-10 sm:w-12 sm:h-12 bg-gradient-to-br from-amber-500 to-orange-600 rounded-xl flex items-center justify-center">
                <span className="text-white text-lg sm:text-xl">⚠️</span>
              </div>
              <div className="flex-1 min-w-0">
                <h3 className="text-base sm:text-lg font-semibold text-gray-900">Areas for Improvement</h3>
              </div>
              <button
                onClick={() => toggleTooltip('improvement-areas-section')}
                className="w-5 h-5 sm:w-6 sm:h-6 bg-amber-100 rounded-full flex items-center justify-center cursor-pointer hover:bg-amber-200 transition-colors duration-200 opacity-0 group-hover:opacity-100"
              >
                <span className="text-amber-600 text-xs font-bold">?</span>
              </button>
            </div>
            <div className="space-y-2 sm:space-y-3">
              {extractImprovementAreas(content).map((area, index) => (
                <div key={index} className="flex items-start space-x-3 text-xs sm:text-sm group/item relative">
                  <div className="w-2 h-2 bg-amber-500 rounded-full mt-1.5 flex-shrink-0"></div>
                  <span className="text-gray-700 cursor-help flex-1">{area}</span>
                  
                  {/* Click Tooltip for each area */}
                  <button
                    onClick={() => toggleTooltip(`improvement-area-${index}`)}
                    className="ml-2 text-gray-400 hover:text-gray-600 transition-colors duration-200"
                    data-tooltip-id={`improvement-area-${index}`}
                  >
                    ℹ️
                  </button>
                  
                  {activeTooltips[`improvement-area-${index}`] && (
                    <div className={getTooltipClasses(`improvement-area-${index}`, 'right')} data-tooltip>
                      <div className={`${getTooltipWidth()} bg-gray-900 text-white text-xs rounded-lg py-2 px-3 shadow-lg`}>
                        <div className="flex items-center justify-between mb-1">
                          <span className="font-semibold">Improvement Area</span>
                          <button
                            onClick={() => toggleTooltip(`improvement-area-${index}`)}
                            className="text-gray-400 hover:text-white text-lg leading-none"
                          >
                            ×
                          </button>
                        </div>
                        <div className="text-gray-200">
                          {getImprovementAreaExplanation(area)}
                        </div>
                        {/* Dynamic arrow positioning */}
                        <div className={`absolute w-0 h-0 border-4 border-transparent ${
                          getTooltipPosition(`improvement-area-${index}`, 'right') === 'left' 
                            ? 'left-full border-l-gray-900' 
                            : 'right-full border-r-gray-900'
                        } top-1/2 transform -translate-y-1/2`}></div>
                      </div>
                    </div>
                  )}
                </div>
              ))}
            </div>
            
            {/* Section Info Tooltip - Mobile Friendly */}
            {activeTooltips['improvement-areas-section'] && (
              <div className={getTooltipClasses('improvement-areas-section', 'bottom')} data-tooltip>
                <div className={`${getTooltipWidth()} bg-gray-900 text-white text-xs rounded-lg py-2 px-3 shadow-lg`}>
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-semibold">Areas for Improvement</span>
                    <button
                      onClick={() => toggleTooltip('improvement-areas-section')}
                      className="text-gray-400 hover:text-white text-lg leading-none"
                    >
                      ×
                    </button>
                  </div>
                  <div className="text-gray-200">
                    These are the areas where your business could perform better. Addressing these can lead to significant improvements in overall performance.
                  </div>
                  {/* Dynamic arrow positioning */}
                  <div className={`absolute w-0 h-0 border-4 border-transparent ${
                    getTooltipPosition('improvement-areas-section', 'bottom') === 'top' 
                      ? 'top-full border-t-gray-900' 
                      : 'bottom-full border-b-gray-900'
                  } right-4`}></div>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Action Items */}
        <div className="bg-gradient-to-br from-purple-50 to-pink-100 rounded-2xl p-4 sm:p-6 border border-purple-200 shadow-lg">
          <div className="flex items-center space-x-3 mb-4">
            <div className="w-10 h-10 sm:w-12 sm:h-12 bg-gradient-to-br from-purple-500 to-pink-600 rounded-xl flex items-center justify-center">
              <span className="text-white text-lg sm:text-xl">🎯</span>
            </div>
            <h3 className="text-base sm:text-lg font-semibold text-gray-900">Recommended Actions</h3>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
            {extractActionItems(content).map((action, index) => (
              <div key={index} className="bg-white/60 rounded-xl p-3 sm:p-4 border border-purple-200">
                <div className="flex items-center space-x-3 mb-2">
                  <span className="text-base sm:text-lg">{action.icon}</span>
                  <span className="font-medium text-gray-900 text-sm sm:text-base">{action.title}</span>
                </div>
                <p className="text-xs sm:text-sm text-gray-600">{action.description}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Progress Indicators */}
        {extractProgressMetrics(content).length > 0 && (
          <div className="bg-gradient-to-br from-indigo-50 to-blue-100 rounded-2xl p-4 sm:p-6 border border-indigo-200 shadow-lg">
            <div className="flex items-center space-x-3 mb-4">
              <div className="w-10 h-10 sm:w-12 sm:h-12 bg-gradient-to-br from-indigo-500 to-blue-600 rounded-xl flex items-center justify-center">
                <span className="text-white text-lg sm:text-xl">📊</span>
              </div>
              <h3 className="text-base sm:text-lg font-semibold text-gray-900">Performance Metrics</h3>
            </div>
            <div className="space-y-3 sm:space-y-4">
              {extractProgressMetrics(content).map((metric, index) => (
                <div key={index} className="space-y-2">
                  <div className="flex items-center justify-between text-xs sm:text-sm">
                    <span className="font-medium text-gray-700 truncate">{metric.label}</span>
                    <span className="text-indigo-600 font-semibold flex-shrink-0 ml-2">{metric.value}</span>
                  </div>
                  <div className="w-full bg-white/60 rounded-full h-2 sm:h-3 border border-indigo-200">
                    <div
                      className="bg-gradient-to-r from-indigo-500 to-blue-600 h-2 sm:h-3 rounded-full transition-all duration-500"
                      style={{ width: `${metric.percentage}%` }}
                    ></div>
                  </div>
                  <div className="text-xs text-gray-500">{metric.description}</div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    );
  };

  // Helper functions to extract and parse content
  const extractMetrics = (content: string) => {
    const metrics = [];
    const lines = content.split('\n');
    
    for (const line of lines) {
      if (line.includes('**') && line.includes(':')) {
        const match = line.match(/\*\*(.*?)\*\*:\s*(.*)/);
        if (match) {
          const label = match[1].trim();
          const value = match[2].trim();
          
          // Determine icon based on label
          let icon = '📊';
          if (label.toLowerCase().includes('revenue')) icon = '💰';
          else if (label.toLowerCase().includes('customer')) icon = '👤';
          else if (label.toLowerCase().includes('growth')) icon = '📈';
          else if (label.toLowerCase().includes('retention')) icon = '🔄';
          else if (label.toLowerCase().includes('margin')) icon = '💵';
          
          metrics.push({
            icon,
            label,
            value,
            description: `Current ${label.toLowerCase()}`,
            change: Math.random() > 0.5 ? Math.floor(Math.random() * 20) + 1 : null
          });
        }
      }
    }
    
    return metrics.slice(0, 3); // Return max 3 metrics
  };

  const extractPositiveIndicators = (content: string) => {
    const indicators = [];
    const lines = content.split('\n');
    
    for (const line of lines) {
      if (line.includes('✅') || line.includes('🟢') || line.includes('**Strong**') || line.includes('**Excellent**')) {
        const cleanLine = line.replace(/[✅🟢*]/g, '').trim();
        if (cleanLine.length > 10) {
          indicators.push(cleanLine);
        }
      }
    }
    
    return indicators.length > 0 ? indicators : ['Strong performance metrics', 'Above industry standards', 'Positive growth trends'];
  };

  const extractImprovementAreas = (content: string) => {
    const areas = [];
    const lines = content.split('\n');
    
    for (const line of lines) {
      if (line.includes('⚠️') || line.includes('🟡') || line.includes('**Needs attention**') || line.includes('**Watch**')) {
        const cleanLine = line.replace(/[⚠️🟡*]/g, '').trim();
        if (cleanLine.length > 10) {
          areas.push(cleanLine);
        }
      }
    }
    
    return areas.length > 0 ? areas : ['Optimize underperforming areas', 'Improve efficiency metrics', 'Address potential risks'];
  };

  const extractActionItems = (content: string) => {
    const actions = [];
    const lines = content.split('\n');
    
    for (const line of lines) {
      if (line.includes('📅') || line.includes('💰') || line.includes('📊') || line.includes('📈') || line.includes('🔄')) {
        const cleanLine = line.replace(/[📅💰📊📈🔄]/g, '').trim();
        if (cleanLine.length > 10) {
          const icon = line.match(/[📅💰📊📈🔄]/)?.[0] || '🎯';
          actions.push({
            icon,
            title: cleanLine.split(':')[0]?.trim() || 'Action Item',
            description: cleanLine.split(':')[1]?.trim() || cleanLine
          });
        }
      }
    }
    
    return actions.length > 0 ? actions : [
      { icon: '📈', title: 'Scale Success', description: 'Focus on high-performing areas' },
      { icon: '🔄', title: 'Optimize Process', description: 'Improve operational efficiency' },
      { icon: '🎯', title: 'Set Targets', description: 'Define clear performance goals' }
    ];
  };

  const extractProgressMetrics = (content: string) => {
    const metrics = [];
    const lines = content.split('\n');
    
    for (const line of lines) {
      if (line.includes('/10') || line.includes('%') || line.includes('score')) {
        const match = line.match(/(\d+(?:\.\d+)?)\/(\d+)/);
        if (match) {
          const value = parseFloat(match[1]);
          const max = parseFloat(match[2]);
          const percentage = (value / max) * 100;
          
          const labelMatch = line.match(/\*\*(.*?)\*\*/);
          const label = labelMatch ? labelMatch[1] : 'Metric';
          
          metrics.push({
            label,
            value: `${value}/${max}`,
            percentage,
            description: percentage >= 80 ? 'Excellent' : percentage >= 60 ? 'Good' : 'Needs improvement'
          });
        }
      }
    }
    
    return metrics;
  };

  // Helper functions for tooltips
  const getPositiveIndicatorExplanation = (indicator: string) => {
    if (indicator.toLowerCase().includes('strong performance')) {
      return 'Your business is exceeding expectations in key performance areas. This indicates effective strategies and strong execution.';
    } else if (indicator.toLowerCase().includes('above industry')) {
      return 'You\'re performing better than the average in your industry. This gives you a competitive advantage.';
    } else if (indicator.toLowerCase().includes('positive growth')) {
      return 'Your business is growing consistently, showing that your current strategies are working well.';
    } else if (indicator.toLowerCase().includes('excellent')) {
      return 'This metric is performing at the highest level, indicating exceptional business performance.';
    } else if (indicator.toLowerCase().includes('strong')) {
      return 'This area is performing well above average, showing solid business fundamentals.';
    } else {
      return 'This is a positive indicator that shows your business is performing well in this area.';
    }
  };

  const getImprovementAreaExplanation = (area: string) => {
    if (area.toLowerCase().includes('optimize')) {
      return 'This area has potential for improvement through better processes and efficiency gains.';
    } else if (area.toLowerCase().includes('improve')) {
      return 'This metric could be enhanced to achieve better business outcomes.';
    } else if (area.toLowerCase().includes('address')) {
      return 'This issue needs attention to prevent it from affecting overall performance.';
    } else if (area.toLowerCase().includes('risk')) {
      return 'This area poses potential risks that should be monitored and mitigated.';
    } else if (area.toLowerCase().includes('attention')) {
      return 'This area requires focus and resources to improve performance.';
    } else {
      return 'This is an area where improvements could lead to better business performance.';
    }
  };

  const getMetricExplanation = (label: string, value: string) => {
    switch (label.toLowerCase()) {
      case 'total revenue':
        return 'This is the total amount of money your business has earned from sales over a specific period. It\'s a key indicator of overall business health and growth.';
      case 'total customers':
        return 'This represents the number of unique individuals who have interacted with your business or made a purchase. It\'s a measure of your customer base size and engagement.';
      case 'repeat customer rate':
        return 'This is the percentage of your customers who return to make another purchase. A high repeat rate indicates customer loyalty and satisfaction.';
      case 'average clv':
        return 'Customer Lifetime Value (CLV) is the total revenue a business can expect from a single customer account over the duration of their relationship.';
      case 'turnover rate':
        return 'Inventory turnover rate measures how many times your inventory is sold and replaced over a given period. A high rate indicates efficient inventory management.';
      case 'stockout rate':
        return 'This is the percentage of products that are out of stock when a customer attempts to purchase them. A high rate can lead to lost sales.';
      case 'excess inventory':
        return 'Excess inventory refers to the amount of inventory that exceeds the optimal level. It can tie up capital and lead to storage costs.';
      case 'order processing time':
        return 'This is the average time it takes for an order to be processed from placement until shipment. Faster times improve customer satisfaction.';
      case 'fulfillment accuracy':
        return 'This is the percentage of orders that are shipped correctly without errors. High accuracy is essential for customer trust.';
      case 'return rate':
        return 'This is the percentage of products that are returned by customers. A high rate can indicate quality or satisfaction issues.';
      case 'mrr growth rate':
        return 'Monthly Recurring Revenue growth rate measures how much your recurring revenue increases month-over-month.';
      case 'churn rate':
        return 'Customer churn rate is the percentage of customers who cancel or stop using your service over a given period.';
      case 'average order value':
        return 'This is the average amount spent per order by your customers. It\'s a key indicator of customer spending habits.';
      case 'revenue growth rate':
        return 'This is the percentage increase in your total revenue from one period to the next. It\'s a measure of overall business growth.';
      case 'customer retention rate':
        return 'This is the percentage of customers who continue to use your service over a given period. High rates are crucial for long-term success.';
      case 'profit margin':
        return 'This is the percentage of revenue that remains after deducting costs. It\'s a measure of your business\'s financial efficiency.';
      case 'market share':
        return 'This is the percentage of the total market that your business occupies. It\'s a measure of your competitive position.';
      default:
        return 'This metric provides important business intelligence data. Higher values generally indicate better performance.';
    }
  };



  return (
    <div className="space-y-8">
      {/* Close All Tooltips Button */}
      {Object.keys(activeTooltips).length > 0 && (
        <motion.div
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          className="flex justify-center px-4 sm:px-0"
        >
          <button
            onClick={closeAllTooltips}
            className="bg-gray-800 hover:bg-gray-900 text-white px-4 py-2 rounded-full text-sm font-medium transition-colors duration-200 flex items-center space-x-2"
          >
            <span>✕</span>
            <span>Close All Tooltips</span>
          </button>
        </motion.div>
      )}
      
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center px-4 sm:px-0"
      >
        <div className="inline-flex items-center justify-center w-16 h-16 sm:w-20 sm:h-20 bg-gradient-to-r from-primary-500 to-accent-500 rounded-full mb-4 sm:mb-6">
          <SparklesIcon className="h-8 w-8 sm:h-10 sm:w-10 text-white" />
        </div>
        <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-gradient mb-4">
          AI-Powered Insights
        </h1>
        <p className="text-lg sm:text-xl text-secondary-600 max-w-3xl mx-auto px-4 sm:px-0">
          Ask intelligent questions about your business data and get AI-generated insights with actionable recommendations
        </p>
      </motion.div>

      {/* Industry Selection */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="bg-white rounded-3xl p-4 sm:p-6 lg:p-8 shadow-soft border border-secondary-200 mx-4 sm:mx-0"
      >
        <h2 className="text-2xl sm:text-3xl font-semibold text-secondary-900 mb-4 text-center sm:text-left">
          🏢 Industry Configuration
        </h2>
        <p className="text-base sm:text-lg text-secondary-600 mb-6 text-center sm:text-left">
          Select your industry for tailored insights and recommendations
        </p>

        <div className="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4">
          {['generic', 'retail', 'saas', 'marketplace'].map((ind) => (
            <button
              key={ind}
              onClick={() => setIndustry(ind)}
              className={`p-3 sm:p-4 lg:p-6 rounded-2xl border-2 transition-all duration-200 ${
                industry === ind
                  ? 'border-primary-500 bg-primary-50 shadow-medium'
                  : 'border-secondary-200 bg-white hover:border-primary-300 hover:bg-primary-50 hover:shadow-soft'
              }`}
            >
              <div className="text-2xl sm:text-3xl mb-2 sm:mb-3">{getIndustryIcon(ind)}</div>
              <div className="font-semibold text-secondary-900 capitalize text-sm sm:text-base lg:text-lg">{ind}</div>
              <div className="text-xs sm:text-sm text-secondary-600 mt-1 sm:mt-2">
                {getIndustryDescription(ind)}
              </div>
            </button>
          ))}
        </div>
      </motion.div>

      {/* Question Categories */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6 px-4 sm:px-0"
      >
        {questionCategories.map((category, index) => (
          <motion.div
            key={category.id}
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: index * 0.1 }}
            className="bg-gradient-to-br from-white to-blue-50 rounded-2xl p-4 sm:p-6 shadow-lg border border-blue-200 hover:shadow-2xl hover:from-blue-50 hover:to-indigo-100 transition-all duration-300 cursor-pointer group relative overflow-hidden"
            onClick={() => setSelectedCategory(category.id)}
          >
            {/* Background Pattern */}
            <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
              <div className="absolute top-0 right-0 w-16 h-16 sm:w-20 sm:h-20 bg-gradient-to-br from-blue-400 to-purple-600 rounded-full -translate-y-8 sm:-translate-y-10 translate-x-8 sm:translate-x-10 opacity-10"></div>
            </div>
            
            <div className="relative z-10">
              <div className="flex items-center space-x-3 mb-4">
                <div className="w-10 h-10 sm:w-12 sm:h-12 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-200">
                  <category.icon className="h-5 w-5 sm:h-6 sm:w-6 text-white" />
                </div>
                <h3 className="text-base sm:text-lg font-semibold text-gray-900 group-hover:text-blue-700 transition-colors duration-200 flex-1">{category.title}</h3>
              </div>

              <div className="space-y-2">
                {category.questions.slice(0, 3).map((question) => (
                  <div key={question.id} className="flex items-center space-x-2 text-xs sm:text-sm text-gray-600 group-hover:text-blue-600 transition-colors duration-200">
                    <span className="group-hover:scale-110 transition-transform duration-200 flex-shrink-0">{question.icon}</span>
                    <span className="line-clamp-2">{question.text}</span>
                  </div>
                ))}
              </div>

              <div className="mt-4 pt-4 border-t border-blue-200 group-hover:border-blue-300 transition-colors duration-200">
                <p className="text-xs text-gray-500 group-hover:text-blue-600 transition-colors duration-200">
                  {category.questions.length} questions available
                </p>
                <p className="text-xs text-blue-600 mt-1 font-medium opacity-0 group-hover:opacity-100 transition-all duration-300">
                  👆 Click to see all questions
                </p>
                
                {/* Hover Effect Line */}
                <div className="w-0 group-hover:w-full h-0.5 bg-gradient-to-r from-blue-500 to-purple-600 transition-all duration-300 rounded-full mt-2"></div>
              </div>
            </div>
          </motion.div>
        ))}
      </motion.div>

      {/* Selected Category Questions */}
      {selectedCategory && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white rounded-3xl p-4 sm:p-6 lg:p-8 shadow-soft border border-secondary-200 mx-4 sm:mx-0"
        >
          <div className="flex items-center justify-between mb-6">
            <div>
              <h2 className="text-2xl sm:text-3xl font-semibold text-secondary-900">
                {questionCategories.find(c => c.id === selectedCategory)?.title} Questions
              </h2>
              <p className="text-base sm:text-lg text-secondary-600 mt-2">
                Select a question to get AI-powered insights
              </p>
            </div>
            <button
              onClick={() => setSelectedCategory(null)}
              className="p-2 sm:p-3 bg-secondary-100 hover:bg-secondary-200 rounded-xl transition-colors duration-200"
            >
              <span className="text-2xl">✕</span>
            </button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 sm:gap-4">
            {questionCategories
              .find(c => c.id === selectedCategory)
              ?.questions.map((question, index) => (
                <motion.button
                  key={question.id}
                  initial={{ opacity: 0, scale: 0.95 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ delay: index * 0.05 }}
                  whileHover={{ scale: 1.02, y: -2 }}
                  whileTap={{ scale: 0.98 }}
                  onClick={() => handleQuestionClick(question.id)}
                  className="text-left p-4 sm:p-6 bg-gradient-to-br from-white to-blue-50 border border-blue-200 rounded-2xl hover:from-blue-50 hover:to-indigo-100 transition-all duration-300 hover:shadow-xl hover:border-blue-300 group relative overflow-hidden"
                >
                  {/* Background Pattern */}
                  <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <div className="absolute top-0 right-0 w-16 h-16 bg-gradient-to-br from-blue-400 to-purple-600 rounded-full -translate-y-8 translate-x-8 opacity-20"></div>
                  </div>
                  
                  <div className="relative z-10">
                    <div className="flex items-center space-x-3 mb-3">
                      <span className="text-2xl sm:text-3xl group-hover:scale-110 transition-transform duration-200">{question.icon}</span>
                      <span className="font-semibold text-gray-900 text-sm sm:text-lg group-hover:text-blue-700 transition-colors duration-200 flex-1">{question.text}</span>
                    </div>
                    
                    {/* Hover Effect Line */}
                    <div className="w-0 group-hover:w-full h-0.5 bg-gradient-to-r from-blue-500 to-purple-600 transition-all duration-300 rounded-full"></div>
                    
                    {/* Action Indicator */}
                    <div className="mt-4 flex items-center justify-between">
                      <div className="text-xs sm:text-sm text-blue-600 font-medium opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                        Click to see AI insight →
                      </div>
                      <div className="w-6 h-6 sm:w-8 sm:h-8 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all duration-300">
                        <SparklesIcon className="h-3 w-3 sm:h-4 sm:w-4 text-white" />
                      </div>
                    </div>
                  </div>
                </motion.button>
              ))}
          </div>
        </motion.div>
      )}

      {/* Selected Question Insight */}
      {selectedQuestion && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-gradient-to-br from-white via-blue-50 to-indigo-50 rounded-3xl p-4 sm:p-6 lg:p-8 shadow-2xl border border-blue-200 relative overflow-hidden mx-4 sm:mx-0"
        >
          {/* Background Pattern */}
          <div className="absolute inset-0 opacity-5">
            <div className="absolute top-0 right-0 w-16 h-16 sm:w-32 sm:h-32 bg-gradient-to-br from-blue-400 to-purple-600 rounded-full -translate-y-8 sm:-translate-y-16 translate-x-8 sm:translate-x-16"></div>
            <div className="absolute bottom-0 left-0 w-12 h-12 sm:w-24 sm:h-24 bg-gradient-to-br from-green-400 to-blue-600 rounded-full translate-y-6 sm:translate-y-12 -translate-x-6 sm:-translate-x-12"></div>
          </div>

          {/* Header with Enhanced Styling */}
          <div className="relative z-10 mb-6 sm:mb-8">
            <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-6 space-y-4 sm:space-y-0">
              <div className="flex items-center space-x-3 sm:space-x-4">
                <div className="w-12 h-12 sm:w-16 sm:h-16 bg-gradient-to-br from-blue-500 to-purple-600 rounded-2xl flex items-center justify-center shadow-lg">
                  <SparklesIcon className="h-6 w-6 sm:h-8 sm:w-8 text-white" />
                </div>
                <div>
                  <h2 className="text-2xl sm:text-3xl lg:text-4xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                    {getInsight(selectedQuestion).title}
                  </h2>
                  <p className="text-sm sm:text-base lg:text-lg text-blue-600 font-medium">
                    AI-Powered Business Intelligence
                  </p>
                </div>
              </div>
              
              <div className="flex items-center space-x-3 sm:space-x-4">
                <div className="bg-gradient-to-r from-green-400 to-blue-500 text-white px-3 sm:px-4 py-2 rounded-full font-semibold text-xs sm:text-sm shadow-lg">
                  <div className="flex items-center space-x-2">
                    <div className="w-2 h-2 bg-white rounded-full animate-pulse"></div>
                    <span>{getInsight(selectedQuestion).confidence}% Confidence</span>
                  </div>
                </div>
                <button
                  onClick={() => setSelectedQuestion(null)}
                  className="w-10 h-10 sm:w-12 sm:h-12 bg-white hover:bg-gray-50 text-gray-500 hover:text-gray-700 rounded-full flex items-center justify-center shadow-lg transition-all duration-200 hover:scale-110"
                >
                  <span className="text-lg sm:text-2xl">✕</span>
                </button>
              </div>
            </div>
          </div>

          {/* Enhanced Content Card */}
          <div className="relative z-10">
            <div className="bg-white/80 backdrop-blur-sm rounded-3xl p-4 sm:p-6 lg:p-8 border border-white/50 shadow-xl">
              {/* Render content as visual cards instead of plain text */}
              {renderVisualAnswer(selectedQuestion)}
            </div>
          </div>

          {/* Enhanced Footer */}
          <div className="relative z-10 mt-6 sm:mt-8">
            <div className="bg-gradient-to-r from-blue-50 to-purple-50 rounded-2xl p-4 sm:p-6 border border-blue-100">
              <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between space-y-4 lg:space-y-0">
                <div className="flex flex-col sm:flex-row sm:items-center space-y-2 sm:space-y-0 sm:space-x-4">
                  <div className="flex items-center space-x-2 text-blue-600">
                    <ChatBubbleLeftRightIcon className="h-5 w-5 sm:h-6 sm:w-6" />
                    <span className="font-medium text-sm sm:text-base">AI-generated insight</span>
                  </div>
                  <div className="flex items-center space-x-2 text-purple-600">
                    <div className="w-2 h-2 bg-purple-500 rounded-full"></div>
                    <span className="text-xs sm:text-sm font-medium">Real-time analysis</span>
                  </div>
                </div>
                
                <div className="flex flex-col sm:flex-row space-y-2 sm:space-y-0 sm:space-x-3">
                  <button className="bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white font-semibold py-2 sm:py-3 px-4 sm:px-6 rounded-xl transition-all duration-200 hover:scale-105 shadow-lg flex items-center justify-center space-x-2 text-sm sm:text-base">
                    <span>💡</span>
                    <span>Ask Follow-up Question</span>
                  </button>
                  <button className="bg-white hover:bg-gray-50 text-blue-600 font-semibold py-2 sm:py-3 px-4 sm:px-6 rounded-xl transition-all duration-200 hover:scale-105 shadow-lg border border-blue-200 flex items-center justify-center space-x-2 text-sm sm:text-base">
                    <span>📊</span>
                    <span>View Analytics</span>
                  </button>
                </div>
              </div>
            </div>
          </div>

          {/* Floating Action Cards */}
          <div className="absolute top-4 sm:top-8 right-4 sm:right-8 space-y-2 sm:space-y-3">
            <motion.div
              whileHover={{ scale: 1.1 }}
              className="w-10 h-10 sm:w-12 sm:h-12 bg-gradient-to-br from-green-400 to-blue-500 rounded-full flex items-center justify-center shadow-lg cursor-pointer"
            >
              <span className="text-white text-base sm:text-lg">📈</span>
            </motion.div>
            <motion.div
              whileHover={{ scale: 1.1 }}
              className="w-10 h-10 sm:w-12 sm:h-12 bg-gradient-to-br from-purple-400 to-pink-500 rounded-full flex items-center justify-center shadow-lg cursor-pointer"
            >
              <span className="text-white text-base sm:text-lg">💡</span>
            </motion.div>
          </div>
        </motion.div>
      )}

      {/* AI Features */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className="bg-gradient-to-r from-primary-50 to-accent-50 rounded-3xl p-4 sm:p-6 lg:p-8 border border-primary-100 mx-4 sm:mx-0"
      >
        <h2 className="text-2xl sm:text-3xl font-semibold text-secondary-900 mb-6 sm:mb-8 text-center">
          🤖 Powered by Advanced AI
        </h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
          <div className="text-center">
            <div className="w-16 h-16 sm:w-20 sm:h-20 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4 sm:mb-6">
              <LightBulbIcon className="h-8 w-8 sm:h-10 sm:w-10 text-primary-600" />
            </div>
            <h3 className="text-lg sm:text-xl font-semibold text-secondary-900 mb-2 sm:mb-3">Smart Analysis</h3>
            <p className="text-secondary-600 text-sm sm:text-base">
              AI automatically analyzes your data patterns and identifies key insights
            </p>
          </div>

          <div className="text-center">
            <div className="w-16 h-16 sm:w-20 sm:h-20 bg-accent-100 rounded-full flex items-center justify-center mx-auto mb-4 sm:mb-6">
              <ChatBubbleLeftRightIcon className="h-8 w-8 sm:h-10 sm:w-10 text-accent-600" />
            </div>
            <h3 className="text-lg sm:text-xl font-semibold text-secondary-900 mb-2 sm:mb-3">Natural Questions</h3>
            <p className="text-secondary-600 text-sm sm:text-base">
              Ask questions in plain English and get intelligent, contextual answers
            </p>
          </div>

          <div className="text-center">
            <div className="w-16 h-16 sm:w-20 sm:h-20 bg-success-100 rounded-full flex items-center justify-center mx-auto mb-4 sm:mb-6">
              <UserGroupIcon className="h-8 w-8 sm:h-10 sm:w-10 text-success-600" />
            </div>
            <h3 className="text-lg sm:text-xl font-semibold text-secondary-900 mb-2 sm:mb-3">Actionable Insights</h3>
            <p className="text-secondary-600 text-sm sm:text-base">
              Get specific recommendations and next steps based on your data
            </p>
          </div>
        </div>
      </motion.div>
    </div>
  )
}
