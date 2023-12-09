# Напишите код, который осуществляет GET-запрос к указанному API для получения погодных данных заданного города.
#
# Преобразовать полученный JSON-ответ в Python-объект с помощью метода response.json().
#
# Проанализировать данные и определить дату с самой минимальной температурой.

import requests

url = 'https://parsinger.ru/3.4/1/json_weather.json'


response = requests.get(url).json()
sorted_response = sorted(response, key=lambda x: int(x['Температура воздуха'][:-2]))

print(sorted_response[0]['Дата'])





