import { Fragment, useState } from 'react'
import { Dialog, Transition, Listbox } from '@headlessui/react'
import { motion } from 'framer-motion'
import { XMarkIcon, CheckIcon, ChevronUpDownIcon } from '@heroicons/react/24/outline'
import { cn } from '@/lib/utils'

interface DataUploadModalProps {
  isOpen: boolean
  onClose: () => void
}

const fileTypes = [
  { id: 'csv', name: 'CSV File', description: 'Comma-separated values', icon: '📄' },
  { id: 'excel', name: 'Excel File', description: 'Microsoft Excel spreadsheet', icon: '📊' },
  { id: 'parquet', name: 'Parquet File', description: 'Columnar storage format', icon: '🗄️' },
]

const columnTypes = [
  { id: 'date', name: 'Date', description: 'Transaction or event date', icon: '📅' },
  { id: 'amount', name: 'Amount', description: 'Revenue or transaction amount', icon: '💰' },
  { id: 'customer', name: 'Customer ID', description: 'Unique customer identifier', icon: '👤' },
  { id: 'product', name: 'Product', description: 'Product name or ID', icon: '📦' },
  { id: 'channel', name: 'Channel', description: 'Sales or marketing channel', icon: '🛣️' },
  { id: 'order', name: 'Order ID', description: 'Unique order identifier', icon: '🛒' },
]

