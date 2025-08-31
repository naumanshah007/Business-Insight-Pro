import { motion } from 'framer-motion'
import { useState, useEffect } from 'react'
import { 
  ChartBarIcon, 
  UsersIcon, 
  CurrencyDollarIcon,
  ShoppingCartIcon,
  CalendarIcon,
  ArrowUpIcon,
  ArrowDownIcon
} from '@heroicons/react/24/outline'

// Real data for the analytics dashboard with better variation
const chartData = {
  revenue: [
    { month: 'Jan', value: 125000, change: 8.2 },
    { month: 'Feb', value: 138000, change: 10.4 },
    { month: 'Mar', value: 145000, change: 5.1 },
    { month: 'Apr', value: 158000, change: 9.0 },
    { month: 'May', value: 162000, change: 2.5 },
    { month: 'Jun', value: 175000, change: 8.0 },
    { month: 'Jul', value: 189000, change: 8.0 },
    { month: 'Aug', value: 195000, change: 3.2 },
    { month: 'Sep', value: 208000, change: 6.7 },
    { month: 'Oct', value: 215000, change: 3.4 },
    { month: 'Nov', value: 228000, change: 6.0 },
    { month: 'Dec', value: 245000, change: 7.5 }
  ],
  customers: [
    { month: 'Jan', value: 8500, change: 12.5 },
    { month: 'Feb', value: 9200, change: 8.2 },
    { month: 'Mar', value: 9800, change: 6.5 },
    { month: 'Apr', value: 10500, change: 7.1 },
    { month: 'May', value: 11200, change: 6.7 },
    { month: 'Jun', value: 11800, change: 5.4 },
    { month: 'Jul', value: 12400, change: 5.1 },
    { month: 'Aug', value: 12900, change: 4.0 },
    { month: 'Sep', value: 13400, change: 3.9 },
    { month: 'Oct', value: 13900, change: 3.7 },
    { month: 'Nov', value: 14400, change: 3.6 },
    { month: 'Dec', value: 14800, change: 2.8 }
  ]
}

// Daily data for short time periods
const dailyData = {
  revenue: [
    { month: 'Mon', value: 4200, change: 5.2 },
    { month: 'Tue', value: 4500, change: 7.1 },
    { month: 'Wed', value: 4800, change: 6.7 },
    { month: 'Thu', value: 5200, change: 8.3 },
    { month: 'Fri', value: 5800, change: 11.5 },
    { month: 'Sat', value: 6200, change: 6.9 },
    { month: 'Sun', value: 5900, change: -4.8 }
  ],
  customers: [
    { month: 'Mon', value: 280, change: 4.5 },
    { month: 'Tue', value: 295, change: 5.4 },
    { month: 'Wed', value: 310, change: 5.1 },
    { month: 'Thu', value: 325, change: 4.8 },
    { month: 'Fri', value: 350, change: 7.7 },
    { month: 'Sat', value: 380, change: 8.6 },
    { month: 'Sun', value: 360, change: -5.3 }
  ]
}

// Weekly data for 30 days
const weeklyData = {
  revenue: [
    { month: 'Week 1', value: 28500, change: 6.8 },
    { month: 'Week 2', value: 29800, change: 4.6 },
    { month: 'Week 3', value: 31200, change: 4.7 },
    { month: 'Week 4', value: 32500, change: 4.2 }
  ],
  customers: [
    { month: 'Week 1', value: 1850, change: 5.2 },
    { month: 'Week 2', value: 1920, change: 3.8 },
    { month: 'Week 3', value: 1980, change: 3.1 },
    { month: 'Week 4', value: 2050, change: 3.5 }
  ]
}

// Monthly data for 90 days
const quarterlyData = {
  revenue: [
    { month: 'Oct', value: 215000, change: 3.4 },
    { month: 'Nov', value: 228000, change: 6.0 },
    { month: 'Dec', value: 245000, change: 7.5 }
  ],
  customers: [
    { month: 'Oct', value: 13900, change: 3.7 },
    { month: 'Nov', value: 14400, change: 3.6 },
    { month: 'Dec', value: 14800, change: 2.8 }
  ]
}

