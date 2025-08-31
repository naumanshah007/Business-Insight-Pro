import { Fragment } from 'react'
import { Dialog, Transition } from '@headlessui/react'
import { Link, useLocation } from 'react-router-dom'
import { motion } from 'framer-motion'
import {
  ChartBarIcon,
  HomeIcon,
  LightBulbIcon,
  DocumentChartBarIcon,
  Cog6ToothIcon,
  XMarkIcon,
  Bars3Icon,
} from '@heroicons/react/24/outline'
import { cn } from '@/lib/utils'

const navigation = [
  { name: 'Dashboard', href: '/', icon: HomeIcon },
  { name: 'Analytics', href: '/analytics', icon: ChartBarIcon },
  { name: 'AI Insights', href: '/insights', icon: LightBulbIcon },
  { name: 'Reports', href: '/reports', icon: DocumentChartBarIcon },
  { name: 'Settings', href: '/settings', icon: Cog6ToothIcon },
]

interface SidebarProps {
  open: boolean
  setOpen: (open: boolean) => void
}

export default function Sidebar({ open, setOpen }: SidebarProps) {
  const location = useLocation()

  return (
    <>
      {/* Mobile sidebar */}
      <Transition.Root show={open} as={Fragment}>
        <Dialog as="div" className="relative z-50 lg:hidden" onClose={setOpen}>
          <Transition.Child
            as={Fragment}
            enter="transition-opacity ease-linear duration-300"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="transition-opacity ease-linear duration-300"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <div className="fixed inset-0 bg-gray-900/80" />
          </Transition.Child>

          <div className="fixed inset-0 flex">
            <Transition.Child
              as={Fragment}
              enter="transition ease-in-out duration-300 transform"
              enterFrom="-translate-x-full"
              enterTo="translate-x-0"
              leave="transition ease-in-out duration-300 transform"
              leaveFrom="translate-x-0"
              leaveTo="-translate-x-full"
            >
              <Dialog.Panel className="relative mr-16 flex w-full max-w-xs flex-1">
                <div className="flex grow flex-col gap-y-5 overflow-y-auto bg-white px-6 pb-4">
                  <div className="flex h-16 shrink-0 items-center">
                    <motion.div
                      initial={{ scale: 0.8 }}
                      animate={{ scale: 1 }}
                      className="flex items-center space-x-2"
                    >
                      <div className="h-8 w-8 rounded-lg gradient-bg flex items-center justify-center">
                        <span className="text-white font-bold text-lg">📊</span>
                      </div>
                      <span className="text-xl font-bold text-gradient">OmniInsights</span>
                    </motion.div>
                  </div>
                  <nav className="flex flex-1 flex-col">
                    <ul role="list" className="flex flex-1 flex-col gap-y-7">
                      <li>
                        <ul role="list" className="-mx-2 space-y-1">
                          {navigation.map((item) => (
                            <li key={item.name}>
                              <Link
                                to={item.href}
                                onClick={() => setOpen(false)}
                                className={cn(
                                  'group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold transition-all duration-200',
                                  location.pathname === item.href
                                    ? 'bg-primary-50 text-primary-700'
                                    : 'text-secondary-700 hover:text-primary-600 hover:bg-primary-50'
                                )}
                              >
                                <item.icon
                                  className={cn(
                                    'h-6 w-6 shrink-0 transition-colors duration-200',
                                    location.pathname === item.href
                                      ? 'text-primary-600'
                                      : 'text-secondary-400 group-hover:text-primary-600'
                                  )}
                                  aria-hidden="true"
                                />
                                {item.name}
                              </Link>
                            </li>
                          ))}
                        </ul>
                      </li>
                    </ul>
                  </nav>
                </div>
              </Dialog.Panel>
            </Transition.Child>
          </div>
        </Dialog>
      </Transition.Root>

      {/* Desktop sidebar */}
      <div className="hidden lg:fixed lg:inset-y-0 lg:z-50 lg:flex lg:w-72 lg:flex-col">
        <div className="flex grow flex-col gap-y-5 overflow-y-auto border-r border-secondary-200 bg-white px-6 pb-4">
          <div className="flex h-16 shrink-0 items-center">
            <motion.div
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ delay: 0.1 }}
              className="flex items-center space-x-2"
            >
              <div className="h-10 w-10 rounded-xl gradient-bg flex items-center justify-center shadow-glow">
                <span className="text-white font-bold text-xl">📊</span>
              </div>
              <span className="text-2xl font-bold text-gradient">OmniInsights</span>
            </motion.div>
          </div>
          <nav className="flex flex-1 flex-col">
            <ul role="list" className="flex flex-1 flex-col gap-y-7">
              <li>
                <ul role="list" className="-mx-2 space-y-1">
                  {navigation.map((item, index) => (
                    <motion.li
                      key={item.name}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: index * 0.1 }}
                    >
                      <Link
                        to={item.href}
                        className={cn(
                          'group flex gap-x-3 rounded-xl p-3 text-sm leading-6 font-semibold transition-all duration-200',
                          location.pathname === item.href
                            ? 'bg-primary-50 text-primary-700 shadow-soft'
                            : 'text-secondary-700 hover:text-primary-600 hover:bg-primary-50'
                        )}
                      >
                        <item.icon
                          className={cn(
                            'h-6 w-6 shrink-0 transition-colors duration-200',
                            location.pathname === item.href
                              ? 'text-primary-600'
                              : 'text-secondary-400 group-hover:text-primary-600'
                          )}
                          aria-hidden="true"
                        />
                        {item.name}
                      </Link>
                    </motion.li>
                  ))}
                </ul>
              </li>
              <li className="mt-auto">
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.5 }}
                  className="rounded-xl bg-gradient-to-r from-primary-50 to-accent-50 p-4 border border-primary-100"
                >
                  <div className="text-sm font-medium text-primary-700">
                    🚀 Pro Features
                  </div>
                  <p className="text-xs text-primary-600 mt-1">
                    Unlock advanced analytics and AI insights
                  </p>
                </motion.div>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </>
  )
}
