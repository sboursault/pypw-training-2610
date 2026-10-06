from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("/accounts/login/")

    def submit(self, email: str, password: str):
        self.page.get_by_role("textbox", name="Email address *").fill(email)
        self.page.get_by_role("textbox", name="Password *").fill(password)
        self.page.get_by_role("button", name="Log In").click()
