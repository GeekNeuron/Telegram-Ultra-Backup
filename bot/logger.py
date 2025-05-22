# bot/logger.py
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import os

# Create logs directory if it doesn't exist
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FILE = log_dir / "telegram.log"

# Setup log handler
handler = RotatingFileHandler(LOG_FILE, maxBytes=2_000_000, backupCount=3)
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# Configure logger
logger = logging.getLogger("telegram-ultra")
logger.setLevel(LOG_LEVEL)
logger.addHandler(handler)
logger.propagate = False
