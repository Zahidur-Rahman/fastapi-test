from db.base_class import Base
from sqlalchemy import Column, Boolean, Integer, DateTime, Text, ForeignKey, String
from sqlalchemy.orm import relationship
from .blog import Blog

class User(Base):
    __tablename__ = 'users'  # Add this line to specify the table name

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    blogs = relationship("Blog", back_populates="author")
