import os
from typing import Optional

from fastapi import FastAPI
from routers.health import api_health

app = FastAPI()

api_health(app)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
