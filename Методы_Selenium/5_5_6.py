# Загрузка Страницы: Откройте страницу с помощью Selenium.
#
# Используйте эту страницу с двумя элементами для тренировки.
#
# Коды Цветов: Получите цвет в формате HEX из каждого элемента <span>.
#
# Выбор в Списке: В выпадающем списке в каждом контейнере найдите и выберите тот же HEX цвет что и у родительского контейнера.
#
# Кнопочная Магия: Найдите и нажмите на кнопку, у которой атрибут data-hex совпадает с HEX цветом родительского контейнера.
#
# Чек-Бокс Челлендж: Поставьте галочку в чек-боксе на странице.
#
# Текстовое Поле: Вставьте в текстовое поле тот же HEX-цвет, который имеет фон родительского контейнера.
#
# Подтверждение: Нажмите на кнопку "Проверить": если вставлен корректный HEX, то на кнопке появится "ОК".
#
# Повторение: Повторите все эти шаги для каждого найденного на странице контейнера.
#
# Финальный Шаг: После выполнения всех действий, нажмите на кнопку "Проверить все элементы", кнопка расположена в самом низу, появится alert если все условия соблюдены.
#
# Секретный Код: Из алерт-окна получите числовой код и вставьте его в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.5/5/1.html')
    elements = driver.find_elements(By.XPATH, "//div[contains(@style, 'background-color')]")

    for el in elements:
        color = el.find_element(By.TAG_NAME, 'span').text
        select_element = el.find_element(By.TAG_NAME, 'select')
        select = Select(select_element)
        select.select_by_value(color)
        el.find_element(By.CSS_SELECTOR, f"button[data-hex='{color}']").click()
        el.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(color)
        el.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
        el.find_element(By.XPATH, "//button[text()='Проверить']").click()

    driver.find_element(By.XPATH, "//button[text()='Проверить все элементы']").click()
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)






