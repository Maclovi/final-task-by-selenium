from .base_page import BasePage
from .locators import ProductLocators


class ProductPage(BasePage):
    def add_to_busket(self, quiz: bool = False) -> None:
        self.open()
        product_name = self.get_product_name()
        self.click_busket()
        if quiz:
            self.solve_quiz_and_get_code()
        self.check_success(product_name)

    def negative_add_to_busket(self) -> None:
        self.open()
        self.click_busket()
        self.should_not_be_success_message()

    def get_product_name(self) -> str:
        return self.browser.find_element(*ProductLocators.PRODUCT_NAME).text

    def click_busket(self) -> None:
        self.browser.find_element(*ProductLocators.BUSKET).click()

    def check_success(self, product_name: str) -> None:
        msg = self.browser.find_element(*ProductLocators.CHECK_ADDED).text
        assert msg == product_name, "product not added"

    def should_not_be_success_message(self) -> None:
        assert self.is_not_element_present(
            *ProductLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def success_message_is_disappeared(self) -> None:
        assert self.is_disappeared(
            *ProductLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"
