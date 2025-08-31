import { motion } from 'framer-motion'
import { useState } from 'react'
import { 
  DocumentChartBarIcon, 
  ArrowDownTrayIcon,
  EyeIcon,
  CalendarIcon,
  ChartBarIcon,
  UsersIcon,
  CurrencyDollarIcon
} from '@heroicons/react/24/outline'

const reportTemplates = [
  {
    id: 'executive',
    name: 'Executive Summary',
    description: 'High-level overview for stakeholders and executives',
    icon: '📊',
    color: 'primary',
    estimatedTime: '2-3 minutes'
  },
  {
    id: 'detailed',
    name: 'Detailed Analysis',
    description: 'Comprehensive analysis with all metrics and insights',
    icon: '📈',
    color: 'accent',
    estimatedTime: '5-7 minutes'
  },
  {
    id: 'custom',
    name: 'Custom Report',
    description: 'Build your own report with specific metrics',
    icon: '🎯',
    color: 'success',
    estimatedTime: '3-5 minutes'
  }
]

const recentReports = [
  {
    id: 1,
    name: 'Q4 2024 Executive Summary',
    type: 'Executive Summary',
    generated: '2024-12-15',
    status: 'completed',
    size: '2.4 MB'
  },
  {
    id: 2,
    name: 'December Performance Report',
    type: 'Detailed Analysis',
    generated: '2024-12-14',
    status: 'completed',
    size: '4.1 MB'
  },
  {
    id: 3,
    name: 'Customer Insights Report',
    type: 'Custom Report',
    generated: '2024-12-13',
    status: 'completed',
    size: '3.2 MB'
  }
]

