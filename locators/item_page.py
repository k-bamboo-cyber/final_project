from selenium.webdriver.common.by import By


class ItemPageLocators:
    ITEM = (By.CLASS_NAME, "inventory_details")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_details_price")
    ITEM_NAME = (By.CLASS_NAME, "inventory_details_name")
    ITEM_DESC = (By.CLASS_NAME, "inventory_details_desc")
    ITEM_IMG = (By.CLASS_NAME, "inventory_details_img")
    ADD_TO_CART_BTN = (By.CLASS_NAME, "btn_inventory")
    BACK_BTN = (By.CLASS_NAME, "inventory_details_back_button")
    CART_NUMBER = (By.CLASS_NAME, "shopping_cart_badge")
    REMOVE_BUTTON = (By.CLASS_NAME, "btn_inventory")
    APP_LOGO = (By.CLASS_NAME, "app_logo")
