from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_BUTTON = (By.CLASS_NAME, 'btn_action')
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    ALERT = (By.XPATH, '//*[@id="login_button_container"]/div/form/h3')
