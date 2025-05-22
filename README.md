# Telegram Ultra Backup

A professional, secure, and multilingual Telegram bot that receives and stores backup files from users.  
Ideal for admins or services needing structured Telegram file submissions.

---

## Features

- **Async Telegram Bot** using Aiogram
- **Local & Cloud Storage** (local filesystem or Amazon S3)
- **Multilingual Support** (14 languages)
- **Admin Dashboard** with Flask + JWT login
- **Webhook & Polling Modes**
- **Auto File Cleanup** (configurable)
- **Unit Testing** with `pytest`
- **Docker Support**
- **Modular & Extensible Codebase**

---

## Supported Languages

English, فارسی, Español, Français, Italiano, Deutsch, Русский, Português,  
हिन्दी, 日本語, 中文, 한국어, العربية, Türkçe

---

## Installation

### 1. Install Dependencies

```bash
pip install poetry
poetry install
```
### 2. Configure Environment

```bash
cp .env.example .env
```
Then edit `.env` with your actual config.


---

## Running the Bot

### Polling Mode
```bash
python bot/main.py
```
### Webhook Mode
```env
RUN_MODE=webhook
WEBHOOK_HOST=https://yourdomain.com
SSL_CERT=cert.pem
SSL_PRIVKEY=key.pem
```

---

## Admin Panel

**Accessible at**:
http://localhost:5000/admin/login

### Default login
**Username**: admin
**Password**: admin123


---

## Auto-Cleanup

Automatically deletes old files after N hours:
```bash
AUTO_CLEANUP=true
MAX_FILE_AGE_HOURS=72
```
**Disable by setting** AUTO_CLEANUP=false.


---

## Amazon S3 Integration

Enable cloud backup via .env:
```env
USE_S3=true
S3_BUCKET=your-bucket
S3_REGION=your-region
S3_ACCESS_KEY=your-access-key
S3_SECRET_KEY=your-secret-key
```

---

## Running Tests
```bash
pytest
```

---

## Docker Build
```bash
docker build -t telegram-ultra-backup .
docker run -p 8000:8000 telegram-ultra-backup
```

---

## Project Structure
```
Telegram-Ultra-Backup/
├── bot/
├── admin/
├── translations/
├── tests/
├── .env.example
├── Dockerfile
├── pyproject.toml
└── README.md
```

---

## License

MIT License
