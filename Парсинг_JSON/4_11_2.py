# Сделать GET-запрос и получить JSON-структуру по указанной ссылке.
# Для каждой категории товаров ('watch', 'mobile', 'mouse', 'hdd', 'headphones') рассчитать общую стоимость( Умножить стоимость товара на количество товара для каждой отдельной карточки).
# Суммируйте значения для каждой отдельной категории.
# Сформируйте словарь, где ключи - названия категорий, а значения - словаря с общей стоимостью товаров в этой категории.

import requests


def count_categories_price():
    url = 'https://parsinger.ru/downloads/get_json/res.json'
    result = {}
    response = requests.get(url).json()

    for item in response:
        if item['categories'] not in result:
            result[item['categories']] = int(item['count']) * int(item['price'].split()[0])
        else:
            result[item['categories']] += int(item['count']) * int(item['price'].split()[0])

    print(result)


count_categories_price()