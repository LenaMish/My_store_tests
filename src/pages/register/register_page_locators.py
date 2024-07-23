from selenium.webdriver.common.by import By


class RegisterPageLocators:
    UsernameInput = (By.ID, "username")
    EmailInput = (By.ID, "email")
    PasswordInput = (By.ID, "password")
    PasswordConfirmationInput = (By.ID, "password-confirmation")
    SubmitRegisterButton = (By.XPATH, "//button[@type='submit']")
    Status = (By.XPATH, '//div[@role="status"]')