import { useState } from 'react'
import UploadZone from './components/UploadZone'
import JobDescInput from './components/JobDescInput'
import ScoreCard from './components/ScoreCard'
import KeywordDiff from './components/KeywordDiff'
import RewritePanel from './components/RewritePanel'
import Loader from './components/Loader'
import { analyzeResume } from './services/api'
import './App.css'

function App() {
  const [file, setFile] = useState(null)
  const [jobDescription, setJobDescription] = useState('')
  const [loading, setLoading] = useState(false)
  const [results, setResults] = useState(null)
  const [error, setError] = useState('')

  const handleAnalyze = async () => {
    if (!file || !jobDescription) {
      setError('Please upload a resume and enter job description')
      return
    }

    setLoading(true)
    setError('')
    setResults(null)

    try {
      const data = await analyzeResume(file, jobDescription)
      setResults(data)
    } catch (err) {
      setError(err.message || 'Analysis failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <header className="header">
        <h1>Resume Screener</h1>
      </header>

      <main className="main">
        {!results ? (
          <div className="upload-section">
            <UploadZone onFileSelect={setFile} />
            <JobDescInput value={jobDescription} onChange={setJobDescription} />
            {error && <div className="error">{error}</div>}
            <button 
              className="analyze-btn" 
              onClick={handleAnalyze}
              disabled={loading}
            >
              {loading ? 'Analyzing...' : 'Analyze Resume'}
            </button>
            {loading && <Loader />}
          </div>
        ) : (
          <div className="results-section">
            <ScoreCard score={results.score} />
            <KeywordDiff 
              present={results.present_keywords} 
              missing={results.missing_keywords} 
            />
            <RewritePanel 
              suggestions={results.suggestions}
              summary={results.rewritten_summary}
              tips={results.ats_tips}
            />
            <button className="back-btn" onClick={() => setResults(null)}>
              ← New Analysis
            </button>
          </div>
        )}
      </main>
    </div>
  )
}

export default App