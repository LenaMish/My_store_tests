from src.pages.login.login_page import LoginPage
from src.test_base.test_base import TestBase
import os


USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


class TestLogin(TestBase):
    def test_login_success(self):
        self.driver.get("http://localhost:3000/login")
        
        (LoginPage(self.driver)
         .fill_form(USERNAME, PASSWORD)
         .assert_success_login(self))
