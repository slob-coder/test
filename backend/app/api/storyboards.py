"""
M04: 分镜管理模块 - API 路由
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.storyboard import (
    GetStoryboardResponse, GenerateStoryboardRequest, GenerateStoryboardResponse,
    ReorderStoryboardRequest, ReorderStoryboardResponse,
    CreateStoryboardItemRequest, CreateStoryboardItemResponse,
    UpdateStoryboardItemRequest, UpdateStoryboardItemResponse,
    SplitStoryboardItemRequest, SplitStoryboardItemResponse,
    MergeStoryboardItemsRequest, MergeStoryboardItemsResponse
)

router = APIRouter()


@router.get("/projects/{project_id}/storyboard", response_model=GetStoryboardResponse)
async def get_storyboard(project_id: str, db: AsyncSession = Depends(get_db)):
    """获取分镜列表"""
    # TODO: 实现获取分镜列表逻辑
    raise NotImplementedError("获取分镜列表功能待实现")


@router.post("/projects/{project_id}/storyboard/generate", response_model=GenerateStoryboardResponse, status_code=status.HTTP_201_CREATED)
async def generate_storyboard(project_id: str, request: GenerateStoryboardRequest, db: AsyncSession = Depends(get_db)):
    """从脚本自动生成分镜"""
    # TODO: 实现从脚本生成分镜逻辑
    raise NotImplementedError("从脚本生成分镜功能待实现")


@router.put("/projects/{project_id}/storyboard/reorder", response_model=ReorderStoryboardResponse)
async def reorder_storyboard(project_id: str, request: ReorderStoryboardRequest, db: AsyncSession = Depends(get_db)):
    """调整分镜顺序"""
    # TODO: 实现调整分镜顺序逻辑
    raise NotImplementedError("调整分镜顺序功能待实现")


@router.post("/storyboard-items", response_model=CreateStoryboardItemResponse, status_code=status.HTTP_201_CREATED)
async def create_storyboard_item(request: CreateStoryboardItemRequest, db: AsyncSession = Depends(get_db)):
    """新增分镜项"""
    # TODO: 实现新增分镜项逻辑
    raise NotImplementedError("新增分镜项功能待实现")


@router.put("/storyboard-items/{item_id}", response_model=UpdateStoryboardItemResponse)
async def update_storyboard_item(item_id: str, request: UpdateStoryboardItemRequest, db: AsyncSession = Depends(get_db)):
    """更新分镜项"""
    # TODO: 实现更新分镜项逻辑
    raise NotImplementedError("更新分镜项功能待实现")


@router.delete("/storyboard-items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_storyboard_item(item_id: str, db: AsyncSession = Depends(get_db)):
    """删除分镜项"""
    # TODO: 实现删除分镜项逻辑
    raise NotImplementedError("删除分镜项功能待实现")


@router.post("/storyboard-items/{item_id}/split", response_model=SplitStoryboardItemResponse)
async def split_storyboard_item(item_id: str, request: SplitStoryboardItemRequest, db: AsyncSession = Depends(get_db)):
    """拆分分镜"""
    # TODO: 实现拆分分镜逻辑
    raise NotImplementedError("拆分分镜功能待实现")


@router.post("/storyboard-items/merge", response_model=MergeStoryboardItemsResponse)
async def merge_storyboard_items(request: MergeStoryboardItemsRequest, db: AsyncSession = Depends(get_db)):
    """合并分镜"""
    # TODO: 实现合并分镜逻辑
    raise NotImplementedError("合并分镜功能待实现")
