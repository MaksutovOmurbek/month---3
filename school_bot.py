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


conn = sqlite3.connect("school.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS resumes (
user_id INTEGER PRIMARY KEY,
full_name VARCHAR (100) NOT NULL,
age INTEGER NOT NULL,
email TEXT DEFAULT NULL,
phone_number TEXT,
experience INTEGER DEFAULT 0
)""")

conn.commit()

sc_buttons = [
    types.KeyboardButton("О нас"),
    types.KeyboardButton("Записаться"),
    types.KeyboardButton("Адрес"),
    types.KeyboardButton("Телефоны"),
    types.KeyboardButton("Режим работы")

]

sc_keybard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*sc_buttons)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f"Здраствуйте {message.from_user.first_name}", reply_markup=sc_keybard)


@dp.message_handler(text='О нас')
async def start(message: types.Message):
    await message.answer("Частная школа Ансар-Тайп мы учим детей по 1 до 7 класс у нас самые хорошие учителя и лучшие ученики мы учим очень хороших учеников")

@dp.message_handler(text='Адрес')
async def start(message: types.Message):
    await message.answer("г. Ош, Алишера Навои, 22")

@dp.message_handler(text='Телефоны')
async def start(message: types.Message):
    await message.answer("""✆ +996 558‒10‒03‒00
✆ +996 505‒10‒03‒00
✆ +996 778‒10‒03‒00""")
    

@dp.message_handler(text='Режим работы')
async def start(message: types.Message):
    await message.answer("""РЕЖИМ РАБОТЫ
ПН
с 08:30
до 17:00
                         
ВТ
с 08:30
до 17:00
 
СР
с 08:30
до 17:00
 
ЧТ
с 08:30
до 17:00
 
ПТ
с 08:30
до 17:00""")
    




class ResumeState(StatesGroup):
    get_full_name = State()
    get_age = State()
    get_email = State()
    get_phone_number = State()
    get_experience = State()


@dp.message_handler(text="Записаться")
async def start_resume(message: types.Message):
    await ResumeState.get_full_name.set()
    await message.answer("Введите Ф.И.О ученика")

@dp.message_handler(state=ResumeState.get_full_name)
async def full_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['full_name'] = message.text

    await ResumeState.next()
    await message.answer("Введите  возраст ученика")

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
    await message.answer("Есть ли у него или у нее особенности")

@dp.message_handler(state=ResumeState.get_experience)
async def experience(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['experience'] = message.text

    cursor.execute("""
INSERT OR REPLACE INTO resumes (user_id, full_name, age,  email, phone_number, experience)
VALUES (?, ?, ?, ?, ? , ?)""", (message.from_user.id, data['full_name'], data['age'], data['email'], data['phone_number'], data['experience']))
    conn.commit()

    await state.finish()
    await message.answer("Мы сохранили ваши данные")
    

executor.start_polling(dp)



    

