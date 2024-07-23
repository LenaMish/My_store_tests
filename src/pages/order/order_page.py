from selenium.webdriver.common.by import By
from src.pages.base.base_page import BasePage
from src.pages.login.login_page_locators import LoginPageLocators
import unittest
from selenium import webdriver

from src.pages.order.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

        self.checkout_button = self.wait_for_element(*OrderPageLocators.CheckoutButton)
        self.zabka_delivery_button = self.wait_for_element(*OrderPageLocators.ZabkaDeliveryRadioButton)
        self.inpot_courier_delivery_button = self.wait_for_element(*OrderPageLocators.InputCourierDeliveryRadioButton)
        self.cash_payment_button = self.wait_for_element(*OrderPageLocators.CashPaymentRadioButton)

    def pay_by_cash(self):
        self.cash_payment_button.click()
        return self

    def approve_payment_by_cash(self):
        btn = self.wait_for_element(*OrderPageLocators.ApproveCashPaymentButton)
        btn.click()
        return self

    def set_delivery(self, delivery_type: str):
        match delivery_type:
            case "zabka":
                self.zabka_delivery_button.click()
            case "input_courier":
                self.inpot_courier_delivery_button.click()
            case _:
                raise ValueError("Invalid delivery_type")
        return self

    def fill_form(self, form_data: dict[str, str]):
        for field_name, value in form_data.items():
            self.enter_text(By.NAME, field_name, value)
        return self

    def submit_form(self):
        self.checkout_button.click()
        return self

