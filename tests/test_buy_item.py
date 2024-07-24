import time

from src.pages.home.home_page import HomePage
from src.pages.login.login_page import LoginPage
from src.pages.order.order_page import OrderPage
from src.pages.orders_list.orders_list_page import OrdersListPage
from src.pages.register.register_page import RegisterPage
from src.pages.shopping_cart.shopping_cart_page import ShoppingCartPage
from src.test_base.test_base import TestBase
from datetime import datetime
import os
import faker

PASSWORD = os.environ.get("PASSWORD")
PASSWORD_CONFIRMATION = os.environ.get("PASSWORD_CONFIRMATION")
WEBSITE_URL = os.environ.get("WEBSITE_URL")
SHIPPING_DETAILS = {
    "name": "Jan Kowalski",
    "street": "Pulaska 401",
    "post_code": "02-784",
    "city": "Warszawa",
    "phone": "125874569",
    "email": "jan@gmail.com"
}

fake = faker.Faker()


class TestBuyItem(TestBase):
    def test_buy_item_success(self):
        self.driver.get(WEBSITE_URL)

        username = fake.user_name()
        email = fake.email()

        (HomePage(self.driver)
         .go_to_register())

        (RegisterPage(self.driver)
         .fill_form(username, email, PASSWORD, PASSWORD_CONFIRMATION))

        (LoginPage(self.driver)
         .fill_form(username, PASSWORD))

        (HomePage(self.driver, is_logged_in=True)
         .add_to_cart("Roses", "pink", "M")
         .add_to_cart("Lilies", "red", "L")
         .add_to_cart("Tulips", "red", "M")
         .go_to_shopping_cart())

        (ShoppingCartPage(self.driver)
         .order_now())

        (OrderPage(self.driver)
         .pay_by_cash()
         .set_delivery("zabka")
         .fill_form(SHIPPING_DETAILS)
         .submit_form()
         .approve_payment_by_cash())

        (HomePage(self.driver, is_logged_in=True)
         .go_to_orders_list())
        time.sleep(10)
        (OrdersListPage(self.driver)
         .assert_page_contains_orders(self, 1)
         .assert_order_contains_data(self,
                                     order_no=1,
                                     expected_date=datetime.now().strftime("%Y-%m-%d"),
                                     expected_price=88.99,
                                     expected_payment_type="cash",
                                     expected_items=["Roses", "Lilies", "Tulips"]))



