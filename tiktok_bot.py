from aiogram import Bot, Dispatcher, types, executor
from video.config import Token
import logging

bot = Bot(Token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f'привет {message.from_user.full_name},  отправь ссылку на тикток ') 



@dp.message_handler()
async def get_url_tiktok(message:types.Message):
    if 'tiktok.com' in message.text:
        await message.reply("Начинаю скачивать видео......")
    else:
        await message.reply('Я вас не понимаю  заново отправьте')


executor.start_polling(dp)
