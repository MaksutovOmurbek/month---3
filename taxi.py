from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from logging import basicConfig, INFO
import sqlite3
from datetime import datetime

token = '7106836516:AAHdrX2n783ZcMNhVRaKnEEkt0uYCIaVL64'


bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
basicConfig(level=INFO)

taxi = [
    types.InlineKeyboardButton('Сайт', callback_data='https://taxi.yandex.ru/'),
    types.InlineKeyboardButton('Заказать', callback_data='ybihss' )]

taxi_l = types.InlineKeyboardMarkup().add(*taxi)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer('Здраствуйте', reply_markup=taxi_l)


# @dp.message_handler(text='Сайт')
# async def start(message:types.Message):
    # await message.reply('https://taxi.yandex.ru/')



executor.start_polling(dp)








 

