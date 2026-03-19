from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *
from config import URLs


class TestNavigationFromProfile:

    def test_go_to_constructor_from_profile(self, driver, logged_in_user):
        """Переход из личного кабинета в конструктор по клику на «Конструктор»"""
        
        # Переходим в личный кабинет (если мы не там)
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PROFILE_LINK))

        # Кликаем на «Конструктор»
        driver.find_element(*CONSTRUCTOR_BUTTON).click()

        # Проверяем, что вернулись на главную страницу
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON)).is_displayed()

    def test_go_to_main_via_logo_from_profile(self, driver, logged_in_user):
        """Переход из личного кабинета на главную по клику на логотип"""
        
        # Переходим в личный кабинет (если мы не там)
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PROFILE_LINK))

        # Кликаем на логотип Stellar Burgers
        driver.find_element(*LOGO).click()

        # Проверяем, что вернулись на главную страницу
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON)).is_displayed()