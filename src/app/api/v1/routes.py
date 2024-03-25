from fastapi import FastAPI, APIRouter
from .controllers.posts import posts_router


def register_routes(app: FastAPI):
    router = APIRouter(prefix='/api/v1')
    router.include_router(posts_router)
