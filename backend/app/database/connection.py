from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = ""

engine = create_engine(DATABASE_URL)

Session_Local = sessionmaker(bind=engine)

base =  declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()