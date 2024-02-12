from config import TOKEN
from aiogram import Bot, Dispatcher, types, executor


bot = Bot(TOKEN) 
dp = Dispatcher(bot)


start_buttons = [
    types.KeyboardButton('Mersedes-Benz'),
    types.KeyboardButton('BMW'),
    types.KeyboardButton('AUDI'),
    types.KeyboardButton('HYUNDAI'),
    types.KeyboardButton('TOYOTA'),
    types.KeyboardButton('KIA'),
    types.KeyboardButton('LEXUS'),
    # types.KeyboardButton(''),
    types.KeyboardButton('HONDA')
]


start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здраствуйте {message.from_user.full_name}",  reply_markup=start_keyboard)



    
mers_buttons = [
    types.KeyboardButton('E212'),
    types.KeyboardButton('W120'),
    types.KeyboardButton('E210'),
    types.KeyboardButton('GELIK'),
    types.KeyboardButton('НАЗАД')
]

mers_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*mers_buttons)

@dp.message_handler(text = 'Mersedes-Benz')
async def texto(message:types.Message):
    await message.answer('вот', reply_markup=mers_keyboard)


@dp.message_handler(text = 'W120')
async def textm(message:types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/1994_Mercedes-Benz_E_220_%28W124%29_sedan_%282012-06-24%29.jpg/1200px-1994_Mercedes-Benz_E_220_%28W124%29_sedan_%282012-06-24%29.jpg')


@dp.message_handler(text = 'E210')
async def textq(message:types.Message):
    await message.answer_photo('https://avatars.mds.yandex.net/get-autoru-reviews/1337757/78mRmsvLlzGYgZZ0mEeFVo6sRPwFDJh9R/640x480')


@dp.message_handler(text = 'E212')
async def texts(message:types.Message):
    await message.answer_photo('https://a.d-cd.net/42abdads-960.jpg')

@dp.message_handler(text = 'GELIK')
async def texta(message:types.Message):
    await message.answer_photo('https://www.ixbt.com/img/n1/news/2023/5/1/2324245_large.png')



bmw_buttons = [
    types.KeyboardButton('E34'),
    types.KeyboardButton('F90'),
    types.KeyboardButton('X5'),
    types.KeyboardButton('M5'),
    types.KeyboardButton('M4'),
    types.KeyboardButton('НАЗАД')
]

bmw_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*bmw_buttons)


@dp.message_handler(text ='BMW')
async def text(message:types.Message):
    await message.answer('вот', reply_markup=bmw_keyboard)

@dp.message_handler(text='E34')
async def bmw(message:types.Message):
    await message.answer_photo('https://www.classicandsportscar.com/sites/default/files/styles/article/public/2023-06/Classic%20%26%20Sports%20Car%20%E2%80%93%20Buyer%E2%80%99s%20guide%20BMW%20M5%20E34%20%E2%80%93%20LEAD.png?itok=ZcY5feBo')

@dp.message_handler(text='F90')
async def bmw(message:types.Message):
    await message.answer_photo('https://avatars.dzeninfra.ru/get-zen_doc/3523766/pub_63d5f1f9f86b2d2a16b3c17d_63d5f2b3db90d61608ac12d3/scale_1200')    


@dp.message_handler(text='X5')
async def bmw(message:types.Message):
    await message.answer_photo('https://letiauto.lv/wp-content/uploads/2023/02/MSS01929.jpg')


@dp.message_handler(text='M5')
async def bmw(message:types.Message):
    await message.answer_photo('https://hips.hearstapps.com/hmg-prod/images/2024-bmw-m5-sedan-rendering-1676575610.jpg')


@dp.message_handler(text='M4')
async def bmw(message:types.Message):
    await message.answer_photo('https://s.auto.drom.ru/i24249/c/photos/fullsize/bmw/m4/bmw_m4_973229.jpg')




audi_buttons = [
    types.KeyboardButton('A4'),
    types.KeyboardButton('R8'),
    types.KeyboardButton('G7'),
    types.KeyboardButton('A1'),
    types.KeyboardButton('G8'),
    types.KeyboardButton('НАЗАД')
]


