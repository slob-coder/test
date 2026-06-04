"""
M10: 任务状态模块 API 路由

覆盖功能: 统一异步任务状态查询、SSE 进度推送
"""

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_current_user, get_db
from app.models.user import User

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("")
async def list_tasks(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """查询当前用户的所有异步任务"""
    raise NotImplementedError("TODO: 实现任务列表查询")


@router.get("/{task_id}")
async def get_task(
    task_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """查询单个任务详情"""
    raise NotImplementedError("TODO: 实现任务详情查询")


@router.get("/{task_id}/stream")
async def task_stream(
    task_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """SSE 实时推送任务进度"""
    raise NotImplementedError("TODO: 实现 SSE 推送逻辑")
