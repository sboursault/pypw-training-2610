from playwright.sync_api import Page, expect

from support.pom.product_page import ProductPage


def test_add_to_basket_from_product_page(product_page: ProductPage):
    product_page.goto()
    product_page.expect_empty_basket()
    product_page.add_to_basket()
    product_page.expect_basket_count(1)
    product_page.expect_message(
        "The Hitchhiker's Guide to the Galaxy has been added to your basket."
    )
