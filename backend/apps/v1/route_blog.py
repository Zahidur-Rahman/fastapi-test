from fastapi import APIRouter
from fastapi import Request,Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.repositary.blog import list_blogs,retreive_blog
from db.session import get_db
from typing import Optional

templates=Jinja2Templates(directory="templates")


router= APIRouter()





@router.get("/")
def home(request: Request,alert: Optional[str] = None, db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return templates.TemplateResponse(
        "blog/home.html", {"request": request, "blogs": blogs,"alert":alert}
    )



@router.get("/app/blog/{id}")
def blog_detail(request: Request, id: int, db: Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    return templates.TemplateResponse(
        "blog/detail.html", {"request": request, "blog": blog}
    )