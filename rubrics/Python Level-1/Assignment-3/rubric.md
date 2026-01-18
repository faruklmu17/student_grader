# Grading Rubric: Assignment-3 (Operators, Data Types, and Functions)

## Goal
The student must demonstrate knowledge of basic arithmetic operators, built-in functions, data types, and how to inspect them.

## Requirements
The submission MUST include the following:

1. **Arithmetic Operators**:
   - List the four basic arithmetic operators (`+`, `-`, `*`, `/`).
   - Create two numeric variables.
   - Print the results of applying all four operators to those variables.

2. **Functions (in comments)**:
   - List three functions learned (e.g., `print()`, `type()`, `int()`, `float()`, `str()`).

3. **Data Types (in comments)**:
   - List three basic data types (e.g., `int`, `float`, `str`).

4. **Type Checking**:
   - Explain or show how to check a variable's type using the `type()` function (e.g., `print(type(a))`).

5. **Fill in the Gaps**:
   - Correctly identify:
     - Whole number -> `int` (Integer)
     - Decimal number -> `float`
     - Text -> `str` (String)

## Scoring (Total: 10 Points)
- **Understanding (3 pts)**: Correclty identified the four operators and three data types.
- **Code Execution (3 pts)**: Four arithmetic operations are performed and printed correctly.
- **Function Knowledge (2 pts)**: Correct listing of three functions and type-checking method.
- **Gap Completion (2 pts)**: Correctly filled in 'int', 'float', and 'str'.

**Deductions:**
- -1 for each incorrect operator/data type listed.
- -2 if the `type()` function explanation is missing or incorrect.
- -3 if code crashes due to syntax errors.

## Grading Criteria
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance
1. **Division Result Type**
   - *Observation*: Student might be surprised that `10 / 2` results in `5.0` (a float).
   - *Feedback*: "Notice that division in Python always results in a `float` (decimal), even if the numbers divide evenly!"

2. **Type Checking syntax**
   - *Error*: `type = a` or `check(a)`.
   - *Feedback*: "To check a type, we use the built-in function `type(variable_name)`. You usually want to wrap it in a print: `print(type(a))`."

3. **Misspelling Data Types**
   - *Error*: 'integar', 'string', 'flot'.
   - *Feedback*: "Python uses specific short names for data types: `int`, `float`, and `str`. Make sure to use these exact terms!"
