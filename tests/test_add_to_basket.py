from playwright.sync_api import Page, expect


def test_add_to_basket_from_product_page(page: Page):
    page.goto("/en-gb/catalogue/the-hitchhikers-guide-to-the-galaxy_4/")

    page.get_by_role("button", name=" Basket").click()
    expect(page.get_by_text("Your basket is empty")).to_be_visible()

    page.get_by_role("button", name="Add to basket").click()

    expect(page.get_by_role("button", name=" Basket (1)")).to_be_visible()
    expect(
        page.get_by_text(
            "The Hitchhiker's Guide to the Galaxy has been added to your basket."
        )
    ).to_be_visible()
