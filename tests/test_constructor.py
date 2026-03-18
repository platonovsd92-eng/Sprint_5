from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import *


class TestConstructor:

    def test_buns_section(self):
        """Переход к разделу «Булки» в конструкторе"""
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://stellarburgers.education-services.ru/")

        # Ждем загрузки страницы
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Булки']")))

        # Проверяем, что по умолчанию активен раздел «Булки»
        active_section = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Булки" in active_section.text

        # Кликаем на раздел «Соусы»
        sauces = driver.find_element(By.XPATH, "//*[text()='Соусы']")
        sauces.click()
        
        # Ждем, что активный раздел сменился на «Соусы»
        WebDriverWait(driver, 5).until(
            lambda x: "Соусы" in driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]").text)

        # Проверяем, что раздел «Соусы» стал активным
        active_section = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Соусы" in active_section.text

        driver.quit()

    def test_sauces_section(self):
        """Переход к разделу «Соусы» в конструкторе"""
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://stellarburgers.education-services.ru/")

        # Ждем загрузки страницы
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Соусы']")))

        # Кликаем на раздел «Соусы»
        sauces = driver.find_element(By.XPATH, "//*[text()='Соусы']")
        sauces.click()
        
        # Ждем, что раздел «Соусы» стал активным
        WebDriverWait(driver, 5).until(
            lambda x: "Соусы" in driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]").text)

        # Проверяем
        active_section = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Соусы" in active_section.text

        driver.quit()

    def test_fillings_section(self):
        """Переход к разделу «Начинки» в конструкторе"""
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://stellarburgers.education-services.ru/")

        # Ждем загрузки страницы
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Начинки']")))

        # Кликаем на раздел «Начинки»
        fillings = driver.find_element(By.XPATH, "//*[text()='Начинки']")
        fillings.click()
        
        # Ждем, что раздел «Начинки» стал активным
        WebDriverWait(driver, 5).until(
            lambda x: "Начинки" in driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]").text)

        # Проверяем
        active_section = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Начинки" in active_section.text

        driver.quit()