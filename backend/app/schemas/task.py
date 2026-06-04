"""Task schemas - M10: Task Status Module."""

from typing import Optional, Any
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

from app.schemas.common import PaginatedResponse


class TaskType(str, Enum):
    """Async task type enumeration."""
    SCRIPT_GENERATION = "script_generation"
    STORYBOARD_GENERATION = "storyboard_generation"
    IMAGE_GENERATION = "image_generation"
    VIDEO_GENERATION = "video_generation"
    VIDEO_COMPOSITION = "video_composition"
    VIDEO_EXPORT = "video_export"


class TaskStatus(str, Enum):
    """Async task status enumeration."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class AsyncTaskDTO(BaseModel):
    """Async task data transfer object."""
    id: str
    type: TaskType
    status: TaskStatus
    progress: int = 0  # 0-100
    message: Optional[str] = None
    result: Optional[dict[str, Any]] = None
    error: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class ListTasksRequest(BaseModel):
    """List tasks request."""
    project_id: Optional[str] = None
    status: Optional[TaskStatus] = None
    type: Optional[TaskType] = None
    page: int = 1
    page_size: int = 20


class ListTasksResponse(PaginatedResponse[AsyncTaskDTO]):
    """List tasks response."""
    pass


class GetTaskResponse(BaseModel):
    """Get task response."""
    task: AsyncTaskDTO


# SSE Event Types
class TaskProgressEvent(BaseModel):
    """Task progress event (SSE)."""
    task_id: str
    progress: int
    message: str


class TaskCompletedEvent(BaseModel):
    """Task completed event (SSE)."""
    task_id: str
    task_type: str
    result: dict[str, Any]


class TaskFailedEvent(BaseModel):
    """Task failed event (SSE)."""
    task_id: str
    task_type: str
    error: str


class ProjectStatusChangeEvent(BaseModel):
    """Project status change event (SSE)."""
    project_id: str
    old_status: str
    new_status: str
