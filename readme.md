# Student Auto-Grading System (Cloud AI Edition)

An automated grading system that connects **Google Forms** to **Cloud AI (Groq/Ollama)** to provide instant, personalized feedback to students.

## 🚀 How it Works
1. **Submit**: Students submit their code via a Google Form.
2. **Detection**: A GitHub Action wakes up every 30 minutes to check for new entries in your Google Sheet.
3. **AI Grading**: The system uses **Llama 3.3 (via Groq)** to compare the student's code against your provided **Rubrics** and **Reference Solutions**.
4. **Record Keeping**: 
   - Updates the main response sheet with status/grade/feedback.
   - Automatically appends a record to the student's **Private Master Gradebook**.
5. **Feedback**: Sends a professional HTML email directly to the student with their grade and next steps.

---

## 🛠 Setup Instructions

### 1. Google Sheets Configuration
Ensure your "Form Responses 1" tab has these exact headers:
- `Timestamp`, `Course Name`, `Student Name`, `Student Email`, `Assignment Number`, `Paste Your Code Here`, `Grade`, `Feedback`, `Status`, `Gradebook Link`

### 2. Local Setup
1. **Clone the repo** and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. **Environment**: Create a `.env` file from your credentials:
   ```env
   EMAIL_SENDER=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password
   AI_PROVIDER=groq
   GROQ_API_KEY=your_key_here
   ```

### 3. Rubric & Solution Setup
For each assignment, create a folder structure:
`rubrics/COURSE_NAME/ASSIGNMENT_NAME/`
- `rubric.md`: Guidelines for the AI.
- `solution.py`: The reference code for comparison.

---

## 🤖 GitHub Automation (24/7 Grading)
To enable automatic grading every 30 minutes, add these **Repository Secrets** in your GitHub Settings:

1. `GOOGLE_CREDENTIALS_JSON`: Entire content of your `credentials.json`.
2. `GROQ_API_KEY`: Your Groq API key.
3. `EMAIL_SENDER`: Your recruitment/teacher email.
4. `EMAIL_PASSWORD`: Your 16-character Gmail App Password.

---

## 📊 AI Limits (Free Tier)
Using **Llama 3.3 70B** on Groq:
- **Daily Limit**: ~12,000 tokens (approx. 15-20 submissions per day).
- **RPM**: 30 requests per minute.
*Note: If you have a larger class, you can switch the `GROQ_MODEL` to `llama-3.1-8b-instant` in `grader.py` to get 100k+ tokens/day.*

---

## 📁 Key Files
- `grader.py`: Core logic (now supports high-performance Batch Updates).
- `.github/workflows/grader.yml`: The automation heartbeat.
- `email_template.html`: Customizable feedback email design.
- `rubrics/`: Your knowledge base for the AI.
