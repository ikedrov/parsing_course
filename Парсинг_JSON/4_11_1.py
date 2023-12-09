# Вашей задачей является обработка данных в формате JSON, полученных по ссылке ​. Для подсчета общего количества товаров в разных категориях. Каждая карточка товара содержит информацию о количестве данного товара.

import requests


def count_categories_items():
    url = 'https://parsinger.ru/downloads/get_json/res.json'
    result = {}
    response = requests.get(url).json()

    for item in response:
        if item['categories'] not in result:
            result[item['categories']] = int(item['count'])
        else:
            result[item['categories']] += int(item['count'])

    print(result)


count_categories_items()

