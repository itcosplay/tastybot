from aiogram import types
from aiogram.dispatcher.filters import Command, Text

from bot import bot, dp
from config import ADMIN_ID
from keyboards import main_menu
from service_google_api import google_service, spreadsheet_id


async def send_to_admin(dp):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот запущен')


async def close_bot_message(bp):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот остановлен')


@dp.message_handler(Command('start'))
async def echo(message: types.Message):
    user = types.User.get_current()
    text = \
        f'Добро пожаловать, {user.first_name}. ' + \
        'Используйте команды из меню ниже.'

    await bot.send_message(ADMIN_ID, text, reply_markup=main_menu)


@dp.message_handler(Text(equals='информация о смс'))
async def get_info(message: types.Message):
    values = google_service().spreadsheets().values().get (
        spreadsheetId = spreadsheet_id,
        range = 'A6',
        majorDimension = 'COLUMNS'
    ).execute()

    await bot.send_message (
        ADMIN_ID,
        text = str(values['values']),
        reply_markup=types.ReplyKeyboardRemove()
    )