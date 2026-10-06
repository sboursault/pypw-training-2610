from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def expect_logged_user(self, email: str):
        expect(self.page.get_by_role("button", name=email)).to_be_visible()

    def expect_heading_visible(self):
        expect(self.page.get_by_role("heading", name="All products")).to_be_visible()

    def expect_message(self, message: str):
        expect(self.page.get_by_text(message)).to_be_visible()