export default function DataUploadModal({ isOpen, onClose }: DataUploadModalProps) {
  const [step, setStep] = useState(1)
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const [columnMappings, setColumnMappings] = useState<Record<string, string>>({})
  const [availableColumns, setAvailableColumns] = useState<string[]>([])

  const handleFileSelect = (file: File) => {
    setSelectedFile(file)
    // Simulate reading file headers
    setAvailableColumns(['Date', 'Amount', 'Customer_ID', 'Product_Name', 'Channel', 'Order_ID'])
    setStep(2)
  }

  const handleColumnMapping = (columnType: string, selectedColumn: string) => {
    setColumnMappings(prev => ({
      ...prev,
      [columnType]: selectedColumn
    }))
  }

  const handleProcess = () => {
    // Process the data with column mappings
    console.log('Processing data with mappings:', columnMappings)
    setStep(3)
    setTimeout(() => {
      onClose()
      setStep(1)
      setSelectedFile(null)
      setColumnMappings({})
    }, 2000)
  }

  return (
    <Transition.Root show={isOpen} as={Fragment}>
      <Dialog as="div" className="relative z-50" onClose={onClose}>
        <Transition.Child
          as={Fragment}
          enter="ease-out duration-300"
          enterFrom="opacity-0"
          enterTo="opacity-100"
          leave="ease-in duration-200"
          leaveFrom="opacity-100"
          leaveTo="opacity-0"
        >
          <div className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </Transition.Child>

        <div className="fixed inset-0 z-10 overflow-y-auto">
          <div className="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <Transition.Child
              as={Fragment}
              enter="ease-out duration-300"
              enterFrom="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enterTo="opacity-100 translate-y-0 sm:scale-100"
              leave="ease-in duration-200"
              leaveFrom="opacity-100 translate-y-0 sm:scale-100"
              leaveTo="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            >
              <Dialog.Panel className="relative transform overflow-hidden rounded-2xl bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-2xl sm:p-6">
                <div className="absolute right-0 top-0 pr-4 pt-4">
                  <button
                    type="button"
                    className="rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
                    onClick={onClose}
                  >
                    <span className="sr-only">Close</span>
                    <XMarkIcon className="h-6 w-6" aria-hidden="true" />
                  </button>
                </div>

                <div className="sm:flex sm:items-start">
                  <div className="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-primary-100 sm:mx-0 sm:h-10 sm:w-10">
                    <span className="text-2xl">📊</span>
                  </div>
                  <div className="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left w-full">
                    <Dialog.Title as="h3" className="text-lg font-semibold leading-6 text-gray-900 mb-4">
                      {step === 1 && 'Upload Your Data'}
                      {step === 2 && 'Map Your Columns'}
                      {step === 3 && 'Processing Data...'}
                    </Dialog.Title>

                    {/* Step 1: File Upload */}
                    {step === 1 && (
                      <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        className="space-y-4"
                      >
                        <p className="text-sm text-gray-500">
                          Choose the type of file you're uploading to help us process it correctly.
                        </p>
                        
                        <div className="space-y-3">
                          {fileTypes.map((fileType) => (
                            <button
                              key={fileType.id}
                              onClick={() => handleFileSelect({} as File)} // Mock file
                              className="w-full text-left p-4 border border-gray-200 rounded-lg hover:border-primary-300 hover:bg-primary-50 transition-colors"
                            >
                              <div className="flex items-center space-x-3">
                                <span className="text-2xl">{fileType.icon}</span>
                                <div>
                                  <p className="font-medium text-gray-900">{fileType.name}</p>
                                  <p className="text-sm text-gray-500">{fileType.description}</p>
                                </div>
                              </div>
                            </button>
                          ))}
                        </div>
                      </motion.div>
                    )}

                    {/* Step 2: Column Mapping */}
                    {step === 2 && (
                      <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        className="space-y-4"
                      >
                        <p className="text-sm text-gray-500">
                          Map your data columns to the correct field types for accurate analysis.
                        </p>
                        
                        <div className="space-y-4">
                          {columnTypes.map((columnType) => (
                            <div key={columnType.id} className="flex items-center justify-between">
                              <div className="flex items-center space-x-3">
                                <span className="text-xl">{columnType.icon}</span>
                                <div>
                                  <p className="font-medium text-gray-900">{columnType.name}</p>
                                  <p className="text-sm text-gray-500">{columnType.description}</p>
                                </div>
                              </div>
                              
                              <Listbox
                                value={columnMappings[columnType.id] || ''}
                                onChange={(value) => handleColumnMapping(columnType.id, value)}
                              >
                                <div className="relative w-48">
                                  <Listbox.Button className="relative w-full cursor-default rounded-lg bg-white py-2 pl-3 pr-10 text-left border border-gray-300 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500">
                                    <span className="block truncate">
                                      {columnMappings[columnType.id] || 'Select column...'}
                                    </span>
                                    <span className="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2">
                                      <ChevronUpDownIcon className="h-5 w-5 text-gray-400" aria-hidden="true" />
                                    </span>
                                  </Listbox.Button>
                                  <Transition
                                    as={Fragment}
                                    leave="transition ease-in duration-100"
                                    leaveFrom="opacity-100"
                                    leaveTo="opacity-0"
                                  >
                                    <Listbox.Options className="absolute z-10 mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm">
                                      {availableColumns.map((column) => (
                                        <Listbox.Option
                                          key={column}
                                          className={({ active }) =>
                                            `relative cursor-default select-none py-2 pl-10 pr-4 ${
                                              active ? 'bg-primary-100 text-primary-900' : 'text-gray-900'
                                            }`
                                          }
                                          value={column}
                                        >
                                          {({ selected }) => (
                                            <>
                                              <span className={`block truncate ${selected ? 'font-medium' : 'font-normal'}`}>
                                                {column}
                                              </span>
                                              {selected ? (
                                                <span className="absolute inset-y-0 left-0 flex items-center pl-3 text-primary-600">
                                                  <CheckIcon className="h-5 w-5" aria-hidden="true" />
                                                </span>
                                              ) : null}
                                            </>
                                          )}
                                        </Listbox.Option>
                                      ))}
                                    </Listbox.Options>
                                  </Transition>
                                </div>
                              </Listbox>
                            </div>
                          ))}
                        </div>
                        
                        <div className="mt-6 flex justify-end space-x-3">
                          <button
                            type="button"
                            className="button-secondary"
                            onClick={() => setStep(1)}
                          >
                            Back
                          </button>
                          <button
                            type="button"
                            className="button-primary"
                            onClick={handleProcess}
                          >
                            Process Data
                          </button>
                        </div>
                      </motion.div>
                    )}

                    {/* Step 3: Processing */}
                    {step === 3 && (
                      <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        className="text-center py-8"
                      >
                        <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-primary-600 mx-auto mb-4"></div>
                        <p className="text-lg font-medium text-gray-900 mb-2">
                          Processing your data...
                        </p>
                        <p className="text-sm text-gray-500">
                          This may take a few moments. We're analyzing your data and preparing insights.
                        </p>
                      </motion.div>
                    )}
                  </div>
                </div>
              </Dialog.Panel>
            </Transition.Child>
          </div>
        </div>
      </Dialog>
    </Transition.Root>
  )
}
