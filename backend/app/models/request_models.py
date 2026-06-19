from pydantic import BaseModel, Field
from typing import Optional

class AnalyzeRequest(BaseModel):
    resume_text: Optional[str] = Field(None, description="Resume text content")
    job_description: str = Field(..., description="Job description text")
    file_name: Optional[str] = Field(None, description="Original file name")

class RewriteRequest(BaseModel):
    section_text: str = Field(..., description="Text section to rewrite")
    context: str = Field(..., description="Context for rewriting")
    section_type: Optional[str] = Field("general", description="Type of section")

class HealthCheck(BaseModel):
    status: str = Field("ok", description="Service health status")
    version: Optional[str] = Field("1.0.0", description="API version")