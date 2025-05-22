# Telegram Ultra Backup – Migration to v1.1

This guide helps you upgrade your existing deployment to version 1.1.

---

## 1. Replace Old Files

### Remove:
- Any file named: `create_bot.py`, `users.json`, `old_config.py`
- Legacy translation folders like: `lang/`, `locale/`, or `.ini` files
- Redundant `requirements.txt` if using Poetry only

### Replace with:
- `pyproject.toml` (from v1.1)
- `translations/` folder (14 full JSON translations)
- `bot/cloud.py`, `bot/cleanup.py`, `bot/database.py`

---

## 2. Update Admin Password

You must replace old plaintext login with secure hashing.

### Step:
- Generate hash using this Python snippet:
```python
import bcrypt
print(bcrypt.hashpw("your-password".encode(), bcrypt.gensalt()).decode())
```
Add the result to your .env file:


ADMIN_PASSWORD_HASH=$2b$12$...


---

3. New Logs Folder

Create a logs directory:

mkdir logs

OR set in .env:

LOG_LEVEL=INFO


---

4. Optional: Switch to GitHub Actions

Create this file: .github/workflows/ci.yml

name: CI
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with: { python-version: '3.10' }
      - run: pip install poetry
      - run: poetry install
      - run: poetry run flake8
      - run: poetry run pytest


---

5. Cleanup Old Files (Optional)

rm -rf __pycache__/ *.log venv/ old/


---

You're now ready to run:

python bot/main.py

And access:

http://localhost:5000/admin/login
