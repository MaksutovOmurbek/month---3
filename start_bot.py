from aiogram import Bot, Dispatcher, types, executor

bot = Bot(token='6429382673:AAGz_-kiSVT-GQEhO1H9bFSg8gd-WfZFa2c')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("привет Geeks")

@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.answer("Чем могу вам помочь?")


@dp.message_handler(text='Geeks')
async def Geeks(message:types.Message): 
    await message.answer("Geeks - айти школа в Оше и Бишкеке ")


@dp.message_handler(commands='test')
async def test(message:types.Message):
    print(message)
    await message.answer(f"Здраствуйте {message.from_user.full_name}")
    await message.answer(f"ваш username @{message.from_user.username}")
    await message.reply("reply - это выделение текста и ответ к нему")
    await message.answer_location(40.5193216724554, 72.8030109959693)
    await message.answer_photo('https://masterpiecer-images.s3.yandex.net/92c9a31b731d11eea116261105627a54:upscaled')
    await message.answer_contact('+996558602060', 'Maksutov', 'Omurbek')
    await message.answer_dice('🎰')
    with open('voice.m4a', 'rb') as my_voice:
        await message.answer_audio(my_voice)



@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("вас не понял, введите /help ")

    executor.start_polling(dp)





