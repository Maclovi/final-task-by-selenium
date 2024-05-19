from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located as is_visible,
)
from selenium.webdriver.support.ui import WebDriverWait as Wait


def test_guest_can_go_to_login_page(browser: WebDriver) -> None:
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
