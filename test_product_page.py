import time

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.locators import BasePageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage

_product_base_link = (
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
)
_urls = [
    f"{_product_base_link}/?promo=offer{no}" for no in range(10) if no != 7
]


@pytest.mark.auth()
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="class", autouse=True)
    def _setup(self, browser: WebDriver) -> None:
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(
            str(time.time()) + "@fakemail.org", "eeh2jh4k23hsfe"
        )
        page.should_be_authorized_user()

    @pytest.mark.need_review()
    def test_user_can_add_product_to_basket(
        self, browser: WebDriver, link: str
    ) -> None:
        page = ProductPage(browser, link)
        page.add_to_busket()

    def test_user_cant_see_success_message(
        self, browser: WebDriver, link: str
    ) -> None:
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.parametrize("link_p", _urls)
@pytest.mark.need_review()
def test_guest_can_add_product_to_basket(
    browser: WebDriver, link_p: str
) -> None:
    page = ProductPage(browser, link_p)
    page.add_to_busket(quiz=True)


def test_guest_should_see_login_link_on_product_page(
    browser: WebDriver,
) -> None:
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review()
def test_guest_can_go_to_login_page_from_product_page(
    browser: WebDriver, link: str
) -> None:
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review()
def test_guest_cant_see_product_in_basket_opened_from_product_page(
    browser: WebDriver, base_link: str
) -> None:
    browser.delete_all_cookies()

    page = BasketPage(browser, base_link)
    page.jump_to_busket()
    page.no_goods(*BasePageLocators.PROCEED_TO_CHECKOUT)
    page.basket_is_empty(*BasePageLocators.BUSKET_IS_EMPTY)


@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(
    browser: WebDriver, link: str
) -> None:
    page = ProductPage(browser, link)
    page.negative_add_to_busket()


def test_guest_cant_see_success_message(browser: WebDriver, link: str) -> None:
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(
    browser: WebDriver, link: str
) -> None:
    page = ProductPage(browser, link)
    page.click_busket()
    page.success_message_is_disappeared()
