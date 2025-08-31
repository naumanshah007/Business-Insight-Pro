import { motion } from 'framer-motion'
import { ArrowUpIcon, ArrowDownIcon } from '@heroicons/react/24/solid'
import { cn } from '@/lib/utils'

interface KPICardProps {
  title: string
  value: string
  change: string
  changeType: 'positive' | 'negative' | 'neutral'
  icon: React.ComponentType<{ className?: string }>
  color: 'primary' | 'secondary' | 'accent' | 'success' | 'warning' | 'error'
}

const colorClasses = {
  primary: 'from-primary-500 to-primary-600',
  secondary: 'from-secondary-500 to-secondary-600',
  accent: 'from-accent-500 to-accent-600',
  success: 'from-success-500 to-success-600',
  warning: 'from-warning-500 to-warning-600',
  error: 'from-error-500 to-error-600',
}

const iconBgColors = {
  primary: 'bg-primary-100',
  secondary: 'bg-secondary-100',
  accent: 'bg-accent-100',
  success: 'bg-success-100',
  warning: 'bg-warning-100',
  error: 'bg-error-100',
}

const iconColors = {
  primary: 'text-primary-600',
  secondary: 'text-secondary-600',
  accent: 'text-accent-600',
  success: 'text-success-600',
  warning: 'text-warning-600',
  error: 'text-error-600',
}

export default function KPICard({ title, value, change, changeType, icon: Icon, color }: KPICardProps) {
  return (
    <motion.div
      whileHover={{ scale: 1.02, y: -2 }}
      className="kpi-card group"
    >
      <div className="flex items-center justify-between">
        <div className="flex-1">
          <p className="text-sm font-medium text-secondary-600 mb-2">{title}</p>
          <p className="text-3xl font-bold text-secondary-900 mb-2">{value}</p>
          
          <div className="flex items-center space-x-1">
            {changeType === 'positive' ? (
              <ArrowUpIcon className="h-4 w-4 text-success-500" />
            ) : changeType === 'negative' ? (
              <ArrowDownIcon className="h-4 w-4 text-error-500" />
            ) : null}
            <span
              className={cn(
                'text-sm font-medium',
                changeType === 'positive' && 'text-success-600',
                changeType === 'negative' && 'text-error-600',
                changeType === 'neutral' && 'text-secondary-600'
              )}
            >
              {change}
            </span>
            <span className="text-sm text-secondary-500">from last month</span>
          </div>
        </div>
        
        <div className={cn(
          'p-3 rounded-xl transition-all duration-200 group-hover:scale-110',
          iconBgColors[color]
        )}>
          <Icon className={cn('h-8 w-8', iconColors[color])} />
        </div>
      </div>
      
      {/* Gradient accent line */}
      <div className={cn(
        'h-1 rounded-full mt-4 bg-gradient-to-r',
        colorClasses[color]
      )} />
    </motion.div>
  )
}
