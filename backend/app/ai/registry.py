"""
AI Provider 注册机制
"""
from typing import Type
from app.ai.base import AIClientBase


class AIProviderRegistry:
    """AI Provider 注册表"""
    
    _providers: dict[str, Type[AIClientBase]] = {}

    @classmethod
    def register(cls, name: str, provider_cls: Type[AIClientBase]) -> None:
        """
        注册 Provider
        
        Args:
            name: Provider 名称
            provider_cls: Provider 类
        """
        cls._providers[name] = provider_cls

    @classmethod
    def get(cls, name: str) -> AIClientBase:
        """
        获取 Provider 实例
        
        Args:
            name: Provider 名称
            
        Returns:
            AIClientBase: Provider 实例
            
        Raises:
            KeyError: Provider 不存在
        """
        if name not in cls._providers:
            raise KeyError(f"AI Provider '{name}' not registered")
        return cls._providers[name]()

    @classmethod
    def list_providers(cls) -> list[str]:
        """
        列出所有已注册的 Provider
        
        Returns:
            list[str]: Provider 名称列表
        """
        return list(cls._providers.keys())
