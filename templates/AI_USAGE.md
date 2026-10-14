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
- Which failure mode was most common in the supplied set?
- Why is a test that passes against buggy code more dangerous than one that crashes?
- What will you check in future before trusting a generated test?
