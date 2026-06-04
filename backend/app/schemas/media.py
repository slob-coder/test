"""Media schemas - M05: Media Generation Module."""

from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class MediaType(str, Enum):
    """Media type enumeration."""
    IMAGE = "image"
    VIDEO = "video"


class MediaStatus(str, Enum):
    """Media status enumeration."""
    PENDING = "pending"
    GENERATING = "generating"
    COMPLETED = "completed"
    FAILED = "failed"


class MediaSource(str, Enum):
    """Media source enumeration."""
    AI_GENERATED = "ai_generated"
    USER_UPLOADED = "user_uploaded"


class MediaDTO(BaseModel):
    """Media data transfer object."""
    id: str
    storyboard_item_id: str
    media_type: MediaType
    file_path: str
    file_url: str
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[float] = None  # For video
    source: MediaSource
    status: MediaStatus
    created_at: datetime


class GenerateImageRequest(BaseModel):
    """Generate single image request."""
    storyboard_item_id: str


class GenerateImageResponse(BaseModel):
    """Generate image response."""
    task_id: str
    media: Optional[MediaDTO] = None


class GenerateImagesRequest(BaseModel):
    """Batch generate images request."""
    storyboard_item_ids: list[str]


class GenerateImagesResponse(BaseModel):
    """Batch generate images response."""
    task_id: str


class GenerateVideoRequest(BaseModel):
    """Generate single video request."""
    storyboard_item_id: str


class GenerateVideoResponse(BaseModel):
    """Generate video response."""
    task_id: str
    media: Optional[MediaDTO] = None


class GenerateVideosRequest(BaseModel):
    """Batch generate videos request."""
    storyboard_item_ids: list[str]


class GenerateVideosResponse(BaseModel):
    """Batch generate videos response."""
    task_id: str


class UploadImageRequest(BaseModel):
    """Upload image request (file upload)."""
    # TODO: Handle file upload
    pass


class UploadImageResponse(BaseModel):
    """Upload image response."""
    media: MediaDTO
