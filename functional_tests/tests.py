import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):
    """тест нового посетителя"""
    # browser = webdriver.Firefox()
    # browser.get('http://localhost:8000')

    ser = Service('d:\\yandexdriver.exe')
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=ser, options=options)

    def setUp(self) -> None:
        """установка"""

    def tearDown(self) -> None:
        """завершение"""
        # self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        """подтверждение строки в таблице списка"""
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        """тест.можно начать список и получить его позже"""
# Эдит слышала про крутое новое онлайн-приложение со списком
# неотложных дел. Она решает оценить его домашнюю страницу
        self.browser.get(self.live_server_url)

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
        self.check_for_row_in_list_table('1: Купить павлиньи перья')

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])

# Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
# Она вводит "Сделать мушку из павлиньих перьев" (Эдит очень методична)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

# Страница снова обновляется, и теперь показывает оба элемента ее списка
        self.check_for_row_in_list_table('1: Купить павлиньи перья')
        self.check_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')

        # Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
# сайт сгенерировал для нее уникальный URL-адрес – об этом
# выводится небольшой текст с объяснениями.
        self.fail('Закончить тест')  # Напоминание об окончании теста

# Она посещает этот URL-адрес – ее список по-прежнему там.
# Удовлетворенная, она снова ложится спать
