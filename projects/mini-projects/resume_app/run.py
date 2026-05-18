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
>>>>>>> 8ee2b4665817a3550d1895555cb83836724637f7
