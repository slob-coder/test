"""
M01: 认证服务

职责: 用户注册、登录、Token 管理
"""

import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.models.user import User
from app.utils.security import (
    verify_password,
    hash_password,
    create_access_token,
    decode_token_for_refresh,
)
from app.config import settings


class UsernameExistsError(Exception):
    """用户名已存在异常"""
    pass


class AuthenticationError(Exception):
    """认证失败异常"""
    pass


class InvalidTokenError(Exception):
    """Token 无效异常"""
    pass


class AuthService:
    """认证服务"""
    
    def __init__(self, db: Optional[AsyncSession]):
        self.db = db
    
    async def register(self, username: str, password: str) -> User:
        """
        用户注册
        
        Args:
            username: 用户名 (2-50字符，字母数字下划线)
            password: 密码 (≥6字符)
            
        Returns:
            User: 新创建的用户对象
            
        Raises:
            UsernameExistsError: 用户名已存在
        """
        if not self.db:
            raise ValueError("Database session is required for registration")
            
        # 检查用户名是否已存在
        result = await self.db.execute(
            select(User).where(User.username == username)
        )
        existing_user = result.scalar_one_or_none()
        
        if existing_user:
            raise UsernameExistsError("用户名已存在")
        
        # 创建新用户 - ID 使用字符串格式
        user = User(
            id=str(uuid.uuid4()),  # 字符串格式的 UUID
            username=username,
            password_hash=hash_password(password),
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        
        self.db.add(user)
        
        try:
            await self.db.commit()
            await self.db.refresh(user)
        except IntegrityError:
            await self.db.rollback()
            raise UsernameExistsError("用户名已存在")
        
        return user
    
    async def login(self, username: str, password: str) -> dict:
        """
        用户登录
        
        Args:
            username: 用户名
            password: 密码
            
        Returns:
            dict: 包含 access_token 和 user 信息
            
        Raises:
            AuthenticationError: 用户名或密码错误
        """
        if not self.db:
            raise ValueError("Database session is required for login")
            
        # 查找用户
        result = await self.db.execute(
            select(User).where(User.username == username)
        )
        user = result.scalar_one_or_none()
        
        # 统一错误提示，防止用户名枚举
        if not user:
            raise AuthenticationError("用户名或密码错误")
        
        # 验证密码
        if not verify_password(password, user.password_hash):
            raise AuthenticationError("用户名或密码错误")
        
        # 生成 JWT Token
        access_token = create_access_token(user_id=str(user.id))
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": settings.JWT_EXPIRE_HOURS * 3600,
            "user": user,
        }
    
    async def refresh_token(self, token: str, db: Optional[AsyncSession] = None) -> dict:
        """
        刷新 Token
        
        Args:
            token: 当前 Token（仍有效期内或宽限期内）
            db: 可选的数据库会话（用于验证用户是否存在）
            
        Returns:
            dict: 包含新的 access_token
            
        Raises:
            InvalidTokenError: Token 无效或已过期
        """
        # 解码 Token（允许宽限期内过期）
        payload = decode_token_for_refresh(token)
        
        if not payload:
            raise InvalidTokenError("Token 无效或已过期")
        
        user_id = payload.get("sub")
        if not user_id:
            raise InvalidTokenError("Token 无效或已过期")
        
        # 如果提供了数据库会话，验证用户是否存在
        if db:
            result = await db.execute(
                select(User).where(User.id == user_id)
            )
            user = result.scalar_one_or_none()
            
            if not user:
                raise InvalidTokenError("Token 无效或已过期")
        
        # 生成新 Token
        new_token = create_access_token(user_id=user_id)
        
        return {
            "access_token": new_token,
            "token_type": "bearer",
            "expires_in": settings.JWT_EXPIRE_HOURS * 3600,
        }
    
    async def get_current_user(self, user_id: str) -> User:
        """
        获取当前用户
        
        Args:
            user_id: 用户 ID
            
        Returns:
            User: 用户对象
            
        Raises:
            AuthenticationError: 用户不存在
        """
        if not self.db:
            raise ValueError("Database session is required")
            
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            raise AuthenticationError("用户不存在")
        
        return user
