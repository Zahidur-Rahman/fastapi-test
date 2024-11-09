from fastapi import APIRouter
from apps.v1 import route_blog  # Ensure this import is correct and points to the right module
from apps.v1 import route_login
app_router = APIRouter()

# Include the route with a prefix and tags if needed, otherwise, omit those optional arguments
app_router.include_router(route_blog.router, prefix="", tags=[""],include_in_schema=False)
app_router.include_router(route_login.router, prefix="/auth", tags=[""],include_in_schema=False)
