from functools import wraps
from time import perf_counter
from app.utils.logger import get_logger
log=get_logger()
def log_call(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        print(f"Function Started: {fn.__name__}"); log.info("Started %s",fn.__name__)
        try:return fn(*args,**kwargs)
        finally: print(f"Function Completed: {fn.__name__}"); log.info("Completed %s",fn.__name__)
    return wrapper
def time_call(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start=perf_counter()
        try:return fn(*args,**kwargs)
        finally:
            elapsed=perf_counter()-start; print(f"{fn.__name__} execution time: {elapsed:.6f}s"); log.info("%s took %.6fs",fn.__name__,elapsed)
    return wrapper
def service_operation(fn): return time_call(log_call(fn))
