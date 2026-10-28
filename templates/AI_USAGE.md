# AI_USAGE.md -- Declaration and audit

Group: <Zero One>   Members: <Shine Khant Moe (6705142026)>
                             <Alex (6705142001)>

## D3.1 Declaration (required)
| AI tool | How we used it |
| | |
| ChatGPT | Used to explain the assignment, Where do i put the codes, Suggestion for how do the assignment and code, and All generated code was reviewed, modified, and validated manually before use.  |

## D3.2 Audit of the supplied ai_review/ test set (graded core)
Run EACH test in ai_review/ against the shipped app and record real evidence.

| Test | What it claims to catch | Does it actually? | Evidence (command + real output) | Verdict |
|---|---|---|---|---|
| test_cart_total_sums_items | Checks whether all cart items are included in the total. | YES | Shipped: FAILED ai_review/test_ai_generated.py::test_cart_total_sums_items - assert 10 == 30 / Fixed: same command → PASSED | genuine |
| test_login_rejects_wrong_password | Checks whether the login process correctly rejects incorrect passwords. | NO | Shipped: ...::test_login_rejects_wrong_password -v → PASSED Fixed: same command → PASSED | passes anyway |
| test_search_finds_exact_title | Checks whether the search functionality finds books with an exact title match. | NO | Shipped: ...::test_search_finds_exact_title -v → PASSED Fixed: same command → PASSED | passes anyway |
| test_import_returns_count | Checks whether bulk import returns the correct number of imported products. | YES | Shipped: FAILED ai_review/test_ai_generated.py::test_import_returns_count - AssertionError: assert 3 == 2 / Fixed: same command → PASSED | genuine |
| test_register_duplicate_returns_false | Checks whether duplicate usernames are rejected. | NO | Shipped: ...::test_register_duplicate_returns_false -v → PASSED Fixed: same command → PASSED | passes anyway |
| test_checkout_empty_returns_none | Checks whether empty checkout returns None. | YES | Shipped: FAILED ai_review/test_ai_generated.py::test_checkout_empty_returns_none - assert [] is None Fixed: same command → PASSED | genuine|
| test_add_to_cart_returns_true_for_known_product | Checks whether an existing product can be added to the cart. | NO | Shipped: ...::test_add_to_cart_returns_true_for_known_product -v → PASSED Fixed: same command → PASSED | passes anyway |
| test_search_is_limited_to_ten_results | Checks whether the search functionality is limited to ten results. | NO | Shipped: FAILED ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results - AssertionError: assert 20 <= 10 Fixed: same command → FAILED | invented bug |

## D3.3 Verdict (a few short paragraphs)
My bug hunt identified six defects across the bookstore application. The supplied AI-generated test set caught three of them. The first was the Cart.total() bug, where the final item in the cart was excluded from the total. The supplied test test_cart_total_sums_items failed on the shipped code and passed after I corrected the calculation, so it was a genuine detection.
The supplied test set also correctly detected the Cart.import_products() bug. My regression test showed that importing three products returned a count of four because the function returned count + 1. The supplied test test_import_returns_count failed on the shipped version and passed after I changed the function to return the correct count. The empty-cart checkout defect was also caught by test_checkout_empty_returns_none. The shipped implementation returned an empty list instead of None, while the test passed after I added the empty-cart check.
However, the supplied AI tests did not detect the special-character password problem in Users.login(). The supplied test only checked an ordinary incorrect password, so it passed even though the special-character defect remained. My own regression test used a registered password containing @, which exposed the problem.
The AI-generated set also failed to detect the case-sensitivity problem in Catalog.search(). Its search test used exactly matching capitalization, whereas my test searched for book after storing Book A, which exposed the defect. Finally, none of the supplied tests checked the Cart.history() problem where modifying returned history can also modify the cart's internal state. Overall, the supplied AI-generated tests genuinely detected three of the six defects I found: the cart-total bug, the bulk-import count bug, and the empty-cart checkout bug. They did not detect the special-character login bug, the case-sensitive catalog search bug, or the mutable order-history bug. Sharpen the final takeaway: a test can seem relevant while still missing the specific input or edge case that reveals the real defect.
