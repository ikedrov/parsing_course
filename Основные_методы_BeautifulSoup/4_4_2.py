# Обработать предоставленную HTML-структуру.
# Найти внутри неё тег <p> с классом card-description.
# Извлечь текстовое описание товара из найденного тега.

from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Пример карточки товара</title>
</head>
<body>
    <div class="card">
        <img src="image.jpg" alt="Пример изображения товара">
        <h2 class="card-title"> iPhone 15 </h2>
        <p class="card-description">Аппаратной основой Apple iPhone 15 Pro Max стал 3-нанометровый чипсет A17 Pro с 6-ядерным GPU и поддержкой трассировки лучей.</p>
        <p class="card-price">999 999 руб.</p>
        <a href="https://example.com/product-link" class="card-link">Подробнее</a>
    </div>
</body>
</html>
"""


def find_description():
    soup = BeautifulSoup(html_doc, 'html.parser')
    p_description = soup.find('p', {'class': 'card-description'})
    print(p_description.text)


find_description()