// Extended data for longer time periods
const extendedData = {
  revenue: [
    ...chartData.revenue,
    { month: 'Jan 2023', value: 98000, change: 6.8 },
    { month: 'Feb 2023', value: 105000, change: 7.1 },
    { month: 'Mar 2023', value: 112000, change: 6.7 },
    { month: 'Apr 2023', value: 118000, change: 5.4 },
    { month: 'May 2023', value: 125000, change: 5.9 },
    { month: 'Jun 2023', value: 132000, change: 5.6 },
    { month: 'Jul 2023', value: 138000, change: 4.5 },
    { month: 'Aug 2023', value: 145000, change: 5.1 },
    { month: 'Sep 2023', value: 152000, change: 4.8 },
    { month: 'Oct 2023', value: 158000, change: 3.9 },
    { month: 'Nov 2023', value: 165000, change: 4.4 },
    { month: 'Dec 2023', value: 172000, change: 4.2 }
  ],
  customers: [
    ...chartData.customers,
    { month: 'Jan 2023', value: 6800, change: 8.5 },
    { month: 'Feb 2023', value: 7200, change: 5.9 },
    { month: 'Mar 2023', value: 7600, change: 5.6 },
    { month: 'Apr 2023', value: 8000, change: 5.3 },
    { month: 'May 2023', value: 8400, change: 5.0 },
    { month: 'Jun 2023', value: 8800, change: 4.8 },
    { month: 'Jul 2023', value: 9200, change: 4.5 },
    { month: 'Aug 2023', value: 9600, change: 4.3 },
    { month: 'Sep 2023', value: 10000, change: 4.2 },
    { month: 'Oct 2023', value: 10400, change: 4.0 },
    { month: 'Nov 2023', value: 10800, change: 3.8 },
    { month: 'Dec 2023', value: 11200, change: 3.7 }
  ]
}

