# Grading Rubric: Assignment-2 (Python Level-2)

## Goal
The student must demonstrate an understanding of data types (`int` and `float`), logical operators (`AND` and `OR`), and nested conditional statements using a real-world shopping scenario.

## Requirements
The submission MUST include the following:

1. **Int vs Float Explanation**:
   - Clear distinction between `int` (whole numbers) and `float` (decimals) using code.
   - Use of `type()` function to check the data type.

2. **Logical Operators**:
   - Explanation of the difference between `AND` and `OR`.
   - Code examples showing how they work.

3. **Shopping Scenario (Part-1)**:
   - Three variables: `money` ($10), `mars` ($2.25), and `kitkat` ($5.50).
   - A conditional statement using `and`: `if mars < kitkat and mars < 2.50`.
   - Print "I will buy the Mars".
   - Calculate and store the `left_amount` in a variable and print it.

4. **Nested Condition (Part-2)**:
   - A nested `if` statement inside the first condition.
   - Check if `left_amount >= 5.50`.
   - Print "you can afford to buy a Kitkat too!".

## Scoring (Total: 10 Points)
- **Functionality (4 pts)**:
  - 2 pts: Code runs without errors.
  - 2 pts: Nested logic correctly determines if a Kitkat can be bought.
- **Requirement Adherence (3 pts)**:
  - 1 pt: Correct use of `type()` to check types.
  - 1 pt: Correct use of `and` operator in the Mars condition.
  - 1 pt: Correct calculation of `left_amount`.
- **Conceptual Understanding (2 pts)**:
  - 1 pt: Correct explanation of `int` vs `float`.
  - 1 pt: Correct explanation of `AND` vs `OR`.
- **Readability & Style (1 pt)**:
  - 1 pt: Variable names are clear and code is well-formatted.

**Standard Deductions:**
- -3 points for Syntax Errors (Code does not run).
- -2 points if the Kitkat condition is NOT nested inside the Mars condition.
- -1 point for missing or incorrect calculation of remaining money.

## Grading Thresholds
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance (RAG CHEAT SHEET)

1. **Incorrect Nesting**
   - *Error*: The Part-2 condition is outside the Part-1 condition.
   - *Feedback*: "The assignment asks to set the second condition *inside* the first condition. This is called nesting. Make sure your Kitkat check is indented inside the Mars `if` block."

2. **Logical Operator Confusion**
   - *Error*: Using `or` instead of `and` for the Mars check.
   - *Feedback*: "Remember that `and` requires BOTH conditions to be true. In this case, we only buy Mars if it's cheaper than Kitkat AND less than $2.50."

3. **Type Check Syntax**
   - *Error*: `if number == int:` instead of `if type(number) == int:` or `isinstance(number, int)`.
   - *Feedback*: "To check if a variable is a specific type, you should use the `type()` function, like `type(x) == int`."

4. **Variable Naming**
   - *Error*: Using generic names like `v1`, `v2`, `v3`.
   - *Feedback*: "It's best practice to use descriptive variable names like `money`, `mars_price`, and `left_amount` so your code is easier to read!"
