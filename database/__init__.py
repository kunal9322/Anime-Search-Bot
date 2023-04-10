from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from config import DB_URI

count_ = 0
def start() -> scoped_session:
    if DB_URI == "":
        if count_ < 1:
            count += 1
            return print("Database url not provided..\nBut this time I won't stop 😉")
        return
    engine = create_engine(DB_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

if DB_URI != "":
    BASE = declarative_base()
    SESSION = start()
