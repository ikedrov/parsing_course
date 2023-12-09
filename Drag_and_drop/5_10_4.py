# Встреча с Зелёными Квадратами: При открытии сайта вы увидите 10 зелёных квадратов, каждый из которых готов к переезду. Ваша задача - помочь им в этом.
# Путешествие к Серой Области: Перетаскивайте квадраты один за другим в серую область. Обратите внимание, каждый квадрат несет в себе частицу целого, и только объединив их в серой области, вы сможете увидеть полную картину.
# Получение Секретного Кода: Как только последний зелёный квадрат окажется в серой области, перед вами откроется секретный код. Этот код символизирует успешное завершение задачи и ваше понимание важности каждого шага в путешествии.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.10/2/index.html')
    blocks = browser.find_elements(By.CLASS_NAME, 'draganddrop')
    end = browser.find_element(By.CLASS_NAME, 'draganddrop_end')
    actions = ActionChains(browser)
    for block in blocks:
        actions.drag_and_drop(block, end).perform()

    print(browser.find_element(By.ID, 'message').text)

