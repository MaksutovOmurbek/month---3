from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.storage import FSMContext
import logging, sqlite3, time, os, requests
from config import Token
from bs4 import BeautifulSoup
from parsing import downloader, characteristics

# ========================================================================================================================================

bot = Bot(token=Token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)
carts = []
cart = {
    'Name' : '',
    'Price' : ''
}

# ========================================================================================================================================

connection = sqlite3.connect('data_bases/laptop_customer.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS customer(
    id VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    username VARCHAR(255),
    created VARCHAR(255)
);
""")
connection.commit()

# ========================================================================================================================================

start_buttons = [
    types.KeyboardButton('Laptops'),
    types.KeyboardButton('Cart'),
    types.KeyboardButton('Qustions?'),
    types.KeyboardButton('To add laptop')
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(start_buttons[0]).add(start_buttons[1]).add(start_buttons[2])
admin_start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

# ========================================================================================================================================

@dp.message_handler(commands='start')
async def start(message:types.Message):
    
    if message.from_user.id == 1930629213:
        await message.answer('Hello', reply_markup=admin_start_keyboard)
        print(message)
    else:
        await message.answer('Hello', reply_markup=start_keyboard)

# ========================================================================================================================================

laptops_buttons = [
    types.InlineKeyboardButton('Acer', callback_data='acer_laptop'),
    types.InlineKeyboardButton('Apple', callback_data='apple_laptop'),
    types.InlineKeyboardButton('Asus', callback_data='asus_laptop'),
    types.InlineKeyboardButton('HP', callback_data='hp_laptop'),
    types.InlineKeyboardButton('Huawei', callback_data='huawei_laptop'),
    types.InlineKeyboardButton('Lenovo', callback_data='lenovo_laptop'),
    types.InlineKeyboardButton('MSI', callback_data='msi_laptop'),
]
laptops_keyboard = types.InlineKeyboardMarkup().add(*laptops_buttons)

# ========================================================================================================================================

cart_botton = [
    types.InlineKeyboardButton('Add to cart', callback_data='to_cart')
]
cart_keyboard = types.InlineKeyboardMarkup().add(*cart_botton)

# @dp.callback_query_handler(lambda call: call.data == "to_cart")
# async def to_cart(callback: types.CallbackQuery, cart = cart):
    # for k, v in cart.items():
    # print(f"Name: {cart['Name']}, Price: {cart['Price']}")
    # carts.append(cart)

    
    # for i in lst:
        # print(i)
        # await callback.message.answer(i)

# ========================================================================================================================================

@dp.message_handler(text='Laptops')
async def laptops(message:types.Message):
    await message.answer("Our Laptops:", reply_markup=laptops_keyboard)


        # @dp.callback_query_handler(lambda call: call.data == "to_cart")
        # async def to_cart(callback: types.CallbackQuery):
        #     # for k, v in cart.items():
        #     cart['Name'] = name.text.replace('\n', '')
        #     cart['Price'] = price.text
        #     print(f"Name: {cart['Name']}, Price: {cart['Price']}")
        #     carts.append(cart)

# ========================================================================================================================================



@dp.callback_query_handler(lambda call: call.data == "acer_laptop")
async def start(callback: types.CallbackQuery):
    await callback.message.answer("Top laptops from Acer:")
    url = 'https://www.barmak.store/category/Acer/'
    response = requests.get(url=url)
    soup_text = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup_text.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup_text.find_all('span', class_ = "tp-product-price-2 new-price")

    lst = []
    downloader(url, lst)
    

    for i, name, price in zip(lst, all_laptops_name, all_laptops_price):  
        with open(f"image/acer/{i}.jpg", 'rb') as photo_file:      
            await callback.message.answer_photo(photo_file, f"Title: {name.text}Price: {price.text}\nCharacteristics: {characteristics(url)}", reply_markup=cart_keyboard)

# ========================================================================================================================================

@dp.callback_query_handler(lambda call: call.data == "apple_laptop")
async def start(callback: types.CallbackQuery):
    await callback.message.answer("Top laptops from Apple:")
    url = 'https://www.barmak.store/category/Macbook/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")
    
    lst = []
    downloader(url, lst)

    cart_list = []
    lstt = []

    id = int(callback.message.message_id)
    
    for i, name, price in zip(lst, all_laptops_name, all_laptops_price):  
        with open(f"image/apple/{i}.jpg", 'rb') as photo_file:
            # id = 
            await callback.message.answer_photo(photo_file, f"Title: {name.text}Price: {price.text}\nCharacteristics: {characteristics(url)}\n{time.ctime()}", reply_markup=cart_keyboard)
            # b += 1
            # count = time.ctime()
            cart['Name'] = name.text.replace('\n', '')
            cart['Price'] = price.text

            cart_id = {i : cart['Name'] + ' ' + cart['Price']}
            cart_list.append(cart_id)

            print(cart_list)

            # lstt.append(id)
            # id += 1

        # print(cart_list)
        
@dp.callback_query_handler(lambda call: call.data == "to_cart")
async def to_cart(callback: types.CallbackQuery, lst, cart_list):
        print(cart_list)
        for i, carts in zip(lst, cart_list):
            print(carts[i])
        else:
            print(i)


            # print(lstt)
        #     # for k, v in cart.items():
        #     cart['Name'] = name.text.replace('\n', '')
        #     cart['Price'] = price.text

        #     # print(name.text, price.text)
            
        #     print(f"Name: {cart['Name']}, Price: {cart['Price']}")
        #     carts.append(cart)
        #     print(carts)    

# ========================================================================================================================================

@dp.callback_query_handler(lambda call: call.data == "asus_laptop")
async def start(callback: types.CallbackQuery):
    await callback.message.answer("Top laptops from Asus:")
    url = 'https://www.barmak.store/category/Asus/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")
    
    lst = []
    downloader(url, lst)

    for i, name, price in zip(lst, all_laptops_name, all_laptops_price):  
        with open(f"image/asus/{i}.jpg", 'rb') as photo_file:      
            await callback.message.answer_photo(photo_file, f"Title: {name.text}Price: {price.text}\nCharacteristics: {characteristics(url)}", reply_markup=cart_keyboard)


@dp.callback_query_handler(lambda call: call.data == "hp_laptop")
async def start(callback: types.CallbackQuery):
    await callback.message.answer("Top laptops from HP:")
    url = 'https://www.barmak.store/category/Hp/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")
    
    lst = []
    downloader(url, lst)

    for i, name, price in zip(lst, all_laptops_name, all_laptops_price):  
        with open(f"image/hp/{i}.jpg", 'rb') as photo_file:      
            await callback.message.answer_photo(photo_file, f"Title: {name.text}Price: {price.text}\nCharacteristics: {characteristics(url)}", reply_markup=cart_keyboard)

# ========================================================================================================================================

@dp.callback_query_handler(lambda call: call.data == "huawei_laptop")
async def start(callback: types.CallbackQuery):
    await callback.message.answer("Top laptops from Huawei:")
    url = 'https://www.barmak.store/category/Huawei/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")
    
    lst = []
    downloader(url, lst)

    for i, name, price in zip(lst, all_laptops_name, all_laptops_price):  
        with open(f"image/huawei/{i}.jpg", 'rb') as photo_file:      
            await callback.message.answer_photo(photo_file, f"""Title: {name.text}Price: {price.text}\nCharacteristics: {characteristics(url)}""", reply_markup=cart_keyboard)
            # await callback.message.answer()

# ========================================================================================================================================

@dp.callback_query_handler(lambda call: call.data == "lenovo_laptop")
async def start(callback: types.CallbackQuery):
    await callback.message.answer("Top laptops from Lenovo:")
    url = 'https://www.barmak.store/category/lenovo/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")
    
    lst = []
    downloader(url, lst)

    for i, name, price in zip(lst, all_laptops_name, all_laptops_price):  
        with open(f"image/lenovo/{i}.jpg", 'rb') as photo_file:      
            await callback.message.answer_photo(photo_file, f"Title: {name.text}Price: {price.text}\nCharacteristics: {characteristics(url)}", reply_markup=cart_keyboard)

# ========================================================================================================================================

@dp.callback_query_handler(lambda call: call.data == "msi_laptop")
async def start(callback: types.CallbackQuery):
    await callback.message.answer("Top laptops from MSI:")
    url = 'https://www.barmak.store/category/MSI/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")
    
    lst = []
    downloader(url, lst)


    for i, name, price in zip(lst, all_laptops_name, all_laptops_price):  
        with open(f"image/msi/{i}.jpg", 'rb') as photo_file:      
            await callback.message.answer_photo(photo_file, f"""Title: {name.text}Price: {price.text}\nCharacteristics: {characteristics(url)}""", reply_markup=cart_keyboard)

# ========================================================================================================================================

executor.start_polling(dp, skip_updates=True)



    # cursor.execute(f"SELECT id FROM customer WHERE id = {message.from_user.id};")
    # result = cursor.fetchall()
    # if result == []:
    #     cursor.execute(f'INSERT INTO users VALUES (?, ?, ?, ?, ?)', (message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, time.ctime()))
    #     cursor.connection.commit()


    # url = 'https://www.barmak.store/category/Laptop/'
    # response = requests.get(url=url)
    # soup = BeautifulSoup(response.text, 'lxml')
