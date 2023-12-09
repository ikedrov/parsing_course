# Посещение и анализ всех категорий, страниц и карточек товаров на веб-сайте (всего 160 карточек товаров).
# Из каждой карточки извлечение стоимости товара и его количества в наличии.
# Умножение стоимости каждого товара на его количество в наличии.
# Суммирование всех полученных значений для вычисления общей стоимости всех товаров.
# Представление итоговой общей стоимости в качестве ответа.

from bs4 import BeautifulSoup
import requests


urls = ['https://parsinger.ru/html/watch/1/1_', 'https://parsinger.ru/html/mobile/2/2_',
        'https://parsinger.ru/html/mouse/3/3_', 'https://parsinger.ru/html/hdd/4/4_',
        'https://parsinger.ru/html/headphones/5/5_']

total = 0


def calculate_total_price_and_amount(url):
    all_prices = []
    all_amount = []
    for i in range(1, 33):
        new_url = f'{url}{i}.html'
        response = requests.get(new_url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        all_prices.append(int(soup.find('span', id='price').text.split()[0]))
        all_amount.append(int(soup.find('span', id='in_stock').text.split(': ')[-1]))

    return sum(c * p for c, p in zip(all_prices, all_amount))


for u in urls:
    total += calculate_total_price_and_amount(u)

print(total)
