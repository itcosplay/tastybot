from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, \
    KeyboardButton, \
    InlineKeyboardMarkup, \
    InlineKeyboardButton


button1 = KeyboardButton('админ панель')
button2 = KeyboardButton('инф об смс')
button3 = KeyboardButton('заявка')
button4 = KeyboardButton('в работе')
button5 = KeyboardButton('заказать пропуск')
button6 = KeyboardButton('активные пропуска')
button7 = KeyboardButton('пропуска за текущие сутки')

markup = ReplyKeyboardMarkup(resize_keyboard=True).row (
    button1, button2
).row (
    button3, button4
).row (
    button5, button6
).add(button7)