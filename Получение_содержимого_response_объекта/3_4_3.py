# Напишите программу которая делает GET-запрос к указанной веб-странице для получения её HTML-кода.
#
# Выведите полученный HTML-код на экран с помощью response.text.
#
# Используйте response.encoding = 'utf-8' чтобы починить кодировку.

import requests

response = requests.get('https://parsinger.ru/3.4/2/index.html')
response.encoding = 'utf-8'
print(response.text)