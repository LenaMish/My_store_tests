from selenium.webdriver.common.by import By


class LoginPageLocators:
    UsernameInput = (By.ID, "username")
    PasswordInput = (By.ID, "password")
    SubmitLoginButton = (By.XPATH, "//button[@type='submit']")
    Status = (By.XPATH, '//div[@role="status"]')

