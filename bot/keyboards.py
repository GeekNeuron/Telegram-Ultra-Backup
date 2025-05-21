from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def language_selection_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("English", callback_data="lang_en"),
         InlineKeyboardButton("Russian", callback_data="lang_ru")],
        [InlineKeyboardButton("Chinese", callback_data="lang_zh"),
         InlineKeyboardButton("Hindi", callback_data="lang_hi")],
        [InlineKeyboardButton("Spanish", callback_data="lang_es"),
         InlineKeyboardButton("Arabic", callback_data="lang_ar")],
        [InlineKeyboardButton("Turkish", callback_data="lang_tr"),
         InlineKeyboardButton("Italian", callback_data="lang_it")],
        [InlineKeyboardButton("Portuguese", callback_data="lang_pt"),
         InlineKeyboardButton("German", callback_data="lang_de")],
        [InlineKeyboardButton("French", callback_data="lang_fr"),
         InlineKeyboardButton("Korean", callback_data="lang_ko")],
        [InlineKeyboardButton("Japanese", callback_data="lang_ja"),
         InlineKeyboardButton("Persian", callback_data="lang_fa")]
    ])

def admin_menu_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Manage Backups", callback_data="admin_backups")],
        [InlineKeyboardButton("Cloning Control", callback_data="admin_clones")],
        [InlineKeyboardButton("Logout", callback_data="admin_logout")]
    ])
