import re
import unicodedata
from typing import List, Optional

class TextCleaner:
    def __init__(self):
        self.boilerplate_patterns = [
            r'(?i)phone:?\s*[\d\+\-\(\)\s]{10,}',
            r'(?i)email:?\s*[\w\.]+@[\w\.]+',
            r'(?i)linkedin\.com/in/[\w\-]+',
            r'(?i)github\.com/[\w\-]+',
            r'(?i)portfolio:?\s*[\w\.\-]+',
            r'(?i)address:?\s*[\w\s,\.]+',
        ]
        self.personal_info_patterns = [
            r'(?i)\b[\w\.]+@[\w\.]+\b',  # email
            r'(?i)\b[\d\+\-\(\)\s]{10,}\b',  # phone
            r'(?i)\blinkedin\.com/in/[\w\-]+\b',
        ]
    
    def clean_text(self, text: str) -> str:
        """Clean text by removing extra whitespace and normalizing"""
        # Unicode normalization
        text = unicodedata.normalize('NFKD', text)
        text = text.encode('ascii', 'ignore').decode('ascii')
        
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\n\s*\n', '\n\n', text)
        
        # Remove boilerplate
        for pattern in self.boilerplate_patterns:
            text = re.sub(pattern, '', text)
        
        return text.strip()
    
    def remove_personal_info(self, text: str) -> str:
        """Remove personal information for privacy"""
        for pattern in self.personal_info_patterns:
            text = re.sub(pattern, '[REDACTED]', text)
        return text
    
    def extract_sections(self, text: str) -> dict:
        """Extract common resume sections"""
        sections = {}
        section_patterns = {
            'summary': r'(?i)(?:professional\s+)?summary',
            'experience': r'(?i)(?:professional\s+)?experience',
            'education': r'(?i)education',
            'skills': r'(?i)(?:technical\s+)?skills',
            'projects': r'(?i)projects?',
            'certifications': r'(?i)certifications?',
            'achievements': r'(?i)achievements?',
        }
        
        lines = text.split('\n')
        current_section = 'header'
        current_text = []
        
        for line in lines:
            is_section = False
            for section, pattern in section_patterns.items():
                if re.match(f'^{pattern}', line, re.IGNORECASE):
                    if current_text:
                        sections[current_section] = '\n'.join(current_text).strip()
                    current_section = section
                    current_text = []
                    is_section = True
                    break
            
            if not is_section:
                current_text.append(line)
        
        if current_text:
            sections[current_section] = '\n'.join(current_text).strip()
        
        return sections
    
    def normalize_keywords(self, keywords: List[str]) -> List[str]:
        """Normalize keywords (lowercase, remove special chars)"""
        normalized = []
        for kw in keywords:
            kw = kw.lower().strip()
            kw = re.sub(r'[^a-z0-9\s]', '', kw)
            if kw and len(kw) > 1:
                normalized.append(kw)
        return list(set(normalized))
    
    def count_words(self, text: str) -> int:
        """Count words in text"""
        words = re.findall(r'\b\w+\b', text)
        return len(words)
    
    def truncate_text(self, text: str, max_words: int = 3000) -> str:
        """Truncate text to max words while preserving sentences"""
        words = text.split()
        if len(words) <= max_words:
            return text
        
        # Try to truncate at sentence boundary
        truncated = ' '.join(words[:max_words])
        last_period = truncated.rfind('.')
        if last_period > len(truncated) * 0.7:
            return truncated[:last_period + 1]
        
        return truncated + '...'

# Singleton instance
text_cleaner = TextCleaner()