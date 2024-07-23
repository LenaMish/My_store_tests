from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import dotenv

dotenv.load_dotenv()


class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")

    def tearDown(self) -> None:
        self.driver.close()

    def click_element(self, by, locator_text, timeout=10):
        element = self.wait_for_element(by, locator_text, timeout)
        element.click()

    def get_element_text(self, by, locator_text):
        element = self.wait_for_element(by, locator_text)
        return element.text

    def enter_text(self, by, locator_text, text, timeout=10):
        element = self.wait_for_element(by, locator_text, timeout)
        element.send_keys(text)

    def wait_for_element(self, by, locator_text, timeout=10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, locator_text)))

    def login_user(self, username, password):
        driver = self.driver

        login_link = driver.find_element(By.XPATH, '//a[text()="Login"]')
        login_link.click()

        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys(username)

        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)

        submit_button = driver.find_element(By.XPATH, '//form[@class="login-form"]/button')
        submit_button.click()

    def fill_form(self, by, form_fields):
        for field_name, value in form_fields.items():
            self.enter_text(by, field_name, value)

    def register_user(self, username, email, password, password_confirmation):
        driver = self.driver

        register_link = driver.find_element(By.XPATH, '//a[text()="Register"]')
        register_link.click()

        username_input = driver.find_element(By.ID, "username")
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")
        password_confirmation_input = driver.find_element(By.ID, "password-confirmation")

        username_input.send_keys(username)
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_confirmation_input.send_keys(password_confirmation)

        submit_button = driver.find_element(By.XPATH, '//form[@class="register-form"]/button')
        submit_button.click()
