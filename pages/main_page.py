import typing

from .base_page import BasePage, BaseProto
from .locators import MainPageLocators


class MainProto(BaseProto, typing.Protocol):
    def go_to_login_page(self) -> None: ...

    def should_be_login_link(self) -> None: ...


class MainPage(BasePage):
    def go_to_login_page(self) -> None:
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self) -> None:
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK,
        ), "Login link is not presented"
