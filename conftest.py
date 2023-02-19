import random

import pytest
from selenium import webdriver

default_email = "testtestov6@yandex.ru"
default_password = "12345678"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


#
@pytest.fixture
def random_login():
    return 'Sergey_Tokarev' + str(random.randint(100, 999)) + '@yandex.ru'


@pytest.fixture
def random_password():
    return random.randint(100000, 999999)