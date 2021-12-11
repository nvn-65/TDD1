import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import unittest

from selenium.webdriver.common.by import By


class NewVisitorTest(unittest.TestCase):
    """тест нового посетителя"""

    def setUp(self) -> None:
        """установка"""

    # browser = webdriver.Firefox()
    # browser.get('http://localhost:8000')

    ser = Service('d:\\yandexdriver.exe')
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=ser, options=options)

    def tearDown(self) -> None:
        """завершение"""
        # self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """тест.можно начать список и получить его позже"""
        # Эдит слышала про крутое новое онлайн-приложение со списком
        # неотложных дел. Она решает оценить его домашнюю страницу
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о списках
        # неотложных дел
        self.assertIn('To-Do lists', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Your To-Do list', header_text)

# Ей сразу же предлагается ввести элемент списка
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Введите задачу')
# Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби –
# вязание рыболовных мушек)
        inputbox.send_keys('Купить павлиньи перья')
# Когда она нажимает enter, страница обновляется, и теперь страница
# содержит "1: Купить павлиньи перья" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(any(row.text == '1: Купить павлиньи перья' for row in rows),
                        "Новый элемент списка не появился в таблице")
# Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
# Она вводит "Сделать мушку из павлиньих перьев"
# (Эдит очень методична)
        self.fail('Закончить тест')  # Напоминание об окончании теста
# Страница снова обновляется, и теперь показывает оба элемента ее списка
# Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
# сайт сгенерировал для нее уникальный URL-адрес – об этом
# выводится небольшой текст с объяснениями.

# Она посещает этот URL-адрес – ее список по-прежнему там.
# Удовлетворенная, она снова ложится спать


if __name__ == '__main':
    unittest.main()
