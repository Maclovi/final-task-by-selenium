import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage
from pages.locators import BasePageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.login_guest()
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser: WebDriver) -> None:
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()

    def test_guest_should_see_login_link(self, browser: WebDriver) -> None:
        page: LoginPage = LoginPage(browser, browser.current_url)
        page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(
    browser: WebDriver, base_link: str
) -> None:
    page = BasePage(browser, base_link)
    page.jump_to_busket()
    assert page.is_not_element_present(*BasePageLocators.PROCEED_TO_CHECKOUT)
    assert page.is_element_present(*BasePageLocators.BUSKET_IS_EMPTY)
