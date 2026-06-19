from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class KeywordAnalysis(BaseModel):
    present: List[str] = Field(..., description="Keywords found in resume")
    missing: List[str] = Field(..., description="Keywords missing from resume")
    total_keywords: int = Field(..., description="Total unique keywords")

class Suggestion(BaseModel):
    section: str = Field(..., description="Section being improved")
    original: str = Field(..., description="Original text")
    improved: str = Field(..., description="Improved text")
    reason: str = Field(..., description="Reason for improvement")

class AnalyzeResponse(BaseModel):
    score: int = Field(..., ge=0, le=100, description="Match score 0-100")
    present_keywords: List[str] = Field(..., description="Keywords found")
    missing_keywords: List[str] = Field(..., description="Keywords missing")
    suggestions: List[Suggestion] = Field(..., description="AI suggestions")
    rewritten_summary: str = Field(..., description="AI rewritten summary")
    ats_tips: List[str] = Field(..., description="ATS optimization tips")
    processing_time_ms: Optional[float] = Field(None, description="Processing time")

class RewriteResponse(BaseModel):
    improved_text: str = Field(..., description="Rewritten text")
    changes_made: Optional[List[str]] = Field(None, description="List of changes")
    word_count_diff: Optional[int] = Field(None, description="Word count change")

class ErrorResponse(BaseModel):
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Error details")
    status_code: int = Field(..., description="HTTP status code")