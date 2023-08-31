from fastapi.responses import PlainTextResponse
from fastapi import APIRouter

router = APIRouter()

@router.get("/health", response_class=PlainTextResponse)
def health_check():
    return "ok"