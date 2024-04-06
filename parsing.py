from bs4 import BeautifulSoup
import requests

def downloader(url, lst):
    main_url = 'https://www.barmak.store'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, 'lxml')

    all_laptops_image = soup.find_all('div', class_ = "tp-product-thumb-2 p-relative z-index-1 fix w-img")
        
    acer = 0
    apple = 0
    asus = 0
    hp = 0
    huawei = 0
    lenovo = 0
    msi = 0

    for image in all_laptops_image:
        image_links = image.find('img').get('src')
        b = main_url + image_links

        if "Acer" in url:
            with open(f'image/acer/{acer}.jpg', 'wb') as file:
                lst.append(acer)
                file.write(requests.get(b).content)
                acer += 1
        elif "Macbook" in url:
            with open(f'image/apple/{apple}.jpg', 'wb') as file:
                lst.append(apple)
                file.write(requests.get(b).content)
                apple += 1
        elif "Asus" in url:
            with open(f'image/asus/{asus}.jpg', 'wb') as file:
                lst.append(asus)
                file.write(requests.get(b).content)
                asus += 1
        elif "Hp" in url:
            with open(f'image/hp/{hp}.jpg', 'wb') as file:
                lst.append(hp)
                file.write(requests.get(b).content)
                hp += 1
        elif "Huawei" in url:
            with open(f'image/huawei/{huawei}.jpg', 'wb') as file:
                lst.append(huawei)
                file.write(requests.get(b).content)
                huawei += 1
        elif "lenovo" in url:
            with open(f'image/lenovo/{lenovo}.jpg', 'wb') as file:
                lst.append(lenovo)
                file.write(requests.get(b).content)
                lenovo += 1
        elif "MSI" in url:
            with open(f'image/msi/{msi}.jpg', 'wb') as file:
                lst.append(msi)
                file.write(requests.get(b).content)
                msi += 1


def characteristics(url):
    main_url = 'https://www.barmak.store'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, 'lxml')

    all_laptops_image = soup.find_all('div', class_ = "tp-product-thumb-2 p-relative z-index-1 fix w-img")

    for image in all_laptops_image:
        image_links = image.find('a').get('href')
        image_url = main_url + image_links
        resp = requests.get(url=image_url)
        characteristics_soup = BeautifulSoup(resp.text, 'lxml')

        all_laptops_characteristics = characteristics_soup.find('div', class_ = "tp-product-details-desc-content pt-25").find('p')

        a = """""".join(all_laptops_characteristics).split('>')[0].split('Где купить')[0].split('Преимущества для Вас')[0].split('Ваши Преимущества')[0].split('Продолжительное Время Работы')[0].split('MSI Katana GF66')[0].split('. ')

        return a[0]


