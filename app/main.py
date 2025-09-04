from fastapi import FastAPI

from app.api.health import router as healthcheck_router
from app.api.endpoints import router as endpoint_router

router = FastAPI(version="1.0.0")

router.include_router(healthcheck_router)
router.include_router(endpoint_router)