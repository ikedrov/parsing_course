# Перейти на сайт и найти таблицу.
# Произвести парсинг данных из таблицы.
# Отфильтровать и извлечь все уникальные числа, исключая числа в заголовке таблицы.
# Посчитать сумму этих чисел.

from bs4 import BeautifulSoup
import requests


def sum_unique_nums():
    url = 'https://parsinger.ru/table/1/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    cells = set()
    line = [float(x.text) for x in soup.find_all('td')]

    for l in line:
        cells.add(l)

    print(sum(cells))


sum_unique_nums()