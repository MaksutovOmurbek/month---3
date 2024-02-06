# from aiogram import Bot, Dispatcher, types, executor
# from config import Token 
# import logging

# bot = Bot(token=Token)
# dp = Dispatcher(bot)
# logging.basicConfig(level=logging.INFO)

# start_buttons = [
#     types.KeyboardButton('О нас'),
#     types.KeyboardButton('Адрес'),
#     types.KeyboardButton('Курсы'),
#     types.KeyboardButton('Отправить заявку')
# ]
# start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer(f"Здраствуйте {message.from_user.full_name}", reply_markup=start_keyboard)

# @dp.message_handler(text="О нас")
# async def about_us(message:types.Message):
#     await message.reply("Geeks - это айти курсы в Бишкеке, Оше, Кара-Балте и в Ташкенте")

# @dp.message_handler(text='Адрес')
# async def send_address(message:types.Message):
#     await message.answer("Наш адрес: Мырзалы Аматова 1Б")
#     await message.answer_location(40.5193216724554, 72.8030109959693)

# courses_buttons = [
#     types.KeyboardButton('Backend'),
#     types.KeyboardButton('Frontend'),
#     types.KeyboardButton('UX/UI'),
#     types.KeyboardButton('Android'),
#     types.KeyboardButton('iOS'),
#     types.KeyboardButton('Назад')
# ]
# courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_buttons)

# @dp.message_handler(text='Курсы')
# async def send_couses(message:types.Message):
#     await message.answer("Вот наши курсы:", reply_markup=courses_keyboard)

# @dp.message_handler(text='Backend')
# async def backend(message:types.Message):
#     await message.reply("Backend - это внутреняя часть сайта которая не видна вам")

# @dp.message_handler(text="Frontend")
# async def frontend(message:types.Message):
#     await message.reply("Frontend - это лицевая сторона сайта которая видна вам")

# @dp.message_handler(text="UX/UI")
# async def uxui(message:types.Message):
#     await message.reply("UX/UI - это дизайн сайта или приложения")

# @dp.message_handler(text="Android")
# async def android(message:types.Message):
#     await message.reply("Android - это приложение на операционную систему Android")

# @dp.message_handler(text="iOS")
# async def ios(message:types.Message):
#     await message.reply("iOS - это операционная система на Apple")

# @dp.message_handler(text='Назад')
# async def rollback(message:types.Message):
#     await start(message)

# @dp.message_handler()
# async def not_found(message:types.Message):
#     await message.reply("вас не понял, введите /start")

# executor.start_polling(dp)
