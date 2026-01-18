# Grading Rubric: Assignment-4 (Comparison Operators and Conditionals)

## Goal
The student must demonstrate understanding of comparison operators (`==`, `>`, `<`), the difference between assignment and equality, and the use of `if-elif` statements.

## Requirements
The submission MUST include the following:

1. **Comparison Operators**:
   - List and demonstrate 3 comparison operators (e.g., `==`, `>`, `<`).
   
2. **Conceptual Questions**:
   - **String Comparison**: Correctly identify that `"Hello" == "hello"` is `False` (case sensitivity).
   - **Int vs Float Comparison**: Correctly identify that `5 == 5.0` is `True`.
   - **Boolean Output**: Identify that Python returns `True` or `False` when comparing values.
   - **= vs ==**: Explain that `=` is for assigning values and `==` is for checking equality.

3. **Conditional Logic (Doritos & Lays Task)**:
   - Create variables `doritos` and `lays` with initial values `3.10` and `3.20`.
   - Implement an `if` condition for `doritos < lays`.
   - Reassign `doritos` to `3.50` and implement an `elif` for `doritos > lays`.
   - Reassign `doritos` to `3.20` and implement an `elif` for `doritos == lays`.
   - Print the specific messages requested for each case.

## Scoring (Total: 10 Points)
- **Comparison Knowledge (3 pts)**: Correct examples of operators and correct answers to the string/number comparison questions.
- **Theory (2 pts)**: Clear explanation of '=' vs '==' and identification of True/False choices.
- **Conditional Logic (3 pts)**: Correct use of `if` and `elif` with proper syntax (indentation, colons).
- **Variable Management (2 pts)**: Correct variable names, correct reassignment (not creating new variables), and correct printed messages.

**Deductions:**
- -1 for each incorrect conceptual answer.
- -2 for mixing up `=` and `==` in conditions.
- -3 if code crashes due to indentation or syntax errors.

## Grading Criteria
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance
1. **Case Sensitivity**
   - *Error*: Thinking `"Hello" == "hello"` is True.
   - *Feedback*: "Python is case-sensitive! A capital 'H' and a lowercase 'h' are different characters to the computer."

2. **Assignment vs Equality**
   - *Error*: Using `if x = 5:` instead of `if x == 5:`.
   - *Feedback*: "Remember: `=` puts a value in a variable, but `==` asks the computer if two values are the same. In an `if` statement, you almost always want `==`."

3. **Indentation Errors**
   - *Error*: Not indenting the code under the `if` or `elif`.
   - *Feedback*: "In Python, the code that belongs inside an `if` block must be indented (pushed to the right using the Tab key or 4 spaces)."
