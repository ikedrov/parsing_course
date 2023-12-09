# Выполните HTTP запрос к каждой ссылке в заданном диапазоне.
# Считывайте HTTP статус-код каждой страницы.
# Определите, какая именно ссылка является рабочей, то есть возвращает HTTP статус-код 200 (OK).
# Перейдите по рабочей ссылке вручную, или получите данные с помощью response.text для извлечения числа на этой странице.

import requests

with requests.Session() as rs:
    for i in range(1, 201):
        response = rs.head(f'https://parsinger.ru/3.3/1/{i}.html')
        if response.status_code == 200:
            url = requests.get(f'https://parsinger.ru/3.3/1/{i}.html')
            print(url.text)
            break

