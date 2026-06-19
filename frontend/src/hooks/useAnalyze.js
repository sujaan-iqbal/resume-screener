import { useState } from 'react'
import { analyzeResume } from '../services/api'

export function useAnalyze() {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [results, setResults] = useState(null)

  const analyze = async (file, jobDescription) => {
    setLoading(true)
    setError(null)
    
    try {
      const data = await analyzeResume(file, jobDescription)
      setResults(data)
      return data
    } catch (err) {
      let message = 'Analysis failed'
      if (err.code === 'ECONNABORTED') {
        message = 'Request timed out. The server might be processing slowly.'
      } else if (err.response?.data?.detail) {
        message = err.response.data.detail
      } else if (err.message) {
        message = err.message
      }
      setError(message)
      throw new Error(message)
    } finally {
      setLoading(false)
    }
  }

  const reset = () => {
    setResults(null)
    setError(null)
    setLoading(false)
  }

  return {
    loading,
    error,
    results,
    analyze,
    reset
  }
}