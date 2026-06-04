"""
媒体模型
"""
from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import String, DateTime, ForeignKey, Float, Integer, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
import enum

from app.database import Base


class MediaType(str, enum.Enum):
    """媒体类型枚举"""
    IMAGE = "image"
    VIDEO = "video"


class MediaStatus(str, enum.Enum):
    """媒体状态枚举"""
    PENDING = "pending"
    GENERATING = "generating"
    COMPLETED = "completed"
    FAILED = "failed"


class MediaSource(str, enum.Enum):
    """媒体来源枚举"""
    AI_GENERATED = "ai_generated"
    USER_UPLOADED = "user_uploaded"


class Media(Base):
    """媒体表"""
    __tablename__ = "media"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    storyboard_item_id: Mapped[UUID] = mapped_column(ForeignKey("storyboard_items.id"), nullable=False, index=True)
    media_type: Mapped[MediaType] = mapped_column(SQLEnum(MediaType), nullable=False)
    file_path: Mapped[str] = mapped_column(String(500), nullable=True)  # MinIO 对象键
    file_url: Mapped[str] = mapped_column(String(500), nullable=True)
    width: Mapped[int] = mapped_column(Integer, nullable=True)
    height: Mapped[int] = mapped_column(Integer, nullable=True)
    duration: Mapped[float] = mapped_column(Float, nullable=True)  # 视频时长(秒)
    source: Mapped[MediaSource] = mapped_column(
        SQLEnum(MediaSource),
        default=MediaSource.AI_GENERATED,
        nullable=False
    )
    status: Mapped[MediaStatus] = mapped_column(
        SQLEnum(MediaStatus),
        default=MediaStatus.PENDING,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
