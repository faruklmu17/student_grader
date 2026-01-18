# Grading Rubric: Assignment-8 (Nested Functions and Type Conversion)

## Goal
The student must demonstrate an advanced understanding of how Python functions can be nested (used inside one another) and how different data types behave when converted.

## Requirements
The submission MUST explain the output of the following 8 expressions:
1.  `str(2.0)`: Converts float to string.
2.  `type(float("2"))`: Converts set string to float, then identifies it as `<class 'float'>`.
3.  `int(2.5)`: Shows truncation (rounding down) of a float to an integer.
4.  `input("...")`: Explains that it prints the user's input back.
5.  `type(round(2.34, 1))`: Identifying that a rounded decimal is still a `<class 'float'>`.
6.  `type(input("..."))`: Crucial realization that `input()` ALWAYS returns a `<class 'str'>`.
7.  `len(str(234.0))`: Length of string "234.0" (which is 5).
8.  `int(input("..."))`: Explanation of converting user input to an integer.

## Scoring (Total: 10 Points)
- **Expression Analysis (8 pts)**: 1 point for each correctly explained expression output.
- **Conceptual Depth (2 pts)**: Clear explanation of *why* the output is what it is (e.g., explaining that input returns strings).

**Deductions:**
- -1 for each incorrect explanation.
- -2 if the student thinks `type(input())` is a number because they typed a number into the prompt.
- -3 if code crashes due to syntax errors.

## Grading Criteria
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance
1. **The input() type trap**
   - *Error*: `print(type(input("Age: ")))` outputs `<class 'int'>`.
   - *Feedback*: "Careful! Even if you type a number into a prompt, Python's `input()` function ALWAYS returns a `str` (String). You have to use `int()` or `float()` to change it."

2. **Length of Decimals**
   - *Error*: `len(str(234.0))` is 3.
   - *Feedback*: "When you convert `234.0` to a string, it includes the decimal point and the zero. Count them all: '2', '3', '4', '.', '0' – that's 5 characters!"

3. **Int Truncation**
   - *Error*: `int(2.5)` is 3.
   - *Feedback*: "The `int()` function doesn't round to the nearest number; it simply chops off (truncates) everything after the decimal point."
