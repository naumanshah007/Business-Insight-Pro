import { motion } from 'framer-motion'
import { useState } from 'react'
import { 
  Cog6ToothIcon, 
  UserIcon,
  BellIcon,
  ShieldCheckIcon,
  PaintBrushIcon,
  GlobeAltIcon
} from '@heroicons/react/24/outline'

const settingsSections = [
  {
    id: 'profile',
    name: 'Profile Settings',
    description: 'Manage your account information and preferences',
    icon: UserIcon,
    color: 'primary'
  },
  {
    id: 'notifications',
    name: 'Notifications',
    description: 'Configure how and when you receive notifications',
    icon: BellIcon,
    color: 'accent'
  },
  {
    id: 'security',
    name: 'Security & Privacy',
    description: 'Manage your security settings and data privacy',
    icon: ShieldCheckIcon,
    color: 'success'
  },
  {
    id: 'appearance',
    name: 'Appearance',
    description: 'Customize the look and feel of the application',
    icon: PaintBrushIcon,
    color: 'warning'
  },
  {
    id: 'regional',
    name: 'Regional Settings',
    description: 'Set your timezone, language, and currency preferences',
    icon: GlobeAltIcon,
    color: 'secondary'
  }
]

export default function Settings() {
  const [activeSection, setActiveSection] = useState('profile')
  const [notifications, setNotifications] = useState({
    email: true,
    push: false,
    sms: false,
    weekly: true,
    monthly: true
  })

  const [appearance, setAppearance] = useState({
    theme: 'light',
    fontSize: 'medium',
    compactMode: false
  })

  return (
    <div className="space-y-8">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <div className="flex items-center justify-center space-x-3 mb-4">
          <div className="w-12 h-12 bg-gradient-to-r from-secondary-500 to-primary-500 rounded-xl flex items-center justify-center">
            <Cog6ToothIcon className="h-6 w-6 text-white" />
          </div>
          <h1 className="text-4xl font-bold text-gradient">Settings</h1>
        </div>
        <p className="text-xl text-secondary-600 max-w-3xl mx-auto">
          Customize your experience and manage your account preferences
        </p>
      </motion.div>

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
        {/* Settings Navigation */}
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.1 }}
          className="lg:col-span-1"
        >
          <div className="bg-white rounded-2xl p-6 shadow-soft border border-secondary-200">
            <h2 className="text-lg font-semibold text-secondary-900 mb-4">Settings</h2>
            
            <nav className="space-y-2">
              {settingsSections.map((section) => (
                <button
                  key={section.id}
                  onClick={() => setActiveSection(section.id)}
                  className={`w-full text-left p-3 rounded-xl transition-all duration-200 ${
                    activeSection === section.id
                      ? 'bg-primary-50 text-primary-700 border border-primary-200'
                      : 'text-secondary-600 hover:text-secondary-900 hover:bg-secondary-50'
                  }`}
                >
                  <div className="flex items-center space-x-3">
                    <div className={`w-8 h-8 bg-${section.color}-100 rounded-lg flex items-center justify-center`}>
                      <section.icon className={`h-4 w-4 text-${section.color}-600`} />
                    </div>
                    <div>
                      <p className="font-medium">{section.name}</p>
                      <p className="text-xs text-secondary-500">{section.description}</p>
                    </div>
                  </div>
                </button>
              ))}
            </nav>
          </div>
        </motion.div>

        {/* Settings Content */}
        <motion.div
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.2 }}
          className="lg:col-span-3"
        >
          <div className="bg-white rounded-2xl p-6 shadow-soft border border-secondary-200">
            {/* Profile Settings */}
            {activeSection === 'profile' && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="space-y-6"
              >
                <h2 className="text-2xl font-semibold text-secondary-900">Profile Settings</h2>
                
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-secondary-700 mb-2">
                      First Name
                    </label>
                    <input
                      type="text"
                      defaultValue="John"
                      className="input-field"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-secondary-700 mb-2">
                      Last Name
                    </label>
                    <input
                      type="text"
                      defaultValue="Doe"
                      className="input-field"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-secondary-700 mb-2">
                      Email
                    </label>
                    <input
                      type="email"
                      defaultValue="john.doe@company.com"
                      className="input-field"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-secondary-700 mb-2">
                      Company
                    </label>
                    <input
                      type="text"
                      defaultValue="Acme Corp"
                      className="input-field"
                    />
                  </div>
                </div>
                
                <div className="pt-4 border-t border-secondary-200">
                  <button className="button-primary">
                    Save Changes
                  </button>
                </div>
              </motion.div>
            )}

            {/* Notifications Settings */}
            {activeSection === 'notifications' && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="space-y-6"
              >
                <h2 className="text-2xl font-semibold text-secondary-900">Notification Preferences</h2>
                
                <div className="space-y-4">
                  <div className="flex items-center justify-between p-4 border border-secondary-200 rounded-xl">
                    <div>
                      <h3 className="font-medium text-secondary-900">Email Notifications</h3>
                      <p className="text-sm text-secondary-600">Receive notifications via email</p>
                    </div>
                    <label className="relative inline-flex items-center cursor-pointer">
                      <input
                        type="checkbox"
                        checked={notifications.email}
                        onChange={(e) => setNotifications({...notifications, email: e.target.checked})}
                        className="sr-only peer"
                      />
                      <div className="w-11 h-6 bg-secondary-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-secondary-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
                    </label>
                  </div>
                  
                  <div className="flex items-center justify-between p-4 border border-secondary-200 rounded-xl">
                    <div>
                      <h3 className="font-medium text-secondary-900">Push Notifications</h3>
                      <p className="text-sm text-secondary-600">Receive push notifications in browser</p>
                    </div>
                    <label className="relative inline-flex items-center cursor-pointer">
                      <input
                        type="checkbox"
                        checked={notifications.push}
                        onChange={(e) => setNotifications({...notifications, push: e.target.checked})}
                        className="sr-only peer"
                      />
                      <div className="w-11 h-6 bg-secondary-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-secondary-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
                    </label>
                  </div>
                  
                  <div className="flex items-center justify-between p-4 border border-secondary-200 rounded-xl">
                    <div>
                      <h3 className="font-medium text-secondary-900">Weekly Summary</h3>
                      <p className="text-sm text-secondary-600">Receive weekly performance summaries</p>
                    </div>
                    <label className="relative inline-flex items-center cursor-pointer">
                      <input
                        type="checkbox"
                        checked={notifications.weekly}
                        onChange={(e) => setNotifications({...notifications, weekly: e.target.checked})}
                        className="sr-only peer"
                      />
                      <div className="w-11 h-6 bg-secondary-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-secondary-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
                    </label>
                  </div>
                </div>
              </motion.div>
            )}

            {/* Appearance Settings */}
            {activeSection === 'appearance' && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="space-y-6"
              >
                <h2 className="text-2xl font-semibold text-secondary-900">Appearance Settings</h2>
                
                <div className="space-y-6">
                  <div>
                    <label className="block text-sm font-medium text-secondary-700 mb-2">
                      Theme
                    </label>
                    <select
                      value={appearance.theme}
                      onChange={(e) => setAppearance({...appearance, theme: e.target.value})}
                      className="input-field"
                    >
                      <option value="light">Light</option>
                      <option value="dark">Dark</option>
                      <option value="auto">Auto (System)</option>
                    </select>
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-secondary-700 mb-2">
                      Font Size
                    </label>
                    <select
                      value={appearance.fontSize}
                      onChange={(e) => setAppearance({...appearance, fontSize: e.target.value})}
                      className="input-field"
                    >
                      <option value="small">Small</option>
                      <option value="medium">Medium</option>
                      <option value="large">Large</option>
                    </select>
                  </div>
                  
                  <div className="flex items-center justify-between p-4 border border-secondary-200 rounded-xl">
                    <div>
                      <h3 className="font-medium text-secondary-900">Compact Mode</h3>
                      <p className="text-sm text-secondary-600">Reduce spacing for more content on screen</p>
                    </div>
                    <label className="relative inline-flex items-center cursor-pointer">
                      <input
                        type="checkbox"
                        checked={appearance.compactMode}
                        onChange={(e) => setAppearance({...appearance, compactMode: e.target.checked})}
                        className="sr-only peer"
                      />
                      <div className="w-11 h-6 bg-secondary-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-secondary-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
                    </label>
                  </div>
                </div>
              </motion.div>
            )}

            {/* Security Settings */}
            {activeSection === 'security' && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="space-y-6"
              >
                <h2 className="text-2xl font-semibold text-secondary-900">Security & Privacy</h2>
                
                <div className="space-y-4">
                  <div className="p-4 border border-secondary-200 rounded-xl">
                    <h3 className="font-medium text-secondary-900 mb-2">Change Password</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      <input
                        type="password"
                        placeholder="Current Password"
                        className="input-field"
                      />
                      <input
                        type="password"
                        placeholder="New Password"
                        className="input-field"
                      />
                    </div>
                    <button className="button-secondary mt-4">
                      Update Password
                    </button>
                  </div>
                  
                  <div className="p-4 border border-secondary-200 rounded-xl">
                    <h3 className="font-medium text-secondary-900 mb-2">Two-Factor Authentication</h3>
                    <p className="text-sm text-secondary-600 mb-4">Add an extra layer of security to your account</p>
                    <button className="button-primary">
                      Enable 2FA
                    </button>
                  </div>
                </div>
              </motion.div>
            )}

            {/* Regional Settings */}
            {activeSection === 'regional' && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="space-y-6"
              >
                <h2 className="text-2xl font-semibold text-secondary-900">Regional Settings</h2>
                
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-secondary-700 mb-2">
                      Timezone
                    </label>
                    <select className="input-field">
                      <option value="utc">UTC</option>
                      <option value="est">Eastern Time</option>
                      <option value="pst">Pacific Time</option>
                      <option value="gmt">GMT</option>
                    </select>
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-secondary-700 mb-2">
                      Language
                    </label>
                    <select className="input-field">
                      <option value="en">English</option>
                      <option value="es">Spanish</option>
                      <option value="fr">French</option>
                      <option value="de">German</option>
                    </select>
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-secondary-700 mb-2">
                      Currency
                    </label>
                    <select className="input-field">
                      <option value="usd">USD ($)</option>
                      <option value="eur">EUR (€)</option>
                      <option value="gbp">GBP (£)</option>
                      <option value="jpy">JPY (¥)</option>
                    </select>
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-secondary-700 mb-2">
                      Date Format
                    </label>
                    <select className="input-field">
                      <option value="mm/dd/yyyy">MM/DD/YYYY</option>
                      <option value="dd/mm/yyyy">DD/MM/YYYY</option>
                      <option value="yyyy-mm-dd">YYYY-MM-DD</option>
                    </select>
                  </div>
                </div>
                
                <div className="pt-4 border-t border-secondary-200">
                  <button className="button-primary">
                    Save Preferences
                  </button>
                </div>
              </motion.div>
            )}
          </div>
        </motion.div>
      </div>
    </div>
  )
}
