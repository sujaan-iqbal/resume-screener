from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import analyze, rewrite

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(analyze.router, prefix="/api")
app.include_router(rewrite.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/health")
async def health():
    return {"status": "ok"}