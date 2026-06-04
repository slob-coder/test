"""Common schemas shared across modules."""

from typing import Generic, TypeVar, Optional, List
from pydantic import BaseModel

T = TypeVar("T")


class BaseResponse(BaseModel):
    """Base response model."""
    code: int = 0
    message: str = "success"


class PaginatedResponse(BaseModel, Generic[T]):
    """Paginated response model."""
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int


class ErrorResponse(BaseModel):
    """Error response model."""
    code: int
    message: str
    detail: Optional[str] = None
