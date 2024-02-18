from aiogram import Bot,Dispatcher, types, executor
from bs4 import BeautifulSoup
from config import Token
import requests
import sqlite3
import logging
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage



bot = Bot(Token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

conn = sqlite3.connect('nout_bot.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS resumes (
user_id INTEGER PRIMARY KEY,
full_name VARCHAR (100) NOT NULL,
email TEXT DEFAULT NULL,
phone_number TEXT,
adress TEXT
)""")

conn.commit()


start_buttons = [
    types.KeyboardButton('Ноутбуки'),
    types.KeyboardButton('Отправить')
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Здрастувуйте вас привествует ноутбук-магазин Sulpak что хотите: ", reply_markup=start_keyboard)



nout_buttons = [
    types.KeyboardButton('/Acer'),
    types.KeyboardButton('/Huawei'),
    types.KeyboardButton('/Lenovo'),
    types.KeyboardButton('/hp'),
    types.KeyboardButton('/Macbook')
] 

nout_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*nout_buttons)

@dp.message_handler(text='Ноутбуки')
async def nout(message: types.Message):
    await message.answer("Это раздел ноутбуков выберите: ", reply_markup=nout_keyboard)

@dp.message_handler(commands='Acer')
async def start(message:types.Message):
    await message.answer("Топ ноутбуков от фирмы Acer в магазине Barmak:")
    url = 'https://barmak.store/category/Acer/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")


    for name, price in zip(all_laptops_name, all_laptops_price):
        await message.answer(f"{name.text} - {price.text}")

@dp.message_handler(commands='Asus')
async def start(message:types.Message):
    await message.answer("Топ ноутбуков от фирмы Asus в магазине Barmak:")
    url = 'https://barmak.store/category/Asus/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

@dp.message_handler(commands='hp')
async def start(message:types.Message):
    await message.answer("Топ ноутбуков от фирмы hp в магазине Barmak:")
    url = 'https://barmak.store/category/Hp/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")


    for name, price in zip(all_laptops_name, all_laptops_price):
        await message.answer(f"{name.text} - {price.text}")


@dp.message_handler(commands='Lenovo')
async def start(message:types.Message):
    await message.answer("Топ ноутбуков от фирмы Lenovo в магазине Barmak:")
    url = 'https://barmak.store/category/Lenovo/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")


    for name, price in zip(all_laptops_name, all_laptops_price):
        await message.answer(f"{name.text} - {price.text}")


@dp.message_handler(commands='Macbook')
async def start(message:types.Message):
    await message.answer("Топ ноутбуков от фирмы Apple в магазине Barmak:")
    url = 'https://barmak.store/category/Macbook/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")


    for name, price in zip(all_laptops_name, all_laptops_price):
        await message.answer(f"{name.text} - {price.text}")


    
@dp.message_handler(commands='Huawei')
async def start(message:types.Message):
    await message.answer("Топ ноутбуков от фирмы Huawei в магазине Barmak:")
    url = 'https://barmak.store/category/HUawei/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")


    for name, price in zip(all_laptops_name, all_laptops_price):
        await message.answer(f"{name.text} - {price.text}")



class ResumeState(StatesGroup):
    get_full_name = State()
    get_email = State()
    get_phone_number = State()
    get_adress = State()
    get_age = State()
    

@dp.message_handler(text='Отправить')
async def start_resume(message: types.Message):
    await ResumeState.get_full_name.set()
    await message.reply("Введите свое полное имя:")

async def start_resume(message: types.Message):
    await ResumeState.get_full_name.set()
    await message.answer("Введите ваше полное имя:")

@dp.message_handler(state=ResumeState.get_full_name)
async def full_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['full_name'] = message.text

    await ResumeState.next()
    await message.answer("Введите ваш возраст")

@dp.message_handler(state=ResumeState.get_age)
async def age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await ResumeState.next()
    await message.answer("Введите ваш email")

@dp.message_handler(state=ResumeState.get_email)
async def email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text

    await ResumeState.next()
    await message.answer("Введите ваш номер телефона")

@dp.message_handler(state=ResumeState.get_phone_number)
async def phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text

    await ResumeState.next()
    await message.answer("Где ваш Адрес?")

@dp.message_handler(state=ResumeState.get_adress)
async def experience(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text

    cursor.execute("""
INSERT OR REPLACE INTO resumes (user_id, full_name, age,  email, phone_number, experience)
VALUES (?, ?, ?, ?, ? , ?)""", (message.from_user.id, data['full_name'], data['email'], data['phone_number'], data['adress']))
    conn.commit()
       
    await state.finish()
    await message.reply("Спасибо! Ваше ноутбук было успешно отправлено.")




cursor.execute("""
CREATE TABLE IF NOT EXISTS cart (
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    PRIMARY KEY (user_id, product_id)
)""")
conn.commit()

@dp.message_handler(commands=['add_to_cart'])
async def add_to_cart(message: types.Message, state: FSMContext):
    product_id = message.text.split(' ')[1]
    user_id = message.from_user.id
    cursor.execute("INSERT INTO cart (user_id, product_id, quantity) VALUES (?, ?, 1)", (user_id, product_id))
    conn.commit()
    await message.reply("Товар добавлен в корзину.", reply_markup=nout_keyboard)

@dp.message_handler(commands=['view_cart'])
async def view_cart(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    cursor.execute("SELECT product_id, quantity FROM cart WHERE user_id=?", (user_id,))
    cart_contents = cursor.fetchall()
    if not cart_contents:
        await message.answer("Корзина пуста.", reply_markup=nout_keyboard)
    else:
        cart_items = []
        for product_id, quantity in cart_contents:
            cart_items.append(f"Товар {product_id}: {quantity} шт.")
        cart_contents_str = "\n".join(cart_items)
        await message.answer(f"Содержимое корзины:\n{cart_contents_str}", reply_markup=nout_keyboard)

@dp.message_handler(commands=['checkout'])
async def checkout(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    cursor.execute("DELETE FROM cart WHERE user_id=?", (user_id,))
    conn.commit()
    await message.answer("Заказ оформлен. Корзина очищена.", reply_markup=nout_keyboard)


    



executor.start_polling(dp)