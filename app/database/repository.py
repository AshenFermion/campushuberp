from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.database.db import Session
from app.utils.singleton import DatabaseSessionFactory

class Repository:
    """Handles database reads and writes."""

    def _dict(self, obj):
        record = {}

        for column in obj.__table__.columns:
            value = getattr(obj, column.name)

            if hasattr(value, "isoformat"):
                value = value.isoformat()

            record[column.name] = value

        return record

    def add(self, model, obj):
        with DatabaseSessionFactory().session_factory() as session:
            try:
                session.add(obj)
                session.commit()
                session.refresh(obj)
                return self._dict(obj)
            except IntegrityError as error:
                session.rollback()
                raise ValueError(
                    "Duplicate ID, email, or relationship constraint"
                ) from error

    def get(self, model, key, value):
        with DatabaseSessionFactory().session_factory() as session:
            obj = session.get(model, value)
            return self._dict(obj) if obj else None

    def list(self, model):
        with DatabaseSessionFactory().session_factory() as session:
            records = session.scalars(select(model)).all()
            return [self._dict(record) for record in records]

    def update(self, model, key, value, data):
        with DatabaseSessionFactory().session_factory() as session:
            obj = session.get(model, value)

            if obj is None:
                return None

            for field, new_value in data.items():
                if field != key and new_value is not None and hasattr(obj, field):
                    setattr(obj, field, new_value)

            try:
                session.commit()
                session.refresh(obj)
                return self._dict(obj)
            except IntegrityError as error:
                session.rollback()
                raise ValueError(
                    "Duplicate email or invalid update"
                ) from error

    def delete(self, model, key, value):
        with DatabaseSessionFactory().session_factory() as session:
            obj = session.get(model, value)

            if obj is None:
                return False

            try:
                session.delete(obj)
                session.commit()
                return True
            except IntegrityError as error:
                session.rollback()
                raise ValueError(
                    "Cannot delete a record that is referenced by another record"
                ) from error

repo = Repository()