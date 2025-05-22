# Telegram Ultra Backup — Changelog

## Version 1.1 – May 2025

### ✅ Added

- **Admin Password Hashing**
  - Passwords are now securely hashed using `bcrypt` instead of hardcoded plaintext.
  - Login system now validates using hash check.

- **Logging System**
  - Integrated Python's `logging` module with rotating log files.
  - Logs are stored in `logs/telegram.log`.

- **Admin Dashboard Statistics**
  - Total file count
  - Unique user count
  - Total backup storage size

- **CI/CD with GitHub Actions**
  - `.github/workflows/ci.yml` runs:
    - `flake8` lint check
    - `pytest` for core functionality

### 🔁 Changed

- Replaced all `print()` calls with structured `logger.info()`/`error()`
- `auth.py` now reads password from `.env` or falls back to hashed constant

### 🛡️ Security

- No credentials or secrets are hardcoded
- `.env` is required for secure setup
- Admin session is cookie-based with JWT

### ⚙️ Dev Tools

- `.gitignore` updated to exclude logs, venvs, cache
- `requirements.txt` added for pip fallback

---

**Tip:**  
For existing deployments, make sure to:
- Update `.env` with `ADMIN_PASSWORD_HASH` or run the hash generator in `auth.py`
- Create a `/logs/` directory if logging is enabled
