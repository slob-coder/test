"""
安全工具模块 - JWT Token 和密码哈希

F01: 用户注册与登录
"""

import uuid
from datetime import datetime, timedelta, timezone
from typing import Optional

import bcrypt
from jose import JWTError, jwt

from app.config import settings


def hash_password(password: str) -> str:
    """
    使用 bcrypt 哈希密码
    
    Args:
        password: 明文密码
        
    Returns:
        bcrypt 哈希后的密码字符串
    """
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证密码是否匹配
    
    Args:
        plain_password: 明文密码
        hashed_password: bcrypt 哈希后的密码
        
    Returns:
        密码是否匹配
    """
    return bcrypt.checkpw(
        plain_password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )


def create_access_token(
    user_id: str,
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    创建 JWT Token
    
    Args:
        user_id: 用户ID
        expires_delta: 过期时间增量，默认使用配置中的 JWT_EXPIRE_HOURS
        
    Returns:
        JWT Token 字符串
    """
    if expires_delta is None:
        expires_delta = timedelta(hours=settings.JWT_EXPIRE_HOURS)
    
    now = datetime.now(timezone.utc)
    expire = now + expires_delta
    
    # 生成唯一的 Token ID
    jti = str(uuid.uuid4())
    
    payload = {
        "sub": user_id,
        "iat": now,
        "exp": expire,
        "jti": jti,
        "type": "access"
    }
    
    encoded_jwt = jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )
    
    return encoded_jwt


def decode_token(
    token: str,
    allow_expired: bool = False,
    grace_period_seconds: int = 300
) -> Optional[dict]:
    """
    解码 JWT Token
    
    Args:
        token: JWT Token 字符串
        allow_expired: 是否允许过期 Token（用于刷新场景）
        grace_period_seconds: 过期宽限期（秒），默认 5 分钟
        
    Returns:
        解码后的 payload 字典，解码失败返回 None
    """
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
            options={"verify_exp": not allow_expired}
        )
        return payload
    except JWTError:
        # 如果允许过期，尝试在宽限期内解码
        if allow_expired:
            try:
                # 不验证过期时间进行解码
                payload = jwt.decode(
                    token,
                    settings.JWT_SECRET_KEY,
                    algorithms=[settings.JWT_ALGORITHM],
                    options={"verify_exp": False}
                )
                
                # 检查是否在宽限期内
                exp = payload.get("exp")
                if exp:
                    now = datetime.now(timezone.utc).timestamp()
                    if now - exp <= grace_period_seconds:
                        return payload
                
                return None
            except JWTError:
                return None
        return None


def decode_token_for_refresh(token: str) -> Optional[dict]:
    """
    用于刷新 Token 的解码函数，允许过期宽限期
    
    Args:
        token: JWT Token 字符串
        
    Returns:
        解码后的 payload 字典，解码失败返回 None
    """
    return decode_token(token, allow_expired=True, grace_period_seconds=300)
