# Grading Rubric: Assignment-11 (While Loops)

## Goal
The student must demonstrate mastery of the `while` loop, including initialization, condition checking, and incrementing/decrementing a counter variable to control the loop.

## Requirements
The submission MUST perform the following 6 tasks using `while` loops:
1.  **Numbers 1-10**: Print 1, 2, 3... up to 10.
2.  **Name Repeat**: Print a name 10 times, each with a serial number (e.g., "1. John").
3.  **Countdown 10-1**: Print numbers in descending order from 10 down to 1.
4.  **Even Numbers 1-20**: Print 2, 4, 6... up to 20.
5.  **Odd Countdown 19-1**: Print 19, 17, 15... down to 1.
6.  **Multiples of 10**: Print 10, 20, 30... up to 100.

## Scoring (Total: 10 Points)
- **Loop Structure (4 pts)**: Correct use of `while <condition>:`, initialization, and counter updates across all tasks.
- **Task Accuracy (6 pts)**: 1 point for each correctly implemented loop task.

**Deductions:**
- -1 for each task that results in an infinite loop (forgetting to update the counter).
- -2 if the student uses `for` loops instead of `while` loops as uniquely requested.
- -3 if code contains syntax errors or crashes.

## Grading Criteria
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance
1. **The Infinite Loop**
   - *Error*: Forgetting `i += 1`.
   - *Feedback*: "Oh no! Your code is running forever. Make sure to increase (or decrease) your counter variable inside the loop so that the condition eventually becomes False."

2. **Wait, that's a For Loop**
   - *Error*: Using `for i in range(...)`.
   - *Feedback*: "While `for` loops are great, this assignment specifically asks for `while` loops to practice manual counter management."

3. **Serial Number Alignment**
   - *Error*: Serial numbers starting at 0 or missing.
   - *Feedback*: "When printing a serial numbered list, humans usually like to start at 1! Make sure your printing logic matches what the user expects to see."
