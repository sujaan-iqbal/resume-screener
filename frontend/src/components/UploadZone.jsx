import { useRef, useState } from 'react'
import './UploadZone.css'

export default function UploadZone({ onFileSelect }) {
  const [dragOver, setDragOver] = useState(false)
  const [fileName, setFileName] = useState('')
  const inputRef = useRef()

  const handleFile = (file) => {
    if (file && (file.type === 'application/pdf' || 
                 file.type === 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' ||
                 file.name.endsWith('.docx'))) {
      onFileSelect(file)
      setFileName(file.name)
    } else {
      alert('Please upload a PDF or DOCX file')
    }
  }

  const handleDrop = (e) => {
    e.preventDefault()
    setDragOver(false)
    const file = e.dataTransfer.files[0]
    handleFile(file)
  }

  const handleChange = (e) => {
    const file = e.target.files[0]
    handleFile(file)
  }

  return (
    <div 
      className={`upload-zone ${dragOver ? 'drag-over' : ''}`}
      onDragOver={(e) => { e.preventDefault(); setDragOver(true) }}
      onDragLeave={() => setDragOver(false)}
      onDrop={handleDrop}
      onClick={() => inputRef.current.click()}
    >
      <input 
        ref={inputRef}
        type="file"
        accept=".pdf,.docx"
        onChange={handleChange}
        style={{ display: 'none' }}
      />
      {fileName ? (
        <p>📄 {fileName}</p>
      ) : (
        <>
          <p>📤 Drop your resume here</p>
          <p className="sub">or click to browse (PDF or DOCX)</p>
        </>
      )}
    </div>
  )
}