"""
Health check tests.
"""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    """Test the health check endpoint."""
    # TODO: Implement health check endpoint
    pass


@pytest.mark.asyncio
async def test_api_root(client: AsyncClient):
    """Test the API root endpoint."""
    # TODO: Implement API root test
    pass
