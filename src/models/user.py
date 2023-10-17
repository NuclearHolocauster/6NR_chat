from uuid import uuid4

from .base import *


class User(Base):
    __tablename__ = 'user'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True)
    name = Column(String(256), nullable=False, index=True)
    login = Column(String(256), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    
