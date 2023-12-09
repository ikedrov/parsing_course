# Открыть веб-сайт и обнаружить интересующую таблицу.
# Для каждого столбца вычислить сумму всех чисел в этом столбце.
# Округлить каждое получившееся значение до трех знаков после запятой.
# row: round(sum(column), 3)
# Формировать словарь, где ключами будут названия столбцов, а значениями - рассчитанные суммы.

import pandas
from urllib import request
import ssl


def dict_sum():
    url = 'https://parsinger.ru/table/5/index.html'
    context = ssl._create_unverified_context()
    response = request.urlopen(url, context=context)
    html = response.read()
    data = pandas.read_html(html, header=0)
    df = data[0]
    result = {i: df[i].sum().astype(float).round(3) for i in df.columns}

    print(result)


dict_sum()


