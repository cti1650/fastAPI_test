import os
from fastapi.responses import PlainTextResponse
from fastapi import APIRouter

router = APIRouter()

DEFAULT_ROBOTS_CONTENT = "User-agent: *\nDisallow: /"


@router.get("/robots.txt")
def generate_robots():
    if os.path.exists("public/robots.txt"):
        with open("public/robots.txt", "r") as f:
            content = f.read()
    else:
        content = DEFAULT_ROBOTS_CONTENT
    return PlainTextResponse(content, media_type="text/plain", status_code=200)
