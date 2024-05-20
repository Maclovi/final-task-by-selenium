from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    JUMP_TO_BUSKET = (By.CSS_SELECTOR, "span.btn-group > a")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "a.btn-lg")
    BUSKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    SEND_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    SEND_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    CLICK_REGISTER = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductLocators:
    BUSKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    CHECK_ADDED = (By.CSS_SELECTOR, "div:first-child > .alertinner > strong")
    SUCCESS_MESSAGE = CHECK_ADDED
