import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export const analyzeResume = async (file, jobDescription) => {
  const formData = new FormData()
  formData.append('resume', file)
  formData.append('job_description', jobDescription)

  const response = await axios.post(`${API_URL}/api/analyze`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
    timeout: 120000, // Increased to 120 seconds
  })

  return response.data
}