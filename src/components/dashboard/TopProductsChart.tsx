import { motion } from 'framer-motion'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts'
import { formatCurrency } from '@/lib/utils'

const data = [
  { name: 'Product A', revenue: 420000, percentage: 28.5 },
  { name: 'Product B', revenue: 380000, percentage: 25.8 },
  { name: 'Product C', revenue: 320000, percentage: 21.7 },
  { name: 'Product D', revenue: 280000, percentage: 19.0 },
  { name: 'Product E', revenue: 75000, percentage: 5.0 },
]

const colors = ['#3b82f6', '#8b5cf6', '#06b6d4', '#10b981', '#f59e0b']

const CustomTooltip = ({ active, payload, label }: any) => {
  if (active && payload && payload.length) {
    return (
      <div className="bg-white p-4 rounded-xl shadow-large border border-secondary-200">
        <p className="font-semibold text-secondary-900">{label}</p>
        <p className="text-primary-600">
          Revenue: {formatCurrency(payload[0].value)}
        </p>
        <p className="text-accent-600">
          Market Share: {payload[0].payload.percentage}%
        </p>
      </div>
    )
  }
  return null
}

export default function TopProductsChart() {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.5, delay: 0.1 }}
      className="chart-container"
    >
      <div className="flex items-center justify-between mb-6">
        <div>
          <h3 className="text-lg font-semibold text-secondary-900">Top Products</h3>
          <p className="text-sm text-secondary-600">Revenue performance by product</p>
        </div>
        <div className="text-right">
          <p className="text-2xl font-bold text-primary-600">
            {formatCurrency(data.reduce((sum, item) => sum + item.revenue, 0))}
          </p>
          <p className="text-sm text-secondary-600">Total Revenue</p>
        </div>
      </div>

      <div className="h-80">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart
            data={data}
            layout="horizontal"
            margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
            <XAxis 
              type="number"
              stroke="#64748b"
              fontSize={12}
              tickLine={false}
              axisLine={false}
              tickFormatter={(value) => formatCurrency(value).replace('$', '')}
            />
            <YAxis 
              type="category"
              dataKey="name"
              stroke="#64748b"
              fontSize={12}
              tickLine={false}
              axisLine={false}
              width={80}
            />
            <Tooltip content={<CustomTooltip />} />
            <Bar dataKey="revenue" radius={[0, 4, 4, 0]}>
              {data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={colors[index % colors.length]} />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div className="mt-6 space-y-3">
        {data.map((item, index) => (
          <div key={item.name} className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div 
                className="w-3 h-3 rounded-full"
                style={{ backgroundColor: colors[index % colors.length] }}
              ></div>
              <span className="text-sm font-medium text-secondary-900">{item.name}</span>
            </div>
            <div className="text-right">
              <p className="text-sm font-semibold text-secondary-900">
                {formatCurrency(item.revenue)}
              </p>
              <p className="text-xs text-secondary-500">{item.percentage}%</p>
            </div>
          </div>
        ))}
      </div>
    </motion.div>
  )
}
