# Сделайте HTTP запрос к каждой странице в указанном диапазоне.
# Получите HTTP статус-код каждой страницы.
# Суммируйте все полученные статус-коды.

import requests

status_sum = 0

with requests.Session()as rs:
    for i in range(1, 201):
        response = rs.head(f'https://parsinger.ru/3.3/2/{i}.html')
        status_sum += response.status_code

print(status_sum)
