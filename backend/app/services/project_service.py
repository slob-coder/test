"""
M02: 项目管理服务

职责: 项目 CRUD、状态管理
"""

from typing import List, Optional
from app.models.project import Project


class ProjectService:
    """项目管理服务"""
    
    async def create(self, user_id: str, name: str, description: Optional[str] = None) -> Project:
        """创建项目"""
        # TODO: 实现项目创建逻辑
        raise NotImplementedError("创建项目功能待实现")
    
    async def list_by_user(
        self, 
        user_id: str, 
        page: int = 1, 
        page_size: int = 20,
        status: Optional[str] = None
    ) -> tuple[List[Project], int]:
        """获取用户项目列表"""
        # TODO: 实现项目列表查询逻辑
        raise NotImplementedError("获取项目列表功能待实现")
    
    async def get(self, project_id: str, user_id: str) -> Project:
        """获取项目详情"""
        # TODO: 实现获取项目详情逻辑
        raise NotImplementedError("获取项目详情功能待实现")
    
    async def update(
        self, 
        project_id: str, 
        user_id: str, 
        name: Optional[str] = None,
        description: Optional[str] = None
    ) -> Project:
        """更新项目"""
        # TODO: 实现项目更新逻辑
        raise NotImplementedError("更新项目功能待实现")
    
    async def delete(self, project_id: str, user_id: str) -> None:
        """删除项目"""
        # TODO: 实现项目删除逻辑
        raise NotImplementedError("删除项目功能待实现")
    
    async def update_status(self, project_id: str, status: str) -> Project:
        """更新项目状态"""
        # TODO: 实现项目状态更新逻辑
        raise NotImplementedError("更新项目状态功能待实现")
