from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, \
    KeyboardButton, \
    InlineKeyboardMarkup, \
    InlineKeyboardButton


main_menu = ReplyKeyboardMarkup (
    keyboard = [
        [
            KeyboardButton(text='управление'),
            KeyboardButton(text='информация о смс')
        ],
        [
            KeyboardButton(text='создать заявку'),
            KeyboardButton(text='в работе')
        ],
        [
            KeyboardButton(text='заказать пропуск'),
            KeyboardButton(text='активные пропуска')
        ],
        [
            KeyboardButton(text='пропуска за текущие сутки'),
        ]
    ]
)
