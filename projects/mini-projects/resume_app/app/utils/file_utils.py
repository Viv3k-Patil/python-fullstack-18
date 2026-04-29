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


    return file_bytes