# Installation Guide

## Prerequisites
- **Docker** installed on your server or local machine.
- **Telegram API credentials** (`API_ID`, `API_HASH`) from [my.telegram.org](https://my.telegram.org).
- **Bot token** from [@BotFather](https://t.me/BotFather).

## Setup Steps

### 1. Clone Repository
```bash
git clone https://github.com/GeekNeuron/Telegram-Ultra-Backup.git
cd Telegram-Ultra-Backup
```

### 2. Configure Environment Variables
Copy the example file:
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```env
API_ID=YOUR_TELEGRAM_API_ID
API_HASH=YOUR_TELEGRAM_API_HASH
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
ADMINS=YOUR_TELEGRAM_USER_ID
CLONE_CONFIRMATION_CODE=YOUR_SECRET_CODE
```

- **API_ID**: Your Telegram API ID.
- **API_HASH**: Your Telegram API Hash.
- **BOT_TOKEN**: Token received from @BotFather.
- **ADMINS**: Your Telegram user ID (comma-separated for multiple admins).
- **CLONE_CONFIRMATION_CODE**: Secret code for clone registration.

### 3. Build Docker Image
```bash
docker build -t telegram-backup .
```

### 4. Run the Stack
```bash
docker run -d \
  -e API_ID=${API_ID} \
  -e API_HASH=${API_HASH} \
  -e BOT_TOKEN=${BOT_TOKEN} \
  -e ADMINS=${ADMINS} \
  -e CLONE_CONFIRMATION_CODE=${CLONE_CONFIRMATION_CODE} \
  -p 8000:8000 \
  telegram-backup
```

### 5. Access Admin Panel
Open the admin panel in your browser:
```bash
http://localhost:8000/backups
```

### 6. Verify Deployment
1. **Start the Bot:**
   - Send `/start` to your bot.
   - Select your preferred language.
   - Add a backup by following the prompts.

2. **Check Admin Dashboard:**
   - Go to `http://localhost:8000/backups` to see active backups.
   - Ensure that backups are being transferred according to the set intervals.

3. **Test Cloning:**
   - Clone the bot using @BotFather.
   - Use the `/clone` command in the original bot with the clone ID and user ID.
   - Verify that the clone is registered in the admin panel.

---

### **Verification**
1. **Bot Response:**
   - Send `/start` to your bot and ensure it responds with the language selection menu.
   
2. **Admin Dashboard:**
   - Navigate to `http://localhost:8000/backups` and verify that backups are listed correctly.
   
3. **Cloning:**
   - Clone the bot using @BotFather.
   - Use the `/clone` command with the clone ID and user ID.
   - Ensure the clone is registered in the admin panel.

---

### **Additional Configuration**
- **Custom Intervals:**
  - You can manually update backup intervals using the admin panel or API endpoints.
  
- **Logging:**
  - Logs are stored in `error.log` within the container.
  - Access logs by running:
    ```bash
    docker logs <container_id>
    ```

- **Security:**
  - Ensure your `ADMINS` variable includes only trusted user IDs.
  - Consider adding authentication middleware for the admin panel.

---

### **Troubleshooting**
- **Bot Not Responding:**
  - Check Docker logs:
    ```bash
    docker logs <container_id>
    ```
  
- **Language Not Working:**
  - Send `/start` to reset language selection.
  
- **Cloning Issues:**
  - Ensure `ADMINS` variable includes your Telegram ID.
  - Verify that the `CLONE_CONFIRMATION_CODE` matches the one used in the bot.

---

### **Example Commands**

#### **Build Docker Image**
```bash
docker build -t telegram-backup .
```

#### **Run Docker Container**
```bash
docker run -d \
  -e API_ID=123456789 \
  -e API_HASH=abcdef1234567890abcdef1234567890abcdef \
  -e BOT_TOKEN=123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ \
  -e ADMINS=123456789 \
  -e CLONE_CONFIRMATION_CODE=mysecretcode \
  -p 8000:8000 \
  telegram-backup
```

#### **Access Admin Panel**
```bash
http://localhost:8000/backups
```

---

### **Final Notes**
- Ensure all environment variables are correctly set before running the Docker container.
- Regularly check logs and manage backups through the admin panel.
- Keep the project updated with the latest security patches and improvements.

---

### **License**
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for more details.
