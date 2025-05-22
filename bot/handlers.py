from aiogram import Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Command
from bot.database import SessionLocal, BackupFile
from bot.cloud import upload_to_s3
from bot.keyboards import main_keyboard
from translations import load_translation
from pathlib import Path
import logging

user_languages = {}
DOWNLOAD_DIR = Path("downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)

async def start_handler(message: Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("English"), KeyboardButton("فارسی"))
    await message.answer("Please choose your language:", reply_markup=kb)

async def language_selected(message: Message):
    lang = "fa" if "فارسی" in message.text else "en"
    user_languages[message.from_user.id] = lang
    t = load_translation(lang)
    await message.answer(t["start"], reply_markup=main_keyboard(lang))

async def echo_handler(message: Message):
    lang = user_languages.get(message.from_user.id, 'en')
    t = load_translation(lang)

    if message.document:
        session = SessionLocal()
        session.add(BackupFile(
            user_id=message.from_user.id,
            file_name=message.document.file_name,
            file_id=message.document.file_id
        ))
        session.commit()
        session.close()

        file_info = await message.bot.get_file(message.document.file_id)
        dest = DOWNLOAD_DIR / f"{message.from_user.id}_{message.document.file_name}"
        await message.bot.download_file(file_info.file_path, destination=dest.open('wb'))

        success = upload_to_s3(dest, f"backups/{message.from_user.id}/{message.document.file_name}")
        msg = t["file_received"] + (" (Cloud)" if success else " (Local)")
        await message.answer(msg)
    else:
        await message.answer(t["send_file"])

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, Command("start"))
    dp.register_message_handler(language_selected, lambda m: m.text in ["English", "فارسی"])
    dp.register_message_handler(echo_handler, content_types=types.ContentType.ANY)
