# Перейти на сайт и найти таблицу.
# Произвести парсинг данных из первого столбца таблицы.
# Суммировать все числа, найденные в первом столбце.

from bs4 import BeautifulSoup
import requests


def sum_first_row():
    url = 'https://parsinger.ru/table/2/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find('table')
    rows = table.find_all('tr')
    res = 0

    for r in rows[1:]:
        num = r.find('td')
        res += (float(num.text))
        
    print(res)


sum_first_row()