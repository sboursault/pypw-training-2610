from playwright.sync_api import Page, expect

from support.pom.home_page import HomePage
from support.pom.login_page import LoginPage


def test_login_ok(login_page: LoginPage, home_page: HomePage):
    login_page.goto()
    login_page.submit("tom@test.test", "tom@test.test")
    home_page.expect_logged_user("tom@test.test")
    home_page.expect_heading_visible()
    home_page.expect_message("Welcome back")
