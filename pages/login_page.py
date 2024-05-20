from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self) -> None:
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self) -> None:
        assert "login" in self.browser.current_url, "login is not in url link"

    def should_be_login_form(self) -> None:
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "there in not login form"

    def should_be_register_form(self) -> None:
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "there is not register from"

    def register_new_user(self, email: str, password: str) -> None:
        self.browser.find_element(*LoginPageLocators.SEND_EMAIL).send_keys(
            email
        )
        self.browser.find_element(*LoginPageLocators.SEND_PASSWORD).send_keys(
            password
        )
        self.browser.find_element(
            *LoginPageLocators.CONFIRM_PASSWORD
        ).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CLICK_REGISTER).click()
