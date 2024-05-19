import typing

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver


class BaseProto(typing.Protocol):
    def open(self) -> None: ...

    def is_element_present(self, how: str, what: str) -> bool: ...


class BasePage:
    def __init__(self, browser: WebDriver, url: str, timeout: int = 10) -> None:
        self.browser = browser
        self.url = url
        browser.implicitly_wait(timeout)

    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, how: str, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
