from aiogram import Bot, Dispatcher, types, executor
import sqlite3
import logging
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

token = "6493590508:AAFde2H_l8GkquL6uLB0c7ww00A9NUaua9A"

storage = MemoryStorage()

bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

conn = sqlite3.connect('resume_bot.db')
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

class ResumeState(StatesGroup):
    get_full_name = State()
    get_age = State()
    get_email = State()
    get_phone_number = State()
    get_experience = State()

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.answer("Привет! Анкета тут /resume")

@dp.message_handler(commands=['resume'])
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
    await message.answer("Какой у вас стаж работы")

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


