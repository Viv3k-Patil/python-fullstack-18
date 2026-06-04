<<<<<<< HEAD
<<<<<<< HEAD
import uvicorn

if __name__=="__main__":
    uvicorn.run("app.main:app",reload=True)
=======
=======
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
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
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
