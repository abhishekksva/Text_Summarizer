# Text Summarizer 📝
### Text Summarization using HuggingFace T5 Transformer

## Overview
An end-to-end text summarization web app that takes any long text or dialogue and returns a concise summary. Built with FastAPI backend and a clean HTML/CSS frontend.

## Tech Stack
- **Model**: T5 (Text-to-Text Transfer Transformer) by Google
- **Framework**: FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **Library**: HuggingFace Transformers
- **Device Support**: CPU, CUDA (GPU), Apple MPS (M1/M2)

## Project Structure
```
Text_Summarizer/
├── app.py              # FastAPI backend
├── index.html          # Frontend UI
├── requirements.txt    # Dependencies
└── saved_summary_model/ # Trained T5 model (not in repo)
```

## Features
- Paste any long text or dialogue
- Click Summarize to get instant summary
- Clean orange-themed UI
- Supports GPU acceleration

## How to Run Locally

### Step 1 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Run the app
```bash
uvicorn app:app --reload
```

### Step 3 — Open in browser
```
http://localhost:8000
```

## API Endpoints
- `GET /` — Home page
- `POST /summarize/` — Summarize text

## Example
**Input:**
"The quick brown fox jumps over the lazy dog. The dog was sleeping near the river bank..."

**Output:**
"A fox jumps over a sleeping dog near a river."

## Note
The trained model (`saved_summary_model/`) is not included in this repo due to large file size. You need to train it first or download from HuggingFace Hub.
