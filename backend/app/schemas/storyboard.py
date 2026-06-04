"""Storyboard schemas - M04: Storyboard Management Module."""

from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime


class StoryboardItemDTO(BaseModel):
    """Storyboard item data transfer object."""
    id: str
    storyboard_id: str
    order_index: int
    scene_description: str
    narration_text: str
    estimated_duration: float
    created_at: datetime
    updated_at: datetime


class StoryboardDTO(BaseModel):
    """Storyboard data transfer object."""
    id: str
    project_id: str
    script_id: str
    items: List[StoryboardItemDTO]
    created_at: datetime
    updated_at: datetime


class GenerateStoryboardRequest(BaseModel):
    """Generate storyboard from script request."""
    # TODO: Define parameters if needed
    pass


class GenerateStoryboardResponse(BaseModel):
    """Generate storyboard response."""
    task_id: str
    storyboard: Optional[StoryboardDTO] = None


class ReorderStoryboardRequest(BaseModel):
    """Reorder storyboard items request."""
    item_ids: List[str]  # New order of item IDs


class ReorderStoryboardResponse(BaseModel):
    """Reorder storyboard response."""
    message: str
    items: List[StoryboardItemDTO]


class CreateStoryboardItemRequest(BaseModel):
    """Create storyboard item request."""
    scene_description: str
    narration_text: str
    estimated_duration: float = Field(..., gt=0)


class UpdateStoryboardItemRequest(BaseModel):
    """Update storyboard item request."""
    scene_description: Optional[str] = None
    narration_text: Optional[str] = None
    estimated_duration: Optional[float] = Field(None, gt=0)


class SplitStoryboardItemRequest(BaseModel):
    """Split storyboard item request."""
    split_position: int  # Character position to split narration


class SplitStoryboardItemResponse(BaseModel):
    """Split storyboard item response."""
    item1: StoryboardItemDTO
    item2: StoryboardItemDTO


class MergeStoryboardItemsRequest(BaseModel):
    """Merge storyboard items request."""
    item_ids: List[str] = Field(..., min_length=2)


class MergeStoryboardItemsResponse(BaseModel):
    """Merge storyboard items response."""
    merged_item: StoryboardItemDTO
