from selenium.webdriver.common.by import By
from src.pages.base.base_page import BasePage
from src.pages.register.register_page_locators import RegisterPageLocators
import unittest
from selenium import webdriver


class RegisterPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.username_input = self.wait_for_element(*RegisterPageLocators.UsernameInput)
        self.email_input = self.wait_for_element(*RegisterPageLocators.EmailInput)
        self.password_input = self.wait_for_element(*RegisterPageLocators.PasswordInput)
        self.password_confirmation_input = self.wait_for_element(*RegisterPageLocators.PasswordConfirmationInput)
        self.submit_button = self.wait_for_element(*RegisterPageLocators.SubmitRegisterButton)

    def fill_form(self, username: str, email: str, password: str, password_confirmation: str):
        self.username_input.send_keys(username)
        self.email_input.send_keys(email)
        self.password_input.send_keys(password)
        self.password_confirmation_input.send_keys(password_confirmation)
        self.submit_button.click()
        return self

    def assert_success_register(self, test_obj: unittest.TestCase):
        status = self.wait_for_element(*RegisterPageLocators.Status)
        expected_status_text = "Good Job!"
        test_obj.assertEqual(expected_status_text, status.text)
        return self
