# REPORT.md

Group: <Zero one>   Members: <Shine Khant Moe (6705142026)>
                             <Alex (6705142001)>

## Part A -- Smoke testing involves running a small number of quick tests to make sure the application's most crucial functions work. 
It is generally done after a new build, deployment, or code changes to catch major problems before more thorough testing. For this bookstore, one smoke test might be to register a new user and then check that the account is stored successfully. 
Another smoke test could be to add a product to the cart and then proceed to checkout with a non-empty cart to verify that the basic purchasing process works correctly. 
Regression testing confirms that a defect that was previously identified and fixed has not reappeared after software modifications. To run a regression test, you must first reproduce the original problem before the fix is applied, then confirm the test passes after the problem is resolved. For this bookstore, one regression test could check that the cart total includes all products and does not omit the last item. 
Another regression test could be used to ensure that checking out an empty cart results in None instead of producing an empty order. 
Slow testing involves testing how the application behaves when subjected to heavier workloads by using a large quantity of data, performing repeated operations, or involving costly processing. 
Because these tests take longer than smoke tests, they are better suited to be scheduled or run at night rather than after every small change. For this bookstore, one slow test could be to bulk-import 50,000 products into the catalog. Another slow test could be to repeatedly search a catalog containing thousands of books to make sure the application still gives correct results when processing large amounts of data.

## Part B -- 1. Smoke and Slow
             This is a regression test because it specifically checks a defect that was previously discovered and fixed.
             2. Regression
             This test specifically checks a defect that was previously found and fixed. If the shipping-cost bug appears again after another code change, the regression test should fail.
             3. Slow
             The processing of ten years' worth of order information involves a huge quantity of data and would require a great deal of processing time, so it is more appropriate for a scheduled slow-test suite than for the quick tests carried out after each commit.
             4. Smoke
             If the payment page doesn't load, there is little reason to continue with more detailed testing until you fix the basic issue.
             5. Regression
             This test checks that a previously reported defect does not recur. It recreates the condition that caused the problem and verifies the corrected behavior is maintained.
             6. Slow
             This test is designed to utilize a very large catalog in order to evaluate system behavior under substantial data volume. Preparing and processing one million titles significantly increases the duration compared to a standard smoke test.

## Part F -- Team reflection
1. Running only regression tests before every commit is inefficient because they focus on previously discovered bugs and grow as the project expands.
2. Smoke tests usually run first because they are fast and check the application's core functionality.
3. If you never run slow tests, problems that appear only with large data or repeated operations may go undiscovered; an application may work correctly with a small dataset but fail, become unreliable, or perform badly with realistic workloads
4. Yes. A test can have characteristics of more than one category; for example, a test checking a previously fixed bug while processing 100,000 orders could be both a regression test and a slow test.
5. When the bug finder and bug fixer are different people, the bug report must be clear, specific, and reproducible. It should describe the affected function, the exact steps or input used, the actual result, the expected result, and any useful evidence, such as pytest output, so the developer can understand and reproduce the problem without relying on the tester's memory. It also makes it easier to confirm that the fix solves the original defect.
