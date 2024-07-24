from selenium.webdriver.common.by import By


class HomePageLocators:
    RegisterLink = (By.XPATH, '//a[@href="/register"]')
    ItemAddButton = (By.XPATH, '//h3[text()="{product_name}"]/../..//button[text()="Add to Cart"]')
    ItemColorSelect = (By.XPATH, '//h3[text()="{product_name}"]/../..//select[@id="colorSelect"]')
    ItemSizeSelect = (By.XPATH, '//h3[text()="{product_name}"]/../..//select[@id="sizeSelect"]')
    ShoppingCartLink = (By.XPATH, "//a[@href='/shopping-cart']")
    OrdersListLink = (By.XPATH, "//a[@href='/orders']")
