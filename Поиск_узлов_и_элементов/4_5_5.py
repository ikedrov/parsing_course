# Открываем сайт
# Извлекаем при помощи bs4 данные о стоимости часов (всего 8 шт)
# Складываем все числа


from bs4 import BeautifulSoup
import requests


def calculate_prices():

    url = 'https://parsinger.ru/html/index1_page_1.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soap = BeautifulSoup(response.text, 'lxml')
    prices = sum([int(i.text.split(' ')[0]) for i in soap.find_all('p', class_='price')])
    print(prices)


calculate_prices()

