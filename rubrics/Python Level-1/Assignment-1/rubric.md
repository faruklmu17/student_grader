# Grading Rubric: Assignment-1 (Intro to Python)

## Goal
The student must demonstrate understanding of basic printing, variables, strings, comments, and reassignment in Python.

## Requirements
The submission MUST include the following:

1. **Definitions**:
   - Print the words "Variable," "String," and "Syntax."
   - Print a definition for each of these terms.

2. **Comments**:
   - Show an example of a single-line comment (using `#`).
   - Use comments throughout the code to explain what is happening.

3. **Printing**:
   - Print the exact sentence: "I am learning Python."

4. **Variables & Reassignment**:
   - Create 4 variables: 2 Numbers (integers/floats) and 2 Strings.
   - Print all 4 variables.
   - Assign **NEW** values to those same 4 variables.
   - Print the new values.
   - Explanation (in print or comments) of what happened when values were changed.

5. **Theory (in comments)**:
   - List rules for naming variables (e.g., start with letter/underscore, no spaces).
   - Explain what the assignment operator is (`=`) and provide an example.

## Scoring (Total: 10 Points)
- **Understanding (3 pts)**: Definitions are correct.
- **Code Quality (3 pts)**: Code runs without errors, uses correct syntax.
- **Requirement Check (2 pts)**: All tasks (4 variables, reassignment, sentences) are present.
- **Comments (2 pts)**: Code is explained well with comments.

**Deductions:**
- -1 for each factual error in definitions.
- -2 for logic errors (e.g. confusing `=` and `==`).
- -3 if code crashes (SyntaxError).

## Grading Criteria
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance (RAG CHEAT SHEET)
If you see these specific errors, provide the corresponding feedback:

1. **Confusion of `=` and `==`**
   - *Error*: Student says `==` is for assignment or writes `x == 5` to set a value.
   - *Feedback*: "Remember: `=` is for assigning a value (putting something in the box). `==` is for comparing two things to see if they are equal."

2. **Variable Naming Violations**
   - *Error*: Student claims variables can start with numbers, or uses spaces in names (`my var`).
   - *Feedback*: "Variable names cannot strictly start with a number or contain spaces. Use underscores (e.g., `my_variable`) instead."

3. **Incomplete Definitions**
   - *Error*: "Variables only store numbers."
   - *Feedback*: "Variables are flexible containers! In Python, they can store numbers, text (strings), and much more."

4. **Spelling & Case Sensitivity**
   - *Error*: `Print("Hello")` (capital P) or typos in key terms like "Sytax".
   - *Feedback*: "Python is case-sensitive. `print` must be lowercase. Also, watch out for typos in your definitions."

5. **String Quotes**
   - *Error*: `text = Hello` (missing quotes).
   - *Feedback*: "Strings must always be wrapped in quotes (e.g., `'Hello'`), otherwise Python thinks you are looking for a variable named Hello."
