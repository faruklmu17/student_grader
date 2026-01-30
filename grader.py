import requests
import gspread
import json
from google.oauth2.service_account import Credentials
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ---------- CONFIG YOU MUST EDIT ----------
SHEET_NAME = "Student Grading"      # your spreadsheet name
TAB_NAME = "Form Responses 1"         # your sheet tab name (bottom left)
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3:latest")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")

# AI Provider Config
AI_PROVIDER = os.getenv("AI_PROVIDER", "ollama") # "ollama" or "groq"
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

CREDENTIALS_FILE = "credentials.json"
COL_COURSE = "Course Name"
COL_ASSIGNMENT = "Assignment Number"
COL_CODE = "Paste Your Code Here"
COL_GRADE = "Grade"
COL_FEEDBACK = "Feedback"
COL_STATUS = "Status"
COL_EMAIL = "Student Email"
COL_NAME = "Student Name"
COL_GRADEBOOK_LINK = "Gradebook Link"

# Master Gradebook Config
MASTER_GRADEBOOK_NAME = "Master Student Gradebook"
MASTER_GRADEBOOK_ID = os.getenv("MASTER_GRADEBOOK_ID")

# Email Config
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("EMAIL_SENDER")
SENDER_PASSWORD = os.getenv("EMAIL_PASSWORD")
TEST_RECIPIENT = "farukqmul@gmail.com"  # Set to None to send to actual students
DASHBOARD_URL = os.getenv("DASHBOARD_URL", "dashboard.html") # e.g. "https://yourdomain.com/dashboard.html"
# -----------------------------------------

STATUS_NEW = "Not Graded"
STATUS_GRADED = "Graded"
STATUS_RESUBMIT = "Need Resubmit"

def call_ai(provider: str, prompt: str) -> dict:
    """Makes a request to the specified AI provider and returns the parsed JSON content."""
    payload = {}
    url = ""
    headers = {}

    if provider == "groq":
        url = GROQ_URL
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": GROQ_MODEL,
            "messages": [
                {"role": "system", "content": "You are a coding teacher grading student work. You must always output responses in valid JSON format."},
                {"role": "user", "content": prompt}
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0.1 
        }
    else:
        # Default to Ollama
        url = OLLAMA_URL
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "format": "json" 
        }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    if provider == "groq":
        content_str = data["choices"][0]["message"]["content"]
        return json.loads(content_str)
    else:
        return json.loads(data["response"])

def ask_llama(course: str, assignment: str, code: str) -> tuple[str, str, str]:
    """
    Returns (grade, feedback, new_status).
    Tries primary AI_PROVIDER, falls back to Ollama if Groq fails.
    """
    # --- RAG: REtrIEVAL ---
    base_rubric_path = os.path.join("rubrics", "general_rubric.md")
    rubric_content = "Use general Python best practices."
    
    if os.path.exists(base_rubric_path):
        with open(base_rubric_path, "r") as f:
            rubric_content = f.read()

    solution_content = "No reference solution provided."
    safe_course = course.strip().replace("/", "_")
    safe_assign = assignment.strip().replace("/", "_")
    
    base_path = os.path.join("rubrics", safe_course, safe_assign)
    rubric_path = os.path.join(base_path, "rubric.md")
    solution_path = os.path.join(base_path, "solution.py")

    if os.path.exists(rubric_path):
        with open(rubric_path, "r") as f:
            rubric_content = f.read()
            
    if os.path.exists(solution_path):
        with open(solution_path, "r") as f:
            solution_content = f.read()

    # --- PROMPT AUGMENTATION ---
    prompt = f"""
You are a coding teacher grading student work.

CONTEXT:
Course: {course}
Assignment: {assignment}

REFERENCE SOLUTION:
```python
{solution_content}
```

GRADING RUBRIC:
{rubric_content}

STUDENT SUBMISSION:
```python
{code}
```

INSTRUCTIONS:
Compare the Student Submission against the Reference Solution and Rubric.
1. Check for **FACTUAL ERRORS** in comments/strings (e.g. definitions, operators, rules).
2. Check for **CODE ERRORS** (syntax, missing requirements).
3. If the code runs but the *explanations* are wrong (like saying = is ==), that is a RESUBMIT.

IMPORTANT:
- If you mark something as wrong, you MUST reference the specific line or quote the student's text.
- Be careful: Do not claim a definition is missing if it is present. Look closely at all print statements.

Please provide:
1. A Score out of 10 (based on the rubric).
2. A short Grade (Pass if score >= 5, otherwise Resubmit).
3. A feedback message. **If score < 10, specifically quote the mistake.**
4. The recommended status update ({STATUS_GRADED} or {STATUS_RESUBMIT}).

Output format (strict JSON):
{{
  "score": 0,
  "grade": "Pass/Pass/Resubmit",
  "feedback": "...",
  "status": "{STATUS_GRADED} or {STATUS_RESUBMIT}"
}}
"""
    
    content = None
    applied_provider = AI_PROVIDER

    # Try Primary Provider
    try:
        content = call_ai(AI_PROVIDER, prompt)
    except Exception as e:
        print(f"  -> Primary AI Provider ({AI_PROVIDER}) failed: {e}")
        
        # Fallback Logic: If Groq fails, try Ollama
        if AI_PROVIDER == "groq":
            print("  -> Attempting fallback to Ollama...")
            try:
                content = call_ai("ollama", prompt)
                applied_provider = "ollama (fallback)"
            except Exception as e2:
                print(f"  -> Fallback to Ollama also failed: {e2}")
                return "Error", f"AI generation failed: {str(e)}", STATUS_NEW
        else:
            return "Error", f"AI generation failed: {str(e)}", STATUS_NEW

    if not content:
        return "Error", "AI returned no content.", STATUS_NEW

    # Process results
    score = content.get("score", 0)
    if score >= 5:
        grade_text = "Pass"
        status = STATUS_GRADED
    else:
        grade_text = "Resubmit"
        status = STATUS_RESUBMIT

    final_grade = f"{grade_text} ({score}/10)"
    feedback = content.get("feedback", "No feedback")
    
    # Optional: tag feedback with provider if fallback happened
    if "fallback" in applied_provider:
        feedback += f"\n\n(Generated via local backup model)"

    return final_grade, feedback, status


