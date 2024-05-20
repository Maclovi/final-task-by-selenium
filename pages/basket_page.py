from .base_page import BasePage


class BasketPage(BasePage):
    def no_goods(self, how: str, what: str, timeout: int = 4) -> None:
        assert super().is_not_element_present(
            how, what, timeout
        ), "there are goods"

    def basket_is_empty(self, how: str, what: str) -> None:
        assert super().is_element_present(how, what), "there is not element"
