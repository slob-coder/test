"""Project schemas - M02: Project Management Module."""

from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class ProjectStatus(str, Enum):
    """Project status enumeration."""
    DRAFT = "draft"
    SCRIPTED = "scripted"
    STORYBOARDED = "storyboarded"
    MATERIALIZED = "materialized"
    COMPOSITING = "compositing"
    COMPLETED = "completed"
    FAILED = "failed"


class CreateProjectRequest(BaseModel):
    """Create project request."""
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None


class CreateProjectResponse(BaseModel):
    """Create project response."""
    id: str
    name: str
    description: str
    status: ProjectStatus
    created_at: datetime
    updated_at: datetime


class ProjectListItem(BaseModel):
    """Project list item."""
    id: str
    name: str
    status: ProjectStatus
    thumbnail_url: Optional[str]
    created_at: datetime
    updated_at: datetime


class ListProjectsRequest(BaseModel):
    """List projects request."""
    page: int = Field(1, ge=1)
    page_size: int = Field(20, ge=1, le=100)
    status: Optional[ProjectStatus] = None


class ListProjectsResponse(BaseModel):
    """List projects response."""
    items: list[ProjectListItem]
    total: int
    page: int
    page_size: int
    total_pages: int


class GetProjectResponse(BaseModel):
    """Get project response."""
    id: str
    name: str
    description: str
    status: ProjectStatus
    user_id: str
    thumbnail_url: Optional[str]
    created_at: datetime
    updated_at: datetime


class UpdateProjectRequest(BaseModel):
    """Update project request."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None


class UpdateProjectResponse(BaseModel):
    """Update project response."""
    id: str
    name: str
    description: str
    status: ProjectStatus
    updated_at: datetime


class DeleteProjectResponse(BaseModel):
    """Delete project response."""
    message: str
