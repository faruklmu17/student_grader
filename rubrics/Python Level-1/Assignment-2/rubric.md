# Grading Rubric: Assignment-2 (Syntax, Datatypes, and Debugging)

## Goal
The student must demonstrate understanding of syntax, string concatenation vs. addition, basic data types (string vs. integer), and the concept of debugging/errors.

## Requirements
The submission MUST include the following answered correctly:

1. **Syntax Definition**: Explain what syntax is in Python.
2. **Concatenation**: Explain what it is and show an example using the `+` operator with two strings.
3. **Implicit Conversion Restrictions**: Explain why you cannot use `+` between a string and a number (integer/float) and provide an example that would fail.
4. **Data Types**: Explain the difference between `a = 3` (Integer) and `b = "3"` (String).
5. **Debugging Concepts**: Define 'Bug', 'Debugging', and list common error messages (e.g., SyntaxError, NameError, TypeError).
6. **Error Specifics**: Explain specifically what causes a `SyntaxError` and a `NameError`.
7. **The Fix-it Challenge**: Correct the provided line of code using only commas and/or plus signs to produce: `I am learning Python 3, and working on assignment #2 .`

## Scoring (Total: 10 Points)
- **Definitions (4 pts)**: Correct explanations for syntax, concatenation, bugs/debugging, and specific errors (Syntax/Name).
- **Concatenation & Type Knowledge (3 pts)**: Correct example of concatenation and correct explanation of why mixing types with `+` fails.
- **The Fix-it Challenge (2 pts)**: The problematic print statement is fixed using commas to allow mixing types.
- **Code Quality & Comments (1 pt)**: Code runs without errors and follows variable naming best practices.

**Deductions:**
- -1 for each missing definition.
- -2 if concatenation example uses a string and a number with `+` (which crashes).
- -3 if code contains syntax errors (other than the one they were asked to fix).

## Grading Criteria
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance
1. **Mixing types with `+`**
   - *Error*: Student tries `"Age: " + 25`.
   - *Feedback*: "In Python, the `+` sign can only concatenate strings to strings or add numbers to numbers. To print both together, use a comma: `print("Age:", 25)`."

2. **Quotes around Numbers**
   - *Error*: Student thinks `a = 3` and `b = "3"` are the same.
   - *Feedback*: "Quotes turn everything inside them into text (a String). Without quotes, Python treats 3 as a number (an Integer) that can be used for math."

3. **NameError Confusion**
   - *Error*: Student thinks NameError is a typo in a string.
   - *Feedback*: "A `NameError` happens when you try to use a variable or function name that hasn't been defined yet (e.g., printing `x` before saying `x = 5`)."
