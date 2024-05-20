import logging
from collections.abc import Generator
from typing import cast

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="class")
def browser(browser_spare: WebDriver) -> Generator[WebDriver, None, None]:
    yield browser_spare
    browser_spare.delete_all_cookies()


@pytest.fixture(scope="session")
def browser_spare(driver: WebDriver) -> Generator[WebDriver, None, None]:
    logging.info("start browser for test..\n")

    yield driver

    logging.info("\nquit browser..")
    driver.quit()


@pytest.fixture(scope="session")
def driver(language: str) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": language}
    )
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope="session")
def language(request: pytest.FixtureRequest) -> str:
    opt = request.config.getoption("--language")
    return cast(str, opt)


@pytest.fixture(scope="session")
def link() -> str:
    return "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.fixture(scope="session")
def base_link() -> str:
    return "https://selenium1py.pythonanywhere.com/en-gb/"


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Select the language you want to test",
    )
