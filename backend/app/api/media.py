"""
M05: 媒体生成模块 API 路由

覆盖功能: F06 AI生成分镜图片, F07 AI生成分镜视频片段
"""

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_current_user, get_db
from app.models.user import User

router = APIRouter(prefix="/media", tags=["media"])


@router.post("/generate-image")
async def generate_image(
    # TODO: 实现单个分镜图片生成
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """生成单个分镜图片"""
    raise NotImplementedError("TODO: 实现图片生成逻辑")


@router.post("/generate-images")
async def generate_images(
    # TODO: 实现批量生成图片
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """批量生成图片"""
    raise NotImplementedError("TODO: 实现批量图片生成逻辑")


@router.post("/generate-video")
async def generate_video(
    # TODO: 实现单个视频片段生成
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """生成单个视频片段"""
    raise NotImplementedError("TODO: 实现视频生成逻辑")


@router.post("/generate-videos")
async def generate_videos(
    # TODO: 实现批量生成视频
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """批量生成视频"""
    raise NotImplementedError("TODO: 实现批量视频生成逻辑")


@router.post("/storyboard-items/{item_id}/upload-image")
async def upload_image(
    item_id: str,
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """上传替换图片"""
    raise NotImplementedError("TODO: 实现图片上传逻辑")


@router.get("/{media_id}")
async def get_media(
    media_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """获取媒体文件信息"""
    raise NotImplementedError("TODO: 实现媒体信息查询")
