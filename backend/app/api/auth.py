"""
M01: 用户认证模块 - API 路由
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.auth import (
    RegisterRequest, RegisterResponse,
    LoginRequest, LoginResponse,
    RefreshTokenRequest, RefreshTokenResponse,
    MeResponse, UserDTO
)
from app.schemas.common import BaseResponse
from app.services.auth_service import AuthService, UsernameExistsError, AuthenticationError, InvalidTokenError

router = APIRouter()


def user_to_dto(user: User) -> UserDTO:
    """Convert User model to UserDTO."""
    return UserDTO(
        id=str(user.id),
        username=user.username,
        created_at=user.created_at,
        updated_at=user.updated_at
    )


@router.post("/register", response_model=BaseResponse, status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest, db: AsyncSession = Depends(get_db)):
    """用户注册"""
    auth_service = AuthService(db)
    
    try:
        user = await auth_service.register(request.username, request.password)
        return BaseResponse(
            code=0,
            message="success",
            data=RegisterResponse(
                user_id=str(user.id),
                username=user.username
            )
        )
    except UsernameExistsError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"code": 40001, "message": str(e)}
        )


@router.post("/login", response_model=BaseResponse)
async def login(request: LoginRequest, db: AsyncSession = Depends(get_db)):
    """用户登录"""
    auth_service = AuthService(db)
    
    try:
        result = await auth_service.login(request.username, request.password)
        user = result["user"]
        token = result["access_token"]
        
        return BaseResponse(
            code=0,
            message="success",
            data=LoginResponse(
                access_token=token,
                token_type="bearer",
                expires_in=86400,
                user=user_to_dto(user)
            )
        )
    except AuthenticationError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"code": 40001, "message": str(e)},
            headers={"WWW-Authenticate": "Bearer"}
        )


@router.post("/refresh", response_model=BaseResponse)
async def refresh_token(request: RefreshTokenRequest, db: AsyncSession = Depends(get_db)):
    """刷新 Token"""
    auth_service = AuthService(db)
    
    try:
        result = await auth_service.refresh_token(request.access_token, db)
        return BaseResponse(
            code=0,
            message="success",
            data=RefreshTokenResponse(
                access_token=result["access_token"],
                token_type="bearer",
                expires_in=86400
            )
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"code": 40001, "message": str(e)},
            headers={"WWW-Authenticate": "Bearer"}
        )


@router.get("/me", response_model=BaseResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    """获取当前用户信息"""
    return BaseResponse(
        code=0,
        message="success",
        data=user_to_dto(current_user)
    )
