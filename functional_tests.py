from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest


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
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """тест.можно начать список и получить его позже"""
        # Эдит слышала про крутое новое онлайн-приложение со списком
        # неотложных дел. Она решает оценить его домашнюю страницу
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о списках
        # неотложных дел
        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест')  # Напоминание об окончании теста


# Ей сразу же предлагается ввести элемент списка

# Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби –
# вязание рыболовных мушек)

# Когда она нажимает enter, страница обновляется, и теперь страница
# содержит "1: Купить павлиньи перья" в качестве элемента списка

# Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
# Она вводит "Сделать мушку из павлиньих перьев"
# (Эдит очень методична)

# Страница снова обновляется, и теперь показывает оба элемента ее списка
# Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
# сайт сгенерировал для нее уникальный URL-адрес – об этом
# выводится небольшой текст с объяснениями.

# Она посещает этот URL-адрес – ее список по-прежнему там.
# Удовлетворенная, она снова ложится спать


if __name__ == '__main':
    unittest.main()
