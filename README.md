# shopping-app

Assignment - https://github.com/neustackapp/assignment/blob/main/README.md

You are designing an ecommerce store. Clients can add items to their cart and checkout to successfully place an order. Every nth order gets a coupon code for 10% discount and can apply to their cart.

We would like you to design and implement APIs for adding items to cart and checkout functionality. The checkout API would validate if the discount code is valid before giving the discount.

Building a UI that showcases the functionality is a stretch goal. If you are primarily a backend engineer, you can also submit postman or REST client or equivalent.

The store also has two admin API's:

    Generate a discount code if the condition above is satisfied.
    Lists count of items purchased, total purchase amount, list of discount codes and total discount amount.

You can build this with a technology stack that you are comfortable with. You would push the code to your github repo and share the link once its complete. We would like to see your commits that show progression and thought process as to how you are completing the exercise.

Things that you will be evaluated on:

    Functional code
    Code quality
    UI in a framework of your choice
    Code comments, readme docs
    Unit tests

Assumptions you can make:

    The API’s don’t need a backend store. It can be an in-memory store.

FAQ:

Q: Can a discount code be used multiple times?

A: Discount code can be requested by every user, but is made available for every nth order only. The discount code can be used only once before the next one becomes available on the next nth order.

Q: Does the discount code apply to one item?

A: Discount code applies to the entire order.

All the best to me!

**************************************************************************************************************************************************************

Technology Stack and Architecture-

Framework: either Flask (for pseudo async) or FastAPI (for real async) - using flask
Storage: In-memory data structures (e.g., Python dictionaries or lists)
Testing: unittest or pytest
Testing: Run tests but add a note on how to rebuild the database.
Frontend/UI: Minimal UI using React or plain HTML/CSS if the time allows - try for plain html/css if required, for now postman requests
Tools: Postman Tool to test APIs, Pycharm for python code.


API Endpoints-

Cart Management
-Add Item to Cart (POST /cart)
-View Cart (GET /cart)

Checkout
-Checkout order (POST /checkout)
Validates (if applicable) and applies a discount code to the total.
Finalizes the order.

Admin APIs
-Generate Discount Code (POST /admin/discount)
Verifies provided nth order condition and returns new discount code.
-Order Summary (GET /admin/summary)
Returns list of purchased items, total revenue, discount codes used and total discount amount.


Design Details

Data Models
Cart: Maintains item list, quantity and per-user cart.
Orders status: Monitor completed orders and discounts.
Discounts: Makes discount codes and tracks their usage and validity


Key Functionalities
-Adding Items to Cart:
Takes user_id, item_id, quantity and price argument
We will add the item to the user cart.

-Checkout:
Calculates the total price.
Validates and applies discount codes.
It saves the order and empties the cart.

-Admin:
If nth order condition satisfied generates discount codes
Tracks orders, revenue, and discounts, and summarizes.

-Validation:
Discount codes can be used only once.
The codes apply to the value of the cart in total.

Next Steps
-Add validation for inputs and error handling.
-Write unit tests to ensure API functionality.
-Optionally, build a simple React or HTML-based UI for testing.

