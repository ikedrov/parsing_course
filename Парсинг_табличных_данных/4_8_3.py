# Перейти на сайт и обнаружить требуемую таблицу.
# Cобрать только числа, отформатированные жирным шрифтом.
# Суммировать выделенные числа.

from bs4 import BeautifulSoup
import requests


def sum_bold_nums():
    url = 'https://parsinger.ru/table/3/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    nums = [float(x.text) for x in soup.find_all('b')]
    
    print(sum(nums))


sum_bold_nums()