from threading import RLock
class SingletonMeta(type):
    _instances={}; _lock=RLock()
    def __call__(cls,*args,**kwargs):
        with cls._lock:
            if cls not in cls._instances: cls._instances[cls]=super().__call__(*args,**kwargs)
            return cls._instances[cls]
class DatabaseSessionFactory(metaclass=SingletonMeta):
    @property
    def session_factory(self):
        from app.database.db import Session
        return Session
