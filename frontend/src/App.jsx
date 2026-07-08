import './App.css'
import Dashboard from './pages/Dashboard'

function App() {
  return (
    <div className="min-h-screen bg-gray-50 font-sans text-gray-900 p-6">
      <div className="max-w-7xl mx-auto h-[90vh]">
        <h1 className="text-2xl font-bold mb-6 text-gray-800">Log HCP Interaction</h1>
        <Dashboard />
      </div>
    </div>
  )
}

export default App
