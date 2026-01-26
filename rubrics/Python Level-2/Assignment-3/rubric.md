# Grading Rubric: Assignment-3 (Python Level-2)

## Goal
The student must demonstrate the ability to manipulate lists (indexing), use `for` loops with `break` statements, and implement `while` loops for counter-based and reverse-iteration tasks.

## Requirements
The submission MUST include the following:

1. **List Indexing**:
   - Create a list with at least 5 snacks.
   - Print ONLY the 3rd item (index `2`).

2. **For Loop with Break**:
   - Iterate through the list of snacks.
   - Print the first three snacks.
   - Use the `break` keyword to stop the loop after the 3rd snack.

3. **While Loop (Counter)**:
   - Print a name 10 times.
   - Include a serial number starting from 1 (e.g., "1. Name").
   - Correct incrementing logic (`i += 1`).

4. **While Loop (Reverse/Decrement)**:
   - Print even numbers from 20 down to 2.
   - Correct starting point (`20`), ending point (`2`), and decrementing logic (`num -= 2`).

## Scoring (Total: 10 Points)
- **Functionality (4 pts)**:
  - 1 pt: List indexing is correct (index 2 for the 3rd item).
  - 1 pt: `for` loop correctly prints 3 items and uses `break`.
  - 1 pt: `while` loop correctly prints name 10 times with serial numbers.
  - 1 pt: `while` loop correctly iterates backwards from 20 to 2 by evens.
- **Requirement Adherence (3 pts)**:
  - 1 pt: Used a `for` loop as requested for the snacks.
  - 1 pt: Used a `while` loop as requested for the name and numbers.
  - 1 pt: Logical structure is sound (no infinite loops).
- **Correct Output Format (2 pts)**:
  - 1 pt: Name serial numbers are formatted correctly (1, 2, 3...).
  - 1 pt: Even numbers are strictly 20, 18, ..., 2.
- **Readability & Style (1 pt)**:
  - 1 pt: Clear variable names (e.g., `snacks`, `counter`, `num`).

**Standard Deductions:**
- -3 points for Syntax Errors (Code does not run).
- -2 points if a `for` loop was used where a `while` loop was requested (or vice-versa).
- -1 point if the 3rd snack was accessed using index `3` instead of index `2`.

## Grading Thresholds
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance (RAG CHEAT SHEET)

1. **Off-by-one indexing**
   - *Error*: `print(snacks[3])` to get the third snack.
   - *Feedback*: "Remember that Python lists start at index 0. So the 1st item is `[0]`, the 2nd is `[1]`, and the 3rd is `[2]`."

2. **Infinite While Loops**
   - *Error*: Forgetting `i += 1` or `num -= 2`, causing the loop to run forever.
   - *Feedback*: "Your `while` loop is missing an update to the variable, which causes an infinite loop. Make sure to increment or decrement your counter inside the loop!"

3. **Incorrect Range for Even Numbers**
   - *Error*: Starting at 2 and going to 20, or stopping at 0 instead of 2.
   - *Feedback*: "The assignment specifically asked to print from 20 down to 2. Check your loop condition and starting value."

4. **Missing the 'break' keyword**
   - *Error*: Printing all snacks or using a slice `snacks[:3]` without a `break`.
   - *Feedback*: "The instructions asked to use a `for` loop and then `break` out of it. Even if the output looks correct, using `break` is a key part of this exercise."
