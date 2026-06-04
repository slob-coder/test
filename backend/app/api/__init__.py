"""
API 路由模块
"""

from fastapi import APIRouter

from app.api import auth, projects, scripts, storyboards, media, subtitles, compose, history, share, tasks

api_router = APIRouter()

# 注册各模块路由
api_router.include_router(auth.router, prefix="/auth", tags=["认证"])
api_router.include_router(projects.router, prefix="/projects", tags=["项目管理"])
api_router.include_router(scripts.router, prefix="/scripts", tags=["脚本生成"])
api_router.include_router(storyboards.router, tags=["分镜管理"])
api_router.include_router(media.router, prefix="/media", tags=["媒体生成"])
api_router.include_router(subtitles.router, tags=["字幕生成"])
api_router.include_router(compose.router, tags=["视频合成"])
api_router.include_router(history.router, tags=["历史记录"])
api_router.include_router(share.router, prefix="/share", tags=["导出分享"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["任务状态"])
