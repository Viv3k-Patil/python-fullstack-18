"""
Middleware that logs every incoming request and outgoing response.
"""

import logging
import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        start = time.perf_counter()
        logger.info(
            "→ REQUEST  | %s %s | client=%s",
            request.method,
            request.url.path,
            request.client.host if request.client else "unknown",
        )

        try:
            response: Response = await call_next(request)
        except Exception:
            logger.exception("Middleware caught unhandled exception.")
            raise

        elapsed_ms = (time.perf_counter() - start) * 1000
        logger.info(
            "← RESPONSE | %s %s | status=%d | %.1f ms",
            request.method,
            request.url.path,
            response.status_code,
            elapsed_ms,
        )
        return response