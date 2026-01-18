# Grading Rubric: Assignment-12 (Vending Machine Debugging)

## Goal
The student must fix the "defective" version of the Vending Machine project provided in the speaker notes. The focus is on identifying logical errors, type conversion errors, and syntax bugs while maintaining the original code structure.

## Requirements
The student MUST fix the following bugs in the provided script:
1. **Type Conversion (Input)**: `user_code` must be converted to `int()` (it's currently a string being compared to integers).
2. **Type Conversion (Money)**: `inserted_money` must be `float()` to handle $2.50 etc. (currently `int()`).
3. **Loop Control**: Added missing `break` statements after successful product selection for Coke and Pepsi.
4. **Logical Check (Pepsi)**: Fixed the error where Pepsi was checking for the Coke product code (`product_codes[1]` instead of `[2]`).
5. **Arithmetic Errors**:
   - Fixed `change_amount = inserted_money + kitkat_price` (should be minus).
   - Fixed `required_amount = inserted_money - kitkat_price` (should be price - money).
   - Fixed `required_amount = coke_price -+ inserted_money`.
   - Fixed `required_amount = pepsi_price * inserted_money` (multiplication bug).
   - Fixed `change_amount = inserted_money / mars_price` (division bug).
6. **Mars Logic**: Corrected the final `if` condition which was incorrectly checking `user_code == product_codes[2]` (Pepsi) twice.
7. **Syntax Errors**: Fixed the missing colon and indentation for the final Mars "less than" check.

## Scoring (Total: 10 Points)
- **Bug Discovery (5 pts)**: Identifying and fixing the core arithmetic and type conversion bugs.
- **Loop & Logic (3 pts)**: Correcting the `break` statements and the variable index choices (0-3).
- **Clean Output (2 pts)**: Using F-strings or proper concatenation to show prices ($2.50).

**Deductions:**
- -1 for each remaining arithmetic error.
- -2 if the vending machine still has infinite loops.
- -3 if the code remains unrunnable due to basic syntax errors.

## Grading Criteria
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance
1. **Type Errors**
   - *Error*: `if user_code == 1001` always failing.
   - *Feedback*: "Remember that `input()` always returns a string. You must convert it to an integer using `int()` before comparing it with the numbers in your list."

2. **The Minus-Plus Confusion**
   - *Error*: `coke_price -+ inserted_money`.
   - *Feedback*: "Python gets confused with multiple operators like `-+`. Just use a single `-` for subtraction."

3. **Wrong Math for Change**
   - *Error*: Using `+`, `/`, or `*` instead of `-` for calculating change and required money.
   - *Feedback*: "Think about the logic: Change is always `Money Inserted - Price`. Required money is always `Price - Money Inserted`."