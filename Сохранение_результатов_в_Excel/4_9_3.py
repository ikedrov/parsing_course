# Соберите указанные на изображении ниже данные с сайта тренажёра.
# Заходить в каждую карточку с товаром не требуется, собирать необходимо только с превью карточки.
# Сохраните данные в формате CSV с разделителем ;.

from bs4 import BeautifulSoup
import requests
import csv


urls = ['https://parsinger.ru/html/index1_page_', 'https://parsinger.ru/html/index2_page_',
        'https://parsinger.ru/html/index3_page_', 'https://parsinger.ru/html/index4_page_',
        'https://parsinger.ru/html/index5_page_']


def all_goods_to_table(url):
    table = []
    for i in range(1, 5):
        new_url = f'{url}{i}.html'
        response = requests.get(new_url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        all_items = soup.find_all('div', class_='item')

        for j in all_items:
            row = []
            row.append(j.find('a', class_='name_item').text.strip())
            row += [k.text.split(':')[1].strip() for k in j.find_all('li')]
            row.append(j.find('p', class_='price').text.strip())
            table.append(row)

    with open('/Users/ivankedrov/parsing_stepik/Сохранение_результатов_в_Excel/4_9_3.csv', 'a', encoding='utf-8-sig',
              newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(table)


for u in urls:
    all_goods_to_table(u)