# Напишите код, который соберёт данные в каждой категории c каждой карточки, всего 160шт.

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
                        item_number = BeautifulSoup(pn_response.text, 'lxml').find_all('a', class_='name_item')

                        for item in item_number:
                            i_url = f'http://parsinger.ru/html/{item["href"]}'
                            item_response = requests.get(i_url)

                            if item_response.raise_for_status():
                                print('Can not proceed request')

                            else:
                                item_response.encoding = 'utf-8'
                                soup = BeautifulSoup(item_response.text, 'lxml')
                                name = [i.text.strip() for i in soup.find_all('p', id='p_header')]
                                article = [i.text.strip() for i in soup.find_all('p', class_='article')]
                                in_stock = [i.text.strip() for i in soup.find_all('span', id='in_stock')]
                                price = [i.text.strip() for i in soup.find_all('span', id='price')]
                                old_price = [i.text.strip() for i in soup.find_all('span', id='old_price')]
                                description = {li['id']: li.text.split(':')[-1].strip() for li in soup.select('#description li')}

                                for n, a, i, p, o, d in zip(name, article, in_stock, price, old_price, description):
                                    result.append({
                                        "categories": i_url.split('/')[4],
                                        "name": n,
                                        "article": a.split(':')[-1].strip(),
                                        "description": description,
                                        "count": i.split(':')[-1].strip(),
                                        "price": p,
                                        "old_price": o,
                                        "link": i_url
                                    })

    with open('/Users/ivankedrov/parsing_stepik/Сохранение_результатов_в_JSON/4_10_4.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
        print('Done')


all_items_to_json()
