from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *
from helpers.data_generator import generate_unique_email, generate_password


class TestPersonalAccount:

    def login_user(self, driver):
        """Вспомогательный метод для входа пользователя"""
        # Регистрируем пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        email = generate_unique_email()
        password = generate_password(6)
        name = "sergei"

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(REGISTER_NAME_INPUT)).send_keys(name)
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*REGISTER_BUTTON).click()

        # Ждем редирект на страницу входа и выполняем вход
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login"))
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        # Ждем появления кнопки «Оформить заказ»
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON))

    def test_go_to_personal_account(self):
        """Переход в личный кабинет по клику на «Личный кабинет»"""
        driver = webdriver.Chrome()
        driver.maximize_window()

        self.login_user(driver)

        # Кликаем на «Личный кабинет»
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        # Проверяем, что открылась страница профиля
        profile_link = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PROFILE_LINK))
        assert profile_link.is_displayed()

        driver.quit()