# Запрашивайте данные с веб-сайта, который содержит таблицу автомобилей.
# Фильтруйте автомобили по заданным критериям:
# Cтоимость не выше 4 000 000 (Стоимость авто <= 4000000),
# Год выпуска начиная с 2005 года (Год выпуска >= 2005),
# Тип двигателя - Бензиновый (Тип двигателя == "Бензиновый").
# Выводите результат в формате JSON, при отправке данных в валидатор, важен каждый пробел и перенос строки.
# Используйте эти параметры для формирования JSON
# json.dumps(sorted_cars, indent=4, ensure_ascii=False)
# Сортируйте отфильтрованный JSON  автомобилей по стоимости от меньшего к большему
# sorted(filtered_cars, key=lambda x: x["Стоимость авто"])

import requests
from bs4 import BeautifulSoup

# Запрашиваем данные с сайта
response = requests.get("https://parsinger.ru/4.8/6/index.html")
response.raise_for_status()  # Проверяем, успешно ли выполнен запрос
response.encoding='utf-8'
# Разбираем содержимое с помощью Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем таблицу с данными
table = soup.find('table')

# Проверяем, найдена ли таблица
if table:
    rows = table.find_all('tr')[1:]  # Исключаем заголовок таблицы
else:
    rows = []

# Собираем данные в список словарей
cars = []
for row in rows:
    columns = row.find_all('td')
    car = {
        "Марка Авто": columns[0].text,
        "Год выпуска": int(columns[1].text),
        "Тип двигателя": columns[4].text,
        "Стоимость авто": int(columns[7].text.replace(',', ''))  # Удаляем запятые для преобразования в число
    }
    cars.append(car)

# Фильтруем список по заданным условиям
filtered_cars = [car for car in cars if car["Стоимость авто"] <= 3000000 and car["Год выпуска"] <= 2010 and car["Тип двигателя"] == "Бензиновый"]

# Сортируем список по стоимости
sorted_cars = sorted(filtered_cars, key=lambda x: x["Стоимость авто"])

print(sorted_cars)