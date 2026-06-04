"""Subtitle schemas - M06: Subtitle Generation Module."""

from typing import List
from pydantic import BaseModel, Field
from datetime import datetime


class SubtitleEntryDTO(BaseModel):
    """Subtitle entry data transfer object."""
    id: str
    subtitle_id: str
    storyboard_item_id: str
    order_index: int
    text: str
    start_time: float  # Seconds
    end_time: float    # Seconds
    created_at: datetime
    updated_at: datetime


class SubtitleDTO(BaseModel):
    """Subtitle data transfer object."""
    id: str
    project_id: str
    entries: List[SubtitleEntryDTO]
    created_at: datetime
    updated_at: datetime


class GenerateSubtitlesRequest(BaseModel):
    """Generate subtitles request."""
    # TODO: Define parameters if needed
    pass


class GenerateSubtitlesResponse(BaseModel):
    """Generate subtitles response."""
    task_id: str
    subtitle: Optional[SubtitleDTO] = None


class ListSubtitlesResponse(BaseModel):
    """List subtitles response."""
    subtitle: SubtitleDTO


class UpdateSubtitleEntryRequest(BaseModel):
    """Update subtitle entry request."""
    text: Optional[str] = None
    start_time: Optional[float] = Field(None, ge=0)
    end_time: Optional[float] = Field(None, ge=0)


class UpdateSubtitleEntryResponse(BaseModel):
    """Update subtitle entry response."""
    entry: SubtitleEntryDTO


class ExportSubtitlesResponse(BaseModel):
    """Export subtitles response (SRT file)."""
    # TODO: Return file content or URL
    content: str
    filename: str
