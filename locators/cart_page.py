from selenium.webdriver.common.by import By


class CartPageLocators:
    REMOVE_BUTTON = (By.CLASS_NAME, "cart_button")
    CHECKOUT_BUTTON = (By.CLASS_NAME, "checkout_button")
    SHOPPING_BUTTON = (By.CLASS_NAME, "btn_secondary")
