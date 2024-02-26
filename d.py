TOKEN = '6664037537:AAGgdjdctiGM_ZqZ6IsT4_UGEPY_1m48Otg'
from config import TOKEN
import random
from aiogram import Bot, Dispatcher, types, executor

bot = Bot(TOKEN) 
dp = Dispatcher(bot)

number = random.randint(1, 3)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Я загадал число от 1 до 3 угадай")

@dp.message_handler(text = ['1'])
async def start(message:types.Message):
  if number == 1:
     await message.reply("Правильно вы отгадали")
     await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')

  elif number != 1:
    await message.reply("Неправильно вы отгадали")
    await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')

@dp.message_handler(text = ['2'])
async def start(message:types.Message):
  if number == 2:
     await message.reply("Правильно вы отгадали")
     await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')

  elif number != 2:
    await message.reply("Неправильно вы отгадали")
    await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')


@dp.message_handler(text = ['3'])
async def start(message:types.Message):
  if number == 3:
     await message.reply("Правильно вы отгадали")
     await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')

  elif number != 3:
    await message.reply("Неправильно вы отгадали")
    await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')


executor.start_polling(dp)


