from sklearn.feature_extraction.text import TfidfVectorizer
import re
from collections import Counter

def extract_keywords(text):
    """Extract keywords from text using TF-IDF"""
    words = re.findall(r'\b[a-zA-Z]{2,}\b', text.lower())
    stopwords = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
        'by', 'from', 'up', 'about', 'into', 'through', 'during', 'including', 'without',
        'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'us', 'them',
        'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
        'should', 'may', 'might', 'must', 'am', 'is', 'are', 'was', 'were',
        'be', 'been', 'being', 'can', 'shall', 'ought'
    }
    return [w for w in words if w not in stopwords and len(w) > 2]

def match_keywords(resume_text, job_description):
    """Match keywords between resume and job description"""
    # Extract keywords from both texts
    jd_keywords = set(extract_keywords(job_description))
    resume_keywords = set(extract_keywords(resume_text))
    
    # Find present and missing keywords
    present = list(jd_keywords.intersection(resume_keywords))
    missing = list(jd_keywords - resume_keywords)
    
    # Sort by relevance (frequency in JD)
    jd_word_freq = Counter(extract_keywords(job_description))
    
    # Prioritize keywords that appear more in JD
    present.sort(key=lambda x: jd_word_freq.get(x, 0), reverse=True)
    missing.sort(key=lambda x: jd_word_freq.get(x, 0), reverse=True)
    
    return {
        "present": present[:20],
        "missing": missing[:20]
    }