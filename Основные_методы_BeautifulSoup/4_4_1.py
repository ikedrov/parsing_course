# Скачивание файла: Скачайте zip-архив по предоставленной ссылке вручную.
#
# Распаковка архива: Распакуйте этот архив в папку с вашим проектом.
#
# Парсинг HTML: Извлеките содержимое из файла index.html из распакованного архива.

import lxml
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')
    print(soup)