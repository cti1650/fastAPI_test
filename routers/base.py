from fastapi import APIRouter
from . import health, robots

router = APIRouter()

router.include_router(health.router)
router.include_router(robots.router)