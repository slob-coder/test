"""Share schemas - M09: Export & Share Module."""

from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

from app.schemas.composition import Resolution


class ExportStatus(str, Enum):
    """Export status enumeration."""
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class ExportDTO(BaseModel):
    """Export data transfer object."""
    id: str
    composition_id: str
    resolution: Resolution
    file_path: str
    file_url: str
    status: ExportStatus
    created_at: datetime


class ExportVideoRequest(BaseModel):
    """Export video request."""
    resolution: Resolution = Resolution.FHD_1080P


class ExportVideoResponse(BaseModel):
    """Export video response."""
    task_id: str
    export: Optional[ExportDTO] = None


class ShareLinkDTO(BaseModel):
    """Share link data transfer object."""
    id: str
    composition_id: str
    token: str
    expires_at: datetime
    created_at: datetime


class CreateShareLinkRequest(BaseModel):
    """Create share link request."""
    expires_in_hours: int = Field(24, ge=1, le=168)  # 1 hour to 7 days


class CreateShareLinkResponse(BaseModel):
    """Create share link response."""
    share_link: ShareLinkDTO
    share_url: str


class AccessShareResponse(BaseModel):
    """Access shared video response."""
    video_url: str
    expires_at: datetime
