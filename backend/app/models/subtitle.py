"""
M06: 字幕模型

Subtitle - 项目级字幕容器
SubtitleEntry - 具体字幕条目
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class Subtitle(Base):
    """字幕容器表"""

    __tablename__ = "subtitles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    format = Column(String(10), default="srt", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    # 关联
    project = relationship("Project", back_populates="subtitles")
    entries = relationship(
        "SubtitleEntry",
        back_populates="subtitle",
        cascade="all, delete-orphan",
        order_by="SubtitleEntry.order_index",
    )


class SubtitleEntry(Base):
    """字幕条目表"""

    __tablename__ = "subtitle_entries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    subtitle_id = Column(
        UUID(as_uuid=True),
        ForeignKey("subtitles.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    storyboard_item_id = Column(
        UUID(as_uuid=True),
        ForeignKey("storyboard_items.id", ondelete="SET NULL"),
        nullable=True,
    )
    order_index = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    start_time = Column(Float, nullable=False)  # 秒
    end_time = Column(Float, nullable=False)  # 秒
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    # 关联
    subtitle = relationship("Subtitle", back_populates="entries")
    storyboard_item = relationship("StoryboardItem", back_populates="subtitle_entries")
