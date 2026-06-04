"""
安全工具模块 - JWT Token 和密码哈希
"""

from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码"""
    # TODO: 实现密码验证逻辑
    raise NotImplementedError("密码验证逻辑待实现")


def get_password_hash(password: str) -> str:
    """生成密码哈希"""
    # TODO: 实现密码哈希逻辑
    raise NotImplementedError("密码哈希逻辑待实现")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """创建 JWT Token"""
    # TODO: 实现 JWT Token 创建逻辑
    raise NotImplementedError("JWT Token 创建逻辑待实现")


def decode_access_token(token: str) -> Optional[dict]:
    """解码 JWT Token"""
    # TODO: 实现 JWT Token 解码逻辑
    raise NotImplementedError("JWT Token 解码逻辑待实现")
