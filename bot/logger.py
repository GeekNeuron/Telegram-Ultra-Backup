import logging
from logging.handlers import RotatingFileHandler
import os

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
log_file = log_dir / "telegram.log"

handler = RotatingFileHandler(log_file, maxBytes=2_000_000, backupCount=5)
formatter = logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
handler.setFormatter(formatter)

logger = logging.getLogger("telegram_backup")
logger.setLevel(LOG_LEVEL)
logger.addHandler(handler)
logger.propagate = False
