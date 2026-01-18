# Grading Rubric: Assignment-10 (Built-in Functions Review)

## Goal
The student must demonstrate an understanding of what built-in functions are and how to correctly use the most common ones learned so far in Python Level-1.

## Requirements
The submission MUST include:
1.  **Definition**: A correct explanation of what a "built-in function" is.
2.  **Code Examples**: Working code examples for each of the following 9 functions:
    - `print()`
    - `input()`
    - `int()`
    - `str()`
    - `float()`
    - `type()`
    - `len()`
    - `list()`
    - `round()`

## Scoring (Total: 10 Points)
- **Definition (1 pt)**: Correct explanation provided.
- **Function Examples (9 pts)**: 1 point for each working, correct example of the listed functions.

**Deductions:**
- -1 for each missing or broken function example.
- -2 if the student confuses functions (e.g., using `round()` but explaining it as `int()`).
- -3 if the code contains major syntax errors that prevent it from running.

## Grading Criteria
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance
1. **Empty Parentheses**
   - *Error*: `print` instead of `print()`.
   - *Feedback*: "Remember that to *call* or use a function, you must include parentheses `()` at the end, even if you don't put anything inside them (like `print()`)."

2. **Casting vs. Type Checking**
   - *Error*: Using `type()` when they meant `int()`.
   - *Feedback*: "`type()` tells you what something IS. `int()` or `str()` CHANGES something into that type. Make sure you use the right tool for the job!"

3. **input() without a prompt**
   - *Observation*: `name = input()`.
   - *Feedback*: "User experience matters! It's always better to include a prompt message inside your input function like `input('Enter name: ')` so the user knows what to do."
