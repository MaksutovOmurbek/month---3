from bs4 import BeautifulSoup
import requests


def parsing_barmak():
    url = 'https://www.barmak.store/category/Acer/'
    response = requests.get(url=url) 
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)  

    all_laptops_name = soup.find_all('div', class_= "tp-product-tag-2")
    all_laptops_price= soup.find_all('span', class_= "tp-product-price-2 new-price")
    all_laptops_image = soup.find_all('img', class_= ".tp-product-thumb-2 img")


    for image in all_laptops_image:
        result = image['src']
        print(result)
    
    # print(all_laptops_name)
    # print(all_laptops_price)


    for name, price in zip(all_laptops_name, all_laptops_price):
        result = "".join(name.text)
        print(result, price.text)



parsing_barmak()



