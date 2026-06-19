from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_client import call_ai

router = APIRouter()

class RewriteRequest(BaseModel):
    section_text: str
    context: str

@router.post("/rewrite")
async def rewrite_section(request: RewriteRequest):
    try:
        prompt = f"""
        Rewrite this section to be more ATS-friendly and impactful.
        Context: {request.context}
        Original: {request.section_text}
        Return only the improved text.
        """
        response = call_ai(prompt, simple=True)
        return {"improved_text": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))