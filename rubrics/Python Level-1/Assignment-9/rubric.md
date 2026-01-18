# Grading Rubric: Assignment-9 (Lists and Indexing)

## Goal
The student must demonstrate an understanding of Python lists, including how to create them, access items via index numbers, use built-in functions like `len()`, and handle indexing errors.

## Requirements
The submission MUST address the following 7 tasks:
1.  **List Definition**: Explain what a list is (a collection of items in a specific order) and how to display its contents.
2.  **Indexing Importance**: Explain why index numbers are important (used for accessing/modifying specific items) and that they start at 0.
3.  **Snacks List**: Create a list of 5 snacks and print the **third** one (which is index 2).
4.  **Decimal List & len()**: Create a list of 6 decimal numbers (floats) and print the count of items using `len()`.
5.  **Last Item & type()**: Print the last decimal from the list and use `type()` to confirm it is a float.
6.  **String to List**: Demonstrate converting a string into a list of characters using `list()`.
7.  **IndexError Analysis**: Explain what an `IndexError` is and when it happens (trying to access an index that doesn't exist).

## Scoring (Total: 10 Points)
- **Conceptual Knowledge (3 pts)**: Clear explanations for lists, indexes, and IndexErrors.
- **List Operations (4 pts)**: Correct creation of lists and use of `len()`, `type()`, and `list()` functions.
- **Indexing Precision (3 pts)**: Correctly targeting the 3rd item (index 2) and the last item.

**Deductions:**
- -1 for each missing or incorrect explanation.
- -2 if the student attempts to access the 3rd item using index 3 instead of 2.
- -3 if code crashes due to any syntax or actual IndexErrors.

## Grading Criteria
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance
1. **The "Off-by-One" Index Error**
   - *Error*: Using index 3 to get the 3rd item.
   - *Feedback*: "Remember, Python starts counting at 0! Index 0 is the 1st item, index 1 is the 2nd, and index 2 is the 3rd."

2. **Negative Indexing**
   - *Observation*: Student uses index -1 to get the last item.
   - *Feedback*: "Great use of negative indexing! `[-1]` is a very professional way to always grab the last item in a list."

3. **String to List Conversion**
   - *Observation*: Student expects `list("Hello")` to be `["Hello"]`.
   - *Feedback*: "The `list()` function breaks a string down into its individual characters: `['H', 'e', 'l', 'l', 'o']`."
