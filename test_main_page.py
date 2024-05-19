from typing import TYPE_CHECKING

from selenium.webdriver.chrome.webdriver import WebDriver

if TYPE_CHECKING:
    from pages.main_page import MainProto

from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser: WebDriver) -> None:
    link = "http://selenium1py.pythonanywhere.com/"
    page: MainProto = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    input("prsss")
    page.should_be_login_link()


def test_form(browser: WebDriver) -> None:
    page: LoginPage = LoginPage(browser, browser.current_url)
    page.should_be_login_page()