def get_or_create_master_gradebook(client):
    """Finds or creates the one Master spreadsheet for all student tabs."""
    if MASTER_GRADEBOOK_ID:
        try:
            return client.open_by_key(MASTER_GRADEBOOK_ID)
        except Exception as e:
            print(f"  -> Error opening Master Gradebook by ID: {e}")

    try:
        return client.open(MASTER_GRADEBOOK_NAME)
    except gspread.SpreadsheetNotFound:
        print(f"  -> Creating Master Gradebook: {MASTER_GRADEBOOK_NAME}...")
        try:
            return client.create(MASTER_GRADEBOOK_NAME)
        except Exception as e:
            if "403" in str(e):
                print(f"  -> CRITICAL: Cannot create sheet (Drive quota exceeded).")
                print(f"     Please create a sheet manually, share it with the service account,")
                print(f"     and add MASTER_GRADEBOOK_ID to your .env file.")
            raise e

def get_or_create_student_tab(spreadsheet, student_name):
    """Finds or creates a specific tab (worksheet) for a student inside the master."""
    # Tab name: Use "FirstLast" (max 31 chars for Sheets tabs)
    tab_name = student_name[:30].strip()
    
    try:
        return spreadsheet.worksheet(tab_name)
    except gspread.WorksheetNotFound:
        print(f"  -> Creating new tab for {student_name}...")
        worksheet = spreadsheet.add_worksheet(title=tab_name, rows=100, cols=7)
        
        # Setup professional headers
        worksheet.update('A1:B1', [['STUDENT GRADEBOOK:', student_name]])
        worksheet.format('A1', {'textFormat': {'bold': True, 'fontSize': 12}})
        
        headers = [['Date', 'Student Name', 'Course', 'Assignment', 'Grade', 'Feedback', 'Submitted Code']]
        worksheet.update('A3:G3', headers)
        worksheet.format('A3:G3', {'textFormat': {'bold': True}, 'backgroundColor': {'red': 0.9, 'green': 0.9, 'blue': 0.9}})
        return worksheet

def append_to_student_tab(worksheet, student_name, course, assignment, grade, feedback, code):
    """Appends results to the specific student worksheet."""
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        worksheet.append_row([now, student_name, course, assignment, grade, feedback, code])
    except Exception as e:
        print(f"  -> Failed to update student tab for {student_name}: {e}")

