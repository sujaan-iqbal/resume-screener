import ScoreCard from '../components/ScoreCard'
import KeywordDiff from '../components/KeywordDiff'
import RewritePanel from '../components/RewritePanel'

export default function Results({ results, onBack }) {
  return (
    <div className="results">
      <ScoreCard score={results.score} />
      
      <div className="section">
        <h3>Keyword Analysis</h3>
        <KeywordDiff 
          present={results.present_keywords} 
          missing={results.missing_keywords} 
        />
      </div>
      
      <div className="section">
        <h3>AI Suggestions</h3>
        <RewritePanel 
          suggestions={results.suggestions}
          summary={results.rewritten_summary}
          tips={results.ats_tips}
        />
      </div>
      
      <button className="back-btn" onClick={onBack}>
        ← New Analysis
      </button>
    </div>
  )
}