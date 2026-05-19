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
<<<<<<< HEAD
>>>>>>> 8ee2b4665817a3550d1895555cb83836724637f7
=======
>>>>>>> ea3141f4e13ba1afa5fb4513ad9ddaf7245c89d2
>>>>>>> 1cbf00331909a46a54aae8247e9731cb55397e45
