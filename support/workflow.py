from support.pom.home_page import HomePage
from support.pom.login_page import LoginPage


class Workflow:
    def __init__(self, login_page: LoginPage, home_page: HomePage):
        self.login_page = login_page
        self.home_page = home_page

    def login(self, username: str, password: str):
        self.login_page.goto()
        self.login_page.submit(username, password)
        self.home_page.expect_logged_user(username)
