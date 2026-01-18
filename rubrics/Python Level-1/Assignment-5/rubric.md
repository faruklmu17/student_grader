# Grading Rubric: Assignment-5 (Inputs and Type Casting)

## Goal
The student must demonstrate proficiency in using the `input()` function, processing strings, and converting user input into numbers (Integers or Floats) using type casting.

## Requirements
The submission MUST include the following:

1. **Function Knowledge (in comments)**:
   - List functions seen/used so far (e.g., `print()`, `input()`, `type()`, `int()`, `float()`, `str()`).

2. **Basic Input & String Formatting**:
   - Ask for first name and store it in `first_name`.
   - Ask for last name and store it in `last_name`.
   - Print a welcome message: `Welcome to Python Programing, [First] [Last]!`.

3. **Conceptual - float(input())**:
   - Explain that `float(input())` converts text input directly into a decimal number.
   - Mention it's needed when dealing with prices, measurements, or weights.

4. **int(input()) vs float(input())**:
   - Explain the difference (whole numbers vs. decimals).
   - Provide an example for each.

5. **Shortcut Techniques**:
   - Demonstrate the two shortcut techniques for `input()`:
     1. Passing the prompt string directly inside `input("Your Name: ")`.
     2. Wrapping the entire `input()` in a conversion function like `int(input("Age: "))`.

## Scoring (Total: 10 Points)
- **Functions & Concepts (3 pts)**: Correct listing of functions and accurate explanations for `float(input())` vs `int(input())`.
- **String Handling (3 pts)**: Success in capturing names and formatting the "Welcome" message correctly (including the comma and space).
- **Type Casting Logic (2 pts)**: Correct code examples for numeric inputs.
- **Shortcuts (2 pts)**: Demonstration of both prompt-inside-input and direct-casting shortcuts.

**Deductions:**
- -1 if the Welcome message is missing required punctuation or spaces.
- -2 if the student uses `+` unnecessarily when commas would be safer for printing mixed types.
- -3 if code crashes during execution with a `ValueError` (e.g., trying to convert text to a number incorrectly).

## Grading Criteria
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance
1. **Case Sensitivity in Names**
   - *Observation*: Student might not capitalize names.
   - *Feedback*: "User input comes in exactly as typed. You'll learn how to force capitalization later, but for now, the names should appear just as you entered them!"

2. **Prompt inside input() shortcut**
   - *Error*: `print("Enter name"); name = input()`.
   - *Feedback*: "Don't forget the shortcut! You can put your message right inside the parentheses: `name = input("Enter name: ")`. This keeps your code cleaner."

3. **Mixing Names and Text**
   - *Error*: `print("Welcome",first_name+last_name)` (no space between names).
   - *Feedback*: "When combining a first and last name, make sure to add a space in between, like this: `first_name + " " + last_name`."
