from io import BytesIO
from pdfminer.high_level import extract_text
from docx import Document
from fastapi import UploadFile

def parse_file(file: UploadFile) -> str:
    content = file.file.read()
    
    if file.filename.endswith('.pdf'):
        return extract_text(BytesIO(content))
    elif file.filename.endswith('.docx'):
        doc = Document(BytesIO(content))
        return '\n'.join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file type. Use PDF or DOCX.")