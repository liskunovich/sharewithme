from sqlalchemy.orm import relationship

from .base import Base

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


class Post(Base):
    __tablename__ = 'post'
    theme_id = Column(UUID(as_uuid=True), ForeignKey('theme.id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    verified = Column(Boolean, default=False)

    theme = relationship("Theme", back_populates="posts")

    def __str__(self):
        return str(self.title) or str(self.description[0:20])
