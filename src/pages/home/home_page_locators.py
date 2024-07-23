from selenium.webdriver.common.by import By


class HomePageLocators:
    RegisterLink = (By.PARTIAL_LINK_TEXT, "Register")
    ItemAddButton = (By.XPATH, '//h3[text()="{product_name}"]/../..//button[text()="Add to Cart"]')
    ShoppingCartLink = (By.XPATH, "//a[@href='/shopping-cart']")
    OrdersListLink = (By.XPATH, "//a[@href='/orders']")
