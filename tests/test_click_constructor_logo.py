from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import Config
from src.locators import Mestolocators
from src.data import get_exist_user_data


class TestClick:

    def test_click_logo(self, driver):
        driver.get(f'{Config.URL}')
        # Нажать кнопку "Личный Кабинет"
        driver.find_element(*Mestolocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.PAGE_LOAD)))
        email_data, password_data = get_exist_user_data()
        driver.find_element(*Mestolocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Mestolocators.PASSWORD_FIELD).send_keys(password_data)
# Нажать кнопку "Войти"
        driver.find_element(*Mestolocators.LOGIN_BUTTON).click()

        # Нажать кнопку "Личный Кабинет"
        driver.find_element(*Mestolocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(EC.url_to_be((f'{Config.URL}/account/profile')))
        # Нажать кнопку logo
        driver.find_element(*Mestolocators.LOGO).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_click_onstructor(self, driver):
        driver.get(f'{Config.URL}')
        # Нажать кнопку "Личный Кабинет"
        driver.find_element(*Mestolocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Mestolocators.PAGE_LOAD)))
        email_data, password_data = get_exist_user_data()
        driver.find_element(*Mestolocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*Mestolocators.PASSWORD_FIELD).send_keys(password_data)
# Нажать кнопку "Войти"
        driver.find_element(*Mestolocators.LOGIN_BUTTON).click()

        # Нажать кнопку "Личный Кабинет"
        driver.find_element(*Mestolocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(EC.url_to_be((f'{Config.URL}/account/profile')))
        # Нажать кнопку Конструктор
        driver.find_element(*Mestolocators.CONSTRUCTOR_BUTTON).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
