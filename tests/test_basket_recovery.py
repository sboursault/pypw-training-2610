from base64 import b64encode

from playwright.sync_api import APIRequestContext, Page, expect

from support.pom.product_page import ProductPage
from support.workflow import Workflow


def test_basket_recovery(
    workflow: Workflow,
    product_page: ProductPage,
    page: Page,
    api_request: APIRequestContext,
):
    login = "tom@test.test"
    password = "tom@test.test"
    auth = b64encode(f"{login}:{password}".encode()).decode("ascii")
    api_request.delete("/api/basket/", headers={"Authorization": f"Basic {auth}"})

    # - je me connecte
    workflow.login("tom@test.test", "tom@test.test")

    # - j'ajoute un produit au panier
    product_page.goto()
    product_page.add_to_basket()

    # - je me déconnecte
    page.goto("/accounts/logout/")

    #   -> le panier est vide
    product_page.goto()
    product_page.expect_empty_basket()

    # - je me reconnecte
    workflow.login("tom@test.test", "tom@test.test")

    #   -> le panier contient 1 produit
    product_page.goto()
    product_page.expect_basket_count(1)
