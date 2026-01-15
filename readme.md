# Student Auto-Grading System (Google Form → Google Sheet → Local LLaMA Grader)

This project automates your grading workflow:

1. Students submit code through **one Google Form**
2. Responses land in **one Google Sheet**
3. A **local Python script** detects new submissions (`Status = not graded`)
4. The script uses your **local LLaMA** (example: Ollama) to generate:
   - **Grade**
   - **Feedback**
   - **Status** (`graded` or `need resubmit`)
5. You review and manually send feedback to students (optional)

---

## ✅ What You Already Have (Google Side)

Your Google Sheet columns (headers) should look like this (exactly):

- Timestamp
- Course Name
- Student Name
- Student Email
- Assignment Number
- Paste Your Code Here
- Grade
- Feedback
- Status

Your Status dropdown values are:

- `not graded`
- `graded`
- `need resubmit`

> **Important:** Keep these values lowercase and consistent. The automation matches these strings exactly.

---

## 1) Create Local Project Folder

Create a folder on your computer (VS Code recommended):

```bash
mkdir student-grader
cd student-grader
