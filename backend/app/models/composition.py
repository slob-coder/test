"""
M07: 视频合成模型

Composition - 合成任务记录
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


class Composition(Base):
    """视频合成任务表"""

    __tablename__ = "compositions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    status = Column(
        String(20),
        default="pending",
        nullable=False,
        index=True,
    )  # pending/processing/completed/failed
    output_path = Column(String(500), nullable=True)  # MinIO 对象键
    output_url = Column(String(500), nullable=True)
    resolution = Column(String(10), default="1080p", nullable=False)  # 720p/1080p
    fps = Column(Integer, default=30, nullable=False)
    duration = Column(Float, nullable=True)  # 视频时长(秒)
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    completed_at = Column(DateTime, nullable=True)

    # 关联
    project = relationship("Project", back_populates="compositions")
    exports = relationship("Export", back_populates="composition", cascade="all, delete-orphan")
    share_links = relationship("ShareLink", back_populates="composition", cascade="all, delete-orphan")


class Export(Base):
    """导出记录表"""

    __tablename__ = "exports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    composition_id = Column(
        UUID(as_uuid=True),
        ForeignKey("compositions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    resolution = Column(String(10), nullable=False)  # 720p/1080p
    file_path = Column(String(500), nullable=True)
    file_url = Column(String(500), nullable=True)
    status = Column(String(20), default="pending", nullable=False)  # pending/completed/failed
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # 关联
    composition = relationship("Composition", back_populates="exports")


class ShareLink(Base):
    """分享链接表"""

    __tablename__ = "share_links"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    composition_id = Column(
        UUID(as_uuid=True),
        ForeignKey("compositions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    token = Column(String(64), unique=True, nullable=False, index=True)
    expires_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # 关联
    composition = relationship("Composition", back_populates="share_links")
