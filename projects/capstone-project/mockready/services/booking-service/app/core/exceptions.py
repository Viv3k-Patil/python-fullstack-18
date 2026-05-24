"""
core/exceptions.py

Custom exceptions — raised in service layer.
In Phase 4 we add global handlers that auto-convert
these into the standard error envelope. For now
routers catch them manually.
"""

class MockReadyException(Exception):
    def __init__(self, message: str, code: str = "ERROR"):
        self.message = message
        self.code = code
        super().__init__(message)

class NotFoundException(MockReadyException):
    def __init__(self, message: str):
        super().__init__(message, code="NOT_FOUND")

class ConflictException(MockReadyException):
    def __init__(self, message: str):
        super().__init__(message, code="CONFLICT")

class UnauthorizedException(MockReadyException):
    def __init__(self, message: str):
        super().__init__(message, code="UNAUTHORIZED")

class ForbiddenException(MockReadyException):
    def __init__(self, message: str):
        super().__init__(message, code="FORBIDDEN")

class ValidationException(MockReadyException):
    def __init__(self, message: str):
        super().__init__(message, code="VALIDATION_ERROR")