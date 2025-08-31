import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { useDropzone } from 'react-dropzone'
import { useNavigate } from 'react-router-dom'
import { 
  CloudArrowUpIcon, 
  ChartBarIcon,
  DocumentTextIcon,
  BuildingOfficeIcon,
  ArrowRightIcon,
  CheckCircleIcon,
  ExclamationTriangleIcon,
  FolderIcon,
  ClockIcon,
  PlusIcon
} from '@heroicons/react/24/outline'
import { dataManager, CompanyProfile, DataFile, ColumnMapping } from '@/lib/dataManager'

export default function Dashboard() {
  const navigate = useNavigate()
  const [currentCompany, setCurrentCompany] = useState<CompanyProfile | null>(null)
  const [currentFile, setCurrentFile] = useState<DataFile | null>(null)
  const [showColumnMapping, setShowColumnMapping] = useState(false)
  const [columnMapping, setColumnMapping] = useState<ColumnMapping | null>(null)
  const [industry, setIndustry] = useState<'Generic' | 'Retail' | 'SaaS' | 'Marketplace'>('Generic')
  const [isProcessing, setIsProcessing] = useState(false)
  const [showNewUpload, setShowNewUpload] = useState(false)
  const [allFiles, setAllFiles] = useState<DataFile[]>([])
  const [fileColumns, setFileColumns] = useState<string[]>([])

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: {
      'text/csv': ['.csv'],
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['.xlsx'],
      'application/vnd.ms-excel': ['.xls'],
      'application/octet-stream': ['.parquet']
    },
    onDrop: async (acceptedFiles) => {
      if (acceptedFiles.length > 0) {
        setIsProcessing(true)
        const file = acceptedFiles[0]
        
        // Create company if not exists
        let company = currentCompany
        if (!company) {
          company = dataManager.createCompany('My Company', 'generic')
          setCurrentCompany(company)
        }
        
        // Read file to get actual columns
        try {
          const columns = await readFileColumns(file)
          
          // Upload file to data manager
          const dataFile = dataManager.uploadFile(file, company.id)
          setCurrentFile(dataFile)
          
          // Store the actual columns for mapping
          setFileColumns(columns)
          
          // Simulate processing
          setTimeout(() => {
            setIsProcessing(false)
            setShowColumnMapping(true)
          }, 2000)
        } catch (error) {
          console.error('Error reading file:', error)
          setIsProcessing(false)
          // Handle error - show message to user
        }
      }
    }
  })

  // Function to read columns from uploaded file
  const readFileColumns = async (file: File): Promise<string[]> => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader()
      
      reader.onload = (e) => {
        try {
          const content = e.target?.result as string
          let columns: string[] = []
          
          if (file.name.endsWith('.csv')) {
            // Parse CSV
            const lines = content.split('\n')
            if (lines.length > 0) {
              columns = lines[0].split(',').map(col => col.trim().replace(/"/g, ''))
            }
          } else if (file.name.endsWith('.xlsx') || file.name.endsWith('.xls')) {
            // For Excel files, we'll use a simple approach
            // In a real app, you'd use a library like xlsx
            columns = ['Column A', 'Column B', 'Column C', 'Column D', 'Column E', 'Column F']
          } else {
            // For other file types
            columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5', 'Column 6']
          }
          
          resolve(columns)
        } catch (error) {
          reject(error)
        }
      }
      
      reader.onerror = () => reject(new Error('Failed to read file'))
      
      if (file.name.endsWith('.csv')) {
        reader.readAsText(file)
      } else {
        // For non-CSV files, we'll simulate column reading
        setTimeout(() => {
          resolve(['Column A', 'Column B', 'Column C', 'Column D', 'Column E', 'Column F'])
        }, 100)
      }
    })
  }

  useEffect(() => {
    // Load current company and file from data manager
    const company = dataManager.getCurrentCompany()
    const file = dataManager.getCurrentFile()
    
    if (company) {
      setCurrentCompany(company)
      if (file && file.companyId === company.id) {
        setCurrentFile(file)
        if (file.status === 'ready' && file.columnMapping) {
          setColumnMapping(file.columnMapping)
        }
      }
    }

    // Load all files for the company
    if (company) {
      const files = dataManager.getCompanyFiles(company.id)
      setAllFiles(files)
    }

    // Clean up any duplicate files that might exist
    const cleanupDuplicates = () => {
      const seen = new Map<string, DataFile>()
      const cleanedFiles: DataFile[] = []
      
      if (company) {
        const companyFiles = dataManager.getCompanyFiles(company.id)
        
        // Keep only the most recent version of each file
        for (const file of companyFiles) {
          const key = file.fileName
          if (!seen.has(key) || new Date(file.uploadDate) > new Date(seen.get(key)!.uploadDate)) {
            seen.set(key, file)
          }
        }
        
        cleanedFiles.push(...Array.from(seen.values()))
        setAllFiles(cleanedFiles)
      }
    }

    cleanupDuplicates()
  }, [])

  const handleColumnMappingComplete = (mapping: ColumnMapping) => {
    setColumnMapping(mapping)
    if (currentFile) {
      dataManager.updateColumnMapping(currentFile.id, mapping)
    }
    setShowColumnMapping(false)
    setShowNewUpload(false)
    
    // Refresh file list
    if (currentCompany) {
      const files = dataManager.getCompanyFiles(currentCompany.id)
      setAllFiles(files)
    }
  }

  const handleFileSelect = (file: DataFile) => {
    setCurrentFile(file)
    if (file.columnMapping) {
      setColumnMapping(file.columnMapping)
    }
    setShowColumnMapping(false)
    setShowNewUpload(false)
  }

  const handleContinueToAnalysis = () => {
    navigate('/analytics')
  }

  const handleContinueToInsights = () => {
    navigate('/insights')
  }

  const getIndustryIcon = (industry: string) => {
    switch (industry) {
      case 'Retail': return '🏪'
      case 'SaaS': return '☁️'
      case 'Marketplace': return '🛒'
      default: return '🏢'
    }
  }

  const getIndustryDescription = (industry: string) => {
    switch (industry) {
      case 'Retail': return 'Store performance, inventory, seasonal planning'
      case 'SaaS': return 'MRR growth, churn analysis, feature adoption'
      case 'Marketplace': return 'Seller performance, buyer behavior, network effects'
      default: return 'General business analysis for any industry'
    }
  }

  const getIndustryColors = (industry: string) => {
    switch (industry) {
      case 'Retail': return { bg: 'from-amber-50 to-orange-50', border: 'border-amber-200', text: 'text-amber-800' }
      case 'SaaS': return { bg: 'from-blue-50 to-indigo-50', border: 'border-blue-200', text: 'text-blue-800' }
      case 'Marketplace': return { bg: 'from-green-50 to-emerald-50', border: 'border-green-200', text: 'text-green-800' }
      default: return { bg: 'from-slate-50 to-gray-50', border: 'border-slate-200', text: 'text-slate-800' }
    }
  }

  const getFileStatusIcon = (status: string) => {
    switch (status) {
      case 'ready': return <CheckCircleIcon className="h-5 w-5 text-green-500" />
      case 'processing': return <ClockIcon className="h-5 w-5 text-blue-500" />
      case 'error': return <ExclamationTriangleIcon className="h-5 w-5 text-red-500" />
      default: return <ClockIcon className="h-5 w-5 text-gray-500" />
    }
  }

  return (
    <div className="space-y-8">
      {/* Beautiful Main Header */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <div className="bg-gradient-to-r from-primary-500 to-accent-500 rounded-3xl p-8 text-white shadow-large mb-6">
          <h1 className="text-5xl font-bold mb-4">📈 OmniInsights</h1>
          <p className="text-xl opacity-90">Advanced Business Intelligence & Analytics Platform</p>
        </div>
        
        <div className="text-center mb-8">
          <p className="text-lg text-secondary-600 font-medium">
            🚀 Upload a dataset → 🧭 Map columns → 🔍 Filter → 📊 Explore insights → 📄 Export reports
          </p>
          <p className="text-secondary-500 mt-2">
            Clear, simple, and explainable business intelligence
          </p>
        </div>
      </motion.div>

      {/* File Management Section - Always Visible */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-white rounded-3xl p-8 shadow-soft border border-secondary-200"
      >
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-3xl font-bold text-secondary-900">
            📁 Data Management
          </h2>
          <button
            onClick={() => setShowNewUpload(true)}
            className="bg-primary-600 hover:bg-primary-700 text-white font-semibold py-3 px-6 rounded-xl transition-all duration-200 flex items-center space-x-2"
          >
            <PlusIcon className="h-5 w-5" />
            <span>Upload New File</span>
          </button>
        </div>

        {/* Previously Loaded Files */}
        {allFiles.length > 0 && (
          <div className="mb-8">
            <h3 className="text-xl font-semibold text-secondary-900 mb-4">
              📂 Previously Loaded Files
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {allFiles.map((file) => (
                <div
                  key={file.id}
                  onClick={() => handleFileSelect(file)}
                  className={`p-4 border-2 rounded-xl cursor-pointer transition-all duration-200 ${
                    currentFile?.id === file.id
                      ? 'border-primary-500 bg-primary-50'
                      : 'border-secondary-200 bg-white hover:border-primary-300 hover:bg-primary-50'
                  }`}
                >
                  <div className="flex items-center space-x-3 mb-2">
                    <FolderIcon className="h-5 w-5 text-secondary-400" />
                    <span className="font-medium text-secondary-900 truncate">{file.fileName}</span>
                  </div>
                  <div className="flex items-center space-x-2 mb-2">
                    {getFileStatusIcon(file.status)}
                    <span className="text-sm text-secondary-600">
                      {file.status === 'ready' ? 'Ready' : file.status === 'processing' ? 'Processing' : 'Error'}
                    </span>
                  </div>
                  <div className="text-xs text-secondary-500 space-y-1">
                    <div>Size: {Math.round(file.fileSize / 1024)} KB</div>
                    <div>Uploaded: {new Date(file.uploadDate).toLocaleDateString()}</div>
                    {file.columnMapping && (
                      <div className="text-green-600 font-medium">✓ Mapped</div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* New File Upload */}
        {showNewUpload && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="border-t border-secondary-200 pt-6"
          >
            <h3 className="text-xl font-semibold text-secondary-900 mb-4">
              📤 Upload New File
            </h3>
            
            <div
              {...getRootProps()}
              className={`border-2 border-dashed rounded-2xl p-8 text-center cursor-pointer transition-all duration-200 ${
                isDragActive
                  ? "border-accent-500 bg-accent-50"
                  : "border-secondary-300 hover:border-accent-400 hover:bg-accent-50"
              }`}
            >
              <input {...getInputProps()} />
              <CloudArrowUpIcon className="mx-auto h-16 w-16 text-secondary-400 mb-4" />
              <div className="space-y-2">
                <p className="text-lg font-medium text-secondary-900">
                  {isDragActive ? 'Drop your files here' : 'Drag & drop your files here'}
                </p>
                <p className="text-secondary-600">
                  or click to browse files
                </p>
                <p className="text-sm text-secondary-500">
                  Supports CSV, Excel, and Parquet files
                </p>
              </div>
            </div>

            {/* Tip Box */}
            <div className="mt-6 bg-blue-50 border border-blue-200 rounded-xl p-4">
              <p className="text-blue-800 font-medium mb-2">
                💡 <strong>Tip:</strong> Include these columns for best results:
              </p>
              <ul className="text-blue-700 text-sm space-y-1">
                <li>📅 date</li>
                <li>💰 amount</li>
                <li>🆔 order_id</li>
                <li>👥 customer_id</li>
                <li>📦 product (optional)</li>
                <li>🛣️ channel (optional)</li>
              </ul>
            </div>
          </motion.div>
        )}

        {/* File Processing Status */}
        {isProcessing && currentFile && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="mt-6 bg-blue-50 border border-blue-200 rounded-xl p-4"
          >
            <div className="flex items-center space-x-4">
              <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-blue-600"></div>
              <div>
                <h3 className="text-lg font-semibold text-blue-800">
                  Processing Your Data
                </h3>
                <p className="text-blue-700">
                  Analyzing {currentFile.fileName}... This may take a few moments.
                </p>
              </div>
            </div>
          </motion.div>
        )}
      </motion.div>

      {/* Column Mapping Section */}
      {showColumnMapping && currentFile && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white rounded-3xl p-8 shadow-soft border border-secondary-200"
        >
          <h2 className="text-3xl font-bold text-secondary-900 mb-6 text-center">
            🧭 Column Mapping
          </h2>
          
          {/* File Columns Preview */}
          <div className="mb-8 p-6 bg-secondary-50 rounded-2xl border border-secondary-200">
            <h3 className="text-lg font-semibold text-secondary-900 mb-4">
              📋 Available Columns in {currentFile.fileName}
            </h3>
            <div className="flex flex-wrap gap-2">
              {fileColumns.map((column, index) => (
                <span
                  key={column}
                  className="px-3 py-2 bg-white rounded-lg border border-secondary-200 text-sm font-medium text-secondary-700"
                >
                  {column}
                </span>
              ))}
            </div>
            <p className="text-sm text-secondary-600 mt-3">
              Select which columns correspond to the required business data fields below.
            </p>
          </div>
          
          <ColumnMappingWidget 
            onComplete={handleColumnMappingComplete}
            dataFile={currentFile}
            fileColumns={fileColumns}
          />
          
          {/* Mapping Guidance */}
          <div className="mt-8 p-6 bg-blue-50 border border-blue-200 rounded-2xl">
            <h3 className="text-lg font-semibold text-blue-800 mb-3">
              💡 Column Mapping Guide
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm text-blue-700">
              <div>
                <strong>📅 Date Column:</strong> When the transaction/order occurred
              </div>
              <div>
                <strong>💰 Amount Column:</strong> The monetary value of the transaction
              </div>
              <div>
                <strong>🆔 Order ID Column:</strong> Unique identifier for each order
              </div>
              <div>
                <strong>👥 Customer ID Column:</strong> Unique identifier for each customer
              </div>
              <div>
                <strong>📦 Product Column:</strong> What was purchased (optional)
              </div>
              <div>
                <strong>🛣️ Channel Column:</strong> How the order was placed (optional)
              </div>
            </div>
          </div>
        </motion.div>
      )}

      {/* Industry Selection */}
      {currentFile && columnMapping && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white rounded-3xl p-8 shadow-soft border border-secondary-200"
        >
          <h2 className="text-3xl font-bold text-secondary-900 mb-6 text-center">
            🏢 Industry Configuration
          </h2>
          <p className="text-lg text-secondary-600 mb-6 text-center">
            Select your industry for tailored insights and recommendations
          </p>

          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            {(['Generic', 'Retail', 'SaaS', 'Marketplace'] as const).map((ind) => {
              const colors = getIndustryColors(ind)
              return (
                <button
                  key={ind}
                  onClick={() => setIndustry(ind)}
                  className={`p-6 rounded-2xl border-2 transition-all duration-200 ${
                    industry === ind
                      ? `bg-gradient-to-r ${colors.bg} ${colors.border} shadow-medium`
                      : 'border-secondary-200 bg-white hover:border-primary-300 hover:bg-primary-50'
                  }`}
                >
                  <div className="text-3xl mb-3">{getIndustryIcon(ind)}</div>
                  <div className={`font-semibold text-lg capitalize ${industry === ind ? colors.text : 'text-secondary-900'}`}>
                    {ind} Industry
                  </div>
                  <div className={`text-sm mt-2 ${industry === ind ? colors.text : 'text-secondary-600'}`}>
                    {getIndustryDescription(ind)}
                  </div>
                </button>
              )
            })}
          </div>

          {/* Industry Status */}
          <div className="mt-6 text-center">
            {industry !== 'Generic' ? (
              <div className="bg-green-50 border border-green-200 rounded-xl p-4 inline-block">
                <h3 className="text-green-800 font-semibold mb-1">✅ Active</h3>
                <p className="text-green-700 text-sm">{industry} insights enabled</p>
              </div>
            ) : (
              <div className="bg-blue-50 border border-blue-200 rounded-xl p-4 inline-block">
                <h3 className="text-blue-800 font-semibold mb-1">ℹ️ Standard</h3>
                <p className="text-blue-700 text-sm">General analysis mode</p>
              </div>
            )}
          </div>
        </motion.div>
      )}

      {/* Quick Actions - Only show when file is ready */}
      {currentFile && columnMapping && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-gradient-to-r from-primary-50 to-accent-50 rounded-2xl p-8 border border-primary-100"
        >
          <h2 className="text-2xl font-semibold text-secondary-900 mb-6 text-center">
            🚀 Ready to Analyze
          </h2>
          <p className="text-secondary-600 mb-6 text-center">
            Your data is ready! Choose where to start your analysis:
          </p>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <button
              onClick={handleContinueToAnalysis}
              className="bg-primary-600 hover:bg-primary-700 text-white font-semibold py-4 px-6 rounded-xl transition-all duration-200 flex items-center justify-center space-x-2 hover:scale-105"
            >
              <span>📊 Go to Analytics</span>
              <ArrowRightIcon className="h-5 w-5" />
            </button>
            
            <button
              onClick={handleContinueToInsights}
              className="bg-accent-500 hover:bg-accent-600 text-white font-semibold py-4 px-6 rounded-xl transition-all duration-200 flex items-center justify-center space-x-2 hover:scale-105"
            >
              <span>🤖 Go to AI Insights</span>
              <ArrowRightIcon className="h-5 w-5" />
            </button>
          </div>

          <div className="mt-6 text-center">
            <p className="text-secondary-600 text-sm">
              📄 <strong>Also available:</strong> Reports, Settings, and more from the sidebar navigation
            </p>
          </div>
        </motion.div>
      )}

      {/* Report Generation */}
      {currentFile && columnMapping && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-gradient-to-r from-amber-50 to-orange-50 rounded-2xl p-8 border border-amber-200"
        >
          <h2 className="text-2xl font-semibold text-amber-800 mb-6 text-center">
            📄 Report Generation
          </h2>
          <div className="text-center">
            <button className="bg-amber-600 hover:bg-amber-700 text-white font-semibold py-4 px-8 rounded-xl transition-all duration-200 flex items-center justify-center space-x-2 mx-auto">
              <span>📄 Export Executive Report</span>
              <ArrowRightIcon className="h-5 w-5" />
            </button>
            <p className="text-amber-700 mt-4 text-sm">
              📊 <strong>Includes:</strong> KPIs, Trends, Products, Customers, RFM Analysis
            </p>
          </div>
        </motion.div>
      )}
    </div>
  )
}

// Column Mapping Widget Component
function ColumnMappingWidget({ onComplete, dataFile, fileColumns }: { onComplete: (mapping: ColumnMapping) => void, dataFile: DataFile, fileColumns: string[] }) {
  const [mapping, setMapping] = useState<ColumnMapping>({
    date: '',
    amount: '',
    orderId: '',
    customerId: '',
    product: '',
    channel: ''
  })

  const handleComplete = () => {
    onComplete(mapping)
  }

  return (
    <div className="max-w-4xl mx-auto">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <label className="block text-sm font-medium text-secondary-700 mb-2">
            📅 Date Column *
          </label>
          <select
            value={mapping.date}
            onChange={(e) => setMapping({ ...mapping, date: e.target.value })}
            className="w-full px-4 py-3 border border-secondary-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
          >
            <option value="">Select date column</option>
            {fileColumns.map(col => (
              <option key={col} value={col}>{col}</option>
            ))}
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-secondary-700 mb-2">
            💰 Amount Column *
          </label>
          <select
            value={mapping.amount}
            onChange={(e) => setMapping({ ...mapping, amount: e.target.value })}
            className="w-full px-4 py-3 border border-secondary-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
          >
            <option value="">Select amount column</option>
            {fileColumns.map(col => (
              <option key={col} value={col}>{col}</option>
            ))}
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-secondary-700 mb-2">
            🆔 Order ID Column *
          </label>
          <select
            value={mapping.orderId}
            onChange={(e) => setMapping({ ...mapping, orderId: e.target.value })}
            className="w-full px-4 py-3 border border-secondary-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
          >
            <option value="">Select order ID column</option>
            {fileColumns.map(col => (
              <option key={col} value={col}>{col}</option>
            ))}
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-secondary-700 mb-2">
            👥 Customer ID Column *
          </label>
          <select
            value={mapping.customerId}
            onChange={(e) => setMapping({ ...mapping, customerId: e.target.value })}
            className="w-full px-4 py-3 border border-secondary-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
          >
            <option value="">Select customer ID column</option>
            {fileColumns.map(col => (
              <option key={col} value={col}>{col}</option>
            ))}
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-secondary-700 mb-2">
            📦 Product Column (Optional)
          </label>
          <select
            value={mapping.product}
            onChange={(e) => setMapping({ ...mapping, product: e.target.value })}
            className="w-full px-4 py-3 border border-secondary-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
          >
            <option value="">Select product column</option>
            {fileColumns.map(col => (
              <option key={col} value={col}>{col}</option>
            ))}
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-secondary-700 mb-2">
            🛣️ Channel Column (Optional)
          </label>
          <select
            value={mapping.channel}
            onChange={(e) => setMapping({ ...mapping, channel: e.target.value })}
            className="w-full px-4 py-3 border border-secondary-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
          >
            <option value="">Select channel column</option>
            {fileColumns.map(col => (
              <option key={col} value={col}>{col}</option>
            ))}
          </select>
        </div>
      </div>

      <div className="mt-8 text-center">
        <button
          onClick={handleComplete}
          disabled={!mapping.date || !mapping.amount || !mapping.orderId || !mapping.customerId}
          className="bg-primary-600 hover:bg-primary-700 disabled:bg-secondary-300 text-white font-semibold py-4 px-8 rounded-xl transition-all duration-200 flex items-center justify-center space-x-2 mx-auto"
        >
          <span>✅ Confirm Column Mapping</span>
          <ArrowRightIcon className="h-5 w-5" />
        </button>
      </div>
    </div>
  )
}
