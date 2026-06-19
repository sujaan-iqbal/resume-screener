import os
import shutil
import tempfile
from pathlib import Path
from typing import Optional
from fastapi import UploadFile
import uuid
import time

class FileUtils:
    def __init__(self, base_dir: str = None):
        self.base_dir = base_dir or tempfile.gettempdir()
        self.upload_dir = Path(self.base_dir) / "resume_uploads"
        self.upload_dir.mkdir(exist_ok=True)
    
    def save_temp_file(self, file: UploadFile) -> str:
        """Save uploaded file to temp location and return path"""
        unique_id = str(uuid.uuid4())[:8]
        timestamp = int(time.time())
        ext = Path(file.filename).suffix
        file_path = self.upload_dir / f"{timestamp}_{unique_id}{ext}"
        
        with open(file_path, "wb") as f:
            content = file.file.read()
            f.write(content)
            file.file.seek(0)  # Reset for later reading
            
        return str(file_path)
    
    def delete_temp_file(self, file_path: str) -> bool:
        """Delete temp file"""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
        except Exception:
            pass
        return False
    
    def cleanup_old_files(self, max_age_hours: int = 24):
        """Delete files older than max_age_hours"""
        current_time = time.time()
        for file_path in self.upload_dir.glob("*"):
            if current_time - file_path.stat().st_mtime > max_age_hours * 3600:
                try:
                    file_path.unlink()
                except Exception:
                    pass
    
    def get_file_size(self, file_path: str) -> int:
        """Get file size in bytes"""
        try:
            return os.path.getsize(file_path)
        except Exception:
            return 0
    
    def get_temp_dir(self) -> str:
        """Get temp directory path"""
        return str(self.upload_dir)

# Singleton instance
file_utils = FileUtils()