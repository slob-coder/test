"""
Authentication tests.
"""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_user(client: AsyncClient, test_user_data):
    """Test user registration."""
    # TODO: Implement registration test
    pass


@pytest.mark.asyncio
async def test_login_user(client: AsyncClient, test_user_data):
    """Test user login."""
    # TODO: Implement login test
    pass


@pytest.mark.asyncio
async def test_get_current_user(client: AsyncClient, test_user_data):
    """Test getting current user info."""
    # TODO: Implement get current user test
    pass


@pytest.mark.asyncio
async def test_refresh_token(client: AsyncClient, test_user_data):
    """Test token refresh."""
    # TODO: Implement token refresh test
    pass
