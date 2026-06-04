"""
M07: 视频合成模块 API 路由

覆盖功能: F10 视频合成
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_current_user, get_db
from app.models.user import User

router = APIRouter(tags=["compose"])


@router.post("/projects/{project_id}/compose")
async def create_composition(
    project_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """发起视频合成"""
    raise NotImplementedError("TODO: 实现视频合成逻辑")


@router.get("/compositions/{task_id}")
async def get_composition_status(
    task_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """查询合成任务状态"""
    raise NotImplementedError("TODO: 实现合成状态查询")


@router.get("/projects/{project_id}/compositions")
async def list_compositions(
    project_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """获取合成历史"""
    raise NotImplementedError("TODO: 实现合成历史查询")


@router.post("/compositions/{task_id}/cancel")
async def cancel_composition(
    task_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """取消合成任务"""
    raise NotImplementedError("TODO: 实现合成取消逻辑")
