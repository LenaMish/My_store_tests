from selenium.webdriver.common.by import By


class BasePageLocators:
    LoginLink = (By.XPATH, '//a[text()="Login"]')
    RegisterLink = (By.XPATH, '//a[text()="Register"]')