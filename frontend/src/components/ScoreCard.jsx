import './ScoreCard.css'

export default function ScoreCard({ score }) {
  const color = score >= 70 ? '#22c55e' : score >= 50 ? '#eab308' : '#ef4444'
  
  return (
    <div className="score-card">
      <div className="score-circle" style={{ borderColor: color }}>
        <span className="score-number">{score}</span>
        <span className="score-label">Match Score</span>
      </div>
    </div>
  )
}