# Telegram-Ultra-Backup

## Features
- **14 Language Support:** English, Russian, Chinese, Hindi, Spanish, Arabic, Turkish, Italian, Portuguese, German, French, Korean, Japanese, Persian
- **Admin Authentication with 2FA:** Secure access to admin functionalities
- **Automatic Channel Backup:** Transfer posts from public channels to personal channels
- **Cloning Control System:** Register and manage clones with admin approval
- **Web Admin Dashboard:** Monitor and manage backups via a web interface
- **Full Error Logging:** Detailed logs for troubleshooting

## Installation
1. **Clone Repository:**
   ```bash
   git clone https://github.com/GeekNeuron/Telegram-Ultra-Backup.git
   cd Telegram-Ultra-Backup
   ```

2. **Configure Environment Variables:**
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

3. **Build Docker Image:**
   ```bash
   docker build -t telegram-backup .
   ```

4. **Run the Stack:**
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

5. **Access Admin Panel:**
   ```bash
   http://localhost:8000/backups
   ```

## Verification
1. **Start the Bot:**
   - Send `/start` to your bot.
   - Select your preferred language.
   - Add a backup by following the prompts.

2. **Check Admin Dashboard:**
   - Navigate to `http://localhost:8000/backups` to see active backups.
   - Ensure that backups are being transferred according to the set intervals.

3. **Test Cloning:**
   - Clone the bot using @BotFather.
   - Use the `/clone` command in the original bot with the clone ID and user ID.
   - Verify that the clone is registered in the admin panel.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
