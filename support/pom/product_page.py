from playwright.sync_api import Page, expect


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("/en-gb/catalogue/the-hitchhikers-guide-to-the-galaxy_4/")

    def expect_empty_basket(self):
        self.page.get_by_role("button", name=" Basket").click()
        expect(self.page.get_by_text("Your basket is empty")).to_be_visible()

    def add_to_basket(self):
        self.page.get_by_role("button", name="Add to basket").click()

    def expect_basket_count(self, count: int):
        expect(
            self.page.get_by_role("button", name=f" Basket ({count})")
        ).to_be_visible()

    def expect_message(self, message: str):
        expect(self.page.get_by_text(message)).to_be_visible()
