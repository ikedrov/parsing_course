# Загрузить страницу с шестью таблцами.
# Пройтись по каждой ячейке каждой таблицы и проверить значение на кратность трём.
# Если число кратно трем, добавить его к общей сумме.

from bs4 import BeautifulSoup
import requests


def sum_if_divides_by_three():
    url = 'https://parsinger.ru/4.8/7/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    tables = soup.find_all('table')
    res = 0

    for table in tables:
        nums = table.find_all('td')
        for num in nums:
            if int(num.text) % 3 == 0:
                res += int(num.text)

    print(res)


sum_if_divides_by_three()

