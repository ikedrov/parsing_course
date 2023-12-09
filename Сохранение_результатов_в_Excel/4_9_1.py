# Используйте страницу чтобы собрать данные с четырёх страниц в категории hdd.
# "Проваливаться" в каждую карточку не нужно, соберите информацию с превью карточки.
# При создании CSV используйте разделитель:
# delimiter=';'
# Отправьте готовый csv файл в валидатор, для успешной валидации файла, необходимо сохранить тот же порядок строк и столбцов что и в эталонном файле.

import csv
import requests
from bs4 import BeautifulSoup


def hdd_to_table():
    main_url = 'https://parsinger.ru/html/index4_page_'
    table = [['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена'],]

    for i in range(1, 5):
        url = f'{main_url}{i}.html'
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        all_items = soup.find_all('div', class_='item')

        for i in all_items:
            row = []
            row.append(i.find('a', class_='name_item').text.strip())
            row += [j.text.split(':')[1].strip() for j in i.find_all('li')]
            row.append(i.find('p', class_='price').text.strip())
            table.append(row)

    with open('/Users/ivankedrov/parsing_stepik/Сохранение_результатов_в_Excel/4_9_1.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(table)


hdd_to_table()

