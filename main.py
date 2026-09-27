from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.route import router

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title="FitBuddy - AI Fitness Plan Generator",
    description="AI-powered fitness planning application",
    version="1.0.0"
)

# Static files configuration
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "app" / "static"),
    name="static"
)

# Include router
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    print("FitBuddy-AI is starting up...")