from selenium.webdriver.common.by import By
from src.pages.base.base_page import BasePage

import unittest
from selenium import webdriver

from src.pages.orders_list.orders_list_page_loctors import OrdersListPageLocators


class OrdersListPage(BasePage):
    def __init__(self, driver: webdriver.Chrome, wait_for_any_order=False):
        super().__init__(driver)

        if wait_for_any_order:
            self.wait_for_element(*OrdersListPageLocators.OrderElement)
        self.orders = self.driver.find_elements(*OrdersListPageLocators.OrderElement)

    def assert_page_contains_orders(self, test_obj: unittest.TestCase, expected_orders_count: int):
        test_obj.assertEqual(expected_orders_count, len(self.orders))
        return self

    def assert_order_contains_data(self, test_obj: unittest.TestCase,
                                   order_no: int, expected_items: list[str],
                                   expected_price: float, expected_date: str, expected_payment_type: str):
        order = self.orders[order_no-1]
        order_properties = order.find_elements(By.TAG_NAME, "p")
        test_obj.assertEqual(f"Payment type: {expected_payment_type}", order_properties[0].text)
        test_obj.assertIn(expected_date, order_properties[1].text)
        test_obj.assertEqual(f"Total: {expected_price}", order_properties[3].text)
        items = [e.text for e in order.find_elements(*OrdersListPageLocators.ProductName)]
        test_obj.assertEqual(sorted(expected_items), sorted(items))
        return self
