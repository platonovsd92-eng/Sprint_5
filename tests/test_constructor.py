from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *  # Импортируем все локаторы
from config import URLs


class TestConstructor:

    def test_buns_section_active_by_default(self, driver):
        """Тест 1: Проверка, что по умолчанию активен раздел «Булки»"""
        driver.get(URLs.MAIN_PAGE)

        # Ждем загрузки страницы
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(BUNS_TEXT))

        # Проверяем, что активный раздел - «Булки»
        active_section = driver.find_element(*ACTIVE_SECTION)
        assert "Булки" in active_section.text

    def test_switch_to_sauces_section(self, driver):
        """Тест 2: Проверка переключения на раздел «Соусы»"""
        driver.get(URLs.MAIN_PAGE)

        # Ждем загрузки страницы
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(SAUCES_SECTION))

        # Кликаем на раздел «Соусы»
        driver.find_element(*SAUCES_SECTION).click()

        # Проверяем, что активный раздел сменился на «Соусы»
        WebDriverWait(driver, 5).until(
            lambda x: "Соусы" in driver.find_element(*ACTIVE_SECTION).text)
        
        active_section = driver.find_element(*ACTIVE_SECTION)
        assert "Соусы" in active_section.text

    def test_switch_to_fillings_section(self, driver):
        """Тест 3: Проверка переключения на раздел «Начинки»"""
        driver.get(URLs.MAIN_PAGE)

        # Ждем загрузки страницы
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(FILLINGS_SECTION))

        # Кликаем на раздел «Начинки»
        driver.find_element(*FILLINGS_SECTION).click()

        # Проверяем, что активный раздел сменился на «Начинки»
        WebDriverWait(driver, 5).until(
            lambda x: "Начинки" in driver.find_element(*ACTIVE_SECTION).text)
        
        active_section = driver.find_element(*ACTIVE_SECTION)
        assert "Начинки" in active_section.text