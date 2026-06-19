import os
import json
import random
from dotenv import load_dotenv

# Try to import the new genai package
try:
    from google import genai
    GENAI_AVAILABLE = True
    print("✅ Using google.genai (new package)")
except ImportError:
    try:
        # Fallback to deprecated package
        import google.generativeai as genai_old
        GENAI_AVAILABLE = False
        print("⚠️ Using deprecated google.generativeai package")
    except ImportError:
        GENAI_AVAILABLE = False
        print("⚠️ No Gemini package installed. Using mock responses.")

load_dotenv()

class GeminiClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.use_mock = not self.api_key
        
        # Available models that work:
        # - gemini-1.5-pro (most capable)
        # - gemini-1.5-flash (fast, good for most tasks)
        # - gemini-1.0-pro (older but reliable)
        self.model_name = "gemini-3.1-flash-lite"  # Using a confirmed working model
        
        if not self.use_mock and GENAI_AVAILABLE:
            try:
                # Initialize the new client
                self.client = genai.Client(api_key=self.api_key)
                self.use_mock = False
                print(f"✅ Gemini API initialized with model: {self.model_name}")
            except Exception as e:
                print(f"⚠️ Error initializing Gemini: {e}")
                self.use_mock = True
        elif not self.use_mock and not GENAI_AVAILABLE:
            # Try deprecated package
            try:
                genai_old.configure(api_key=self.api_key)
                self.model = genai_old.GenerativeModel(self.model_name)
                self.use_mock = False
                print(f"✅ Gemini API initialized (deprecated) with model: {self.model_name}")
            except Exception as e:
                print(f"⚠️ Error initializing Gemini: {e}")
                self.use_mock = True
        else:
            print("⚠️ No Gemini API key found. Using mock responses.")
    
    def call_ai(self, prompt, simple=False):
        """Call Gemini API or return mock response"""
        if self.use_mock:
            print("🔄 Using mock response (fallback)")
            return self._mock_response()
        
        try:
            if GENAI_AVAILABLE:
                # New API
                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=prompt,
                )
                content = response.text
            else:
                # Deprecated API
                response = self.model.generate_content(prompt)
                content = response.text
            
            if simple:
                return content
            
            # Extract JSON from response
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            if json_start != -1 and json_end > json_start:
                content = content[json_start:json_end]
                return json.loads(content)
            
            print("⚠️ No JSON found in response, using mock")
            return self._mock_response()
            
        except Exception as e:
            print(f"❌ Gemini API Error: {e}")
            print("🔄 Falling back to mock response")
            return self._mock_response()
    
    def _mock_response(self):
        """Fallback mock responses"""
        suggestions = [
            {
                "section": "Experience",
                "original": "Worked on development projects",
                "improved": "Led development of key features using modern technologies",
                "reason": "Missing action verbs and specific technologies"
            },
            {
                "section": "Skills",
                "original": "Programming, Databases",
                "improved": "Python, JavaScript, SQL, MongoDB, AWS, Docker",
                "reason": "Need specific technologies instead of generic terms"
            },
            {
                "section": "Projects",
                "original": "Built a web application",
                "improved": "Developed a full-stack e-commerce platform with React and Node.js",
                "reason": "Add technologies used and impact metrics"
            }
        ]
        
        summaries = [
            "Highly motivated professional with strong technical skills and proven ability to deliver results.",
            "Results-driven developer with expertise in full-stack development and cloud technologies.",
            "Innovative software engineer with passion for building scalable applications."
        ]
        
        tips = [
            "Use keywords from the job description",
            "Quantify your achievements with numbers",
            "Use action verbs (led, developed, created, improved)",
            "Keep formatting simple (no tables or graphics)",
            "Remove personal pronouns (I, my) from your resume"
        ]
        
        return {
            "suggestions": random.sample(suggestions, min(2, len(suggestions))),
            "rewritten_summary": random.choice(summaries),
            "ats_tips": random.sample(tips, 4)
        }

# Create singleton instance
ai_client = GeminiClient()

# Export function
def call_ai(prompt, simple=False):
    """Main function to call AI"""
    return ai_client.call_ai(prompt, simple)