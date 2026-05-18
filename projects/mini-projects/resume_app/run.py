<<<<<<< HEAD
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
=======
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
>>>>>>> ea3141f4e13ba1afa5fb4513ad9ddaf7245c89d2
