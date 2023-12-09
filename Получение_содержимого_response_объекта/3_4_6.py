# Написать скрипт на Python, который выполнит GET-запрос к данному API для получения JSON-данных.
#
# Преобразовать полученный JSON-ответ в Python-объект с использованием метода response.json().
#
# Проанализировать древовидную структуру переписки и подсчитать количество сообщений, отправленных каждым участником.

import requests

dct_name = {}


def get_user(dct):
    dct_name[dct['username']] = dct_name.get(dct['username'], 0) + 1
    if dct['comments']:
        for i in dct['comments']:
            get_user(i)


get_user(requests.get('https://parsinger.ru/3.4/3/dialog.json').json())
print(dict(sorted(sorted(dct_name.items()), key=lambda x: x[1], reverse=True)))
