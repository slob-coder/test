"""History schemas - M08: History Record Module."""

from typing import Any, Optional
from pydantic import BaseModel
from datetime import datetime


class HistoryDTO(BaseModel):
    """History record data transfer object."""
    id: str
    project_id: str
    action_type: str
    action_summary: str
    snapshot: dict[str, Any]
    created_at: datetime


class ListHistoriesResponse(BaseModel):
    """List histories response."""
    items: list[HistoryDTO]
    total: int


class GetHistoryResponse(BaseModel):
    """Get history detail response."""
    history: HistoryDTO
