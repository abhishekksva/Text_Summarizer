cat > app.py << 'EOF'
from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline
import re
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Lightweight summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-6-6")

templates = Jinja2Templates(directory="templates")

class DialogueInput(BaseModel):
    dialogue: str

def clean_data(text):
    text = re.sub(r"\r\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    return text.strip()

@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    text = clean_data(dialogue_input.dialogue)
    result = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return {"summary": result[0]["summary_text"]}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

