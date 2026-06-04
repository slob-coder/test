"""
Authentication API tests.
F01: 用户注册与登录
"""

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.utils.security import hash_password, verify_password, create_access_token, decode_token


# ============================================================
# Registration tests
# ============================================================

@pytest.mark.asyncio
async def test_register_success(client: AsyncClient, test_user_data):
    """Test successful user registration."""
    response = await client.post("/api/v1/auth/register", json=test_user_data)
    
    assert response.status_code == 201
    data = response.json()
    assert data["code"] == 0
    assert "user_id" in data["data"]
    assert data["data"]["username"] == test_user_data["username"]


@pytest.mark.asyncio
async def test_register_username_exists(client: AsyncClient, test_user_data):
    """Test registration with existing username."""
    # First registration
    await client.post("/api/v1/auth/register", json=test_user_data)
    
    # Second registration with same username
    response = await client.post("/api/v1/auth/register", json=test_user_data)
    
    assert response.status_code == 409
    data = response.json()
    assert data["code"] == 40001
    assert "已存在" in data["message"]


@pytest.mark.asyncio
async def test_register_username_too_short(client: AsyncClient):
    """Test registration with username too short."""
    response = await client.post("/api/v1/auth/register", json={
        "username": "a",
        "password": "testpassword123"
    })
    
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_register_username_invalid_chars(client: AsyncClient):
    """Test registration with invalid characters in username."""
    response = await client.post("/api/v1/auth/register", json={
        "username": "test@user",
        "password": "testpassword123"
    })
    
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_register_password_too_short(client: AsyncClient):
    """Test registration with password too short."""
    response = await client.post("/api/v1/auth/register", json={
        "username": "testuser",
        "password": "12345"
    })
    
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_register_missing_fields(client: AsyncClient):
    """Test registration with missing required fields."""
    response = await client.post("/api/v1/auth/register", json={})
    
    assert response.status_code == 422


# ============================================================
# Login tests
# ============================================================

@pytest.mark.asyncio
async def test_login_success(client: AsyncClient, test_user_data):
    """Test successful user login."""
    # Register user first
    await client.post("/api/v1/auth/register", json=test_user_data)
    
    # Login
    response = await client.post("/api/v1/auth/login", json=test_user_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 0
    assert "access_token" in data["data"]
    assert data["data"]["token_type"] == "bearer"
    assert data["data"]["expires_in"] == 86400
    assert data["data"]["user"]["username"] == test_user_data["username"]


@pytest.mark.asyncio
async def test_login_user_not_found(client: AsyncClient):
    """Test login with non-existent username."""
    response = await client.post("/api/v1/auth/login", json={
        "username": "nonexistent",
        "password": "testpassword123"
    })
    
    assert response.status_code == 401
    data = response.json()
    assert data["code"] == 40001
    assert "用户名或密码错误" in data["message"]


@pytest.mark.asyncio
async def test_login_wrong_password(client: AsyncClient, test_user_data):
    """Test login with wrong password."""
    # Register user first
    await client.post("/api/v1/auth/register", json=test_user_data)
    
    # Login with wrong password
    response = await client.post("/api/v1/auth/login", json={
        "username": test_user_data["username"],
        "password": "wrongpassword"
    })
    
    assert response.status_code == 401
    data = response.json()
    assert data["code"] == 40001
    assert "用户名或密码错误" in data["message"]


@pytest.mark.asyncio
async def test_login_missing_fields(client: AsyncClient):
    """Test login with missing required fields."""
    response = await client.post("/api/v1/auth/login", json={})
    
    assert response.status_code == 422


# ============================================================
# Token refresh tests
# ============================================================

@pytest.mark.asyncio
async def test_refresh_token_success(client: AsyncClient, test_user_data):
    """Test successful token refresh."""
    # Register and login
    await client.post("/api/v1/auth/register", json=test_user_data)
    login_response = await client.post("/api/v1/auth/login", json=test_user_data)
    token = login_response.json()["data"]["access_token"]
    
    # Refresh token
    response = await client.post("/api/v1/auth/refresh", json={
        "access_token": token
    })
    
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 0
    assert "access_token" in data["data"]
    assert data["data"]["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_refresh_token_invalid(client: AsyncClient):
    """Test token refresh with invalid token."""
    response = await client.post("/api/v1/auth/refresh", json={
        "access_token": "invalid_token"
    })
    
    assert response.status_code == 401
    data = response.json()
    assert data["code"] == 40001


# ============================================================
# Get current user tests
# ============================================================

@pytest.mark.asyncio
async def test_get_current_user_success(client: AsyncClient, test_user_data):
    """Test getting current user info with valid token."""
    # Register and login
    await client.post("/api/v1/auth/register", json=test_user_data)
    login_response = await client.post("/api/v1/auth/login", json=test_user_data)
    token = login_response.json()["data"]["access_token"]
    
    # Get current user
    response = await client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 0
    assert data["data"]["username"] == test_user_data["username"]


@pytest.mark.asyncio
async def test_get_current_user_no_token(client: AsyncClient):
    """Test getting current user info without token."""
    response = await client.get("/api/v1/auth/me")
    
    # HTTPBearer returns 403 when no credentials are provided
    # But our app might return 401 in some cases
    assert response.status_code in [401, 403]


@pytest.mark.asyncio
async def test_get_current_user_invalid_token(client: AsyncClient):
    """Test getting current user info with invalid token."""
    response = await client.get(
        "/api/v1/auth/me",
        headers={"Authorization": "Bearer invalid_token"}
    )
    
    assert response.status_code == 401


# ============================================================
# Security utility tests
# ============================================================

def test_hash_password():
    """Test password hashing."""
    password = "testpassword123"
    hashed = hash_password(password)
    
    assert hashed != password
    assert hashed.startswith("$2b$")


def test_verify_password():
    """Test password verification."""
    password = "testpassword123"
    hashed = hash_password(password)
    
    assert verify_password(password, hashed) is True
    assert verify_password("wrongpassword", hashed) is False


def test_create_and_decode_token():
    """Test JWT token creation and decoding."""
    user_id = "test-user-id-123"
    token = create_access_token(user_id)
    
    assert token is not None
    
    payload = decode_token(token)
    assert payload is not None
    assert payload["sub"] == user_id
    assert payload["type"] == "access"


def test_decode_expired_token():
    """Test decoding expired token."""
    # Create an already expired token
    import uuid
    from datetime import datetime, timedelta, timezone
    from jose import jwt
    from app.config import settings
    
    now = datetime.now(timezone.utc)
    payload = {
        "sub": "test-user-id",
        "iat": now - timedelta(hours=25),
        "exp": now - timedelta(hours=1),  # Expired 1 hour ago
        "jti": str(uuid.uuid4()),
        "type": "access"
    }
    
    expired_token = jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )
    
    # Should return None for expired token
    result = decode_token(expired_token)
    assert result is None
    
    # Should return payload with allow_expired=True
    result = decode_token(expired_token, allow_expired=True)
    assert result is not None
    assert result["sub"] == "test-user-id"


def test_decode_invalid_token():
    """Test decoding invalid token."""
    result = decode_token("invalid_token_string")
    assert result is None
