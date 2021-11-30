from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Установка прошла успешно! Поздравляем!' in browser.title
