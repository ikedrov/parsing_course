# Открыть веб-сайт и обнаружить необходимую таблицу.
# Для каждой строки таблицы найти числа в оранжевой и голубой ячейках, после чего умножить их друг на друга.
# Сложить все получившиеся произведения, чтобы получить общую сумму.

from bs4 import BeautifulSoup
import requests


def mult_orange_and_blue_nums():
    url = 'https://parsinger.ru/table/5/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    nums_orange = [float(x.text) for x in soup.find_all('td', class_='orange')]
    nums_blue = [float(y.text) for y in soup.select('td:last-child')]
    result = sum(o * b for o, b in zip(nums_orange, nums_blue))

    print(result)


mult_orange_and_blue_nums()