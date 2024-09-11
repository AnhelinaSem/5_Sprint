from selenium.webdriver.common.by import By

class Mestolocators:
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/following-sibling::input"
    PASSWORD_FIELD = By.XPATH, "//input[contains(@type,'password')]"
    NAME_FIELD = By.XPATH, "//label[text()='Имя']/following-sibling::input"
    PERSONAL_ACCOUNT = By.XPATH, "//p[text()='Личный Кабинет']"
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']"
    BYLKI_SECTION = By.XPATH, "//h2[text()='Булки']"
    SOYS_SECTION = By.XPATH, "//h2[text()='Соусы']"
    NACHINKA_SECTION = By.XPATH, "//h2[text()='Начинки']"
    LOGO = By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]"
    CONSTRUCTOR_BUTTON = By.XPATH, ".//li[1]/a/p[text()='Конструктор']"
    EXIT = By.XPATH, "//button[text()='Выход']"
    PAGE_LOAD = By.CLASS_NAME, "App_App__aOmNj"
    REGISTRATION_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']"
    LOGIN_ACCOUNT = By.XPATH, "//button[text()='Войти в аккаунт']"
    LOGIN_EXTRA = By.XPATH, ".//a[text()='Войти']"
    INCORRECT_PASSWORD = By.XPATH, "//fieldset[3]/div/p[contains(text(), 'Некорректный пароль')]"
