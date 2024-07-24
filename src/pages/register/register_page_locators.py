from selenium.webdriver.common.by import By


class RegisterPageLocators:
    UsernameInput = (By.XPATH, '//form[@class="register-form"]//input[@id="username"]')
    EmailInput = (By.XPATH, '//form[@class="register-form"]//input[@id="email"]')
    PasswordInput = (By.XPATH, '//form[@class="register-form"]//input[@id="password"]')
    PasswordConfirmationInput = (By.XPATH, '//form[@class="register-form"]//input[@id="password-confirmation"]')
    SubmitRegisterButton = (By.XPATH, "//button[@type='submit']")
    Status = (By.XPATH, '//div[@role="status"]')