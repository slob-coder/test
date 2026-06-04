"""
LLM 客户端封装
"""
from app.ai.base import AIClientBase, AIResult


class LLMClient(AIClientBase):
    """大语言模型客户端"""

    async def generate(self, prompt: str, **kwargs) -> AIResult:
        """
        生成文本
        
        Args:
            prompt: 输入提示
            **kwargs: 额外参数 (model, temperature, max_tokens 等)
            
        Returns:
            AIResult: 生成结果
        """
        # TODO: 实现 LLM 调用逻辑
        raise NotImplementedError("LLM client not implemented")

    def get_provider_name(self) -> str:
        """返回 Provider 名称"""
        return "llm"
