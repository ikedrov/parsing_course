# Напишите код, который соберёт данные в каждой категории c каждой карточки, всего 160шт.

from bs4 import BeautifulSoup
import requests
import csv


def all_items_to_table():
    main_url = 'https://parsinger.ru/html/index1_page_1.html'
    table = [['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена',
              'Ссылка на карточку с товаром'], ]

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
                                all_items = soup.find_all('div', class_='description')

                                for i in all_items:
                                    row = list()
                                    row.append(i.find('p', id='p_header').text.strip())
                                    row.append(i.find('p', class_='article').text.split(':')[1].strip())
                                    row.append(i.find('li', id='brand').text.split(':')[1].strip())
                                    row.append(i.find('li', id='model').text.split(':')[1].strip())
                                    row.append(i.find('span', id='in_stock').text.split(':')[1].strip())
                                    row.append(i.find('span', id='price').text.strip())
                                    row.append(i.find('span', id='old_price').text.strip())
                                    row.append(i_url)
                                    table.append(row)

    with open('/Users/ivankedrov/parsing_stepik/Сохранение_результатов_в_Excel/4_9_4.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(table)


all_items_to_table()








