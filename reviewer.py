from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import sys
import os

# ================= CONFIG =================
GEMINI_API_KEY = "AIzaSyDydGvz1D04J_piLJO_5ouK_fsvVaJRaFg"   # replace locally ONLY
genai.configure(api_key=GEMINI_API_KEY)

# ================= MODEL =================
def get_model():
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            return genai.GenerativeModel(m.name)
    print("No supported Gemini model found")
    sys.exit(1)

model = get_model()

# ================= FASTAPI =================
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= REQUEST MODEL =================
class CodeRequest(BaseModel):
    code: str

# ================= AI REVIEW =================
def ai_review(code: str) -> str:
    prompt = f"""
You are a senior software engineer reviewing code.

RULES:
- Give only one-line bullet points
- No paragraphs

FORMAT:

SUMMARY:
- <one line>

ISSUES:
- <one line or None>

SECURITY:
- <one line or None>

IMPROVEMENTS:
- <one line>

VERDICT:
- <one line>

CODE:
{code}
"""
    response = model.generate_content(prompt)

    if hasattr(response, "text") and response.text:
        return response.text

    if hasattr(response, "candidates"):
        return response.candidates[0].content.parts[0].text

    return "No review generated"

# ================= FRONTEND =================
@app.get("/")
def home():
    return FileResponse("index.html")

# ================= API =================
@app.post("/review")
def review(req: CodeRequest):
    if not req.code.strip():
        return JSONResponse({"review": "No code provided"})

    result = ai_review(req.code)
    return JSONResponse({"review": result})