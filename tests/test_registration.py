from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os

# Добавляем путь к корневой папке проекта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортируем локаторы
from locators import *
from helpers.data_generator import generate_unique_email, generate_password, generate_name


class TestRegistration:

    def test_successful_registration(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://stellarburgers.education-services.ru/register")

        # Генерируем данные для регистрации
        email = generate_unique_email()
        password = generate_password(6)
        name = generate_name()

        # Заполняем форму регистрации
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(REGISTER_NAME_INPUT)).send_keys(name)
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*REGISTER_BUTTON).click()

        # Проверяем, что произошел редирект на страницу входа
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login"))

        assert "login" in driver.current_url

        driver.quit()

    def test_registration_with_short_password(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://stellarburgers.education-services.ru/register")

        # Генерируем данные с коротким паролем
        email = generate_unique_email()
        password = generate_password(5)  # Пароль короче 6 символов
        name = generate_name()

        # Заполняем форму регистрации
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(REGISTER_NAME_INPUT)).send_keys(name)
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*REGISTER_BUTTON).click()

        # Проверяем появление ошибки для некорректного пароля
        error = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(ERROR_MESSAGE))
        assert "Некорректный пароль" in error.text

        driver.quit()