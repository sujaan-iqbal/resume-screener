import './RewritePanel.css'

export default function RewritePanel({ suggestions, summary, tips }) {
  return (
    <div className="rewrite-panel">
      <h3>✏️ AI Suggestions</h3>
      
      <div className="summary-section">
        <h4>Rewritten Summary</h4>
        <p>{summary}</p>
      </div>

      {suggestions.map((s, i) => (
        <div key={i} className="suggestion">
          <h4>{s.section}</h4>
          <div className="before-after">
            <div className="before">
              <span className="label">Before:</span>
              <p>{s.original || 'No original text provided'}</p>
            </div>
            <div className="after">
              <span className="label">After:</span>
              <p>{s.improved}</p>
            </div>
          </div>
          <p className="reason">💡 {s.reason}</p>
        </div>
      ))}

      <div className="tips">
        <h4>📋 ATS Tips</h4>
        <ul>
          {tips.map((tip, i) => (
            <li key={i}>{tip}</li>
          ))}
        </ul>
      </div>
    </div>
  )
}