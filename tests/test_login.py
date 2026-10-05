from playwright.sync_api import Page, expect


def test_login_ok(page: Page):
    page.goto("/")

    page.get_by_role("link", name=" Account").click()
    expect(page.get_by_role("navigation", name="breadcrumb")).to_be_visible()
    page.get_by_role("textbox", name="Email address *").fill("tom@test.test")
    page.get_by_role("textbox", name="Password *").fill("tom@test.test")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_text("Welcome back")).to_be_visible()
    expect(page.get_by_role("button", name=" tom@test.test")).to_be_visible()
    expect(page.get_by_role("heading", name="All products")).to_be_visible()
    expect(page.locator("h1", has_text="All products")).to_be_visible()
    expect(page.locator("h1")).to_have_text("All products")
