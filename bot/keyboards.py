from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from translations import load_translation

def main_keyboard(lang='en'):
    t = load_translation(lang)
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(t['button_send']))
    return kb