export default function Reports() {
  const [selectedTemplate, setSelectedTemplate] = useState<string | null>(null)
  const [isGenerating, setIsGenerating] = useState(false)

  const handleGenerateReport = (templateId: string) => {
    setSelectedTemplate(templateId)
    setIsGenerating(true)
    
    // Simulate report generation
    setTimeout(() => {
      setIsGenerating(false)
      setSelectedTemplate(null)
    }, 3000)
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <div className="flex items-center justify-center space-x-3 mb-4">
          <div className="w-12 h-12 bg-gradient-to-r from-accent-500 to-primary-500 rounded-xl flex items-center justify-center">
            <DocumentChartBarIcon className="h-6 w-6 text-white" />
          </div>
          <h1 className="text-4xl font-bold text-gradient">Reports & Analytics</h1>
        </div>
        <p className="text-xl text-secondary-600 max-w-3xl mx-auto">
          Generate comprehensive reports and export insights for stakeholders, presentations, and analysis
        </p>
      </motion.div>

      {/* Report Templates */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="grid grid-cols-1 md:grid-cols-3 gap-6"
      >
        {reportTemplates.map((template, index) => (
          <motion.div
            key={template.id}
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: index * 0.1 }}
            className="bg-white rounded-2xl p-6 shadow-soft border border-secondary-200 hover:shadow-medium transition-all duration-200"
          >
            <div className="text-center mb-6">
              <div className="text-4xl mb-4">{template.icon}</div>
              <h3 className="text-xl font-semibold text-secondary-900 mb-2">{template.name}</h3>
              <p className="text-secondary-600 text-sm mb-4">{template.description}</p>
              <div className="inline-flex items-center space-x-2 text-xs text-secondary-500 bg-secondary-100 px-3 py-1 rounded-full">
                <CalendarIcon className="h-3 w-3" />
                <span>{template.estimatedTime}</span>
              </div>
            </div>
            
            <button
              onClick={() => handleGenerateReport(template.id)}
              disabled={isGenerating}
              className="w-full button-primary"
            >
              {isGenerating && selectedTemplate === template.id ? (
                <div className="flex items-center justify-center space-x-2">
                  <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></div>
                  <span>Generating...</span>
                </div>
              ) : (
                'Generate Report'
              )}
            </button>
          </motion.div>
        ))}
      </motion.div>

      {/* Recent Reports */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="bg-white rounded-2xl p-6 shadow-soft border border-secondary-200"
      >
        <h2 className="text-2xl font-semibold text-secondary-900 mb-6">Recent Reports</h2>
        
        <div className="space-y-4">
          {recentReports.map((report) => (
            <motion.div
              key={report.id}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              className="flex items-center justify-between p-4 border border-secondary-200 rounded-xl hover:bg-secondary-50 transition-colors"
            >
              <div className="flex items-center space-x-4">
                <div className="w-10 h-10 bg-primary-100 rounded-lg flex items-center justify-center">
                  <DocumentChartBarIcon className="h-5 w-5 text-primary-600" />
                </div>
                <div>
                  <h3 className="font-medium text-secondary-900">{report.name}</h3>
                  <p className="text-sm text-secondary-600">{report.type}</p>
                </div>
              </div>
              
              <div className="flex items-center space-x-4">
                <div className="text-right">
                  <p className="text-sm text-secondary-600">{report.generated}</p>
                  <p className="text-xs text-secondary-500">{report.size}</p>
                </div>
                
                <div className="flex items-center space-x-2">
                  <button className="p-2 text-secondary-600 hover:text-primary-600 transition-colors">
                    <EyeIcon className="h-5 w-5" />
                  </button>
                  <button className="p-2 text-secondary-600 hover:text-primary-600 transition-colors">
                    <ArrowDownTrayIcon className="h-5 w-5" />
                  </button>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Report Features */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className="bg-gradient-to-r from-accent-50 to-primary-50 rounded-2xl p-8 border border-accent-100"
      >
        <h2 className="text-2xl font-semibold text-secondary-900 mb-6 text-center">
          📊 Professional Report Features
        </h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div className="text-center">
            <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <ChartBarIcon className="h-8 w-8 text-primary-600" />
            </div>
            <h3 className="text-lg font-semibold text-secondary-900 mb-2">Interactive Charts</h3>
            <p className="text-secondary-600 text-sm">
              Beautiful, responsive charts that bring your data to life
            </p>
          </div>
          
          <div className="text-center">
            <div className="w-16 h-16 bg-accent-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <UsersIcon className="h-8 w-8 text-accent-600" />
            </div>
            <h3 className="text-lg font-semibold text-secondary-900 mb-2">Stakeholder Ready</h3>
            <p className="text-secondary-600 text-sm">
              Professional formatting perfect for executive presentations
            </p>
          </div>
          
          <div className="text-center">
            <div className="w-16 h-16 bg-success-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <CurrencyDollarIcon className="h-8 w-8 text-success-600" />
            </div>
            <h3 className="text-lg font-semibold text-secondary-900 mb-2">Multiple Formats</h3>
            <p className="text-secondary-600 text-sm">
              Export as PDF, PowerPoint, or interactive HTML
            </p>
          </div>
          
          <div className="text-center">
            <div className="w-16 h-16 bg-secondary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <DocumentChartBarIcon className="h-8 w-8 text-secondary-600" />
            </div>
            <h3 className="text-lg font-semibold text-secondary-900 mb-2">Custom Branding</h3>
            <p className="text-secondary-600 text-sm">
              Add your company logo and customize colors
            </p>
          </div>
        </div>
      </motion.div>

      {/* Quick Actions */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
        className="bg-white rounded-2xl p-6 shadow-soft border border-secondary-200"
      >
        <h2 className="text-xl font-semibold text-secondary-900 mb-4">Quick Actions</h2>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <button className="button-secondary w-full">
            📊 Schedule Report
          </button>
          <button className="button-accent w-full">
            🎨 Customize Template
          </button>
          <button className="button-primary w-full">
            📤 Export All Reports
          </button>
        </div>
      </motion.div>
    </div>
  )
}
