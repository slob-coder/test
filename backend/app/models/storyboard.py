"""
分镜模型
"""
from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import String, DateTime, Text, ForeignKey, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Storyboard(Base):
    """分镜容器表"""
    __tablename__ = "storyboards"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id"), unique=True, nullable=False)
    script_id: Mapped[UUID] = mapped_column(ForeignKey("scripts.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class StoryboardItem(Base):
    """分镜条目表"""
    __tablename__ = "storyboard_items"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    storyboard_id: Mapped[UUID] = mapped_column(ForeignKey("storyboards.id"), nullable=False, index=True)
    order_index: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    scene_description: Mapped[str] = mapped_column(Text, nullable=True)
    narration_text: Mapped[str] = mapped_column(Text, nullable=True)
    estimated_duration: Mapped[float] = mapped_column(Float, nullable=True)  # 秒
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
