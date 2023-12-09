# Загрузить страницу на которой расположена таблица с объединёнными ячейками.
# Извлечь данные из каждой объединённой ячейки(всего 16 ячеек), объединённую ячейку можно определить по атрибуту colspan.
# Суммировать все числовые значения, полученные из объединённых ячеек.


from bs4 import BeautifulSoup
import requests


def sum_colspan():
    url = 'https://parsinger.ru/4.8/8/index.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    total = 0

    all_td_colspan = soup.find_all(['td', 'th', 'table', '#mainTable'], {'colspan': True})
    for td in all_td_colspan:
        if len(td.find_all()) == 0:
            total += float(td.text)

    print(total)


sum_colspan()