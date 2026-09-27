from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
   return templates.TemplateResponse(request=request, name="index.html")
@router.post("/api/chat")
async def chat_endpoint(data: dict):
    user_message = data.get("message", "")
    response_text = f"FitBuddy AI Response for: {user_message}"
    return {"reply": response_text}