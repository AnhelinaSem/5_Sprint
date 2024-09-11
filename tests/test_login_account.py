from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import Config
from src.locators import Mestolocators
from src.data import get_exist_user_data



class TestLogin:

    def test_personal_login_account(self, driver):
        driver.get(f'{Config.URL}')
        # Нажать кнопку "Личный Кабинет"
        driver.find_element(*Mestolocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.PAGE_LOAD)))
        email_data, password_data = get_exist_user_data()
        driver.find_element(*Mestolocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Mestolocators.PASSWORD_FIELD).send_keys(password_data)
# Нажать кнопку "Войти"
        driver.find_element(*Mestolocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        # Проверка успешного входа
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


    def test_login_button(self,driver):
        driver.get(f'{Config.URL}')

        driver.find_element(*Mestolocators.LOGIN_ACCOUNT).click()
        email_data, password_data = get_exist_user_data()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.PAGE_LOAD)))
        driver.find_element(*Mestolocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Mestolocators.PASSWORD_FIELD).send_keys(password_data)
        # Нажать кнопку "Войти"
        driver.find_element(*Mestolocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        # Проверка успешного входа
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_button_password_reset(self, driver):
        driver.get(f'{Config.URL}/forgot-password')
        # Нажать кнопку
        driver.find_element(*Mestolocators.LOGIN_EXTRA).click()
        email_data, password_data = get_exist_user_data()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.PAGE_LOAD)))
        driver.find_element(*Mestolocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Mestolocators.PASSWORD_FIELD).send_keys(password_data)
        # Нажать кнопку "Войти"
        driver.find_element(*Mestolocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        # Проверка успешного входа
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_button_registration(self, driver):
        driver.get(f'{Config.URL}/register')
        # Нажать кнопку
        driver.find_element(*Mestolocators.LOGIN_EXTRA).click()
        email_data, password_data = get_exist_user_data()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.PAGE_LOAD)))
        driver.find_element(*Mestolocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Mestolocators.PASSWORD_FIELD).send_keys(password_data)
        # Нажать кнопку "Войти"
        driver.find_element(*Mestolocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        # Проверка успешного входа
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
