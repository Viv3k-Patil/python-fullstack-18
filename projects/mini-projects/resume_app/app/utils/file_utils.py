"""
Utility helpers for validating uploaded files.
"""

import logging

from fastapi import UploadFile

from app.exceptions.custom_exception import FileTooLargeException, InvalidFileTypeException

logger = logging.getLogger(__name__)

ALLOWED_CONTENT_TYPES = {"application/pdf"}
ALLOWED_EXTENSIONS = {".pdf"}
MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024


async def validate_pdf_file(file: UploadFile) -> bytes:
    """
    Reads the file into memory and validates:
    - Content-type header is application/pdf
    - File extension is .pdf
    - File size does not exceed MAX_FILE_SIZE_BYTES
    - File starts with the PDF magic bytes (%PDF-)

    Returns the raw bytes on success; raises appropriate exceptions on failure.
    """
    logger.info(
        "Validating upload | filename=%s | content_type=%s",
        file.filename,
        file.content_type,
    )

    # --- Content-type check ---
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        logger.warning("Rejected upload — bad content-type: %s", file.content_type)
        raise InvalidFileTypeException()

    # --- Extension check ---
    filename = file.filename or ""
    if not any(filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS):
        logger.warning("Rejected upload — bad extension: %s", filename)
        raise InvalidFileTypeException()

    # --- Read into memory ---
    file_bytes: bytes = await file.read()

    # --- Size check ---
    if len(file_bytes) > MAX_FILE_SIZE_BYTES:
        logger.warning(
            "Rejected upload — file too large: %d bytes (max %d MB)",
            len(file_bytes),
            MAX_FILE_SIZE_MB,
        )
        raise FileTooLargeException(MAX_FILE_SIZE_MB)

    # --- Magic bytes check (%PDF-) ---
    if not file_bytes.startswith(b"%PDF-"):
        logger.warning("Rejected upload — file does not start with PDF magic bytes.")
        raise InvalidFileTypeException()

    logger.info("File validation passed | size=%d bytes", len(file_bytes))
    return file_bytes