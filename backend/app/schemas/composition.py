"""Composition schemas - M07: Video Composition Module."""

from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class CompositionStatus(str, Enum):
    """Composition status enumeration."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class Resolution(str, Enum):
    """Video resolution enumeration."""
    HD_720P = "720p"
    FHD_1080P = "1080p"


class CompositionDTO(BaseModel):
    """Composition data transfer object."""
    id: str
    project_id: str
    status: CompositionStatus
    output_path: Optional[str] = None
    output_url: Optional[str] = None
    resolution: Resolution
    fps: int = 30
    duration: Optional[float] = None
    error_message: Optional[str] = None
    created_at: datetime
    completed_at: Optional[datetime] = None


class ComposeVideoRequest(BaseModel):
    """Compose video request."""
    resolution: Resolution = Resolution.FHD_1080P
    fps: int = Field(30, ge=24, le=60)


class ComposeVideoResponse(BaseModel):
    """Compose video response."""
    task_id: str
    composition: Optional[CompositionDTO] = None


class GetCompositionResponse(BaseModel):
    """Get composition response."""
    composition: CompositionDTO


class ListCompositionsResponse(BaseModel):
    """List compositions response."""
    items: list[CompositionDTO]
    total: int


class CancelCompositionResponse(BaseModel):
    """Cancel composition response."""
    message: str
    composition: CompositionDTO
