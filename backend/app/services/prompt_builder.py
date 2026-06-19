def build_prompt(resume_text, job_description, keyword_analysis):
    return f"""You are an ATS (Applicant Tracking System) expert and career coach.

RESUME:
{resume_text[:3000]}

JOB DESCRIPTION:
{job_description[:2000]}

KEYWORD ANALYSIS:
Present: {', '.join(keyword_analysis['present'][:10])}
Missing: {', '.join(keyword_analysis['missing'][:10])}

Return ONLY valid JSON with this exact structure:
{{
  "suggestions": [
    {{
      "section": "Experience",
      "original": "example original text",
      "improved": "example improved text",
      "reason": "why this change"
    }}
  ],
  "rewritten_summary": "Full professional summary incorporating missing keywords",
  "ats_tips": ["tip 1", "tip 2", "tip 3"]
}}

Important: Return ONLY the JSON, no other text."""