import os
import json
import requests
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
CREDENTIALS_FILE = "credentials.json"
PRESENTATION_ID = "1ewwLhNpLgE0vVCXVQ_XYKP687DVd7bk_ehOpfAx_8k8"
COURSE_LEVEL = "Python Level-1"

# AI Config (Same as grader.py)
AI_PROVIDER = os.getenv("AI_PROVIDER", "ollama")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3:latest")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


def get_slides_content(presentation_id):
    """Fetches all text content from the presentation."""
    scopes = ["https://www.googleapis.com/auth/presentations.readonly"]
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scopes)
    service = build("slides", "v1", credentials=creds)

    presentation = service.presentations().get(presentationId=presentation_id).execute()
    slides = presentation.get("slides", [])

    assignments = []
    for i, slide in enumerate(slides):
        title = ""
        body_text = []
        notes = ""
        
        # Look for Title and Body elements on the slide
        for element in slide.get("pageElements", []):
            if "shape" in element:
                shape = element["shape"]
                text_content = ""
                if "text" in shape:
                    for text_run in shape["text"].get("textElements", []):
                        if "textRun" in text_run:
                            text_content += text_run["textRun"]["content"]
                
                if "placeholder" in shape and shape["placeholder"].get("type") in ["TITLE", "CENTERED_TITLE"]:
                    title = text_content.strip()
                else:
                    body_text.append(text_content.strip())

        # Extract Speaker Notes
        notes_page = slide.get("slideProperties", {}).get("notesPage", {})
        for element in notes_page.get("pageElements", []):
            if "shape" in element:
                shape = element["shape"]
                if "text" in shape:
                    for text_run in shape["text"].get("textElements", []):
                        if "textRun" in text_run:
                            notes += text_run["textRun"]["content"]

        # Logic: Only process if "Assignment" is in the TITLE specifically
        if "assignment" in title.lower():
            assignments.append({
                "index": i + 1,
                "title": title,
                "content": "\n".join(body_text).strip(),
                "notes": notes.strip()
            })
    
    return assignments

def generate_rubric_and_solution(title, assignment_text, notes):
    """Uses AI to generate rubric.md and solution.py contents."""
    prompt = f"""
Given the following assignment instructions from a slide, generate a detailed grading rubric and a reference Python solution.

TITLE: {title}
INSTRUCTIONS:
{assignment_text}

SPEAKER NOTES (May contain source code or extra context):
{notes}

OUTPUT FORMAT:
Please output the rubric and the solution using these specific delimiters. 

===RUBRIC_START===
(Markdown content here)
===RUBRIC_END===

===SOLUTION_START===
(Python code here)
===SOLUTION_END===

CRITICAL: 
- For the Solution, ensure you provide the final FIXED version of any code mentioned in the notes.
- For the Rubric, list the specific bugs that need to be fixed (found in the notes/instructions).
"""
    # Use call_ai but expect raw text back
    # We need to modify call_ai or just use a simpler version here
    response = call_ai_raw(AI_PROVIDER, prompt)
    
    rubric = ""
    solution = ""
    
    import re
    r_match = re.search(r"===RUBRIC_START===(.*?)===RUBRIC_END===", response, re.DOTALL)
    s_match = re.search(r"===SOLUTION_START===(.*?)===SOLUTION_END===", response, re.DOTALL)
    
    if r_match: rubric = r_match.group(1).strip()
    if s_match: solution = s_match.group(1).strip()
    
    return {
        "rubric_md": rubric,
        "solution_py": solution
    }

def call_ai_raw(provider: str, prompt: str) -> str:
    """Makes a request to the AI and returns the raw text."""
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
                {"role": "system", "content": "You are a coding teacher creating curriculum."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.1 
        }
    else:
        url = OLLAMA_URL
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    if provider == "groq":
        return data["choices"][0]["message"]["content"]
    else:
        return data["response"]

def main():
    print(f"Syncing assignments from Slides: {PRESENTATION_ID}...")
    assignments = get_slides_content(PRESENTATION_ID)
    
    if not assignments:
        print("No assignments found in the slides.")
        return

    for assign in assignments:
        print(f"Checking slide {assign['index']} (Title: '{assign['title']}')...")
        
        # Try to find if this assignment already exists
        # We look for "Assignment X" in the TITLE first
        import re
        # Regex to handle "Assignment 1", "Assignment-1", "Assignment #1", "Assignment-#1"
        assign_num_pattern = r"assignment[- #]*(\d+)"
        match = re.search(assign_num_pattern, assign["title"], re.IGNORECASE)
        if not match:
            # Fallback to body content if title doesn't have the number but has the word
            match = re.search(assign_num_pattern, assign["content"], re.IGNORECASE)

        if match:
            assign_num = match.group(1).lstrip('0') # Normal 1, 2, 3...
            assign_folder = f"Assignment-{assign_num}"
        else:
            # If "Assignment" is in title but no number, skip or name by index
            print(f"  -> Skipping slide {assign['index']} because no assignment number was found.")
            continue

        target_dir = os.path.join("rubrics", COURSE_LEVEL, assign_folder)
        
        if os.path.exists(target_dir):
            print(f"  -> {assign_folder} already exists, skipping.")
            continue

        print(f"  -> Generating content for {assign_folder}...")
        result = generate_rubric_and_solution(assign["title"], assign["content"], assign["notes"])
        
        os.makedirs(target_dir, exist_ok=True)
        
        with open(os.path.join(target_dir, "rubric.md"), "w") as f:
            f.write(result["rubric_md"])
            
        with open(os.path.join(target_dir, "solution.py"), "w") as f:
            f.write(result["solution_py"])
            
        print(f"  -> Successfully created {assign_folder}")

if __name__ == "__main__":
    main()
