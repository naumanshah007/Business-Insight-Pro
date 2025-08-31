import { motion } from 'framer-motion'
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from 'recharts'

const data = [
  { name: 'New Customers', value: 45, color: '#3b82f6' },
  { name: 'Returning Customers', value: 35, color: '#10b981' },
  { name: 'Loyal Customers', value: 20, color: '#8b5cf6' },
]

const customerMetrics = [
  { label: 'Total Customers', value: '12,847', change: '+15.3%', trend: 'up' },
  { label: 'New This Month', value: '1,234', change: '+8.7%', trend: 'up' },
  { label: 'Repeat Rate', value: '35.2%', change: '+2.1%', trend: 'up' },
  { label: 'Churn Rate', value: '4.8%', change: '-0.5%', trend: 'down' },
]

const CustomTooltip = ({ active, payload }: any) => {
  if (active && payload && payload.length) {
    return (
      <div className="bg-white p-4 rounded-xl shadow-large border border-secondary-200">
        <p className="font-semibold text-secondary-900">{payload[0].name}</p>
        <p className="text-primary-600">
          {payload[0].value}% of total customers
        </p>
      </div>
    )
  }
  return null
}

export default function CustomerMetricsChart() {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.5, delay: 0.2 }}
      className="chart-container"
    >
      <div className="flex items-center justify-between mb-6">
        <div>
          <h3 className="text-lg font-semibold text-secondary-900">Customer Metrics</h3>
          <p className="text-sm text-secondary-600">Customer segmentation and performance</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Pie Chart */}
        <div className="h-80">
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={data}
                cx="50%"
                cy="50%"
                innerRadius={60}
                outerRadius={120}
                paddingAngle={5}
                dataKey="value"
              >
                {data.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Pie>
              <Tooltip content={<CustomTooltip />} />
              <Legend />
            </PieChart>
          </ResponsiveContainer>
        </div>

        {/* Metrics Grid */}
        <div className="space-y-4">
          {customerMetrics.map((metric, index) => (
            <motion.div
              key={metric.label}
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 }}
              className="bg-secondary-50 rounded-xl p-4 border border-secondary-200"
            >
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-secondary-600">{metric.label}</p>
                  <p className="text-2xl font-bold text-secondary-900">{metric.value}</p>
                </div>
                <div className="text-right">
                  <p className={`text-sm font-medium ${
                    metric.trend === 'up' ? 'text-success-600' : 'text-error-600'
                  }`}>
                    {metric.change}
                  </p>
                  <p className="text-xs text-secondary-500">vs last month</p>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>

      {/* Customer Insights */}
      <div className="mt-8 p-6 bg-gradient-to-r from-primary-50 to-accent-50 rounded-xl border border-primary-100">
        <h4 className="text-lg font-semibold text-secondary-900 mb-4">Customer Insights</h4>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="text-center">
            <div className="text-3xl font-bold text-primary-600 mb-2">🎯</div>
            <p className="text-sm text-secondary-700">
              <strong>High Retention:</strong> 35% of customers make repeat purchases
            </p>
          </div>
          <div className="text-center">
            <div className="text-3xl font-bold text-accent-600 mb-2">📈</div>
            <p className="text-sm text-secondary-700">
              <strong>Growing Base:</strong> 15% month-over-month customer growth
            </p>
          </div>
          <div className="text-center">
            <div className="text-3xl font-bold text-success-600 mb-2">💎</div>
            <p className="text-sm text-secondary-700">
              <strong>Low Churn:</strong> Only 4.8% customer attrition rate
            </p>
          </div>
        </div>
      </div>
    </motion.div>
  )
}
