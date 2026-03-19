from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *
from config import URLs  # Импортируем URL из конфига


class TestLogout:

    def test_logout(self, driver, logged_in_user):
        """Выход из аккаунта по кнопке «Выйти» в личном кабинете"""
        
        # Переходим в личный кабинет
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PROFILE_LINK))

        # Нажимаем кнопку «Выход»
        driver.find_element(*LOGOUT_BUTTON).click()

        # Проверяем, что произошел выход и открылась страница входа
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LOGIN_BUTTON)).is_displayed()
        assert "login" in driver.current_url