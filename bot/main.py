import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.executor import start_polling, start_webhook
from dotenv import load_dotenv
from bot.handlers import register_handlers
from bot.cleanup import cleanup_old_files
from bot.logger import logger

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
RUN_MODE = os.getenv("RUN_MODE", "polling").lower()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
register_handlers(dp)

WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", f"/webhook/{API_TOKEN}")
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
WEBAPP_HOST = os.getenv("WEBAPP_HOST", "0.0.0.0")
WEBAPP_PORT = int(os.getenv("WEBAPP_PORT", 8443))
SSL_CERT = os.getenv("SSL_CERT")
SSL_PRIVKEY = os.getenv("SSL_PRIVKEY")

if __name__ == '__main__':
    cleanup_old_files()
    if RUN_MODE == "polling":
        logger.info("Starting bot in polling mode...")
        start_polling(dp, skip_updates=True)
    elif RUN_MODE == "webhook":
        if not all([WEBHOOK_HOST, SSL_CERT, SSL_PRIVKEY]):
            logger.error("Webhook configuration missing in .env")
            raise RuntimeError("Missing webhook configuration.")
        from aiohttp import web

        async def on_startup(dispatcher):
            await bot.set_webhook(WEBHOOK_URL, certificate=open(SSL_CERT, 'rb'))
            logger.info("Webhook set: %s", WEBHOOK_URL)

        async def on_shutdown(dispatcher):
            await bot.delete_webhook()
            logger.info("Webhook deleted.")

        start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
            ssl_cert=SSL_CERT,
            ssl_private_key=SSL_PRIVKEY
        )
    else:
        logger.error("Invalid RUN_MODE: %s", RUN_MODE)
        raise ValueError("Invalid RUN_MODE in .env")
