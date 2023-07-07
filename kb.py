from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="📝 Предложить новость", callback_data="send_post"),
    InlineKeyboardButton(text="🖼 Наши ресурсы", callback_data="generate_image")],
]

image_request = [
    [InlineKeyboardButton(text="✅ Да", callback_data="send_image"),
     InlineKeyboardButton(text="❗️ Нет", callback_data="accept_post")],
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
image_request = InlineKeyboardMarkup(inline_keyboard=image_request)

exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])