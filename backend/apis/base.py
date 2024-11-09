from fastapi import APIRouter
from apis.v1 import route_user
from apis.v1 import route_blog
from apis.v1 import route_login 


api_router=APIRouter()
api_router.include_router(route_user.router,prefix="/user",tags=["user"])
api_router.include_router(route_blog.router,prefix="/blog",tags=["blog"])
api_router.include_router(route_login.router,prefix="/login",tags=[""])