export default function Analytics() {
  const [selectedTimeRange, setSelectedTimeRange] = useState('12m')
  const [currentPage, setCurrentPage] = useState(0)
  const [isLoading, setIsLoading] = useState(false)

  useEffect(() => {
    setIsLoading(true)
    setTimeout(() => setIsLoading(false), 1000)
  }, [])

  // Reset to first page when time range changes
  useEffect(() => {
    setCurrentPage(0)
  }, [selectedTimeRange])

  // Get data based on selected time range with pagination
  const getDataForTimeRange = (timeRange: string, page: number = 0) => {
    const monthsPerPage = 12
    let allData
    
    switch (timeRange) {
      case '7d':
        return {
          revenue: dailyData.revenue,
          customers: dailyData.customers
        }
      case '30d':
        return {
          revenue: weeklyData.revenue,
          customers: weeklyData.customers
        }
      case '90d':
        return {
          revenue: quarterlyData.revenue,
          customers: quarterlyData.customers
        }
      case '12m':
        allData = chartData
        break
      case '24m':
        allData = extendedData
        break
      case 'all':
        allData = extendedData
        break
      default:
        allData = chartData
    }
    
    // Apply pagination only for monthly data (12m, 24m, all)
    if (['12m', '24m', 'all'].includes(timeRange)) {
      const startIndex = page * monthsPerPage
      const endIndex = startIndex + monthsPerPage
      
      return {
        revenue: allData.revenue.slice(startIndex, endIndex).map((item, index) => ({
          ...item,
          month: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][index]
        })),
        customers: allData.customers.slice(startIndex, endIndex).map((item, index) => ({
          ...item,
          month: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][index]
        }))
      }
    }
    
    // For daily/weekly/quarterly data, return as is
    return allData
  }

  const currentData = getDataForTimeRange(selectedTimeRange, currentPage)
  
  // Calculate total pages for pagination
  const getTotalPages = (timeRange: string) => {
    switch (timeRange) {
      case '12m':
        return 1 // Only 12 months
      case '24m':
        return 2 // 24 months = 2 pages
      case 'all':
        return Math.ceil(extendedData.revenue.length / 12) // Calculate based on total data
      default:
        return 1
    }
  }
  
  const totalPages = getTotalPages(selectedTimeRange)

  // Debug: Log the current data for the selected time range
  useEffect(() => {
    console.log('Selected time range:', selectedTimeRange)
    console.log('Current data loaded:', currentData)
    console.log('Revenue data points:', currentData.revenue.length)
    console.log('Customer data points:', currentData.customers.length)
    console.log('Revenue months:', currentData.revenue.map(item => item.month))
    console.log('Customer months:', currentData.customers.map(item => item.month))
  }, [selectedTimeRange, currentData])

  // Debug: Log the chart data
  useEffect(() => {
    console.log('Chart data loaded:', chartData)
    console.log('Revenue data:', chartData.revenue)
    console.log('Customer data:', chartData.customers)
  }, [])

  const getCurrentMetrics = () => {
    const currentRevenue = currentData.revenue[currentData.revenue.length - 1]
    const previousRevenue = currentData.revenue[currentData.revenue.length - 2]
    const revenueChange = ((currentRevenue.value - previousRevenue.value) / previousRevenue.value) * 100
    
    return {
      revenue: currentRevenue.value,
      revenueChange: revenueChange,
      customers: currentData.customers[currentData.customers.length - 1].value,
      customerChange: currentData.customers[currentData.customers.length - 1].change,
      orders: Math.round(currentRevenue.value / 99.85), // Calculate orders based on average order value
      orderChange: 8.2
    }
  }

  const metrics = getCurrentMetrics()



  const renderLineChart = (data: any[], title: string) => {
    const maxValue = Math.max(...data.map(d => d.value))
    const minValue = Math.min(...data.map(d => d.value))
    const range = maxValue - minValue

    console.log(`Rendering line chart: ${title}`, { 
      data, 
      maxValue, 
      minValue, 
      range,
      dataLength: data.length,
      samplePoints: data.map((item, index) => ({
        month: item.month,
        value: item.value,
        x: (index / (data.length - 1)) * 100,
        y: 100 - ((item.value - minValue) / range) * 80
      }))
    })

    // Intelligent tooltip positioning functions
    const getTooltipPosition = (index: number, totalPoints: number) => {
      const x = (index / (totalPoints - 1)) * 100
      
      // More aggressive positioning to prevent cutoff
      if (x < 15) return 'bottom'     // Very left - show below
      if (x > 85) return 'top'        // Very right - show above
      if (x < 30) return 'right'      // Left side - show to the right
      if (x > 70) return 'left'       // Right side - show to the left
      return 'bottom'                  // Middle - default to below
    }

    const getTooltipClasses = (position: string) => {
      switch (position) {
        case 'top':
          return 'bottom-full mb-2'
        case 'bottom':
          return 'top-full mt-2'
        case 'left':
          return 'right-full mr-2'
        case 'right':
          return 'left-full ml-2'
        default:
          return 'bottom-full mb-2'
      }
    }

    const getTooltipArrowClasses = (position: string) => {
      switch (position) {
        case 'top':
          return 'absolute bottom-full left-1/2 transform -translate-x-1/2 w-0 h-0 border-l-3 border-r-3 border-t-3 border-transparent border-t-secondary-800'
        case 'bottom':
          return 'absolute top-full left-1/2 transform -translate-x-1/2 w-0 h-0 border-l-3 border-r-3 border-b-3 border-transparent border-b-secondary-800'
        case 'left':
          return 'absolute right-full top-1/2 transform -translate-y-1/2 w-0 h-0 border-t-3 border-b-3 border-l-3 border-transparent border-l-secondary-800'
        case 'right':
          return 'absolute left-full top-1/2 transform -translate-y-1/2 w-0 h-0 border-t-3 border-b-3 border-r-3 border-transparent border-r-secondary-800'
        default:
          return 'absolute bottom-full left-1/2 transform -translate-x-1/2 w-0 h-0 border-l-3 border-r-3 border-t-3 border-transparent border-t-secondary-800'
      }
    }

    return (
      <div className="bg-white rounded-2xl p-8 shadow-soft border border-secondary-200">
        <div className="flex items-center justify-between mb-6">
          <h3 className="text-2xl font-bold text-secondary-900 flex items-center gap-3">
            {title}
            <div className="w-3 h-3 bg-gradient-to-r from-primary-500 to-accent-500 rounded-full"></div>
          </h3>
          <div className="text-right">
            <div className="text-3xl font-bold text-primary-600">
              {title.includes('Revenue') ? `$${(maxValue / 1000).toFixed(0)}k` : maxValue.toLocaleString()}
            </div>
            <div className="text-sm text-secondary-500">Peak Value</div>
          </div>
        </div>
        
        <div className={`h-96 bg-gradient-to-b from-gray-50 to-white p-8 rounded-xl border border-gray-100 relative overflow-visible`}>

          {/* Grid lines */}
          <div className="absolute inset-0 grid grid-cols-5 grid-rows-4 opacity-20">
            {[...Array(5)].map((_, i) => (
              <div key={i} className="border-r border-gray-300"></div>
            ))}
            {[...Array(4)].map((_, i) => (
              <div key={i} className="border-b border-gray-300"></div>
            ))}
          </div>
          
          {/* Y-axis labels */}
          <div className="absolute left-2 top-0 bottom-0 flex flex-col justify-between text-xs text-gray-500 font-medium">
            {[...Array(5)].map((_, i) => {
              const value = maxValue - (i * range / 4)
              return (
                <div key={i} className="transform -translate-y-1">
                  {title.includes('Revenue') ? `$${(value / 1000).toFixed(0)}k` : Math.round(value).toLocaleString()}
                </div>
              )
            })}
          </div>
          
          {/* Line chart - Fixed container */}
          <div className="relative h-full w-full">
            <svg className="w-full h-full" viewBox="0 0 100 100" preserveAspectRatio="none">
              {/* Line path */}
              <path
                d={data.map((item, index) => {
                  const x = (index / (data.length - 1)) * 100
                  const y = 100 - ((item.value - minValue) / range) * 80
                  return `${index === 0 ? 'M' : 'L'} ${x} ${y}`
                }).join(' ')}
                stroke={title.includes('Revenue') ? 'url(#revenueGradient)' : 'url(#customerGradient)'}
                strokeWidth="1"
                fill="none"
                strokeLinecap="round"
                strokeLinejoin="round"
                className="drop-shadow-sm"
              />
              
              {/* Area fill */}
              <path
                d={`M 0 100 ${data.map((item, index) => {
                  const x = (index / (data.length - 1)) * 100
                  const y = 100 - ((item.value - minValue) / range) * 80
                  return `L ${x} ${y}`
                }).join(' ')} L 100 100 Z`}
                fill={title.includes('Revenue') ? 'url(#revenueAreaGradient)' : 'url(#customerAreaGradient)'}
                opacity="0.05"
              />
              
              {/* Data points */}
              {data.map((item, index) => {
                const x = (index / (data.length - 1)) * 100
                const y = 100 - ((item.value - minValue) / range) * 80
                return (
                  <circle
                    key={index}
                    cx={x}
                    cy={y}
                    r="1"
                    fill="white"
                    stroke={title.includes('Revenue') ? '#8b5cf6' : '#10b981'}
                    strokeWidth="0.5"
                    className="drop-shadow-sm"
                  />
                )
              })}
              
              {/* Gradients */}
              <defs>
                <linearGradient id="revenueGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stopColor="#8b5cf6" />
                  <stop offset="100%" stopColor="#3b82f6" />
                </linearGradient>
                <linearGradient id="customerGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stopColor="#10b981" />
                  <stop offset="100%" stopColor="#059669" />
                </linearGradient>
                <linearGradient id="revenueAreaGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stopColor="#8b5cf6" stopOpacity="0.3" />
                  <stop offset="100%" stopColor="#3b82f6" stopOpacity="0.1" />
                </linearGradient>
                <linearGradient id="customerAreaGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stopColor="#10b981" stopOpacity="0.3" />
                  <stop offset="100%" stopColor="#059669" stopOpacity="0.1" />
                </linearGradient>
              </defs>
            </svg>
            
            {/* Interactive data points */}
            {data.map((item, index) => {
              const x = (index / (data.length - 1)) * 100
              const y = 100 - ((item.value - minValue) / range) * 80
              const tooltipPosition = getTooltipPosition(index, data.length)
              
              return (
                <div
                  key={index}
                  className="absolute transform -translate-x-1/2 -translate-y-1/2 group cursor-pointer"
                  style={{ left: `${x}%`, top: `${y}%` }}
                >
                  {/* Intelligent positioned tooltip */}
                  <div className={`fixed opacity-0 group-hover:opacity-100 transition-all duration-300 pointer-events-none z-50 transform scale-110 ${getTooltipClasses(tooltipPosition)}`}>
                    <div className="bg-gradient-to-r from-secondary-900 to-secondary-800 text-white text-xs font-semibold rounded-lg py-1.5 px-2.5 whitespace-nowrap shadow-xl border border-secondary-700 max-w-[100px] text-center">
                      <div className="font-bold text-xs">{item.month}</div>
                      <div className="text-sm font-bold text-primary-200 truncate">
                        {title.includes('Revenue') ? `$${(item.value / 1000).toFixed(0)}k` : item.value.toLocaleString()}
                      </div>
                      <div className="text-xs text-secondary-300 mt-0.5 truncate">
                        {item.change > 0 ? '+' : ''}{item.change}% vs prev
                      </div>
                    </div>
                    {/* Intelligent arrow positioning */}
                    <div className={getTooltipArrowClasses(tooltipPosition)}></div>
                  </div>
                  
                  {/* Invisible hit area for better hover */}
                  <div className="w-4 h-4 bg-transparent"></div>
                </div>
              )
            })}
          </div>
          
          {/* X-axis labels with horizontal scroll for many months */}
          <div className="absolute bottom-0 left-0 right-0 px-8 pb-2">
            <div className="flex justify-between overflow-x-auto scrollbar-none">
              {data.map((item, index) => (
                <div key={index} className="text-center flex-shrink-0" style={{ minWidth: data.length <= 12 ? 'auto' : '60px' }}>
                  <div className="text-xs font-medium text-secondary-600 mb-1 truncate">
                    {data.length <= 12 ? item.month : 
                     data.length <= 24 ? `${item.month.substring(0, 3)}` : 
                     item.month.substring(0, 2)}
                  </div>
                  <div className="text-xs font-semibold text-secondary-700 mb-1">
                    {title.includes('Revenue') ? `$${(item.value / 1000).toFixed(0)}k` : item.value.toLocaleString()}
                  </div>
                  <div className={`text-xs font-semibold ${
                    item.change > 0 ? 'text-green-600' : item.change < 0 ? 'text-red-600' : 'text-secondary-500'
                  } truncate`}>
                    {item.change > 0 ? '↗' : item.change < 0 ? '↘' : '→'} {Math.abs(item.change)}%
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
        
        {/* Enhanced chart footer */}
        <div className="mt-6 grid grid-cols-2 gap-6">
          <div className="text-center p-4 bg-gradient-to-r from-primary-50 to-accent-50 rounded-xl border border-primary-100">
            <div className="text-sm font-semibold text-primary-700">Data Points</div>
            <div className="text-2xl font-bold text-primary-600">{data.length}</div>
          </div>
          <div className="text-center p-4 bg-gradient-to-r from-success-50 to-emerald-50 rounded-xl border border-success-100">
            <div className="text-sm font-semibold text-success-700">Range</div>
            <div className="text-lg font-bold text-success-600">
              {title.includes('Revenue') ? `$${minValue.toLocaleString()}` : minValue.toLocaleString()} - {title.includes('Revenue') ? `$${maxValue.toLocaleString()}` : maxValue.toLocaleString()}
            </div>
          </div>
        </div>
      </div>
    )
  }

  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-20">
        <div className="text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-primary-600 mx-auto mb-4"></div>
          <p className="text-lg text-secondary-600">Loading Analytics Dashboard...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-white rounded-2xl p-8 shadow-soft border border-secondary-200"
      >
        <div className="flex items-center justify-between mb-8">
          <div>
            <h1 className="text-3xl font-bold text-secondary-900">Analytics Dashboard</h1>
            <p className="text-secondary-600 mt-2">Real-time business intelligence and performance metrics.</p>
          </div>
          
          {/* Time Range Selector */}
          <select
            value={selectedTimeRange}
            onChange={(e) => setSelectedTimeRange(e.target.value)}
            className="bg-white border border-secondary-200 rounded-xl px-4 py-2 text-sm font-medium text-secondary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent shadow-sm"
          >
            <option value="7d">Last 7 days</option>
            <option value="30d">Last 30 days</option>
            <option value="90d">Last 90 days</option>
            <option value="12m">Last 12 months</option>
            <option value="24m">Last 24 months</option>
            <option value="all">All Data</option>
          </select>
        </div>
      </motion.div>

      {/* Key Metrics Grid */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="grid grid-cols-1 md:grid-cols-3 gap-6"
      >
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.1 }}
          className="p-6 rounded-2xl border-2 bg-primary-50 border-primary-200 text-primary-700 shadow-soft hover:shadow-medium transition-all duration-200"
        >
          <div className="flex items-center justify-between mb-4">
            <div className="w-12 h-12 bg-white/50 rounded-xl flex items-center justify-center">
              <CurrencyDollarIcon className="h-6 w-6" />
            </div>
            <div className={`flex items-center space-x-1 text-sm font-medium ${
              metrics.revenueChange >= 0 ? 'text-green-600' : 'text-red-600'
            }`}>
              {metrics.revenueChange >= 0 ? (
                <ArrowUpIcon className="h-4 w-4" />
              ) : (
                <ArrowDownIcon className="h-4 w-4" />
              )}
              <span>{Math.abs(metrics.revenueChange).toFixed(1)}%</span>
            </div>
          </div>
          
          <div className="text-3xl font-bold mb-2">${metrics.revenue.toLocaleString()}</div>
          <div className="text-sm opacity-80">Total Revenue</div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.2 }}
          className="p-6 rounded-2xl border-2 bg-accent-50 border-accent-200 text-accent-700 shadow-soft hover:shadow-medium transition-all duration-200"
        >
          <div className="flex items-center justify-between mb-4">
            <div className="w-12 h-12 bg-white/50 rounded-xl flex items-center justify-center">
              <ShoppingCartIcon className="h-6 w-6" />
            </div>
            <div className={`flex items-center space-x-1 text-sm font-medium ${
              metrics.orderChange >= 0 ? 'text-green-600' : 'text-red-600'
            }`}>
              {metrics.orderChange >= 0 ? (
                <ArrowUpIcon className="h-4 w-4" />
              ) : (
                <ArrowDownIcon className="h-4 w-4" />
              )}
              <span>{Math.abs(metrics.orderChange).toFixed(1)}%</span>
            </div>
          </div>
          
          <div className="text-3xl font-bold mb-2">{metrics.orders.toLocaleString()}</div>
          <div className="text-sm opacity-80">Total Orders</div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.3 }}
          className="p-6 rounded-2xl border-2 bg-success-50 border-success-200 text-success-700 shadow-soft hover:shadow-medium transition-all duration-200"
        >
          <div className="flex items-center justify-between mb-4">
            <div className="w-12 h-12 bg-white/50 rounded-xl flex items-center justify-center">
              <UsersIcon className="h-6 w-6" />
            </div>
            <div className={`flex items-center space-x-1 text-sm font-medium ${
              metrics.customerChange >= 0 ? 'text-green-600' : 'text-red-600'
            }`}>
              {metrics.customerChange >= 0 ? (
                <ArrowUpIcon className="h-4 w-4" />
              ) : (
                <ArrowDownIcon className="h-4 w-4" />
              )}
              <span>{Math.abs(metrics.customerChange).toFixed(1)}%</span>
            </div>
          </div>
          
          <div className="text-3xl font-bold mb-2">{metrics.customers.toLocaleString()}</div>
          <div className="text-sm opacity-80">Total Customers</div>
        </motion.div>
      </motion.div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
        {renderLineChart(currentData.revenue, `📈 Revenue Trend (${(() => {
          if (selectedTimeRange === '7d') return 'Last 7 Days'
          if (selectedTimeRange === '30d') return 'Last 30 Days'
          if (selectedTimeRange === '90d') return 'Last 90 Days'
          const startYear = 2023 + Math.floor(currentPage * 12 / 12)
          const endYear = 2023 + Math.floor((currentPage + 1) * 12 / 12)
          if (startYear === endYear) {
            return `${startYear}`
          } else {
            return `${startYear}-${endYear.toString().slice(-2)}`
          }
        })()})`)}
        
        {renderLineChart(currentData.customers, `👥 Customer Growth (${(() => {
          if (selectedTimeRange === '7d') return 'Last 7 Days'
          if (selectedTimeRange === '30d') return 'Last 30 Days'
          if (selectedTimeRange === '90d') return 'Last 90 Days'
          const startYear = 2023 + Math.floor(currentPage * 12 / 12)
          const endYear = 2023 + Math.floor((currentPage + 1) * 12 / 12)
          if (startYear === endYear) {
            return `${startYear}`
          } else {
            return `${startYear}-${endYear.toString().slice(-2)}`
          }
        })()})`)}
      </div>

      {/* Pagination Controls */}
      {totalPages > 1 && (
        <div className="bg-white rounded-2xl p-6 shadow-soft border border-secondary-200 mb-8">
          <div className="flex items-center justify-between">
            <div className="text-sm text-secondary-600">
              <div className="font-medium">
                Page {currentPage + 1} of {totalPages}
              </div>
              <div className="text-secondary-500 mt-1">
                {(() => {
                  const startYear = 2023 + Math.floor(currentPage * 12 / 12)
                  const endYear = 2023 + Math.floor((currentPage + 1) * 12 / 12)
                  if (startYear === endYear) {
                    return `${startYear} (${currentData.revenue.length} months)`
                  } else {
                    return `${startYear}-${endYear.toString().slice(-2)} (${currentData.revenue.length} months)`
                  }
                })()}
              </div>
            </div>
            
            <div className="flex items-center space-x-2">
              <button
                onClick={() => setCurrentPage(Math.max(0, currentPage - 1))}
                disabled={currentPage === 0}
                className="px-3 py-2 text-sm font-medium text-secondary-600 bg-secondary-100 rounded-lg hover:bg-secondary-200 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
              >
                ← Previous
              </button>
              
              <div className="flex items-center space-x-1">
                {Array.from({ length: totalPages }, (_, i) => (
                  <button
                    key={i}
                    onClick={() => setCurrentPage(i)}
                    className={`w-8 h-8 text-sm font-medium rounded-lg transition-colors ${
                      currentPage === i
                        ? 'bg-primary-500 text-white'
                        : 'bg-secondary-100 text-secondary-600 hover:bg-secondary-200'
                    }`}
                  >
                    {i + 1}
                  </button>
                ))}
              </div>
              
              <button
                onClick={() => setCurrentPage(Math.min(totalPages - 1, currentPage + 1))}
                disabled={currentPage === totalPages - 1}
                className="px-3 py-2 text-sm font-medium text-secondary-600 bg-secondary-100 rounded-lg hover:bg-secondary-200 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
              >
                Next →
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Performance Metrics */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className="grid grid-cols-1 md:grid-cols-2 gap-8"
      >
        {/* Performance Summary */}
        <div className="bg-white rounded-2xl p-6 shadow-soft border border-secondary-200">
          <h3 className="text-xl font-semibold text-secondary-900 mb-4">
            📊 Performance Summary
          </h3>
          <div className="space-y-4">
            <div className="flex items-center justify-between p-3 bg-secondary-50 rounded-xl">
              <div className="flex items-center space-x-3">
                <ChartBarIcon className="h-5 w-5 text-primary-600" />
                <span className="font-medium text-secondary-900">Average Order Value</span>
              </div>
              <div className="text-right">
                <div className="font-semibold text-secondary-900">$99.85</div>
                <div className="text-xs text-green-600">+5.2% vs last month</div>
              </div>
            </div>
            
            <div className="flex items-center justify-between p-3 bg-secondary-50 rounded-xl">
              <div className="flex items-center space-x-3">
                <CalendarIcon className="h-5 w-5 text-accent-600" />
                <span className="font-medium text-secondary-900">Monthly Growth Rate</span>
              </div>
              <div className="text-right">
                <div className="font-semibold text-secondary-900">7.8%</div>
                <div className="text-xs text-green-600">Consistent growth</div>
              </div>
            </div>
            
            <div className="flex items-center justify-between p-3 bg-secondary-50 rounded-xl">
              <div className="flex items-center space-x-3">
                <UsersIcon className="h-5 w-5 text-success-600" />
                <span className="font-medium text-secondary-900">Customer Retention</span>
              </div>
              <div className="text-right">
                <div className="font-semibold text-secondary-900">87.3%</div>
                <div className="text-xs text-green-600">Excellent retention</div>
              </div>
            </div>
          </div>
        </div>

        {/* Recent Activity */}
        <div className="bg-white rounded-2xl p-6 shadow-soft border border-secondary-200">
          <h3 className="text-xl font-semibold text-secondary-900 mb-4">
            🔥 Recent Activity
          </h3>
          <div className="space-y-3">
            <div className="flex items-center space-x-3 p-3 bg-green-50 rounded-xl border border-green-100">
              <div className="w-3 h-3 bg-green-500 rounded-full"></div>
              <div>
                <div className="font-medium text-green-800">New record sales day</div>
                <div className="text-sm text-green-600">$12,847 in single day</div>
              </div>
            </div>
            
            <div className="flex items-center space-x-3 p-3 bg-blue-50 rounded-xl border border-blue-100">
              <div className="w-3 h-3 bg-blue-500 rounded-full"></div>
              <div>
                <div className="font-medium text-blue-800">Customer milestone</div>
                <div className="text-sm text-blue-600">Reached 15,000 customers</div>
              </div>
            </div>
            
            <div className="flex items-center space-x-3 p-3 bg-amber-50 rounded-xl border border-amber-100">
              <div className="w-3 h-3 bg-amber-500 rounded-full"></div>
              <div>
                <div className="font-medium text-amber-800">Growth alert</div>
                <div className="text-sm text-amber-600">15% increase in orders</div>
              </div>
            </div>
          </div>
        </div>
      </motion.div>

      {/* Quick Actions */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
        className="bg-gradient-to-r from-primary-50 to-accent-50 rounded-2xl p-8 border border-primary-100"
      >
        <h3 className="text-2xl font-semibold text-secondary-900 mb-6 text-center">
          🚀 Quick Actions
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <button className="bg-primary-600 hover:bg-primary-700 text-white font-semibold py-3 px-6 rounded-xl transition-all duration-200 flex items-center justify-center space-x-2 hover:scale-105">
            <ChartBarIcon className="h-5 w-5" />
            <span>Export Report</span>
          </button>
          <button className="bg-accent-500 hover:bg-accent-600 text-white font-semibold py-3 px-6 rounded-xl transition-all duration-200 flex items-center justify-center space-x-2 hover:scale-105">
            <ChartBarIcon className="h-5 w-5" />
            <span>View Trends</span>
          </button>
          <button className="bg-success-500 hover:bg-success-600 text-white font-semibold py-3 px-6 rounded-xl transition-all duration-200 flex items-center justify-center space-x-2 hover:scale-105">
            <UsersIcon className="h-5 w-5" />
            <span>Customer Analysis</span>
          </button>
        </div>
      </motion.div>
    </div>
  )
}
