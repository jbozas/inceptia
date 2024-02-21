from fastapi import FastAPI

import logging

from app.controllers import router
from app.cache import SimpleCache

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

print("init cache")
cache = SimpleCache()
app.include_router(router)


@app.get("/api/healthchecker")
def root():
    return {"message": "FastAPI Bot."}
