from fastapi.responses import PlainTextResponse
from fastapi import APIRouter

router = APIRouter()

@router.get("/robots.txt")
def generate_robots():
    return PlainTextResponse("User-agent: *\nDisallow: /", media_type="text/plain")