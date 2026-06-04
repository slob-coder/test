"""
AI Video Generation Application - FastAPI Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.api import auth, projects, scripts, storyboards, media, subtitles, compose, history, share, tasks

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered video generation platform",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(projects.router, prefix="/api/v1/projects", tags=["projects"])
app.include_router(scripts.router, prefix="/api/v1/scripts", tags=["scripts"])
app.include_router(storyboards.router, prefix="/api/v1/storyboards", tags=["storyboards"])
app.include_router(media.router, prefix="/api/v1/media", tags=["media"])
app.include_router(subtitles.router, prefix="/api/v1/subtitles", tags=["subtitles"])
app.include_router(compose.router, prefix="/api/v1/compose", tags=["compose"])
app.include_router(history.router, prefix="/api/v1/history", tags=["history"])
app.include_router(share.router, prefix="/api/v1/share", tags=["share"])
app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["tasks"])


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "app": settings.APP_NAME}
