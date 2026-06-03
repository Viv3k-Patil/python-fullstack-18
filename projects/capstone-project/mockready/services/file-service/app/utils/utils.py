# import os
# import shutil

# from fastapi import UploadFile
# from app.core.exception import ConflictException,FileToLargeException,FileNotFoundError

# UPLOAD_DIR = "uploads"
# MAX_FILE_SIZE = 1 * 1024 * 1024


# def upload_file(uploaded_file: UploadFile):

#     os.makedirs(UPLOAD_DIR, exist_ok=True)

#     file_path = os.path.join(
#         UPLOAD_DIR,
#         uploaded_file.filename
#     )

#     # Save file
#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(
#             uploaded_file.file,
#             buffer
#         )

#     # Get file size
#     file_size = os.path.getsize(file_path)

#     # Empty file validation
#     if file_size == 0:
#         os.remove(file_path)

#         raise ConflictException(
#             "Empty file is not allowed"
#         )

#     # Max size validation
#     if file_size > MAX_FILE_SIZE:
#         os.remove(file_path)

#         raise FileToLargeException(
#             "File size exceeds 1 MB limit"
#         )

#     return {
#         "original_name": uploaded_file.filename,
#         "stored_path": file_path,
#         "file_type": uploaded_file.content_type,
#         "size_bytes": file_size
#     }

import os

from fastapi import UploadFile
from app.core.exception import(
    ConflictException,
    FileToLargeException,
    InvalidFileTypeException
)

MAX_FILE_SIZE = 1 * 1024 * 1024


def upload_file(uploaded_file: UploadFile):

    # check file is pdf or not
    if uploaded_file.content_type != "application/pdf":
        raise InvalidFileTypeException(
            "Invalid file type"
        )

    # read file content only
    file_content = uploaded_file.file.read()

    path=f"memory//{uploaded_file.filename}"

    # get file size
    file_size = len(file_content)

    # empty file validation
    if file_size == 0:
        raise ConflictException(
            "Empty file is not allowed"
        )

    # max size validation
    if file_size > MAX_FILE_SIZE:
        raise FileToLargeException(
            "File size is above 1 MB limit"
        )

    return {
        "original_name": uploaded_file.filename,
        "file_type": uploaded_file.content_type,
        "stored_path":path,
        "size_bytes": file_size,
        "content": file_content
    }