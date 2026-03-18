from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *
from helpers.data_generator import generate_unique_email, generate_password


class TestLogin:

    def create_test_user(self, driver):
        """Создает тестового пользователя и возвращает его email и пароль"""
        driver.get("https://stellarburgers.education-services.ru/register")
        email = generate_unique_email()
        password = generate_password(6)
        name = "sergei"

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(REGISTER_NAME_INPUT)).send_keys(name)
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login"))
        return email, password

    def test_login_main_page_button(self):
        """Вход по кнопке «Войти в аккаунт» на главной странице"""
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Создаем пользователя
        email, password = self.create_test_user(driver)

        # Переходим на главную и кликаем «Войти в аккаунт»
        driver.get("https://stellarburgers.education-services.ru/")
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(MAIN_PAGE_LOGIN_BUTTON)).click()

        # Вводим данные и входим
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LOGIN_EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        # Проверяем успешный вход (появилась кнопка «Оформить заказ»)
        order_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON))
        assert order_button.is_displayed()

        driver.quit()

    def test_login_personal_account_button(self):
        """Вход через кнопку «Личный кабинет»"""
        driver = webdriver.Chrome()
        driver.maximize_window()

        email, password = self.create_test_user(driver)

        driver.get("https://stellarburgers.education-services.ru/")
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LOGIN_EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON))
        assert order_button.is_displayed()

        driver.quit()

    def test_login_from_registration_form(self):
        """Вход через кнопку в форме регистрации"""
        driver = webdriver.Chrome()
        driver.maximize_window()

        email, password = self.create_test_user(driver)

        driver.get("https://stellarburgers.education-services.ru/register")
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LOGIN_LINK_FROM_REGISTER)).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LOGIN_EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON))
        assert order_button.is_displayed()

        driver.quit()

    def test_login_from_password_recovery(self):
        """Вход через кнопку в форме восстановления пароля"""
        driver = webdriver.Chrome()
        driver.maximize_window()

        email, password = self.create_test_user(driver)

        driver.get("https://stellarburgers.education-services.ru/login")
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(RESTORE_PASSWORD_LINK)).click()

        # На странице восстановления пароля кликаем «Войти»
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LOGIN_LINK_FROM_REGISTER)).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LOGIN_EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON))
        assert order_button.is_displayed()

        driver.quit()