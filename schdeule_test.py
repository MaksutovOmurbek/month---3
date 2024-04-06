import schedule, time


# def hello_world():
#     print('Hello world and Geeks', time.ctime())

# # schedule.every().seconds.do(hello_world)
# # schedule.every().minutes.do(hello_world)
# # schedule.every().hours.do(hello_world)
    

# # schedule.every().day.at("19:31").do(hello_world)
# # schedule.every().day.at("19:09:33", "Asia/Bishkek").do(hello_world)
# # schedule.every().minute.at(":10").do(hello_world)
# # schedule.every().hours.at(":13").do(hello_world)
    

# def bakcend12_1b():
#     print("Здраствуйте, сегодня у вас урок 15:00(ПН-ЧТ)")


# def bakcend13_1b():
#     print("Здраствуйте, сегодня у вас урок 17:00(ПН-ЧТ)")

# def bakcend14_1b():
#     print("Здраствуйте, сегодня у вас урок 19:00(ПН-ЧТ)")


# schedule.every(10).seconds.do(bakcend12_1b)
# schedule.every(20).seconds.do(bakcend13_1b)
# schedule.every(30).seconds.do(bakcend14_1b)

         
###########################################################################################

import schedule, time, requests

def get_dollar_price():
    url = 'https://www.nbkr.kg/index1.jsp?item=1562&lang=RUS'
    response = requests.get(url=url).json()
    bts_price = round(int(response['']), 2)

    print(f"Цена биткоина {time.ctime()} составляет {bts_price['price']}$")


def get_eth_price():
    url = 'https://www.binance.com/api/v3/ticker/price?symbol=ETHUSDT'
    response = requests.get(url=url).json()
    eth_price = round(int(response['price']), 2)

    print(f"Цена эфериума {time.ctime()} составляет {eth_price['price']}$")

schedule.every(5).seconds.do(get_dollar_price)
schedule.every(10).seconds.do(get_eth_price)



while True:
    schedule.run_pending()
    