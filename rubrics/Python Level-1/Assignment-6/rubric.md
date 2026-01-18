# Grading Rubric: Assignment-6 (Logical Operators)

## Goal
The student must demonstrate understanding of logical operators (`and`, `or`, `not`) and how to use them within conditional statements to check multiple criteria.

## Requirements
The submission MUST include the following:

1. **Logical Operators (in comments)**:
   - List the three logical operators: `and`, `or`, and `not`.

2. **Conceptual - AND vs OR**:
   - Explain that `and` requires **both** conditions to be True.
   - Explain that `or` requires **at least one** condition to be True.
   - Explain when to use `and` (restricting a range) vs `or` (allowing multiple options).

3. **Number Check Task (< 10 and < 20)**:
   - Create a variable with value `7`.
   - Use an `if` statement with the `and` operator to check if the number is `< 10` AND `< 20`.
   - Print the specific message: `You typed a number that is both less than 20 and 10!`.

4. **Grade & Validation Task**:
   - Create an `if` condition using `and` for the range `90` to `100`.
   - Print: `You got an A grade!`.
   - Create an `elif` condition using `or` to catch numbers `< 90` or `> 100`.
   - Print: `You typed an invalid number!`.

## Scoring (Total: 10 Points)
- **Logical Operators & Theory (3 pts)**: Correct listing of operators and accurate explanation of AND vs OR.
- **Double-Condition Logic (3 pts)**: Correct implementation of the `< 10 and < 20` check.
- **Range & Invalidity Logic (3 pts)**: Success in checking the 90-100 range and identifying invalid numbers using the `or` operator.
- **Code Quality (1 pt)**: Proper indentation and use of colons in `if/elif` blocks.

**Deductions:**
- -1 if the `and` operator is misused (e.g., trying to check if a single number is simultaneously 5 and 10).
- -2 if the invalidity check logic is reversed (e.g., using `and` instead of `or` for the outside-range check).
- -3 if code contains syntax errors.

## Grading Criteria
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance
1. **Inefficient AND logic**
   - *Observation*: If a number is < 10, it is automatically < 20.
   - *Feedback*: "While your code works, notice that checking `num < 10 and num < 20` is a bit redundant because anything less than 10 is always less than 20! It's good practice to think about which condition is stronger."

2. **OR for Range Overlap**
   - *Error*: `if num < 90 and num > 100` (This is impossible).
   - *Feedback*: "To catch numbers outside a range (like less than 90 OR more than 100), you must use the `or` operator. A number cannot be less than 90 and more than 100 at the same time!"

3. **Syntax - Repeating Variable Names**
   - *Error*: `if num >= 90 and <= 100`.
   - *Feedback*: "In Python, you must repeat the variable name for each comparison: `if num >= 90 and num <= 100:`."
