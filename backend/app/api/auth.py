"""
M01: 用户认证模块 - API 路由
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.auth import (
    RegisterRequest, RegisterResponse,
    LoginRequest, LoginResponse,
    RefreshTokenRequest, RefreshTokenResponse,
    MeResponse
)

router = APIRouter()


@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest, db: AsyncSession = Depends(get_db)):
    """用户注册"""
    # TODO: 实现用户注册逻辑
    raise NotImplementedError("用户注册功能待实现")


@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest, db: AsyncSession = Depends(get_db)):
    """用户登录"""
    # TODO: 实现用户登录逻辑
    raise NotImplementedError("用户登录功能待实现")


@router.post("/refresh", response_model=RefreshTokenResponse)
async def refresh_token(request: RefreshTokenRequest):
    """刷新 Token"""
    # TODO: 实现 Token 刷新逻辑
    raise NotImplementedError("Token 刷新功能待实现")


@router.get("/me", response_model=MeResponse)
async def get_current_user():
    """获取当前用户信息"""
    # TODO: 实现获取当前用户逻辑
    raise NotImplementedError("获取当前用户功能待实现")
