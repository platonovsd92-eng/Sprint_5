from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *
from config import URLs


class TestPersonalAccount:

    def test_go_to_personal_account(self, driver, logged_in_user):
        """Переход в личный кабинет по клику на «Личный кабинет»"""
        
        # Кликаем на «Личный кабинет»
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        # Проверяем, что открылась страница профиля
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PROFILE_LINK)).is_displayed()