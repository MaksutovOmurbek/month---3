from aiogram import Bot,Dispatcher, types, executor
from bs4 import BeautifulSoup
from config import Token
import requests
import logging

bot = Bot(Token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

start_buttons = [
    types.KeyboardButton('Ноутбуки'),
    types.KeyboardButton('Телефоны'),
    types.KeyboardButton('Часы'),
    types.KeyboardButton('Наушники'),
    types.KeyboardButton('PowerBank'),
    types.KeyboardButton('Назад')
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Привет!", reply_markup=start_keyboard)

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
async def start(message: types.Message):
    await message.answer("Топ ноутбуков Acer")
        
    url = 'https://www.barmak.store/category/Acer/'
    response = requests.get(url=url) 
    soup = BeautifulSoup(response.text, 'lxml')
 
    all_laptops_name = soup.find_all('div', class_= "tp-product-tag-2")
    all_laptops_price= soup.find_all('span', class_= "tp-product-price-2 new-price")
    

    for name, price in zip(all_laptops_name, all_laptops_price):
        await message.answer(f"{name.text} - {price.text}")


@dp.message_handler(commands='Apple')
async def okk(message: types.Message):
    await message.answer("Топ ноутбуков Apple")
        
    url = 'https://www.barmak.store/category/Apple/'
    response = requests.get(url=url) 
    soup = BeautifulSoup(response.text, 'lxml')
 
    all_laptops_name = soup.find_all('div', class_= "tp-product-tag-2")
    all_laptops_price= soup.find_all('span', class_= "tp-product-price-2 new-price")
    
    
    

    for name, price in zip(all_laptops_name, all_laptops_price):
        await message.answer(f"{name.text} - {price.text}")

@dp.message_handler(commands='Huawei')
async def okk(message: types.Message):
    await message.answer("Топ ноутбуков Huawei")
        
    url = 'https://www.barmak.store/category/Huawei/'
    response = requests.get(url=url) 
    soup = BeautifulSoup(response.text, 'lxml')
 
    all_laptops_name = soup.find_all('div', class_= "tp-product-tag-2")
    all_laptops_price= soup.find_all('span', class_= "tp-product-price-2 new-price")
    
    
    

    for name, price in zip(all_laptops_name, all_laptops_price):
        await message.answer(f"{name.text} - {price.text}")



@dp.message_handler(commands='Lenovo')
async def start(message: types.Message):
    await message.answer("Топ ноутбуков Lenovo")
        
    url = 'https://www.barmak.store/category/lenovo/'
    response = requests.get(url=url) 
    soup = BeautifulSoup(response.text, 'lxml')
 
    all_laptops_name = soup.find_all('div', class_= "tp-product-tag-2")
    all_laptops_price= soup.find_all('span', class_= "tp-product-price-2 new-price")
    

    for name, price in zip(all_laptops_name, all_laptops_price):
        await message.answer(f"{name.text} - {price.text}")


@dp.message_handler(commands='Macbook')
async def okk(message: types.Message):
    await message.answer("Топ ноутбуков Apple")
        
    url = 'https://www.barmak.store/category/Macbook/'
    response = requests.get(url=url) 
    soup = BeautifulSoup(response.text, 'lxml')
 
    all_laptops_name = soup.find_all('div', class_= "tp-product-tag-2")
    all_laptops_price= soup.find_all('span', class_= "tp-product-price-2 new-price")
    
    
    

    for name, price in zip(all_laptops_name, all_laptops_price):
        await message.answer(f"{name.text} - {price.text}")



@dp.message_handler(commands='hp')
async def okk(message: types.Message):
    await message.answer("Топ ноутбуков hp")
        
    url = 'https://www.barmak.store/category/Hp/'
    response = requests.get(url=url) 
    soup = BeautifulSoup(response.text, 'lxml')
 
    all_laptops_name = soup.find_all('div', class_= "tp-product-tag-2")
    all_laptops_price= soup.find_all('span', class_= "tp-product-price-2 new-price")
    
    
    

    for name, price in zip(all_laptops_name, all_laptops_price):
        await message.answer(f"{name.text} - {price.text}")


executor.start_polling(dp)
