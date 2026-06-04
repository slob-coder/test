"""Script schemas - M03: Script Generation Module."""

from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class ScriptSource(str, Enum):
    """Script source enumeration."""
    AI_GENERATED = "ai_generated"
    USER_UPLOADED = "user_uploaded"
    AI_OPTIMIZED = "ai_optimized"


class SceneDTO(BaseModel):
    """Scene data transfer object."""
    scene_description: str
    narration: str


class ScriptDTO(BaseModel):
    """Script data transfer object."""
    id: str
    project_id: str
    scenes: List[SceneDTO]
    source: ScriptSource
    version: int
    created_at: datetime
    updated_at: datetime


class GenerateScriptRequest(BaseModel):
    """Generate script request."""
    # TODO: Define request parameters based on AI generation requirements
    pass


class GenerateScriptResponse(BaseModel):
    """Generate script response."""
    task_id: str
    script: Optional[ScriptDTO] = None


class SaveScriptRequest(BaseModel):
    """Save script request."""
    scenes: List[SceneDTO]


class SaveScriptResponse(BaseModel):
    """Save script response."""
    id: str
    project_id: str
    scenes: List[SceneDTO]
    version: int
    updated_at: datetime


class UploadScriptRequest(BaseModel):
    """Upload script request (file upload)."""
    # TODO: Handle file upload
    pass
