from aiogram import Bot, Dispatcher, types, executor
import logging, aioschedule, asyncio

Token = '7106836516:AAHdrX2n783ZcMNhVRaKnEEkt0uYCIaVL64'


# Инициализация бота и диспетчера
bot = Bot(Token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Обработчик команды 'start'
@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f"{message.from_user.first_name} {message.chat.id}")

# Функция для отправки сообщения
async def send_message():
    await bot.send_message(-4142647964, "Это сообщение приходит каждые 5 секунд")

# Функция для создания задачи отправки сообщения
def schedule_message():
    asyncio.create_task(send_message())

# Планировщик для регулярной отправки сообщений
async def scheduler():
    aioschedule.every(5).seconds.do(schedule_message)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

# Асинхронная функция для запуска при старте бота
async def on_startup(_):
    asyncio.create_task(scheduler())

# Запуск бота
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
