import logging
from pathlib import Path
LOG_DIR=Path(__file__).resolve().parents[2]/"logs"; LOG_DIR.mkdir(parents=True,exist_ok=True)
def get_logger():
    logger=logging.getLogger("campushub"); logger.setLevel(logging.INFO)
    if not logger.handlers:
        h=logging.FileHandler(LOG_DIR/"application.log",encoding="utf-8"); h.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")); logger.addHandler(h)
    return logger
