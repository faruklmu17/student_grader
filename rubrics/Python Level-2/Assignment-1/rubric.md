# Grading Rubric: Assignment-1 (Python Level-2)

## Goal
The student must demonstrate the ability to use a single `print()` statement for multi-line output, handle user input, and use conditional statements (`if/elif/else`) to match strings and provide output.

## Requirements
The submission MUST include the following:

1. **Multi-line Print**:
   - The word list (1-10) must be printed using **ONLY ONE** `print()` statement.
   - Using triple quotes `"""` or `\n` characters are both acceptable ways to achieve this.

2. **User Input**:
   - Prompt the user with "Type a word to see the definition- ".
   - Store the user's input in a variable.

3. **Conditional Logic**:
   - Use `if`, `elif`, and `else` (or multiple `if`s, though `if/elif` is preferred) to check the input against the list.
   - If the input matches a word from the list, the program must print its definition.

4. **Correct Definitions**:
   - The definitions provided should be accurate for the terms: Programming Language, Pseudocode, Binary Number, Syntax, Variable, Data Type, Whole Number, Integer Number, Logical operator, and Debugging.

## Scoring (Total: 10 Points)
- **Functionality (4 pts)**:
  - 2 pts: Code runs without errors.
  - 2 pts: Logic correctly matches input to definitions.
- **Requirement Adherence (3 pts)**:
  - 1 pt: Used only ONE `print()` statement for the initial list.
  - 1 pt: Used `input()` correctly.
  - 1 pt: Used conditional blocks (`if/elif`).
- **Accuracy (2 pts)**:
  - Definitions are correct and complete for at least several words.
- **Readability & Style (1 pt)**:
  - Variable names are clear and code is well-formatted.

**Standard Deductions:**
- -3 points for Syntax Errors (Code does not run).
- -2 points if multiple `print()` statements were used for the initial 1-10 list.
- -1 point for inconsistent indentation.

## Grading Thresholds
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance (RAG CHEAT SHEET)

1. **Multiple Print Statements for the List**
   - *Error*: Student uses 10 separate `print()` statements.
   - *Feedback*: "The assignment specifically asks to print the list using only one `print()` statement. You can use triple quotes `\"\"\"` to print multiple lines at once."

2. **Case Sensitivity Issues**
   - *Error*: `input()` is compared to "Syntax" but user types "syntax" and it fails.
   - *Feedback*: "Python is case-sensitive. If you type 'syntax' (lowercase) but check for 'Syntax' (capital S), it won't match. You can use `.lower()` on your variable to make it more user-friendly!"

3. **Missing `elif`**
   - *Error*: Student uses only `if` statements for every check.
   - *Feedback*: "While multiple `if` statements work, using `elif` is more efficient because Python stops checking once it finds a match."

4. **String comparison with `=` instead of `==`**
   - *Error*: `if word = "Syntax":`
   - *Feedback*: "Remember to use `==` for comparison! A single `=` is for assigning a value to a variable."
