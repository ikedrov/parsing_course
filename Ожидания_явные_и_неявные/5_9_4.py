# Портал В Неизвестное: Ваш первый шаг - зайти на сайт и стать свидетелем этого волшебства: блоки появляются и исчезают, как призраки.
# Легенда о Таинственном Блоке: Среди множества блоков есть один особенный. Его ID "qQm9y1rk", и он – ключ к забытым знаниям.
# Сражение с Временем: Проблема в том, что никто не знает, когда и где этот блок решит показать себя. Он может мелькнуть на долю секунды или вовсе остаться в тени. Но если вы его увидите, действуйте быстро!
# Ключевой Момент: Как только вы обнаружите блок с ID "qQm9y1rk", мгновенно кликните по нему. Ведь этот блок не привык к вниманию и быстро исчезнет.
# Сокровище Знаний: Если вам удастся кликнуть по блоку, вы будете вознаграждены: в alert-окне появится секретный код, который приведет вас к решению задачи.

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.alert import Alert

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.9/2/index.html')

    box = (By.ID, 'qQm9y1rk')
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(box)).click()

    try:
        alert = Alert(driver)
        print(alert.text)
        alert.accept()
    except NoAlertPresentException:
        pass

