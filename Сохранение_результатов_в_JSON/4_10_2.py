# Соберите данные всех карточек товара всех категорий и со всех страниц тренажера
# (всего 160шт).
# Не "проваливайтесь" внутрь каждой карточки. Соберите только информацию из превью.
# Сохраните данные в JSON файл с использованием указанных параметров.
# json.dump(res, file, indent=4, ensure_ascii=False)

from bs4 import BeautifulSoup
import requests
import json


def all_items_to_json():
    main_url = 'https://parsinger.ru/html/index1_page_1.html'
    result = []

    response = requests.get(main_url)

    if response.raise_for_status():
        print('Can not proceed request')

    else:
        response.encoding = 'utf-8'
        pages = BeautifulSoup(response.text, 'lxml').find('div', class_='nav_menu').find_all('a')

        for page in pages:
            page_url = f'http://parsinger.ru/html/{page["href"]}'
            page_response = requests.get(page_url)

            if page_response.raise_for_status():
                print('Can not proceed request')

            else:
                page_response.encoding = 'utf-8'
                page_number = BeautifulSoup(page_response.text, 'lxml').find('div', class_='pagen').find_all('a')

                for pn in page_number:
                    item_url = f'http://parsinger.ru/html/{pn["href"]}'
                    pn_response = requests.get(item_url)

                    if pn_response.raise_for_status():
                        print('Can not proceed request')

                    else:
                        pn_response.encoding = 'utf-8'
                        item_number = BeautifulSoup(pn_response.text, 'lxml')
                        name = [i.text.strip() for i in item_number.find_all('a', class_='name_item')]
                        description = [i.text.strip().split('\n') for i in item_number.find_all('div', class_='description')]
                        price = [i.text.strip() for i in item_number.find_all('p', class_='price')]

                        for d, p, n in zip(description, price, name):
                            result.append({
                                'Наименование': n,
                                'Бренд': d[0].split(':', 1)[1].strip(),
                                d[1].split(':', 1)[0].strip(): d[1].split(':', 1)[1].strip(),
                                d[2].split(':', 1)[0].strip(): d[2].split(':', 1)[1].strip(),
                                d[3].split(':', 1)[0].strip(): d[3].split(':', 1)[1].strip(),
                                'Цена': p
                            })

    with open('/Users/ivankedrov/parsing_stepik/Сохранение_результатов_в_JSON/4_10_2.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
        print('Done')


all_items_to_json()

