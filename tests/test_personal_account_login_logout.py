from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import Config
from src.locators import Mestolocators
from src.data import get_exist_user_data
from selenium.webdriver.common.by import By


class TestLoginLogout:

    def test_account_login(self, driver):
        driver.get(f'{Config.URL}')
        # Нажать кнопку "Личный Кабинет"
        driver.find_element(*Mestolocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.PAGE_LOAD)))
        email_data, password_data = get_exist_user_data()
        driver.find_element(*Mestolocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Mestolocators.PASSWORD_FIELD).send_keys(password_data)
# Нажать кнопку "Войти"
        driver.find_element(*Mestolocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.PERSONAL_ACCOUNT)))

        # Нажать кнопку "Личный Кабинет"
        driver.find_element(*Mestolocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(EC.url_to_be((f'{Config.URL}/account/profile')))
        assert driver.current_url == f'{Config.URL}/account/profile'

    def test_account_logout(self, driver):
        driver.get(f'{Config.URL}')
        # Нажать кнопку "Личный Кабинет"
        driver.find_element(*Mestolocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.PAGE_LOAD)))
        email_data, password_data = get_exist_user_data()
        driver.find_element(*Mestolocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Mestolocators.PASSWORD_FIELD).send_keys(password_data)
        # Нажать кнопку "Войти"
        driver.find_element(*Mestolocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.PERSONAL_ACCOUNT)))

        # Нажать кнопку "Личный Кабинет"
        driver.find_element(*Mestolocators.PERSONAL_ACCOUNT).click()

        # Добавить явное ожидание для кнопки "Выход"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.EXIT)))

        # Нажать кнопку "Выход"
        driver.find_element(*Mestolocators.EXIT).click()

        WebDriverWait(driver, 10).until(EC.url_to_be((f'{Config.URL}/login')))
        assert driver.current_url == f'{Config.URL}/login'
