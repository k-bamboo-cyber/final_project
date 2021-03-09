class Users:
    STANDARD_USERNAME = "standard_user"
    LOCKED_OUT_USERNAME = "locked_out_user"
    PROBLEM_USERNAME = "problem_user"
    PER_GLITCH_USERNAME = "performance_glitch_user"
    EMPTY_USERNAME = ""
    PASSWORD = "secret_sauce"
    EMPTY_PASSWORD = ""


class ButtonTexts:
    LOGOUT_BUTTON_TEXT = "Logout"
    ADD_TO_CART_BUTTON = "ADD TO CART"
    BACK_BUTTON = "<- Back"
    REMOVE_BUTTON = "REMOVE"
    USERS_LIST = "Accepted usernames are:"


class Alerts:
    LOCKED_OUT_ALERT = "Epic sadface: Sorry, this user has been locked out."
    NON_EXIST_USER_ALERT = (
        "Epic sadface: Username and password do not match any user in this service"
    )
    EMPTY_MAIL_ALERT = "Epic sadface: Username is required"
    EMPTY_PASSWORD_ALERT = "Epic sadface: Password is required"
    EMPTY_FIRSTAME_ALERT = "Error: First Name is required"
    EMPTY_LASTAME_ALERT = "Error: Last Name is required"
    EMPTY_ZIPCODE_ALERT = "Error: Postal Code is required"


class Links:
    LINKEDIN_LINK = "https://www.linkedin.com/company/sauce-labs/"
    TWITTER_LINK = "https://twitter.com/saucelabs"
    FACEBOOK_LINK = "https://www.facebook.com/saucelabs"


class Pictures:
    COMPLETE_IMG = "https://www.saucedemo.com/static/media/pony-express.46394a5d.png"
