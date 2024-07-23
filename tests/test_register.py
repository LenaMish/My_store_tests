from src.pages.register.register_page import RegisterPage
from src.test_base.test_base import TestBase
import os
import faker

PASSWORD = os.environ.get("PASSWORD")
PASSWORD_CONFIRMATION = os.environ.get("PASSWORD_CONFIRMATION")

fake = faker.Faker()


class TestRegister(TestBase):
    def test_register_success(self):
        self.driver.get("http://localhost:3000/register")

        username = fake.user_name()
        email = fake.email()

        (RegisterPage(self.driver)
         .fill_form(username, email, PASSWORD, PASSWORD_CONFIRMATION)
         .assert_success_register(self))
