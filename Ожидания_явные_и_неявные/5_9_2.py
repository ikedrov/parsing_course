# Начало пути: Запустите браузер с помощью Selenium и посетите таинственный сайт.
# Терпение – ключ к успеху: Обратите внимание на кнопку, которая оживает после загрузки страницы. Время, которое потребуется для её активации, варьируется от 1 до 3 секунд.
# Секретные коды: Нажмите на кнопку, и начните слежение за заголовком страницы. Коды будут мелькать в этом заголовке с промежутками от 0,1 до 0,6 секунды.
# Открывайте глаза: Ваша цель - не просто просмотреть коды. Вам нужно отловить тот момент, когда в заголовке появится фраза "JK8HQ".
# Секретный знак: При обнаружении этой фразы в заголовке, используйте знакомый вам метод title_contains('JK8HQ'). Если он вернет True, сохраните полный текст этого заголовка.

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/expectations/4/index.html')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()
    WebDriverWait(driver, 20).until(EC.title_contains('JK8HQ'))
    print(driver.title)
