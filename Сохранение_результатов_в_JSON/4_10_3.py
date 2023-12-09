# Соберите данные из категории mobile  (всего 32 карточки).
# "Провалитесь" в каждую карточку и соберите необходимую информацию.
# Сохраните данные в JSON файл с использованием указанных параметров.
# json.dump(res, file, indent=4, ensure_ascii=False)

from bs4 import BeautifulSoup
import requests
import json


def mobiles_to_json():
    main_url = 'https://parsinger.ru/html/index2_page_1.html'
    result = []

    response = requests.get(main_url)

    if response.raise_for_status():
        print('Can not proceed request')

    else:
        response.encoding = 'utf-8'
        page_number = BeautifulSoup(response.text, 'lxml').find('div', class_='pagen').find_all('a')

        for pn in page_number:
            item_url = f'https://parsinger.ru/html/{pn["href"]}'
            pn_response = requests.get(item_url)

            if pn_response.raise_for_status():
                print('Can not proceed request')

            else:
                pn_response.encoding = 'utf-8'
                item_number = BeautifulSoup(pn_response.text, 'lxml').find_all('a', class_='name_item')

                for item in item_number:
                    i_url = f'https://parsinger.ru/html/{item["href"]}'
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
                                "categories": "mobile",
                                "name": n,
                                "article": a.split(':')[-1].strip(),
                                "description": description,
                                "count": i.split(':')[-1].strip(),
                                "price": p,
                                "old_price": o,
                                "link": i_url
                            })

    with open('/Users/ivankedrov/parsing_stepik/Сохранение_результатов_в_JSON/4_10_3.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
        print('Done')


mobiles_to_json()
