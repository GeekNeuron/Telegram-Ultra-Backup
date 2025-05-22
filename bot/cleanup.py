import os
import time
from pathlib import Path

DOWNLOAD_DIR = Path("downloads")
MAX_FILE_AGE_HOURS = int(os.getenv("MAX_FILE_AGE_HOURS", 72))
CLEANUP_ENABLED = os.getenv("AUTO_CLEANUP", "true").lower() == "true"

def cleanup_old_files():
    if not CLEANUP_ENABLED:
        print("[Cleanup] Disabled")
        return
    cutoff = time.time() - (MAX_FILE_AGE_HOURS * 3600)
    deleted = 0
    for file in DOWNLOAD_DIR.iterdir():
        if file.is_file() and file.stat().st_mtime < cutoff:
            file.unlink()
            deleted += 1
    print(f"[Cleanup] {deleted} file(s) deleted.")
