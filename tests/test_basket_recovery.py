from playwright.sync_api import Page, expect

from support.pom.home_page import HomePage
from support.pom.login_page import LoginPage
from support.pom.product_page import ProductPage


def test_basket_recovery(
    login_page: LoginPage, home_page: HomePage, product_page: ProductPage, page: Page
):

    # - je me connecte
    login_page.goto()
    login_page.submit("tom@test.test", "tom@test.test")
    home_page.expect_logged_user("tom@test.test")

    # - j'ajoute un produit au panier
    product_page.goto()
    product_page.add_to_basket()

    # - je me déconnecte
    page.goto("/accounts/logout/")

    #   -> le panier est vide
    product_page.goto()
    product_page.expect_empty_basket()

    # - je me reconnecte
    login_page.goto()
    login_page.submit("tom@test.test", "tom@test.test")
    home_page.expect_logged_user("tom@test.test")

    #   -> le panier contient 1 produit
    product_page.goto()
    product_page.expect_basket_count(1)
