"""
core/responses.py

Every endpoint returns the same shape. Always.
Frontend never guesses what's coming back.

Success:  { "success": true,  "message": "...", "data": {...} }
Paginated:{ "success": true,  "message": "...", "data": [...], "pagination": {...} }
Error:    { "success": false, "message": "...", "error": {...} }
"""

import math
from typing import Any, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str = "OK"
    data: T


class PaginationMeta(BaseModel):
    total: int
    page: int
    size: int
    pages: int


class PaginatedResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str = "OK"
    data: list[T]
    pagination: PaginationMeta


class ErrorDetail(BaseModel):
    code: str
    message: str
    request_id: str | None = None  # wired up in Phase 4


class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    error: ErrorDetail


# ── Helper functions ─────────────────────────────────────
# Use these inside routers. Don't construct dicts manually.

def success(data: Any, message: str = "OK") -> dict:
    return {"success": True, "message": message, "data": data}


def paginated(
    data: list,
    total: int,
    page: int,
    size: int,
    message: str = "OK",
) -> dict:
    return {
        "success": True,
        "message": message,
        "data": data,
        "pagination": {
            "total": total,
            "page": page,
            "size": size,
            "pages": math.ceil(total / size) if size > 0 else 0,
        },
    }