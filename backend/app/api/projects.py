"""
M02: 项目管理模块 - API 路由
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.project import (
    CreateProjectRequest, CreateProjectResponse,
    ListProjectsRequest, ListProjectsResponse,
    GetProjectResponse, UpdateProjectRequest,
    UpdateProjectResponse, DeleteProjectResponse
)

router = APIRouter()


@router.post("", response_model=CreateProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(request: CreateProjectRequest, db: AsyncSession = Depends(get_db)):
    """创建项目"""
    # TODO: 实现创建项目逻辑
    raise NotImplementedError("创建项目功能待实现")


@router.get("", response_model=ListProjectsResponse)
async def list_projects(request: ListProjectsRequest = Depends(), db: AsyncSession = Depends(get_db)):
    """获取项目列表"""
    # TODO: 实现获取项目列表逻辑
    raise NotImplementedError("获取项目列表功能待实现")


@router.get("/{project_id}", response_model=GetProjectResponse)
async def get_project(project_id: str, db: AsyncSession = Depends(get_db)):
    """获取项目详情"""
    # TODO: 实现获取项目详情逻辑
    raise NotImplementedError("获取项目详情功能待实现")


@router.put("/{project_id}", response_model=UpdateProjectResponse)
async def update_project(project_id: str, request: UpdateProjectRequest, db: AsyncSession = Depends(get_db)):
    """更新项目"""
    # TODO: 实现更新项目逻辑
    raise NotImplementedError("更新项目功能待实现")


@router.delete("/{project_id}", response_model=DeleteProjectResponse)
async def delete_project(project_id: str, db: AsyncSession = Depends(get_db)):
    """删除项目"""
    # TODO: 实现删除项目逻辑
    raise NotImplementedError("删除项目功能待实现")
