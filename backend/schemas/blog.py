from typing import Optional
from pydantic import BaseModel, model_validator
from datetime import datetime

class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @model_validator(mode="before")
    def generate_slug(cls, value, values):
        # Automatically generate slug from title if not provided
        if not value and 'title' in values:
            return values['title'].replace(" ", "-").lower()
        return value

class UpdateBlog(CreateBlog):
    pass

class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
