from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from logging import basicConfig, INFO
import sqlite3
from datetime import datetime

# Инициализация бота, хранилища состояний и диспетчера
bot = Bot('7106836516:AAHdrX2n783ZcMNhVRaKnEEkt0uYCIaVL64')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
basicConfig(level=INFO)


class OrderFoodState(StatesGroup):
    name = State()
    title = State()
    phone_number = State()
    address = State()

# Создание подключения к базе данных SQLite
connect = sqlite3.connect('ojak_kebap.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username VARCHAR(100),
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        date_joined DATETIME
);''')
connect.commit()

cursor.execute(''' CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100),
        title TEXT,
        phone_number VARCHAR(100),
        address VARCHAR(100)
);''')
connect.commit()

# Создание клавиатуры для начала работы с ботом
start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Меню'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('Заказать еду'),
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

# Обработчик команды /start
@dp.message_handler(commands='start')
async def start(message: types.Message):
    cursor.execute(f"SELECT id FROM users WHERE id = {message.from_user.id};")
    res = cursor.fetchall()
    if not res:
        cursor.execute(f"""INSERT INTO users (id, username, first_name, last_name, date_joined) VALUES (
            {message.from_user.id},
            '{message.from_user.username}',
            '{message.from_user.first_name}',
            '{message.from_user.last_name}',
            '{datetime.now()}'
);""")
        cursor.connection.commit()
    await message.answer("Привет! Чтобы сделать заказ, нажмите 'Заказать еду' или воспользуйтесь другими доступными командами.", reply_markup=start_keyboard)

# Обработчик команды "Меню"
@dp.message_handler(text='Меню')
async def menu(message: types.Message):
    await message.answer("Шашлыки'🖇🙌🏻\nhttps://nambafood.kg/ojak-kebap", reply_markup=start_keyboard)

# Обработчик команды "О нас"
@dp.message_handler(text='О нас')
async def about(message: types.Message):
    await message.answer('''Кафе "Ожак Кебап" на протяжении 18 лет радует своих гостей с изысканными турецкими блюдами в особенности своим кебабом.

Наше кафе отличается от многих кафе своими доступными ценами и быстрым сервисом.

В 2016 году по голосованию на сайте "Horeca" были удостоены "Лучшее кафе на каждый день" и мы стараемся оправдать доверие наших гостей.

Мы не добавляем консерванты, усилители вкуса, красители, ароматизаторы, растительные и животные жиры, вредные добавки с маркировкой «Е». У нас строгий контроль качества: наши филиалы придерживаются норм Кырпотребнадзор и санэпидемстанции. Мы используем только сертифицированную мясную и рыбную продукцию от крупных поставщиков''')

# Обработчик команды "Адрес"
@dp.message_handler(text='Адрес')
async def address(message: types.Message):
    await message.answer("📌 Адрес:  234، 246 Курманжан-Датка ул., Ош")

# Обработчик команды "Заказать еду"
@dp.message_handler(text='Заказать еду')
async def order_food(message: types.Message):
    await message.answer('Введите ваше имя: ')
    await OrderFoodState.name.set()

# Обработчик ввода имени
@dp.message_handler(state=OrderFoodState.name)
async def process_food_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Что хотите заказать?")
    await OrderFoodState.title.set()
    

@dp.message_handler(state=OrderFoodState.title)
async def process_food_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await message.answer("Ваш номер:")
    await OrderFoodState.phone_number.set()

@dp.message_handler(state=OrderFoodState.phone_number)
async def process_food_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
    await message.answer("ваш адрес")
    await OrderFoodState.address.set()

@dp.message_handler(state=OrderFoodState.address)
async def experience(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text

    cursor.execute("""
INSERT OR REPLACE INTO orders ( id, name, title,  address, phone_number)
VALUES (?, ?, ?, ?)""", (message.from_user.id, data['name'], data['title'], data['address'], data['phone_number']))
    connect.commit()

    await state.finish()
    await message.answer("Мы сохранили ваши данные")




executor.start_polling(dp, skip_updates=True)

