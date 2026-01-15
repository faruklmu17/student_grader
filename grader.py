import requests
import gspread
import json
from google.oauth2.service_account import Credentials

# ---------- CONFIG YOU MUST EDIT ----------
SHEET_NAME = "Student Grading"      # your spreadsheet name
TAB_NAME = "Form Responses 1"         # your sheet tab name (bottom left)
OLLAMA_MODEL = "llama3:latest"
OLLAMA_URL = "http://localhost:11434/api/generate"
CREDENTIALS_FILE = "credentials.json"
COL_COURSE = "Course Name"
COL_ASSIGNMENT = "Assignment Number"
COL_CODE = "Paste Your Code Here"
COL_GRADE = "Grade"
COL_FEEDBACK = "Feedback"
COL_STATUS = "Status"
# -----------------------------------------

STATUS_NEW = "Not Graded"
STATUS_GRADED = "Graded"
STATUS_RESUBMIT = "Need Resubmit"

def ask_llama(course: str, assignment: str, code: str) -> tuple[str, str, str]:
    """
    Returns (grade, feedback, new_status).
    """
    prompt = f"""
You are a coding teacher grading student work.

Course: {course}
Assignment: {assignment}

Student code:
```text
{code}
```

Please provide:
1. A short Grade (Pass, Fail, or Resubmit).
2. A brief, helpful Feedback message for the student (max 2 sentences).
3. The recommended status update ({STATUS_GRADED} or {STATUS_RESUBMIT}).

Output format (strict JSON):
{{
  "grade": "Pass/Fail/Resubmit",
  "feedback": "...",
  "status": "{STATUS_GRADED} or {STATUS_RESUBMIT}"
}}
"""
    
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json" 
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        content = json.loads(data["response"])
        
        return content.get("grade", "Unknown"), content.get("feedback", "No feedback"), content.get("status", STATUS_GRADED)
    except Exception as e:
        print(f"Error calling Ollama: {e}")
        return "Error", f"AI generation failed: {str(e)}", STATUS_NEW

def get_column_index(headers, possible_names):
    """Helper to find column index (1-based) for a list of possible header names."""
    lower_headers = [h.lower().strip() for h in headers]
    for name in possible_names:
        if name.lower() in lower_headers:
            return lower_headers.index(name.lower()) + 1
    return None

def main():
    print(f"Connecting to Sheet: {SHEET_NAME}...")
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    try:
        creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scopes)
        client = gspread.authorize(creds)
        sheet = client.open(SHEET_NAME).worksheet(TAB_NAME)
    except Exception as e:
        print(f"Error connecting to Google Sheets: {e}")
        return

    # Get all values
    rows = sheet.get_all_values()
    if not rows:
        print("Sheet is empty!")
        return

    headers = rows[0]
    print(f"Found headers: {headers}")

    # Identify key columns based on exact names
    col_status = get_column_index(headers, [COL_STATUS])
    col_grade = get_column_index(headers, [COL_GRADE])
    col_feedback = get_column_index(headers, [COL_FEEDBACK])
    
    col_course = get_column_index(headers, [COL_COURSE])
    col_assignment = get_column_index(headers, [COL_ASSIGNMENT])
    col_code = get_column_index(headers, [COL_CODE])

    # If critical columns needed for grading shouldn't be guessed, you can hardcode indices or error out
    if not (col_course and col_assignment and col_code):
        print("Could not automatically find Case/Assignment/Code columns. Please rename headers to include 'Course', 'Assignment', and 'Code'.")
        # Fallback for simple structures if headers are missing/weird? 
        # For now, let's assume they exist or user prints headers and fixes them.
        return

    # If output columns don't exist, maybe append them? For now, assume they exist or we found them.
    # If not found, we can't write back safely without risking overwriting.
    if not col_status:
        print("Could not find 'Status' column. Please add one.")
        return

    print("Starting grading loop...")
    updates_made = 0

    # Iterate rows (skipping header)
    # Note: 'rows' is a list of lists. gspread is 1-indexed for cell updates.
    for i, row in enumerate(rows[1:], start=2):
        # Safety for short rows
        current_status = row[col_status - 1] if (col_status - 1) < len(row) else ""
        
        # Check if we should grade this
        if current_status.strip() == STATUS_NEW:
            course = row[col_course - 1] if (col_course - 1) < len(row) else "Unknown Course"
            assignment = row[col_assignment - 1] if (col_assignment - 1) < len(row) else "Unknown Assignment"
            code = row[col_code - 1] if (col_code - 1) < len(row) else ""

            if not code.strip():
                print(f"Row {i}: Empty code, skipping.")
                continue

            print(f"Grading Row {i} (Course: {course}, Assignment: {assignment})...")
            
            grade, feedback, new_status = ask_llama(course, assignment, code)
            
            # Update sheet
            # We construct a batch update or just update cells one by one for simplicity seeing usage volume
            
            if col_grade:
                sheet.update_cell(i, col_grade, grade)
            if col_feedback:
                sheet.update_cell(i, col_feedback, feedback)
            
            sheet.update_cell(i, col_status, new_status)
            print(f"  -> Result: {grade} | Status: {new_status}")
            updates_made += 1

    if updates_made == 0:
        print("No new submissions to grade.")
    else:
        print(f"Done. Graded {updates_made} submissions.")

if __name__ == "__main__":
    main()
