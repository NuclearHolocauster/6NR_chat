from uuid import uuid4

from .base import *


class Message(Base):
    __tablename__ = 'message'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True)
    text = Column(String(512))
    # created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    # user_id = Column(ForeignKey("user.id", ondelete='cascade'), nullable=False, index=True)
    user_id = Column(String(100))
