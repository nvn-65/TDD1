from selenium import webdriver

# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

options = webdriver.ChromeOptions()
binary_yandex_driver_file = 'd:\\yandexdriver.exe'  # path to YandexDriver
driver = webdriver.Chrome(binary_yandex_driver_file)
# driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
driver.get('http://localhost:8000')

assert 'Установка прошла успешно! Поздравляем!' in driver.title
# driver.quit()
