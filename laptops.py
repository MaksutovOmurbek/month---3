from aiogram import Bot, Dispatcher, types, executor
from bs4 import BeautifulSoup
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import Token
import requests
import sqlite3
import logging
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext





bot = Bot(Token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


connect = sqlite3.connect("nout_bot.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS goods(
        id INTEGER PRIMARY KEY,
        title TEXT,
        price INTEGER
);
""")
connect.commit()


class ResumeState(StatesGroup):
    title = State()
    price = State()
    get_full_name = State()
    get_address = State()
    get_email = State()
    get_phone_number = State()
    get_laptop = State()


@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Здравствуйте, вас приветствует магазин ноутбуков Barmak.Store чтобы сделать покупки нажмите /help")
   
@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.reply("Доступные команды:\n"
                        "/start - начать чат\n"
                        "/info - Информация о магазине ноутбуков https://www.barmak.store\n"
                        "/laptops - Отправляет ноутбуки в наличии\n"
                        "/help - вывести список доступных команд\n"
                        "/buy - Купить ноутбук \n"
                        "/bucket - посмотреть корзину")
                        

@dp.message_handler(commands='laptops')
async def send_laptops(message:types.Message):
    await message.answer("Отправляю ноутбуки в наличии....")
    url = f'https://www.barmak.store/category/Laptop/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    all_laptops = soup.find_all('div', class_='tp-product-tag-2')
    all_prices = soup.find_all('span', class_='tp-product-price-2 new-price')

    for name, price in zip(all_laptops, all_prices):
        await message.answer(f"{name.text} - {price.text}")
    await message.answer("Вот все ноутбуки в наличии")

@dp.message_handler(commands='bucket')
async def bucket(message: types.Message):
    cursor.execute("SELECT * FROM goods")
    title1 = cursor.fetchall()
    await message.answer(f"ваша корзина: {title1}\n\n")

@dp.message_handler(commands='buy')
async def order_foor(message:types.Message):
    await message.answer(f"Введите название товара ")
    await ResumeState.title.set()
    
@dp.message_handler(state=ResumeState.title)
async def ordes(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await message.answer("цена товара: ")
    await ResumeState.next()

@dp.message_handler(state=ResumeState.price)
async def food_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
        
    async with state.proxy() as data:
        title = data['title']
        price = data['price']
        
    cursor.execute('''
        INSERT INTO goods (title, price)
        VALUES (?, ?)''', (title, price))
    connect.commit()


    await state.finish()
    await message.answer("Ваш товар корзине можете посмотреть /bucket")



executor.start_polling(dp, skip_updates=True)