audi_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*audi_buttons)

@dp.message_handler(text='AUDI')
async def audit(message:types.Message):
    await message.answer('вот',reply_markup=audi_keyboard)

@dp.message_handler(text='A4')
async def bmw(message:types.Message):
    await message.answer_photo('https://www.shutterstock.com/image-photo/whittleburynorthantsuk-aug-6th-2023-2018-600nw-2343504405.jpg')


@dp.message_handler(text='R8')
async def bmw(message:types.Message):
    await message.answer_photo('https://kolesa-uploads.ru/r/880x/40b1ac13-f5e7-4488-806e-ff8c56b6880e/a1914479-large.jpg')

@dp.message_handler(text='G7')
async def bmw(message:types.Message):
    await message.answer_photo('https://avatars.mds.yandex.net/get-verba/1604130/2a0000017f6f0d9fc86002cd5db3ef657769/cattouchret')

@dp.message_handler(text='G8')
async def bmw(message:types.Message):
    await message.answer_photo('https://hips.hearstapps.com/hmg-prod/images/2024-audi-q8-exterior-static-103-64f0ba52d994a.jpg?crop=0.723xw:0.781xh;0.156xw,0.219xh&resize=768:*')

@dp.message_handler(text='A1')
async def bmw(message:types.Message):
    await message.answer_photo('https://images.drive.ru/i/0/5b28af75ec05c46c19000007.jpg')





hun_buttons = [
    types.KeyboardButton('SONATA'),
    types.KeyboardButton('SOLARIS'),
    types.KeyboardButton('SANTA FE'),
    types.KeyboardButton('I30'),
    types.KeyboardButton('AVANTE'),
    types.KeyboardButton('НАЗАД')
]


hun_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*hun_buttons)

@dp.message_handler(text='HYUNDAI')
async def audit(message:types.Message):
    await message.answer('вот',reply_markup=hun_keyboard)

@dp.message_handler(text='SONATA')
async def bmw(message:types.Message):
    await message.answer_photo('https://leasing.express/wp-content/uploads/2022/02/SonataYF.jpg')

@dp.message_handler(text='AVANTE')
async def bmw(message:types.Message):
    await message.answer_photo('https://avatars.mds.yandex.net/get-verba/1540742/2a000001885342e4cf42c6e8133c9d8c7aa0/cattouchret')

@dp.message_handler(text='SOLARIS')
async def bmw(message:types.Message):
    await message.answer_photo('https://avatars.mds.yandex.net/get-verba/1030388/2a0000017080b874c59ece700722941db579/cattouchret')


@dp.message_handler(text='SANTA FE')
async def bmw(message:types.Message):
    await message.answer_photo('https://www.hyundai-kemerovo.ru/upload/iblock/ca6/ca6929666d85c9662d2aabda64254c9c.jpg')

@dp.message_handler(text='I30')
async def bmw(message:types.Message):
    await message.answer_photo('https://avatars.mds.yandex.net/get-verba/1604130/2a0000017ff613dbe2112f7badbaed8e8fa7/cattouch')


toyo_buttons = [
    types.KeyboardButton('CAMRY'),
    types.KeyboardButton('RAV4'),
    types.KeyboardButton('CARROLA'),
    types.KeyboardButton('CROWN'),
    types.KeyboardButton('LAND CRUISER'),
    types.KeyboardButton('НАЗАД')
]

toyo_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*toyo_buttons)


@dp.message_handler(text ='TOYOTA')
async def toyota(message:types.Message):
    await message.answer('вот', reply_markup=toyo_keyboard)


@dp.message_handler(text='CARROLA')
async def toyota(message:types.Message):
    await message.answer_photo('https://d8a6a33f-3369-444b-9b5f-793c13ff0708.selcdn.net/media/common/just_strip/tradeins.space/uploads/models_gallery_image/13778/450d7266a8acac506ddc97c36c79cedee2addd42.jpeg?v77')

