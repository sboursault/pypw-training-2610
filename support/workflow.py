from playwright.sync_api import APIRequestContext, Page, Playwright, expect

from support.pom.home_page import HomePage
from support.pom.login_page import LoginPage


class Workflow:
    def __init__(self, login_page: LoginPage, home_page: HomePage, page: Page):
        self.login_page = login_page
        self.home_page = home_page
        self.page = page

    def login(self, username: str, password: str):
        self.page.request.post(
            "/api/login/",
            data={"username": username, "password": password},
            fail_on_status_code=True,
        )
