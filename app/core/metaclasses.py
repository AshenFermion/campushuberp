from datetime import datetime, timezone
from abc import ABCMeta

class TimestampMeta(ABCMeta):
    def __new__(cls, name, bases, namespace):
        namespace.setdefault("created_at", None)
        namespace.setdefault("updated_at", None)
        return super().__new__(cls, name, bases, namespace)

def now():
    return datetime.now(timezone.utc)