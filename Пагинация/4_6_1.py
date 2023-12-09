# Посещение и анализ четырех страниц веб-сайта с пагинацией.
# Извлечение названий товаров с каждой страницы (8 шт на каждой странице).
# Сохранение названий товаров с каждой страницы в отдельном списке.
# Объединение всех четырех списков в один главный список.

from bs4 import BeautifulSoup
import requests


def get_all_goods():
    all_goods = []
    url = 'https://parsinger.ru/html/index3_page_1.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    schema = 'https://parsinger.ru/html/'
    pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
    for i in pagen:
        goods_url = f'{schema}{i}'
        goods_response = requests.get(goods_url)
        goods_response.encoding = 'utf-8'
        soap1 = BeautifulSoup(goods_response.text, 'lxml')
        all_goods.append([s.text for s in soap1.find_all('a', class_='name_item')])
    print(all_goods)


get_all_goods()