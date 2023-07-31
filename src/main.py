from functools import lru_cache
from typing import Annotated
from fastapi import Depends, FastAPI
from config import Settings




app = FastAPI()

@lru_cache()
def get_settings():
    return Settings()


@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "DEFAULT_ENV" : settings.DEFAULT_ENV,
        "TEST_ENV": settings.TEST_ENV,
        "NAMESPACE":settings.NAMESPACE,
        "APPLICATION": settings.APPLICATION
        }

