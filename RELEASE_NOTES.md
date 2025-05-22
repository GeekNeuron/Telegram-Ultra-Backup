# Telegram Ultra Backup – Release Notes

## Version: 1.1
**Status:** ✅ Stable  
**Release Date:** May 2025  
**Maintainer:** @your-github-username

---

## Highlights

- Admin dashboard statistics (total files, users, storage)
- Secure admin password with bcrypt hash
- Auto-cleanup of expired files
- Amazon S3 optional upload support
- Multilingual support (14 languages)
- Testable with `pytest`
- Deployable with Docker
- GitHub Actions for CI pipeline

---

## Files Added

- `bot/cloud.py`, `bot/cleanup.py`, `bot/keyboards.py`
- `admin/auth.py`, `admin/dashboard.py`, `templates/`
- `translations/*.json`
- `.github/workflows/ci.yml`
- `.env.example`, `.gitignore`, `requirements.txt`

---

## Project Requirements

- Python 3.10+
- PostgreSQL or SQLite
- Telegram Bot Token
- Optional: S3 Credentials

---

## Deployment Options

- **Polling:** local machine, Termux, VPS
- **Webhook:** cloud server with SSL

---

## Maintainer Checklist

- [x] `.env` configured
- [x] Docker builds clean
- [x] Tests pass locally and in CI
- [x] Admin login works
- [x] README and changelog updated

---

> For feedback or issues, open an issue at:  
> https://github.com/your-username/telegram-ultra-backup/issues