def send_email(to_email, student_name, course, assignment, grade, feedback, gradebook_url=""):
    """Sends an email with the grade and feedback using an HTML template."""
    if not SENDER_EMAIL or "your_email" in SENDER_EMAIL:
        print("Skipping email: SENDER_EMAIL not configured.")
        return

    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = f"Feedback: {course} - {assignment}"

        # Determine next step based on grade
        next_step = "Great job! You can move on to the next assignment."
        if "Fail" in grade or "Resubmit" in grade:
             next_step = "Please review the feedback, fix your code, and resubmit using the same form."

        # Load and fill template
        try:
            with open("email_template.html", "r", encoding="utf-8") as f:
                html_content = f.read()
            
            # Replace placeholders
            html_content = html_content.replace("{{StudentName}}", student_name if student_name else "Student")
            html_content = html_content.replace("{{Course}}", course)
            html_content = html_content.replace("{{Assignment}}", assignment)
            html_content = html_content.replace("{{Grade}}", grade)
            html_content = html_content.replace("{{Feedback}}", feedback)
            html_content = html_content.replace("{{NextStep}}", next_step)
            
            # If link is missing, remove the entire button section
            if not gradebook_url or gradebook_url == "#":
                import re
                # This regex removes everything between the placeholders
                html_content = re.sub(r"<!-- GradebookSection -->.*?<!-- /GradebookSection -->", "", html_content, flags=re.DOTALL)
                print(f"  -> Info: Gradebook link missing for {student_name}, hiding button in email.")
            else:
                html_content = html_content.replace("{{GradebookLink}}", gradebook_url)
            
            msg.attach(MIMEText(html_content, 'html'))
        except FileNotFoundError:
            print("  -> Warning: email_template.html not found, sending plain text fallback.")
            body = f"""
Hello {student_name},

Here is the feedback for your submission:

Course: {course}
Assignment: {assignment}

Grade: {grade}
Feedback: {feedback}

Best regards,
Your Coding Teacher
"""
            msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT) # type: ignore
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, to_email, text)
        server.quit()
        print(f"  -> Email sent to {to_email}")
    except Exception as e:
        print(f"  -> Failed to send email: {e}")

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
    col_email = get_column_index(headers, [COL_EMAIL])
    col_name = get_column_index(headers, [COL_NAME, "Name", "Student"])
    col_gradebook = get_column_index(headers, [COL_GRADEBOOK_LINK])

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
    cell_updates = []

    # Pre-open master gradebook to save resources
    master_gradebook = None
    try:
        master_gradebook = get_or_create_master_gradebook(client)
    except Exception as m_err:
        print(f"  -> Warning: Master Gradebook offline: {m_err}")

    # Iterate rows (skipping header)
    for i, row in enumerate(rows[1:], start=2):
        # Safety for short rows
        current_status = row[col_status - 1] if (col_status - 1) < len(row) else ""
        
        # Check if we should grade this
        s = current_status.strip()
        if s == STATUS_NEW or s == "":
            course = row[col_course - 1] if (col_course - 1) < len(row) else "Unknown Course"
            assignment = row[col_assignment - 1] if (col_assignment - 1) < len(row) else "Unknown Assignment"
            code = row[col_code - 1] if (col_code - 1) < len(row) else ""

            if not code.strip():
                print(f"Row {i}: Empty code, skipping.")
                continue

            print(f"Grading Row {i} (Course: {course}, Assignment: {assignment})...")
            
            grade, feedback, new_status = ask_llama(course, assignment, code)
            
            # Prepare updates for main sheet
            if col_grade:
                cell_updates.append(gspread.Cell(i, col_grade, grade))
            if col_feedback:
                cell_updates.append(gspread.Cell(i, col_feedback, feedback))
            
            cell_updates.append(gspread.Cell(i, col_status, new_status))
            
            print(f"  -> Result: {grade} | Status: {new_status}")
            updates_made += 1

            # Send Email Data Prep
            student_email = row[col_email - 1] if col_email and (col_email - 1) < len(row) else ""
            student_name = row[col_name - 1] if col_name and (col_name - 1) < len(row) else "Student"
            gradebook_url = row[col_gradebook - 1] if col_gradebook and (col_gradebook - 1) < len(row) else ""

            # Personal Gradebook Logic (Tabs Mode)
            try:
                if master_gradebook and student_name:
                    student_tab = get_or_create_student_tab(master_gradebook, student_name)
                    append_to_student_tab(student_tab, student_name, course, assignment, grade, feedback, code)

                    tab_link = f"{master_gradebook.url}#gid={student_tab.id}"

                    # Dashboard Link (Enhanced View)
                    # We prioritize the absolute DASHBOARD_URL from env/secrets
                    if DASHBOARD_URL and DASHBOARD_URL.startswith("http"):
                        # Extract spreadsheet ID from the master gradebook URL
                        # URL format: https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit
                        spreadsheet_id = master_gradebook.id
                        student_name_encoded = student_name.replace(' ', '%20')
                        dashboard_link = f"{DASHBOARD_URL}?student={student_name_encoded}&sheet={spreadsheet_id}"
                    else:
                        # If no absolute URL is set, we fallback to the raw Google Sheet tab
                        dashboard_link = tab_link
                        print(f"  -> Warning: DASHBOARD_URL not set to a full URL (starting with http). Falling back to Google Sheet link.")

                    # ALWAYS update the tracking variable with the best available link
                    gradebook_url = dashboard_link

                    if col_gradebook:
                        cell_updates.append(gspread.Cell(i, col_gradebook, gradebook_url))
            except Exception as gradebook_err:
                print(f"  -> Gradebook Sync Error: {gradebook_err}")

            # Send Email immediately (don't batch email sending)
            target_email = TEST_RECIPIENT if TEST_RECIPIENT else student_email
            if target_email:
                send_email(target_email, student_name, course, assignment, grade, feedback, gradebook_url)

    # 🚀 APPLY BATCH UPDATES AT THE END
    if cell_updates:
        print(f"Finalizing updates to Google Sheet...")
        try:
            sheet.update_cells(cell_updates)
        except Exception as e:
            print(f"CRITICAL ERROR: Failed to update Google Sheet: {e}")

    if updates_made == 0:
        print("No new submissions to grade.")
    else:
        print(f"Done. Graded {updates_made} submissions.")

if __name__ == "__main__":
    main()
