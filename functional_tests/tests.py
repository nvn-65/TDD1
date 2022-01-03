import time
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase

MAX_WAIT = 10


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

    def wait_for_row_in_list_table(self, row_text):
        """ожидать строку в таблице списка"""
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        """тест.можно начать список для одного пользователя"""
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
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])

# Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
# Она вводит "Сделать мушку из павлиньих перьев" (Эдит очень методична)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)

# Страница снова обновляется, и теперь показывает оба элемента ее списка
        self.wait_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')


# Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
# сайт сгенерировал для нее уникальный URL-адрес – об этом
# выводится небольшой текст с объяснениями.
        self.fail('Закончить тест')  # Напоминание об окончании теста

# Она посещает этот URL-адрес – ее список по-прежнему там.
# Удовлетворенная, она снова ложится спать

    def test_multiple_users_can_start_lists_at_different_urls(self):
        """тест: многочисленные пользователи могут начать списки по разным url"""
        # Эдит начинает новый список
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')

        # Она замечает, что её список имеет уникальный URL-адрес
        edit_list_url = self.browser.current_url
        self.assertRegex(edit_list_url, 'lists/.+')

        # Теперь новый пользователь, Френсис, приходит на сайт.

        ## Мы используем новый сеанс браузера, тем самым обеспечивая, чтобы никокая
        ## информация от Эдит не прошла через данные cookie и пр.
        self.browser.quit()
        ser = Service('d:\\yandexdriver.exe')
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(service=ser, options=options)

        # Френсис посещает домашнюю страницу. Нет никаких признаков списка Эдит.
        self.browser.get(self.live_server_url)
        page_test = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Купить павлиньи перья', page_test)
        self.assertNotIn('Сделать мушку', page_test)

        # Фрэнсис начинает новый список, вводя новый элемент. Он менее
        # интересен, чем список Эдит...
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Купить молоко')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Купить молоко')

        # Френсис получает уникальный URL-адрес
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertEqual(francis_list_url, edit_list_url)

        # Опять-таки, нет ни следа от списка Эдит
        page_test = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Купить павлиньи перья', page_test)
        self.assertIn('Купить молоко', page_test)

        # Удовлетворенные, они оба ложатся спать
