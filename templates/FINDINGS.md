# FINDINGS.md -- Bug-hunt log

One entry per bug, five maximum, ~150 words each. Copy the block per bug.
Marks are for the Observed/Expected pair being specific and checkable.

Group: <Zero One>   Members: <Shine Khant Moe (6705142026)>
                             <Alex (6705142001)>

---

## Bug 1
- **Suspected:** <cart.py -> Cart.total(), I identified this function as a potential issue because the loop terminated prior to processing the final item in the cart.>
- **Tried:** <I added two products priced at 10 and 20 to the cart and ran a regression test, expecting `cart.total()` to return 30.>
- **Observed:** <FAILED tests/test_bookstore.py::test_cart_total_item - assert 10 == 30>
- **Expected:** <The result should be 30 because both products are in the cart and their prices included in the total.>
- **Fixed:** <Changed total() so it iterates through every product ID in self.items instead of stopping before the final item.>
- **Author:** <Shine Khant Moe (6705142026)>
    
---

## Bug 2
- **Suspected:** <`cart.py -> Cart.checkout()`. The docstring states that an empty cart should return None, but the function did not check for an empty cart.>
- **Tried:** I created a new empty cart and called `checkout()`.
- **Observed:** `FAILED tests/test_bookstore.py::test_checkout_empty_cart - assert [] is None
- **Expected:** `checkout()` should return [] if no order should be recorded when the cart is empty.
- **Fixed:** Added a check at the beginning of `checkout()` that returns `None` when `self.items` is empty.
- **Author:** Shine Khant Moe (6705142026)

---

## Bug 3
- **Suspected:** <cart.py -> import_products(), The function increased `count` once for every imported product but returned `count + 1`, making the result one too high.>
- **Tried:** < I imported 3 products and checked the value returned by `import_products()`>
- **Observed:** <FAILED tests/test_bookstore.py::test_import_products_count - assert 4 == 3>
- **Expected:** <The function should return 3 because exactly three products were imported.>
- **Fixed:** <Changed 'count + 1' to 'count'.>
- **Author:** Shine Khant Moe (6705142026)

## Bug 4
- **Suspected:** <users.py -> login(), Registration stores the password exactly as entered. However, `login()` removes non-alphanumeric characters from the password before comparing it with the stored one.>
- **Tried:** <I registered the user `shine` with the password `pass@word123` and then tried to log in with it.>
- **Observed:** <FAILED tests/test_bookstore.py::test_login_password - AssertionError: assert False is True>
- **Expected:** <Login should return `True` because the username exists and the entered password matches the registered one.>
- **Fixed:** <Removed the password cleaning logic from the `login()` method to match the registration behavior.>
- **Author:** Shine Khant Moe (6705142026)

## Bug 5
- **Suspected:** <catalog.py -> search(), The search function compared the keyword directly with the product title, so different capitalization could prevent finding a matching title.>
- **Tried:** <I added a product titled `Book A` and searched with the keyword `book`.>
- **Observed:** <FAILED tests/test_bookstore.py::test_search_keyword - assert [] == [1]>
- **Expected:** <The search should return `[1]` because the title contains the same word with only a capitalization difference.>
- **Fixed:** <Modified the `search()` method to convert both the keyword and the product title to lowercase before comparing them.>
- **Author:** Shine Khant Moe (6705142026)

## Bug 6
- **Suspected:** <cart.py -> Cart.history(), The function returns a reference to the internal order history list, allowing external modification of the cart's state.>
- **Tried:** <I added a product to the cart, called `history()`, and modified the returned list.>
- **Observed:** <FAILED tests/test_bookstore.py::test_history_orders_data - AssertionError: assert [[1, 999]] == [[1]]>
- **Expected:** <Changing a returned history value should not affect the cart's internally stored order history.>
- **Fixed:** <I changed `history()` to return copies of the stored orders instead of the internal `self.orders` list directly.>
- **Author:** Shine Khant Moe (6705142026)
