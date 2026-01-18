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

def call_ai(provider: str, prompt: str) -> dict:
    """Makes a request to the specified AI provider (copied from grader.py)."""
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
                {"role": "system", "content": "You are a coding teacher creating curriculum. You must always output responses in valid JSON format."},
                {"role": "user", "content": prompt}
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0.1 
        }
    else:
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
        
        # Look for Title and Body elements
        for element in slide.get("pageElements", []):
            if "shape" in element:
                shape = element["shape"]
                # Extract text
                text_content = ""
                if "text" in shape:
                    for text_run in shape["text"].get("textElements", []):
                        if "textRun" in text_run:
                            text_content += text_run["textRun"]["content"]
                
                # Check if it's a title placeholder
                if "placeholder" in shape and shape["placeholder"].get("type") in ["TITLE", "CENTERED_TITLE"]:
                    title = text_content.strip()
                else:
                    body_text.append(text_content.strip())

        # Logic: Only process if "Assignment" is in the TITLE specifically
        if "assignment" in title.lower():
            assignments.append({
                "index": i + 1,
                "title": title,
                "content": "\n".join(body_text).strip()
            })
    
    return assignments

def generate_rubric_and_solution(title, assignment_text):
    """Uses AI to generate rubric.md and solution.py contents."""
    prompt = f"""
Given the following assignment instructions from a slide, generate a detailed grading rubric and a reference Python solution.

TITLE: {title}
ASSIGNMENT INSTRUCTIONS:
{assignment_text}

OUTPUT FORMAT (JSON):
{{
  "assignment_name": "Assignment-X",
  "rubric_md": "Full markdown content for rubric.md...",
  "solution_py": "Full python code for solution.py..."
}}

INSTRUCTIONS for Rubric:
- Use a 10-point scoring system.
- Include a 'Goal', 'Requirements', 'Scoring', and 'Common Mistakes & Feedback Guidance' section.
- Be very specific about identifying factual errors vs syntax errors.

INSTRUCTIONS for Solution:
- Include comments explaining every step.
- Answer all questions asked in the instructions.
"""
    return call_ai(AI_PROVIDER, prompt)

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
        result = generate_rubric_and_solution(assign["title"], assign["content"])
        
        os.makedirs(target_dir, exist_ok=True)
        
        with open(os.path.join(target_dir, "rubric.md"), "w") as f:
            f.write(result["rubric_md"])
            
        with open(os.path.join(target_dir, "solution.py"), "w") as f:
            f.write(result["solution_py"])
            
        print(f"  -> Successfully created {assign_folder}")

if __name__ == "__main__":
    main()
