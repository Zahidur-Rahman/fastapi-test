from datetime import datetime
from sqlalchemy import Column, Boolean, Integer, DateTime, Text, ForeignKey, String
from sqlalchemy.orm import relationship
from db.base_class import Base



class Blog(Base):
    __tablename__ = 'blogs'  # Add this line
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="blogs")
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)
