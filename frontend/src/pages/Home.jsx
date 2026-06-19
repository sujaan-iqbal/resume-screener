import { useState } from 'react'
import UploadZone from '../components/UploadZone'
import JobDescInput from '../components/JobDescInput'
import Loader from '../components/Loader'

export default function Home({ onAnalyze, loading, error }) {
  const [file, setFile] = useState(null)
  const [jobDescription, setJobDescription] = useState('')

  const handleSubmit = () => {
    if (!file || !jobDescription) {
      alert('Please upload a resume and enter job description')
      return
    }
    onAnalyze(file, jobDescription)
  }

  return (
    <div className="home">
      <h2>Upload Resume & Job Description</h2>
      <UploadZone onFileSelect={setFile} />
      <JobDescInput value={jobDescription} onChange={setJobDescription} />
      {error && <div className="error">{error}</div>}
      <button 
        className="analyze-btn" 
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? 'Analyzing...' : 'Analyze Resume'}
      </button>
      {loading && <Loader />}
    </div>
  )
}