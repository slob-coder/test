"""
M09: 导出分享模块 API 路由

覆盖功能: F12 导出分享
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_current_user, get_db
from app.models.user import User

router = APIRouter(tags=["share"])


@router.post("/compositions/{composition_id}/export")
async def export_video(
    composition_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """导出视频"""
    raise NotImplementedError("TODO: 实现视频导出逻辑")


@router.post("/compositions/{composition_id}/share")
async def create_share_link(
    composition_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """生成分享链接"""
    raise NotImplementedError("TODO: 实现分享链接生成")


@router.get("/share/{token}")
async def access_shared_video(
    token: str,
    db: AsyncSession = Depends(get_db),
):
    """访问分享视频（无需登录）"""
    raise NotImplementedError("TODO: 实现分享视频访问")
