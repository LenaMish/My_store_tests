from selenium.webdriver.common.by import By
from src.pages.base.base_page import BasePage
from src.pages.login.login_page_locators import LoginPageLocators
import unittest
from selenium import webdriver


class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

        self.wait_for_page_contains_url("login")
        self.username_input = self.wait_for_element(*LoginPageLocators.UsernameInput)
        self.password_input = self.wait_for_element(*LoginPageLocators.PasswordInput)
        self.submit_button = self.wait_for_element(*LoginPageLocators.SubmitLoginButton)

    def fill_form(self, username: str, password: str):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.submit_button.click()
        return self

    def assert_success_login(self, test_obj: unittest.TestCase):
        status = self.wait_for_element(*LoginPageLocators.Status)
        expected_status_text = "Good Job!"
        test_obj.assertEqual(expected_status_text, status.text)
        return self
