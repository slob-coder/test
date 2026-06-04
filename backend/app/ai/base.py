"""
AI 服务抽象基类
"""
from abc import ABC, abstractmethod
from typing import Any
from pydantic import BaseModel


class AIResult(BaseModel):
    """AI 生成结果"""
    success: bool
    content: str | None = None
    metadata: dict[str, Any] = {}
    error: str | None = None


class AIClientBase(ABC):
    """AI 服务抽象基类"""

    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> AIResult:
        """
        统一生成接口
        
        Args:
            prompt: 输入提示
            **kwargs: 额外参数
            
        Returns:
            AIResult: 生成结果
        """
        raise NotImplementedError("Subclasses must implement generate()")

    @abstractmethod
    def get_provider_name(self) -> str:
        """
        返回 Provider 标识
        
        Returns:
            str: Provider 名称
        """
        raise NotImplementedError("Subclasses must implement get_provider_name()")
