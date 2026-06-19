import './JobDescInput.css'

export default function JobDescInput({ value, onChange }) {
  return (
    <div className="jd-input">
      <label>Job Description</label>
      <textarea
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Paste the job description here..."
        rows={6}
      />
    </div>
  )
}