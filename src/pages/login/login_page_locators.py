from selenium.webdriver.common.by import By


class LoginPageLocators:
    UsernameInput = (By.XPATH, '//form[@class="login-form"]//input[@id="username"]')
    PasswordInput = (By.XPATH, '//form[@class="login-form"]//input[@id="password"]')
    SubmitLoginButton = (By.XPATH, "//button[@type='submit']")
    Status = (By.XPATH, '//div[@role="status"]')

