from pyrogram import Client, filters
from bot.keyboards import *
from bot.database import Database
from bot.utils import load_translations
import os
import asyncio

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = [int(id) for id in os.getenv("ADMINS", "").split(",")]

app = Client("TelegramUltraBackup", 
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN)

db = Database()

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(
        load_translations("en")["welcome"],
        reply_markup=language_selection_buttons()
    )

@app.on_callback_query(filters.regex("^lang_"))
async def set_language(client, query):
    lang_code = query.data.split("_")[1]
    db.update_user_language(query.from_user.id, lang_code)
    await query.answer("Language updated")

@app.on_message(filters.command("admin"))
async def admin_login(client, message):
    if message.from_user.id in ADMINS:
        await message.reply("Admin menu opened", reply_markup=admin_menu_buttons())

async def run_backups():
    while True:
        try:
            backups = db.get_all_backups()
            for backup in backups:
                if time.time() - backup.last_run >= backup.interval:
                    await transfer_posts(backup)
            await asyncio.sleep(60)
        except Exception as e:
            await notify_admins(f"Backup error: {str(e)}")

def validate_interval(value):
    if not (900 <= value <= 86400):
        raise ValueError("Interval must be between 15 minutes and 24 hours")

async def transfer_posts(backup):
    async for msg in app.get_chat_history(backup.source):
        await app.copy_message(backup.target, msg.chat.id, msg.id)
    db.update_last_run(backup.id)

if __name__ == "__main__":
    asyncio.run(run_backups())
    app.run()