@dp.message_handler(text='CAMRY')
async def toyota(message:types.Message):
    await message.answer_photo('https://scene7.toyota.eu/is/image/toyotaeurope/cam0001a_21-2:Medium-Landscape?ts=0&resMode=sharp2&op_usm=1.75,0.3,2,0')

@dp.message_handler(text='CROWN')
async def toyota(message:types.Message):
    await message.answer_photo('https://motor.ru/thumb/1500x0/filters:quality(75):no_upscale()/imgs/2023/11/02/12/6207392/1a6194de77a7cc2179239239f5eec4f71e202c9b.jpg')

@dp.message_handler(text='RAV4')
async def toyota(message:types.Message):
    await message.answer_photo('https://www.major-toyota.ru/assets/client/images/rav4_teaser_1.jpg')


@dp.message_handler(text='LAND CRUISER')
async def bmw(message:types.Message):
    await message.answer_photo('https://autorating.ru/upload/medialibrary/948/948a165ce83548d8c07c69a17557b1d6.jpg')



lex_buttons = [
    types.KeyboardButton('470'),
    types.KeyboardButton('570'),
    types.KeyboardButton('600'),
    types.KeyboardButton('350'),
    types.KeyboardButton('ES'),
    types.KeyboardButton('НАЗАД')
]

lex_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*lex_buttons)


@dp.message_handler(text ='LEXUS')
async def toyota(message:types.Message):
    await message.answer('вот', reply_markup=lex_keyboard)


@dp.message_handler(text='470')
async def toyota(message:types.Message):
    await message.answer_photo('https://autopark.kg/wp-content/uploads/2023/04/1-24-scaled-1.webp')
@dp.message_handler(text='570')
async def toyota(message:types.Message):
    await message.answer_photo('https://s.auto.drom.ru/i24248/r/photos/1398033/big_1521262.jpg')
@dp.message_handler(text='600')
async def toyota(message:types.Message):
    await message.answer_photo('https://s.auto.drom.ru/i24262/c/photos/fullsize/lexus/lx600/lexus_lx600_1034752.jpg')
@dp.message_handler(text='350')
async def toyota(message:types.Message):
    await message.answer_photo('https://s.auto.drom.ru/i24234/c/photos/fullsize/lexus/rx350/lexus_rx350_897844.jpg')


@dp.message_handler(text='ES')
async def bmw(message:types.Message):
    await message.answer_photo('https://scene7.toyota.eu/is/image/toyotaeurope/2022-lexus-es-bold-design-coupe-like-roofline-1920x1080-1?wid=1280&fit=fit,1&ts=1666339513566&resMode=sharp2&op_usm=1.75,0.3,2,0')



honda_buttons = [
    types.KeyboardButton('ACCORD'),
    types.KeyboardButton('CR-V'),
    types.KeyboardButton('CIVIC'),
    types.KeyboardButton('ARIA'),
    types.KeyboardButton('FIT'),
    types.KeyboardButton('НАЗАД')
]

honda_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*honda_buttons)


@dp.message_handler(text ='HONDA')
async def honda(message:types.Message):
    await message.answer('вот', reply_markup=honda_keyboard)


@dp.message_handler(text='ACCORD')
async def toyota(message:types.Message):
    await message.answer_photo('https://editorials.autotrader.ca/media/mvfb51px/2023-honda-accord-ex-03-jm.jpg?center=0.55296285774816079,0.49995024572193458&mode=crop&width=1920&height=1080&rnd=133282811715630000')
@dp.message_handler(text='CR-V')
async def toyota(message:types.Message):
    await message.answer_photo('https://photos.prnewswire.com/prnfull/20120831/LA66248')
@dp.message_handler(text='CIVIC')
async def toyota(message:types.Message):
    await message.answer_photo('https://avatars.mds.yandex.net/get-autoru-reviews/1393169/t0SPNsIC1Oi2fE1QNBlLS4cioZHXO4rjA/1200x900')
