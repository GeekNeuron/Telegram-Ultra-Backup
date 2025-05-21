# User Guide

## Introduction
Welcome to **Telegram-Ultra-Backup**! This bot helps you automatically back up posts from public Telegram channels to your personal channels. Follow this guide to get started and make the most out of the bot.

## Getting Started

### 1. Start the Bot
- Open your Telegram app and search for your bot.
- Start a conversation with the bot by sending the `/start` command.
- Select your preferred language from the options provided.

### 2. Add a Backup
- Once you've selected your language, you'll see the main menu.
- Click on **"Add Backup"** to configure a new backup.
- Enter the **source channel ID** (without the `@` symbol).
- Enter the **target channel ID** (without the `@` symbol).
- Confirm the backup settings by clicking **"Confirm"**.

### 3. Manage Backups
- Click on **"List Backups"** to view all your configured backups.
- Each backup will show the source and target channels.
- You can delete backups by clicking on the **"Delete"** button next to each backup.

### 4. Admin Panel
- If you are an admin, you can access the admin panel by sending the `/admin` command.
- Enter the admin password to log in.
- The admin panel allows you to:
  - View all active backups.
  - Update transfer intervals.
  - Manage clone registrations.

## Admin Features

### 1. Admin Login
- Send the `/admin` command to access the admin panel.
- Enter the admin password to log in.

### 2. View Backups
- Navigate to the admin panel and click on **"Manage Backups"**.
- You will see a list of all active backups with their source, target, last run time, and interval.

### 3. Update Backup Intervals
- In the admin panel, click on **"Manage Backups"**.
- Click on the **"Update Interval"** button next to the backup you want to modify.
- Enter the new interval in seconds (minimum 900 seconds, maximum 86400 seconds).

### 4. Cloning Control
- Navigate to the admin panel and click on **"Cloning Control"**.
- You will see a list of all registered clones.
- You can approve or reject clone requests from this panel.

### 5. Logout
- In the admin panel, click on **"Logout"** to log out of the admin session.

## Language Support
Telegram-Ultra-Backup supports 14 languages:
- English
- Russian
- Chinese
- Hindi
- Spanish
- Arabic
- Turkish
- Italian
- Portuguese
- German
- French
- Korean
- Japanese
- Persian

You can change your language at any time by sending the `/start` command and selecting a new language.

## Cloning the Bot

### 1. Clone the Bot
- Go to [@BotFather](https://t.me/BotFather) on Telegram.
- Type `/newbot` and follow the instructions to create a new bot.
- Note down the new bot's API credentials and bot token.

### 2. Register the Clone
- Send the `/clone` command to your original bot.
- Provide the new bot's ID and your user ID.
- The original bot will send a confirmation code to the admin panel.

### 3. Approve the Clone
- Log in to the admin panel at `http://localhost:8000/backups`.
- Approve the clone request by entering the confirmation code.
- The new bot will now be able to manage backups.

## Troubleshooting

### 1. Bot Not Responding
- Ensure that your bot is running properly.
- Check Docker logs for any errors:
  ```bash
  docker logs <container_id>
  ```

### 2. Language Not Working
- Send the `/start` command to reset your language selection.
- Ensure that the language file exists in the `bot/translations/` directory.

### 3. Cloning Issues
- Ensure that your `ADMINS` variable includes your Telegram ID.
- Verify that the `CLONE_CONFIRMATION_CODE` matches the one used in the bot.
- Check the admin panel for any pending clone requests.

### 4. Transfer Errors
- If you encounter errors during transfer, check the logs in the admin panel.
- Ensure that the source and target channels are public and accessible.

## Example Commands

### 1. Add Backup
- Send `/start` to your bot.
- Click on **"Add Backup"**.
- Enter the source channel ID (e.g., `source_channel`).
- Enter the target channel ID (e.g., `target_channel`).
- Click **"Confirm"** to add the backup.

### 2. List Backups
- Send `/start` to your bot.
- Click on **"List Backups"**.
- View all your configured backups.

### 3. Admin Login
- Send `/admin` to your bot.
- Enter the admin password to log in.

### 4. Access Admin Panel
- Open the admin panel in your browser:
  ```bash
  http://localhost:8000/backups
  ```

## Final Notes
- Ensure all environment variables are correctly set before running the Docker container.
- Regularly check logs and manage backups through the admin panel.
- Keep the project updated with the latest security patches and improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for more details.
