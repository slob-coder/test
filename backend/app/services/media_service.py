"""
M05: 媒体生成服务

职责: AI 图片/视频生成、素材上传
"""

from typing import List
from app.models.media import Media


class MediaService:
    """媒体生成服务"""
    
    async def generate_image(self, storyboard_item_id: str, prompt: str) -> Media:
        """生成单个分镜图片"""
        # TODO: 调用 AI 图片生成服务
        raise NotImplementedError("生成图片功能待实现")
    
    async def generate_images_batch(self, storyboard_id: str) -> List[Media]:
        """批量生成图片"""
        # TODO: 实现批量生成图片逻辑
        raise NotImplementedError("批量生成图片功能待实现")
    
    async def generate_video(self, storyboard_item_id: str) -> Media:
        """生成单个视频片段"""
        # TODO: 调用 AI 视频生成服务
        raise NotImplementedError("生成视频功能待实现")
    
    async def generate_videos_batch(self, storyboard_id: str) -> List[Media]:
        """批量生成视频"""
        # TODO: 实现批量生成视频逻辑
        raise NotImplementedError("批量生成视频功能待实现")
    
    async def upload_image(self, storyboard_item_id: str, file_data: bytes) -> Media:
        """上传替换图片"""
        # TODO: 实现图片上传逻辑
        raise NotImplementedError("上传图片功能待实现")
    
    async def get_media(self, media_id: str) -> Media:
        """获取媒体文件信息"""
        # TODO: 实现获取媒体信息逻辑
        raise NotImplementedError("获取媒体信息功能待实现")
