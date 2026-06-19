from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.file_parser import parse_file
from app.services.keyword_matcher import match_keywords
from app.services.score_engine import calculate_score
from app.services.ai_client import call_ai
from app.services.prompt_builder import build_prompt
import time

router = APIRouter()

@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        start_time = time.time()
        
        # 1. Extract text from file
        resume_text = parse_file(resume)
        
        # 2. Keyword analysis
        keywords = match_keywords(resume_text, job_description)
        
        # 3. Calculate score
        score = calculate_score(keywords)
        
        # 4. Build prompt
        prompt = build_prompt(resume_text, job_description, keywords)
        
        # 5. Call Gemini
        ai_response = call_ai(prompt)
        
        processing_time = time.time() - start_time
        
        return {
            "score": score,
            "present_keywords": keywords["present"],
            "missing_keywords": keywords["missing"],
            "suggestions": ai_response.get("suggestions", []),
            "rewritten_summary": ai_response.get("rewritten_summary", "Professional summary"),
            "ats_tips": ai_response.get("ats_tips", []),
            "processing_time_ms": round(processing_time * 1000, 2)
        }
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))