@dp.message_handler(text='ARIA')
async def toyota(message:types.Message):
    await message.answer_photo('https://bluetooth-aux.com/upload/iblock/6bf/6bf9493cc0afd57ab55c01570ebec2b6.jpg')


@dp.message_handler(text='FIT')
async def bmw(message:types.Message):
    await message.answer_photo('https://avatars.mds.yandex.net/get-verba/1030388/2a00000160957a71a054bea7dbe2a6389ed8/cattouchret')

kia_buttons = [
    types.KeyboardButton('SORENTO'),
    types.KeyboardButton('CARNIVAL'),
    types.KeyboardButton('K7'),
    types.KeyboardButton('OPTIMA'),
    types.KeyboardButton('SELTOS'),
    types.KeyboardButton('НАЗАД')
]

kia_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*kia_buttons)


@dp.message_handler(text ='KIA')
async def kia(message:types.Message):
    await message.answer('вот', reply_markup=kia_keyboard)


@dp.message_handler(text='SELTOS')
async def toyota(message:types.Message):
    await message.answer_photo('https://avatars.mds.yandex.net/get-vertis-journal/3934100/d069c7d0e15e455bbab4da24c76f55d4.jpg_1658410295225/orig')

@dp.message_handler(text='SORENTO')
async def toyota(message:types.Message):
    await message.answer_photo('https://images.prismic.io/carwow/815ca9aa-4b72-45e9-84df-25285116be1a_2023+Kia+Sorento+front+quarter+moving.jpg')

@dp.message_handler(text='CARNIVAL')
async def toyota(message:types.Message):
    await message.answer_photo('https://motor.ru/imgs/2021/07/12/13/4762933/e2b301d83f6ca1714858484c5211b8060ec74c67.jpg')

@dp.message_handler(text='K7')
async def toyota(message:types.Message):
    await message.answer_photo('https://s.auto.drom.ru/i24274/c/photos/fullsize/kia/k7/kia_k7_1099487.jpg')

@dp.message_handler(text='OPTIMA')
async def bmw(message:types.Message):
    await message.answer_photo('https://cdn.jdpower.com/ArticleImages/2019%20Kia%20Optima%2013750_635.jpg')


# _buttons = [
#     types.KeyboardButton('A4'),
#     types.KeyboardButton('R8'),
#     types.KeyboardButton('G7'),
#     types.KeyboardButton('A1'),
#     types.KeyboardButton('G8'),
#     types.KeyboardButton('НАЗАД')
# ]


# _keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*_buttons)

# @dp.message_handler(text='')
# async def audit(message:types.Message):
#     await message.answer('вот',reply_markup=_keyboard)

# @dp.message_handler(text='A4')
# async def bmw(message:types.Message):
#     await message.answer_photo('https://www.shutterstock.com/image-photo/whittleburynorthantsuk-aug-6th-2023-2018-600nw-2343504405.jpg')


# @dp.message_handler(text='R8')
# async def bmw(message:types.Message):
#     await message.answer_photo('https://kolesa-uploads.ru/r/880x/40b1ac13-f5e7-4488-806e-ff8c56b6880e/a1914479-large.jpg')

# @dp.message_handler(text='G7')
# async def bmw(message:types.Message):
#     await message.answer_photo('https://avatars.mds.yandex.net/get-verba/1604130/2a0000017f6f0d9fc86002cd5db3ef657769/cattouchret')

# @dp.message_handler(text='G8')
# async def bmw(message:types.Message):
#     await message.answer_photo('https://hips.hearstapps.com/hmg-prod/images/2024-audi-q8-exterior-static-103-64f0ba52d994a.jpg?crop=0.723xw:0.781xh;0.156xw,0.219xh&resize=768:*')

# @dp.message_handler(text='A1')
# async def bmw(message:types.Message):
#     await message.answer_photo('https://images.drive.ru/i/0/5b28af75ec05c46c19000007.jpg')


@dp.message_handler(text='НАЗАД')
async def rollback(message:types.Message):
    await start(message)

@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("вас не понял, введите /start")

executor.start_polling(dp)
