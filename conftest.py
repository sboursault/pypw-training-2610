import os

import pytest
from playwright.sync_api import APIRequestContext, Page, Playwright, expect

from support.pom.home_page import HomePage
from support.pom.login_page import LoginPage
from support.pom.product_page import ProductPage
from support.workflow import Workflow

# Playwrigth settings and base fixtures


@pytest.fixture(scope="session")
def base_url():
    """
    Override the --base-url option: base url comes from the env file
    """
    return os.environ["BASE_URL"]


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict):
    """
    Override browser locale
    """
    return {**browser_context_args, "locale": "en-GB"}


@pytest.fixture
def page(page: Page):
    """
    Override default timeout for navigation, actions and verifications
    """
    page.set_default_navigation_timeout(10_000)
    page.set_default_timeout(5_000)
    expect.set_options(timeout=5_000)
    return page


@pytest.fixture
def api_request(playwright: Playwright, base_url: str):
    """
    Define the api_request fixture:
    an isolated APIRequestContext instance to make http request
    """
    ctx = playwright.request.new_context(base_url=base_url)
    yield ctx
    ctx.dispose()


# Api fixtures

# Workflow fixtures


@pytest.fixture
def workflow(login_page: LoginPage, home_page: HomePage):
    return Workflow(login_page, home_page)


# Page object fixtures


@pytest.fixture
def product_page(page: Page):
    return ProductPage(page)


@pytest.fixture
def home_page(page: Page):
    return HomePage(page)


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)
