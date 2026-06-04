"""
Project management tests.
"""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_project(client: AsyncClient, test_project_data):
    """Test project creation."""
    # TODO: Implement create project test
    pass


@pytest.mark.asyncio
async def test_list_projects(client: AsyncClient):
    """Test listing projects."""
    # TODO: Implement list projects test
    pass


@pytest.mark.asyncio
async def test_get_project(client: AsyncClient):
    """Test getting a single project."""
    # TODO: Implement get project test
    pass


@pytest.mark.asyncio
async def test_update_project(client: AsyncClient, test_project_data):
    """Test updating a project."""
    # TODO: Implement update project test
    pass


@pytest.mark.asyncio
async def test_delete_project(client: AsyncClient):
    """Test deleting a project."""
    # TODO: Implement delete project test
    pass
