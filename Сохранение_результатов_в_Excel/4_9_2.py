# Изучите указанную страницу для получения информации о часах с четырёх страниц в разделе "ЧАСЫ".
# Вам потребуется заходить в каждую товарную карточку и собирать данные, отмеченные на предоставленном изображении.
# Сохраните данные в формате CSV с разделителем ;:

import csv
import requests
from bs4 import BeautifulSoup


def watches_to_table():
    main_url = 'https://parsinger.ru/html/watch/1/1_'
    table = [['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип',
              'Технология экрана', 'Материал корпуса', 'Материал браслета',
              'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',
              'Ссылка на карточку с товаром'], ]

    for i in range(1, 33):
        url = f'{main_url}{i}.html'
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        all_items = soup.find_all('div', class_='description')

        for j in all_items:
            row = []
            row.append(j.find('p', id='p_header').text.strip())
            row.append(j.find('p', class_='article').text.split(':')[1].strip())
            row += [k.text.split(':')[1].strip() for k in j.find_all('li')]
            row.append(j.find('span', id='in_stock').text.split(':')[1].strip())
            row.append(j.find('span', id='price').text.strip())
            row.append(j.find('span', id='old_price').text.strip())
            row.append(url)
            table.append(row)

    with open('/Users/ivankedrov/parsing_stepik/Сохранение_результатов_в_Excel/4_9_2.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(table)


watches_to_table()