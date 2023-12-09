# Соберите данные о HDD с четырёх страниц в категории HDD.
# Не "проваливайтесь" внутрь каждой карточки. Соберите только информацию из превью.
# Сохраните данные в JSON файл с использованием указанных параметров.
# json.dump(res, file, indent=4, ensure_ascii=False)

import json
import requests
from bs4 import BeautifulSoup


def hdd_to_table():
    main_url = 'https://parsinger.ru/html/index4_page_'
    result = []

    for i in range(1, 5):
        url = f'{main_url}{i}.html'
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        name = [i.text.strip() for i in soup.find_all('a', class_='name_item')]
        description = [i.text.strip().split('\n') for i in soup.find_all('div', class_='description')]
        price = [i.text.strip() for i in soup.find_all('p', class_='price')]

        for d, p, n in zip(description, price, name):
            result.append({
                "Наименование": n,
                "Бренд": [x.split(':')[-1].strip() for x in d][0],
                "Форм-фактор": [x.split(':')[-1].strip() for x in d][1],
                "Ёмкость": [x.split(':')[-1].strip() for x in d][2],
                "Объем буферной памяти": [x.split(':')[-1].strip() for x in d][3],
                "Цена": p
            })

    with open('/Users/ivankedrov/parsing_stepik/Сохранение_результатов_в_JSON/4_10_1.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


hdd_to_table()


