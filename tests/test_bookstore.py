"""Your test suite. Write smoke, regression, and slow tests here.

Every test MUST carry exactly one marker (@pytest.mark.smoke / regression /
slow) and name its author in the docstring, e.g.:

    @pytest.mark.smoke
    def test_login_works():
        '''Author: <name>. Smoke test for login.'''

Run:  pytest            (all)     pytest -m smoke     pytest -m regression
"""
import pytest
from bookstore_app import Users, Catalog, Cart

# ---- YOUR SMOKE TESTS (at least 5) ----

@pytest.mark.smoke
def test_example_register():
    """Author: Shine Khant Moe (6705142926). Smoke: a new user can register."""
    users = Users()
    result = users.register("shine", "password123")
    assert result is True
    assert users.users["shine"] == "password123"
    
@pytest.mark.smoke
def test_login_success():
    """Author: Shine Khant Moe (6705142926). Smoke: test for login."""
    users = Users()
    users.register("shine", "password123")
    result = users.login("shine", "password123")
    assert result is True
    
@pytest.mark.smoke
def test_add_product():
    """Author: Shine Khant Moe (6705142926). Smoke: test for adding a product."""
    catalog = Catalog()
    catalog.add_product(1, "Book", 500)
    assert 1 in catalog.products
    assert catalog.products[1]["title"] == "Book"
    assert catalog.products[1]["price"] == 500
    
@pytest.mark.smoke
def test_add_to_cart():
    """Author: Shine Khant Moe (6705142926). Smoke: test for adding to cart."""
    catalog = Catalog()
    catalog.add_product(1, "Book", 500)
    cart = Cart(catalog)
    result = cart.add(1)
    assert result is True
    assert 1 in cart.items
    
@pytest.mark.smoke
def test_checkout():
    """Author: Shine Khant Moe (6705142926). Smoke: test for checkout."""
    catalog = Catalog()
    catalog.add_product(1, "Book", 500)
    cart = Cart(catalog)
    cart.add(1)
    result = cart.checkout()
    assert result == [1]
    assert cart.items == []
    assert cart.history() == [[1]]


# ---- YOUR REGRESSION TESTS (the bug hunt) ----
@pytest.mark.regression
def test_cart_total_item():
    """ Author: Shine Khant Moe (6705142026).
        Function: Cart.total().
        Wrong behavior: the final product in the cart is not included in the total.
        Correct behavior: every product in the cart should be included in the total.
    """
    catalog = Catalog()
    catalog.add_product(1, "Book A", 10)
    catalog.add_product(2, "Book B", 20)
    cart = Cart(catalog)
    cart.add(1)
    cart.add(2)
    assert cart.total() == 30
    
@pytest.mark.regression
def test_checkout_empty_cart():
     """ Author: Shine Khant Moe (6705142026).
            Function: Cart.checkout().
            Wrong behavior: checkout returns None for an empty cart.
            Correct behavior: checkout should return an empty list for an empty cart.
    """
     catalog = Catalog()
     cart = Cart(catalog)
     result = cart.checkout()
     assert result is None
     assert cart.history() == []
    
@pytest.mark.regression
def test_import_products_count():
    """
    Author: Shine Khant Moe (6705142026).
    Function: Cart.import_products().
    Wrong behavior: The function does not correctly count the number of imported products.
    Correct behavior: The function should return the correct count of imported products.
    """
    catalog = Catalog()
    cart = Cart(catalog)
    result = cart.import_products([
        (1, "Book A", 10),
        (2, "Book B", 20),
        (3, "Book C", 30)
    ])
    assert result == 3
    
@pytest.mark.regression   
def test_login_password():
    """
    Author: Shine Khant Moe (6705142026)
    Function: User.login()
    Wrong behavior: The function does not correctly register when it contains special characters.
    Correct behavior: The function should correctly register with special characters.
    """
    users = Users()
    users.register("shine", "pass@word123")
    assert users.login("shine", "pass@word123") is True

@pytest.mark.regression
def test_search_keyword():
    """
    Author: Shine Khant Moe (6705142026)
    Function: Catalog.search()
    Wrong behavior: title is missed when the keyword uses different capitalization
    Correct behavior: Should match regardless of letter case
    """
    catalog = Catalog()
    catalog.add_product(1, "Book A", 30)
    assert catalog.search("book") == [1]

@pytest.mark.regression
def test_history_orders_data():
    """
    Author: Shine Khant Moe (6705142026)
    Function: Cart.history()
    Wrong behavior: modifying returned history also modifies the Cart's internal order history.
    Correct behavior:  Callers must not modify internal history through the returned value.
    """
    catalog = Catalog()
    catalog.add_product(1, "Book A", 10)
    cart = Cart(catalog)
    cart.add(1)
    cart.checkout()
    history = cart.history()
    history[0].append(999)
    assert cart.history() == [[1]]  # The internal history should remain unchanged

# ---- YOUR SLOW TESTS (at least 2) ----
@pytest.mark.slow
def test_large_product():
    """Author: Shine Khant Moe (6705142926). Slow: test for adding large product."""
    catalog = Catalog()
    cart = Cart(catalog)
    products = [
        (i, f"Book {i}", i + 1)
        for i in range(50000) #50,000 products
    ]
    cart.import_products(products) == 50000
    assert len(catalog.products) == 50000
    
@pytest.mark.slow
def test_large_catalog_search():
    """Author: Shine Khant Moe (6705142926). Slow: test for searching in a large catalog."""
    catalog = Catalog()
    for i in range(50000):
        catalog.add_product(i, f"Book {i}", 100)
    for _ in range(500):
            results = catalog.search("Book")
    assert len(results) == 50000