"""Auth schemas - M01: Authentication Module."""

from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class RegisterRequest(BaseModel):
    """User registration request."""
    username: str = Field(..., min_length=2, max_length=50, pattern=r"^[a-zA-Z0-9_]+$")
    password: str = Field(..., min_length=6)


class RegisterResponse(BaseModel):
    """User registration response."""
    user_id: str
    username: str


class LoginRequest(BaseModel):
    """User login request."""
    username: str
    password: str


class UserDTO(BaseModel):
    """User data transfer object."""
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    username: str
    created_at: datetime
    updated_at: Optional[datetime] = None


class LoginResponse(BaseModel):
    """User login response."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int = 86400  # 24 hours in seconds
    user: UserDTO


class RefreshTokenRequest(BaseModel):
    """Token refresh request."""
    access_token: str


class RefreshTokenResponse(BaseModel):
    """Token refresh response."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int = 86400


class MeResponse(UserDTO):
    """Current user info response."""
    pass
