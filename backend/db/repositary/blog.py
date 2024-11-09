from sqlalchemy.orm import Session
from schemas.blog import CreateBlog,ShowBlog,UpdateBlog
from db.models.blog import Blog
from fastapi import HTTPException


def create_new_blog(blog:CreateBlog,db:Session,author_id:int):
    blog=Blog(
        title=blog.title,
        slug=blog.slug,
        content=blog.content,
        author_id=author_id
    )

    db.add(blog)
    db.commit()
    db.refresh(blog)

    return blog


def retreive_blog(id:int,db:Session):
    blog=db.query(Blog).filter(Blog.id==id).first()
    return blog

def list_blogs(db:Session):
    blogs=db.query(Blog).filter(Blog.is_active==True).all()
    return blogs

def update_blog_by_id(id: int, blog: UpdateBlog, db: Session, author_id: int ):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    if not blog_in_db:
        return {"error":f"blog with id {id} does not exists"}
    
    if not blog_in_db.author_id==author_id:

         return {"error":f"Only the author can modify this blog"}
    
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    db.add(blog_in_db)
    db.commit()
    db.refresh(blog_in_db)
    return blog_in_db

def delete_blog_by_id(id:int,db:Session,author_id:int):
    blog_in_db=db.query(Blog).filter(Blog.id==id)
    if not blog_in_db.first():
        return {"error":f"Could not find the blog with id {id}"} 
    
    if not blog_in_db.first().author_id==author_id:
        return{"error","Only the author can delet this blog"}
    blog_in_db.delete()
    db.commit()
    return {"msg":f"Blog has been deleted with id {id}"}


