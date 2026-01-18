The grading rubric for this assignment is as follows:
* **Correct Product Dispensing** (20 points): Ensure the vending machine dispenses the correct product based on the product code entered by the user.
* **Product Code Recognition** (15 points): Ensure the vending machine recognizes the product code entered by the user and matches it with the correct product.
* **Infinite Loop Prevention** (10 points): Prevent the vending machine from entering an infinite loop when an invalid product code is entered.
* **Amount Prompting** (15 points): Prompt the user to enter the correct amount if the entered amount is less than the product price.
* **Change Calculation** (20 points): Correctly calculate the change if more money is inserted than the product price.
* **Change/Required Money Calculation** (10 points): Ensure the vending machine calculates the change or required money for each product correctly.
* **F-String Usage** (10 points): Use F-strings to ensure clean formatting of the output.
* **Code Quality and Readability** (10 points): Ensure the code is well-organized, readable, and follows best practices.
* **Bug Fixing** (30 points): Fix the following bugs:
  + The `user_code` is read as a string but compared with integers.
  + The `break` statement is missing in some `if` conditions.
  + The `elif` condition for Pepsi is incorrect.
  + The `if` condition for Mars is repeated.
  + The calculation of `change_amount` and `required_amount` is incorrect in some cases.
  + The `inserted_money` is read as an integer but should be read as a float.
  + The `required_amount` calculation is incorrect when the user inserts less money than the product price.
  + The `change_amount` calculation is incorrect when the user inserts more money than the product price.