# Получение данных: Используйте инструменты разработчика для определения источника данных(вкладка Network). В нашем случае, данные лежат на этом веб-сайте.
# Обработка данных: Извлеките данные со страницы и создайте словарь, в котором для каждой карточки вычислите произведение значений "article" и "rating".
# Сбор значений: Суммируйте результаты произведений для каждой категории.
# Формирование словаря: Завершая задачу, создайте словарь, в котором ключами будут категории, а значениями - суммы произведений "article" и "rating".

import requests


def count_articles_and_rating():
    url = 'https://parsinger.ru/4.6/1/res.json'
    result = {}
    response = requests.get(url).json()

    for item in response:
        if item['categories'] not in result:
            result[item['categories']] = int(item['article']) * item['description']['rating']
        else:
            result[item['categories']] += int(item['article']) * item['description']['rating']

    print(result)


count_articles_and_rating()

