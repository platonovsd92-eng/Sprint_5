from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *
from config import URLs  # Импортируем URL из конфига
from helpers.data_generator import generate_unique_email, generate_password


class TestLogin:

    def test_login_main_page_button(self, driver, registered_user):
        """Вход по кнопке «Войти в аккаунт» на главной странице"""
        # Переходим на главную
        driver.get(URLs.MAIN_PAGE)
        
        # Кликаем «Войти в аккаунт»
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(MAIN_PAGE_LOGIN_BUTTON)).click()

        # Вводим данные зарегистрированного пользователя
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LOGIN_EMAIL_INPUT)).send_keys(registered_user["email"])
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LOGIN_BUTTON).click()

        # Проверяем успешный вход - ждем кнопку и проверяем в одном шаге
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON)).is_displayed()

    def test_login_personal_account_button(self, driver, registered_user):
        """Вход через кнопку «Личный кабинет»"""
        driver.get(URLs.MAIN_PAGE)
        
        # Кликаем «Личный кабинет»
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()

        # Вводим данные
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LOGIN_EMAIL_INPUT)).send_keys(registered_user["email"])
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LOGIN_BUTTON).click()

        # Проверка успешного входа
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON)).is_displayed()

    def test_login_from_registration_form(self, driver, registered_user):
        """Вход через кнопку в форме регистрации"""
        driver.get(URLs.REGISTER_PAGE)
        
        # Кликаем ссылку «Войти» на странице регистрации
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LOGIN_LINK_FROM_REGISTER)).click()

        # Вводим данные
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LOGIN_EMAIL_INPUT)).send_keys(registered_user["email"])
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LOGIN_BUTTON).click()

        # Проверка успешного входа
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON)).is_displayed()

    def test_login_from_password_recovery(self, driver, registered_user):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get(URLs.LOGIN_PAGE)
        
        # Кликаем ссылку восстановления пароля
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(RESTORE_PASSWORD_LINK)).click()

        # На странице восстановления пароля кликаем «Войти»
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LOGIN_LINK_FROM_REGISTER)).click()

        # Вводим данные
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LOGIN_EMAIL_INPUT)).send_keys(registered_user["email"])
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LOGIN_BUTTON).click()

        # Проверка успешного входа
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON)).is_displayed()