import './KeywordDiff.css'

export default function KeywordDiff({ present, missing }) {
  return (
    <div className="keyword-diff">
      <div className="keyword-section">
        <h3>✅ Present Keywords ({present.length})</h3>
        <div className="keyword-chips">
          {present.map(kw => (
            <span key={kw} className="chip present">{kw}</span>
          ))}
        </div>
      </div>
      <div className="keyword-section">
        <h3>❌ Missing Keywords ({missing.length})</h3>
        <div className="keyword-chips">
          {missing.map(kw => (
            <span key={kw} className="chip missing">{kw}</span>
          ))}
        </div>
      </div>
    </div>
  )
}