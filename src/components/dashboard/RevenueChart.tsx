import { motion } from 'framer-motion'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Area, AreaChart } from 'recharts'
import { formatCurrency } from '@/lib/utils'

const data = [
  { month: 'Jan', revenue: 240000, orders: 1200 },
  { month: 'Feb', revenue: 280000, orders: 1400 },
  { month: 'Mar', revenue: 320000, orders: 1600 },
  { month: 'Apr', revenue: 380000, orders: 1900 },
  { month: 'May', revenue: 420000, orders: 2100 },
  { month: 'Jun', revenue: 480000, orders: 2400 },
  { month: 'Jul', revenue: 520000, orders: 2600 },
  { month: 'Aug', revenue: 580000, orders: 2900 },
  { month: 'Sep', revenue: 640000, orders: 3200 },
  { month: 'Oct', revenue: 680000, orders: 3400 },
  { month: 'Nov', revenue: 720000, orders: 3600 },
  { month: 'Dec', revenue: 780000, orders: 3900 },
]

const CustomTooltip = ({ active, payload, label }: any) => {
  if (active && payload && payload.length) {
    return (
      <div className="bg-white p-4 rounded-xl shadow-large border border-secondary-200">
        <p className="font-semibold text-secondary-900">{label}</p>
        <p className="text-primary-600">
          Revenue: {formatCurrency(payload[0].value)}
        </p>
        <p className="text-accent-600">
          Orders: {payload[1].value.toLocaleString()}
        </p>
      </div>
    )
  }
  return null
}

export default function RevenueChart() {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.5 }}
      className="chart-container"
    >
      <div className="flex items-center justify-between mb-6">
        <div>
          <h3 className="text-lg font-semibold text-secondary-900">Revenue Trends</h3>
          <p className="text-sm text-secondary-600">Monthly revenue and order performance</p>
        </div>
        <div className="flex items-center space-x-4">
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 rounded-full bg-primary-500"></div>
            <span className="text-sm text-secondary-600">Revenue</span>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 rounded-full bg-accent-500"></div>
            <span className="text-sm text-secondary-600">Orders</span>
          </div>
        </div>
      </div>

      <div className="h-80">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
            <defs>
              <linearGradient id="revenueGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3}/>
                <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
              </linearGradient>
              <linearGradient id="ordersGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#f59e0b" stopOpacity={0.3}/>
                <stop offset="95%" stopColor="#f59e0b" stopOpacity={0}/>
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
            <XAxis 
              dataKey="month" 
              stroke="#64748b"
              fontSize={12}
              tickLine={false}
              axisLine={false}
            />
            <YAxis 
              stroke="#64748b"
              fontSize={12}
              tickLine={false}
              axisLine={false}
              tickFormatter={(value) => formatCurrency(value).replace('$', '')}
            />
            <Tooltip content={<CustomTooltip />} />
            <Area
              type="monotone"
              dataKey="revenue"
              stroke="#3b82f6"
              strokeWidth={3}
              fill="url(#revenueGradient)"
              dot={{ fill: '#3b82f6', strokeWidth: 2, r: 4 }}
              activeDot={{ r: 6, stroke: '#3b82f6', strokeWidth: 2 }}
            />
            <Line
              type="monotone"
              dataKey="orders"
              stroke="#f59e0b"
              strokeWidth={2}
              dot={{ fill: '#f59e0b', strokeWidth: 2, r: 3 }}
              activeDot={{ r: 5, stroke: '#f59e0b', strokeWidth: 2 }}
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>

      <div className="mt-6 grid grid-cols-3 gap-4 text-center">
        <div>
          <p className="text-2xl font-bold text-primary-600">
            {formatCurrency(data[data.length - 1].revenue)}
          </p>
          <p className="text-sm text-secondary-600">Current Month</p>
        </div>
        <div>
          <p className="text-2xl font-bold text-accent-600">
            {data[data.length - 1].orders.toLocaleString()}
          </p>
          <p className="text-sm text-secondary-600">Current Orders</p>
        </div>
        <div>
          <p className="text-2xl font-bold text-success-600">
            +{((data[data.length - 1].revenue / data[data.length - 2].revenue - 1) * 100).toFixed(1)}%
          </p>
          <p className="text-sm text-secondary-600">Growth Rate</p>
        </div>
      </div>
    </motion.div>
  )
}
