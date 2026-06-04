<<<<<<< HEAD
import uvicorn

if __name__=="__main__":
    uvicorn.run("app.main:app",reload=True)
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

>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
