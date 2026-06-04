"""
M03: 脚本生成模块 - API 路由
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.script import (
    GenerateScriptRequest, GenerateScriptResponse,
    SaveScriptRequest, SaveScriptResponse,
    GetScriptResponse
)

router = APIRouter()


@router.post("/{project_id}/generate", response_model=GenerateScriptResponse, status_code=status.HTTP_201_CREATED)
async def generate_script(project_id: str, request: GenerateScriptRequest, db: AsyncSession = Depends(get_db)):
    """AI 生成脚本"""
    # TODO: 实现 AI 生成脚本逻辑
    raise NotImplementedError("AI 生成脚本功能待实现")


@router.put("/{project_id}", response_model=SaveScriptResponse)
async def save_script(project_id: str, request: SaveScriptRequest, db: AsyncSession = Depends(get_db)):
    """保存脚本"""
    # TODO: 实现保存脚本逻辑
    raise NotImplementedError("保存脚本功能待实现")


@router.get("/{project_id}", response_model=GetScriptResponse)
async def get_script(project_id: str, db: AsyncSession = Depends(get_db)):
    """获取脚本"""
    # TODO: 实现获取脚本逻辑
    raise NotImplementedError("获取脚本功能待实现")
