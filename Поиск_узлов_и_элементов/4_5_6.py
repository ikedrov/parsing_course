# Открываем сайт
# Получаем данные при помощи bs4 о старой цене и новой цене
# По формуле высчитываем процент скидки
# Формула (старая цена - новая цена) * 100 / старая цена)
# Вставьте получившийся результат в поле ответа
# Ответ должен быть числом с 1 знаком после запятой.

from bs4 import BeautifulSoup
import requests


def calculate_sale():
    url = 'https://parsinger.ru/html/hdd/4/4_1.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soap = BeautifulSoup(response.text, 'lxml')
    old_price = int(soap.find('span', id='old_price').text.split()[0])
    new_price = int(soap.find('span', id='price').text.split()[0])
    print(round((old_price - new_price) * 100 / old_price, 1))


calculate_sale()
