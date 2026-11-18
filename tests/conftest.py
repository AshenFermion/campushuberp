import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.database.db import Base,Session
from app.main import app
from app.database import db as db_module
from app.database import repository as repository_module
@pytest.fixture
def client(monkeypatch):
    engine=create_engine("sqlite://",connect_args={"check_same_thread":False},poolclass=StaticPool)
    TestingSession=sessionmaker(bind=engine,expire_on_commit=False)
    Base.metadata.create_all(engine)
    monkeypatch.setattr(db_module,"Session",TestingSession)
    monkeypatch.setattr(repository_module,"Session",TestingSession)
    with TestClient(app) as c: yield c
    Base.metadata.drop_all(engine); engine.dispose()
