"""
脚本模型
"""
from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import String, DateTime, Text, ForeignKey, JSON, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
import enum

from app.database import Base


class ScriptSource(str, enum.Enum):
    """脚本来源枚举"""
    AI_GENERATED = "ai_generated"
    USER_UPLOADED = "user_uploaded"
    AI_OPTIMIZED = "ai_optimized"


class Script(Base):
    """脚本表"""
    __tablename__ = "scripts"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id"), unique=True, nullable=False)
    scenes: Mapped[dict] = mapped_column(JSON, nullable=False, default=list)  # 结构化场景数组
    source: Mapped[ScriptSource] = mapped_column(
        SQLEnum(ScriptSource),
        default=ScriptSource.AI_GENERATED,
        nullable=False
    )
    version: Mapped[int] = mapped_column(default=1)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
