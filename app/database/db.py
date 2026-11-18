from pathlib import Path
from sqlalchemy import create_engine, event
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB = Path(__file__).resolve().parents[2] / "campushub.db"

engine = create_engine(
    f"sqlite:///{DB.as_posix()}",
    connect_args={"check_same_thread": False},
    future=True,
)

@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

Session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)

class Base(DeclarativeBase):
    pass

def init_db():
    from app.database import models

    Base.metadata.create_all(engine)