from sqlalchemy.orm import relationship

from .base import Base
from sqlalchemy import String, Column


class Theme(Base):
    __tablename__ = 'theme'
    title = Column(String, nullable=False)

    posts = relationship("Post", back_populates="theme")

    def __str__(self):
        return str(self.title)
