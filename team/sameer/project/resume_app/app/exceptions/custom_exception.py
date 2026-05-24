"""
Custom exception hierarchy for the Resume Portal.
"""


class ResumeAppException(Exception):
    """Base exception; caught by the global exception handler."""

    def __init__(self, message: str, status_code: int = 400) -> None:
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class ResumeNotFoundException(ResumeAppException):
    def __init__(self, resume_id) -> None:
        super().__init__(
            message=f"Resume with id '{resume_id}' not found.",
            status_code=404,
        )


class InvalidFileTypeException(ResumeAppException):
    def __init__(self) -> None:
        super().__init__(
            message="Only PDF files are accepted. Please upload a .pdf file.",
            status_code=415,
        )


class FileTooLargeException(ResumeAppException):
    def __init__(self, max_mb: int) -> None:
        super().__init__(
            message=f"File exceeds the maximum allowed size of {max_mb} MB.",
            status_code=413,
        )


class MissingFieldException(ResumeAppException):
    def __init__(self, field: str) -> None:
        super().__init__(
            message=f"Required field '{field}' is missing or empty.",
            status_code=422,
        )