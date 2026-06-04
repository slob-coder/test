"""
Pytest configuration and fixtures for backend tests.
"""

import pytest
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

# Import only what we need for auth tests
from app.models.user import User
from app.dependencies import get_current_user


# Test database URL (in-memory SQLite for testing)
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests."""
    import asyncio
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def test_engine():
    """Create test database engine."""
    engine = create_async_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    
    # Only create User table for auth tests
    async with engine.begin() as conn:
        await conn.run_sync(User.__table__.create)
    
    yield engine
    
    async with engine.begin() as conn:
        await conn.run_sync(User.__table__.drop)
    
    await engine.dispose()


@pytest.fixture(scope="function")
async def db_session(test_engine) -> AsyncGenerator[AsyncSession, None]:
    """Create test database session."""
    async_session_maker = async_sessionmaker(
        test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    
    async with async_session_maker() as session:
        yield session


@pytest.fixture(scope="function")
async def client(db_session: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    """Create test HTTP client."""
    from app.api.auth import router as auth_router
    from app.database import get_db
    
    # Create a minimal test app with only auth routes
    app = FastAPI()
    
    # Add exception handler for HTTPException to return unified format
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        """统一处理 HTTPException，返回标准格式"""
        if isinstance(exc.detail, dict):
            # 如果 detail 是字典（包含 code 和 message）
            return JSONResponse(
                status_code=exc.status_code,
                content={
                    "code": exc.detail.get("code", 40001),
                    "message": exc.detail.get("message", "Error"),
                    "data": None
                }
            )
        else:
            # 如果 detail 是字符串
            return JSONResponse(
                status_code=exc.status_code,
                content={
                    "code": 40001,
                    "message": str(exc.detail),
                    "data": None
                }
            )
    
    app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])
    
    async def override_get_db():
        yield db_session
    
    app.dependency_overrides[get_db] = override_get_db
    
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        yield ac
    
    app.dependency_overrides.clear()


@pytest.fixture
def test_user_data():
    """Test user registration data."""
    return {
        "username": "testuser",
        "password": "testpassword123"
    }


@pytest.fixture
def test_project_data():
    """Test project creation data."""
    return {
        "name": "Test Project",
        "description": "A test project for video generation"
    }
