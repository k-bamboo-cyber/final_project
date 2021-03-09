from selenium.webdriver.common.by import By


class InfoPageLocators:
    FIRSTNAME_INPUT = (By.ID, "first-name")
    LASTNAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    ALERT = (By.XPATH, '//*[@id="checkout_info_container"]/div/form/h3')
    CONTINUE_BUTTON = (By.CLASS_NAME, "btn_primary")
