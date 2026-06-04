"""
M08: 历史记录模型

History - 项目操作历史
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship

from app.database import Base


class History(Base):
    """项目历史记录表"""

    __tablename__ = "histories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    action_type = Column(
        String(50),
        nullable=False,
        index=True,
    )  # script_generated/script_modified/storyboard_split/shot_modified/image_generated/video_composed/...
    action_summary = Column(Text, nullable=True)
    snapshot = Column(JSONB, nullable=True)  # 操作快照
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    # 关联
    project = relationship("Project", back_populates="histories")
