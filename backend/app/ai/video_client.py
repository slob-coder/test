"""
视频生成客户端封装
"""
from app.ai.base import AIClientBase, AIResult


class VideoGenClient(AIClientBase):
    """视频生成客户端"""

    async def generate(self, prompt: str, **kwargs) -> AIResult:
        """
        生成视频
        
        Args:
            prompt: 视频描述
            **kwargs: 额外参数 (duration, resolution 等)
            
        Returns:
            AIResult: 生成结果 (content 为视频 URL)
        """
        # TODO: 实现视频生成调用逻辑
        raise NotImplementedError("Video generation client not implemented")

    def get_provider_name(self) -> str:
        """返回 Provider 名称"""
        return "video_gen"
