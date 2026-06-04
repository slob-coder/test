"""
M08: 历史记录模块 API 路由

覆盖功能: F11 历史记录
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_current_user, get_db
from app.models.user import User

router = APIRouter(tags=["history"])


@router.get("/projects/{project_id}/histories")
async def list_histories(
    project_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """获取项目历史记录"""
    raise NotImplementedError("TODO: 实现历史记录列表查询")


@router.get("/histories/{history_id}")
async def get_history(
    history_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """获取历史详情"""
    raise NotImplementedError("TODO: 实现历史详情查询")
