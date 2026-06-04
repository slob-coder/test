"""
M01: 认证服务

职责: 用户注册、登录、Token 管理
"""

from app.models.user import User


class AuthService:
    """认证服务"""
    
    async def register(self, username: str, password: str) -> User:
        """用户注册"""
        # TODO: 实现用户注册逻辑
        raise NotImplementedError("用户注册功能待实现")
    
    async def login(self, username: str, password: str) -> dict:
        """用户登录，返回 JWT Token"""
        # TODO: 实现用户登录逻辑
        raise NotImplementedError("用户登录功能待实现")
    
    async def refresh_token(self, token: str) -> dict:
        """刷新 Token"""
        # TODO: 实现 Token 刷新逻辑
        raise NotImplementedError("Token 刷新功能待实现")
    
    async def get_current_user(self, user_id: str) -> User:
        """获取当前用户"""
        # TODO: 实现获取当前用户逻辑
        raise NotImplementedError("获取当前用户功能待实现")
