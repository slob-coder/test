"""
M06: 字幕生成模块 API 路由

覆盖功能: F09 字幕生成
"""

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_current_user, get_db
from app.models.user import User

router = APIRouter(tags=["subtitles"])


@router.post("/projects/{project_id}/subtitles/generate")
async def generate_subtitles(
    project_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """自动生成字幕"""
    raise NotImplementedError("TODO: 实现字幕生成逻辑")


@router.get("/projects/{project_id}/subtitles")
async def list_subtitles(
    project_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """获取字幕列表"""
    raise NotImplementedError("TODO: 实现字幕列表查询")


@router.put("/subtitles/{subtitle_id}")
async def update_subtitle(
    subtitle_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """更新字幕条目"""
    raise NotImplementedError("TODO: 实现字幕更新逻辑")


@router.get("/projects/{project_id}/subtitles/export")
async def export_subtitles(
    project_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """导出 SRT 文件"""
    raise NotImplementedError("TODO: 实现字幕导出逻辑")


@router.delete("/projects/{project_id}/subtitles")
async def delete_subtitles(
    project_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """删除项目全部字幕"""
    raise NotImplementedError("TODO: 实现字幕删除逻辑")
