import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.data_generator import generate_unique_email, generate_password

# Импортируем локаторы на уровне модуля
from locators import (
    REGISTER_NAME_INPUT, REGISTER_EMAIL_INPUT, REGISTER_PASSWORD_INPUT,
    REGISTER_BUTTON, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON,
    PLACE_ORDER_BUTTON, PERSONAL_ACCOUNT_BUTTON, PROFILE_LINK,
    CONSTRUCTOR_BUTTON, LOGO, LOGOUT_BUTTON, MAIN_PAGE_LOGIN_BUTTON,
    RESTORE_PASSWORD_LINK, LOGIN_LINK_FROM_REGISTER, ERROR_MESSAGE
)


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(driver):
    """Фикстура для создания зарегистрированного пользователя"""
    # Открываем страницу регистрации
    driver.get("https://stellarburgers.education-services.ru/register")
    
    # Генерируем данные
    email = generate_unique_email()
    password = generate_password(6)
    name = "sergei"
    
    # Регистрируем пользователя
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(REGISTER_NAME_INPUT)).send_keys(name)
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*REGISTER_BUTTON).click()
    
    # Ждем редирект на страницу входа
    WebDriverWait(driver, 5).until(EC.url_contains("/login"))
    
    return {"email": email, "password": password, "name": name}


@pytest.fixture
def logged_in_user(driver, registered_user):
    """Фикстура для создания авторизованного пользователя"""
    # Выполняем вход
    driver.get("https://stellarburgers.education-services.ru/login")
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(LOGIN_EMAIL_INPUT)).send_keys(registered_user["email"])
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user["password"])
    driver.find_element(*LOGIN_BUTTON).click()
    
    # Ждем успешного входа
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(PLACE_ORDER_BUTTON))
    
    return registered_user