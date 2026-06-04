"""
M07: 视频合成服务

职责: FFmpeg 视频拼接、字幕叠加
"""

from typing import List
from app.models.composition import Composition


class ComposeService:
    """视频合成服务"""
    
    async def start_composition(
        self, 
        project_id: str,
        resolution: str = "1080p",
        fps: int = 30
    ) -> Composition:
        """发起视频合成"""
        # TODO: 发起 Celery 异步任务进行视频合成
        raise NotImplementedError("发起视频合成功能待实现")
    
    async def get_composition(self, task_id: str) -> Composition:
        """查询合成任务状态"""
        # TODO: 实现查询合成任务状态逻辑
        raise NotImplementedError("查询合成任务状态功能待实现")
    
    async def list_compositions(self, project_id: str) -> List[Composition]:
        """获取合成历史"""
        # TODO: 实现获取合成历史逻辑
        raise NotImplementedError("获取合成历史功能待实现")
    
    async def cancel_composition(self, task_id: str) -> None:
        """取消合成任务"""
        # TODO: 实现取消合成任务逻辑
        raise NotImplementedError("取消合成任务功能待实现")
