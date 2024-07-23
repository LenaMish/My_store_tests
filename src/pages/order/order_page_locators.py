from selenium.webdriver.common.by import By


class OrderPageLocators:
    CheckoutButton = (By.XPATH, '//button[@class="checkout-button"]')
    ZabkaDeliveryRadioButton = (By.XPATH, '//input[@id="delivery_4"]')
    InputCourierDeliveryRadioButton = (By.XPATH, '//input[@id="delivery_1"]')
    CashPaymentRadioButton = (By.XPATH, '//input[@id="cash"]')
    ApproveCashPaymentButton = (By.XPATH, '//button[text()="Approve payment by cash"]')
