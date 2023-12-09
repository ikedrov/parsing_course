# Погружение: Откройте сайт с помощью Selenium.
# Активация тайных порталов: Нажимая на каждую из 10 кнопок, вы активируете ворота в другую вкладку. Это ваш шанс найти одну из частей кода.
# Исследование: В каждой новой вкладке ищите в title число — ваш ключ к решению.
# Сбор информации: Соберите все 10 чисел и сложите их.

from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/blank/3/index.html')
    buttons = driver.find_elements(By.TAG_NAME, 'input')
    result = []
    for button in buttons:
        button.click()
    for i in reversed(range(len(driver.window_handles))):
        driver.switch_to.window(driver.window_handles[i])
        title = driver.execute_script("return document.title;")
        if title.isdigit():
            result.append(int(title))
        driver.close()
    print(sum(result))
