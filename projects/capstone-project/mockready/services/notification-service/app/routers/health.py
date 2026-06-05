"""
routers/health.py

Two endpoints, two different purposes — teach students this distinction:

/health       → liveness  — is the PROCESS alive?
/health/ready → readiness — are the DEPENDENCIES ready?

Load balancers use liveness.
Kubernetes uses readiness to decide whether to send traffic.
"""

from datetime import datetime, timezone
from fastapi import APIRouter, Depends

from app.core.settings import Settings, get_settings
from app.core.responses import success

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check(settings: Settings = Depends(get_settings)):
    return success(
        data={
            "service": settings.app_name,
            "version": settings.app_version,
            "environment": settings.app_env,
            "status": "alive",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
        message="Service is running",
    )


@router.get("/health/ready")
async def readiness_check(settings: Settings = Depends(get_settings)):
    checks = {
        "postgres": "not_configured", 
        "redis":    "not_configured",
        "kafka":    "not_configured",
    }

    return success(
        data={
            "service": settings.app_name,
            "status": "ready",
            "checks": checks,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
        message="Service is ready",
    )