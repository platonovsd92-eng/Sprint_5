from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *
from helpers.data_generator import generate_unique_email, generate_password


class TestLogout:

    def test_logout(self):
        """Выход из аккаунта по кнопке «Выйти» в личном кабинете"""
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Регистрируем нового пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        email = generate_unique_email()
        password = generate_password(6)
        name = "sergei"

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(REGISTER_NAME_INPUT)).send_keys(name)
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*REGISTER_BUTTON).click()

        # Выполняем вход
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login"))
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON))

        # Переходим в личный кабинет
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PROFILE_LINK))

        # Нажимаем кнопку «Выход»
        driver.find_element(*LOGOUT_BUTTON).click()

        # Проверяем, что произошел выход и открылась страница входа
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LOGIN_BUTTON))
        assert "login" in driver.current_url

        driver.quit()