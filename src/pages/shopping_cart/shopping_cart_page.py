from selenium.webdriver.common.by import By
from src.pages.base.base_page import BasePage
from src.pages.login.login_page_locators import LoginPageLocators
import unittest
from selenium import webdriver

from src.pages.shopping_cart.shopping_cart_page_locators import ShoppingCartPageLocators


class ShoppingCartPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.order_now_button = self.wait_for_element(*ShoppingCartPageLocators.OrderNowButton)

    def order_now(self):
        self.order_now_button.click()
        return self
