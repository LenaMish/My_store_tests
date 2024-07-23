from selenium.webdriver.common.by import By


class OrdersListPageLocators:
    OrderElement = (By.XPATH, '//div[@class="orders-container"]/ul/li')
    ProductName = (By.XPATH, '//span[@data-testid="product-name"]')
