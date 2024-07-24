import time

from selenium import webdriver
from src.pages.base.base_page import BasePage
from src.pages.home.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver: webdriver.Chrome, is_logged_in=False):
        super().__init__(driver)
        self.is_logged_in = is_logged_in

        if self.is_logged_in:
            self.shopping_cart_link = self.wait_for_element(*HomePageLocators.ShoppingCartLink)
            self.orders_link = self.wait_for_element(*HomePageLocators.OrdersListLink)
        else:
            self.register_link = self.wait_for_element(*HomePageLocators.RegisterLink)

    def go_to_register(self):
        if not self.is_logged_in:
            self.register_link.click()
            return self

    def go_to_shopping_cart(self):
        if self.is_logged_in:
            self.shopping_cart_link.click()
            return self

    def add_to_cart(self, product_name, color, size):
        color_xpath = HomePageLocators.ItemColorSelect
        self.find_select(color_xpath[0], color_xpath[1].replace("{product_name}", product_name))\
            .select_by_visible_text(color)

        size_xpath = HomePageLocators.ItemSizeSelect
        self.find_select(size_xpath[0], size_xpath[1].replace("{product_name}", product_name)) \
            .select_by_visible_text(size)

        xpath = HomePageLocators.ItemAddButton
        self.click_element(xpath[0], xpath[1].replace("{product_name}", product_name))

        return self

    def go_to_orders_list(self):
        if self.is_logged_in:
            self.orders_link.click()
            return self
