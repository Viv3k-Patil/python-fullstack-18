<<<<<<< HEAD
from fastapi import UploadFile
from app.exceptions.custom_exception import InvalidFileTypeException, FileTooLargeException
import logging

logger = logging.getLogger(__name__)
async def validate_pdf_file(file: UploadFile) -> bytes:
    """
    Read the file into memory and validates
    checks added:
        - Content-type is .pdf
        - File extension is .pdf
        - File starts with PDF byte checking
        - File size

    Returns the raw bytes on success; raise appropriate except
    """
    # TODO: add logging here
    logger.info(
        "validating upload | filename= "
    )

    #------------- content-type check ---------------------------

    # check if file is pdf or not
    if file.content_type != "application/pdf":
        logger.warn()
        raise InvalidFileTypeException()
    
    #------------- file extension check ---------------------------
    # check if file extension is pdf or not
    filename = file.filename or ""
    if not filename.lower().endswith(".pdf"):
        logger.warn()
        raise InvalidFileTypeException()

    file_bytes = await file.read()
    
    #------------- file extension check ---------------------------
    # check if file is really a pdf
    if not file_bytes.startwith(b"%PDF-"):
        logger.warn()
        raise InvalidFileTypeException()

    #------------- file extension check ---------------------------
    # check if bytes are over 5mb
    if len(file_bytes) > 5*1024*1024:
        logger.warn()
        raise FileTooLargeException(5)


=======
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
<<<<<<< HEAD
>>>>>>> 8ee2b4665817a3550d1895555cb83836724637f7
=======
>>>>>>> ea3141f4e13ba1afa5fb4513ad9ddaf7245c89d2
>>>>>>> 1cbf00331909a46a54aae8247e9731cb55397e45
    return file_bytes