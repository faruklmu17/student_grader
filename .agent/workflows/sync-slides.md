---
description: Synchronizes assignments from Google Slides to the codebase
---

Follow these steps to sync new assignments from your Google Slides presentation:

1. Ensure the Google Slides API is enabled in your Google Cloud Console.
2. Ensure `credentials.json` is present in the root directory and has access to the presentation.
3. Run the sync command:
// turbo
```bash
python3 sync_slides.py
```

This will:
- Read all slides from the specified presentation ID.
- Detect "Assignment" slides.
- Use AI to generate `rubric.md` and `solution.py`.
- Create new folders in `rubrics/Python Level-1/` automatically.
