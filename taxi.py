from aiogram import Bot, Dispatcher, types, executor
from config import Token
import logging

bot = Bot(Token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

start_inline_buttons = [
    types.InlineKeyboardButton('Заказать'),
    types.InlineKeyboardButton('Наш сайт', url='https://taxi.yandex.com/'),
    types.InlineKeyboardButton('Такси',)
    

]
start_inline_keyboard = types.InlineKeyboardMarkup().add(*start_inline_buttons)

dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Добро Пожаловать Yandex Taxi!!!", reply_markup=start_inline_keyboard)



executor.start_polling(dp)