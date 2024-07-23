from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_element(self, by, locator_text, timeout=10):
        element = self.wait_for_element(by, locator_text, timeout)
        element.click()

    def get_element_text(self, by, locator_text):
        element = self.wait_for_element(by, locator_text)
        return element.text

    def enter_text(self, by, locator_text, text, timeout=10):
        element = self.wait_for_element(by, locator_text, timeout)
        element.send_keys(text)

    def wait_for_element(self, by, locator_text, timeout=20) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, locator_text)))

    def wait_for_page_contains_url(self, url: str, timeout=10):
        WebDriverWait(self.driver, timeout=timeout).until(EC.url_contains(url))
