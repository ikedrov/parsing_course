# Открыть веб-сайт и найти целевую таблицу.
# Провести анализ данных в таблице, фокусируясь на ячейках зелёного цвета.
# Выделить и подсчитать сумму всех чисел из зелёных ячеек.

from bs4 import BeautifulSoup
import requests


def sum_green_nums():
    url = 'https://parsinger.ru/table/4/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    nums = [float(x.text) for x in soup.find_all('td', class_='green')]

    print(sum(nums))


sum_green_nums()