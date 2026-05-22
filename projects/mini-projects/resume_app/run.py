"""
Run the Resume Portal with:
    python run.py
or:
    uvicorn app.main:app --reload
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        reload=True,
        log_level="info",
    )

