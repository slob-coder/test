"""
图片生成客户端封装
"""
from app.ai.base import AIClientBase, AIResult


class ImageGenClient(AIClientBase):
    """图片生成客户端"""

    async def generate(self, prompt: str, **kwargs) -> AIResult:
        """
        生成图片
        
        Args:
            prompt: 图片描述
            **kwargs: 额外参数 (size, style, quality 等)
            
        Returns:
            AIResult: 生成结果 (content 为图片 URL)
        """
        # TODO: 实现图片生成调用逻辑
        raise NotImplementedError("Image generation client not implemented")

    def get_provider_name(self) -> str:
        """返回 Provider 名称"""
        return "image_gen"
