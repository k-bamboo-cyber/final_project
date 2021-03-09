from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    AZ_SORT_BUTTON = (By.CSS_SELECTOR, '[value = "az"]')
    ZA_SORT_BUTTON = (By.CSS_SELECTOR, '[value = "za"]')
    L_TO_H_BUTTON = (By.CSS_SELECTOR, '[value = "lohi"]')
    H_TO_L_BUTTON = (By.CSS_SELECTOR, '[value = "hilo"]')
    ITEM = (By.CLASS_NAME, "inventory_item")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESC = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_IMG = (By.CLASS_NAME, "inventory_item_img")
    TWITTER_BUTTON = (By.CLASS_NAME, "social_twitter")
    FACEBOOK_BUTTON = (By.CLASS_NAME, "social_facebook")
    LINKEDIN_BUTTON = (By.CLASS_NAME, "social_linkedin")
    A = (By.TAG_NAME, "a")
    CART_ICON = (By.CLASS_NAME, "fa-shopping-cart")
