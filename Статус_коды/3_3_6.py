# Написать скрипт, который будет делать GET запросы к каждой странице в диапазоне.
#
# Определить, какая страница в диапазоне является первой доступной (статус-код 200).
#
# Определить, какая страница в диапазоне является последней доступной (также статус-код 200).

import requests

available_pages = []

with requests.Session() as rs:
    for i in range(1, 101):
        response = rs.head(f'https://parsinger.ru/3.3/4/{i}.html')
        if response.status_code == 200:
            available_pages.append(i)

print(f'Первая доступная страница: {available_pages[0]}.html')
print(f'Последняя доступная страница: {available_pages[-1]}.html')