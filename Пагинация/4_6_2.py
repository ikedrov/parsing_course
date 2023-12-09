# Посещение и анализ всех страниц в категории "МЫШИ" на веб-сайте (всего 4 страницы).
# Переход в каждую карточку товара на каждой странице категории "МЫШИ" (всего 32 товара).
# Используя библиотеку bs4, извлечение артикула из каждой карточки товара
# (например, из элемента <p class="article">Артикул: 80244813</p>).
# Сложение всех извлеченных артикулов.

from bs4 import BeautifulSoup
import requests


def calculate_mouse_articles():
    total = 0
    url = 'https://parsinger.ru/html/mouse/3/3_'

    for i in range(1, 33):
        mouse_url = f'{url}{i}.html'
        response = requests.get(mouse_url)
        response.encoding = 'utf-8'
        soap = BeautifulSoup(response.text, 'lxml')
        total += int(soap.find('p', class_='article').text.split(': ')[-1])
    print(total)


calculate_mouse_articles()
