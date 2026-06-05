
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from dotenv import load_dotenv


<<<<<<< HEAD:projects/capstone-project/mockready/database/database.py
=======
#load_dotenv()
#DATABASE_URL = os.getenv("DATABASE_URL")


>>>>>>> 4808daaa (booking service file changes some code):projects/capstone-project/mockready/services/booking-service/app/db/session.py
DATABASE_URL = "postgresql://neondb_owner:npg_W3cyKHnXL9dl@ep-quiet-voice-aplrv8k0-pooler.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# DB Session Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()