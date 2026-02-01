"""
FastAPI Frontend Server
Simple, clean UI for RAG Chat System
"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(title="RAG Frontend")

# Templates directory
templates = Jinja2Templates(directory="templates")

# API Base URL - can be set via environment variable
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Redirect to chat page without session"""
    return templates.TemplateResponse("chat.html", {
        "request": request,
        "api_base_url": API_BASE_URL,
        "session_id": None
    })


@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    """Chat page without session"""
    return templates.TemplateResponse("chat.html", {
        "request": request,
        "api_base_url": API_BASE_URL,
        "session_id": None
    })


@app.get("/chat/{session_id}", response_class=HTMLResponse)
async def chat_page_with_session(request: Request, session_id: str):
    """Chat page with session ID"""
    return templates.TemplateResponse("chat.html", {
        "request": request,
        "api_base_url": API_BASE_URL,
        "session_id": session_id
    })


@app.get("/admin", response_class=HTMLResponse)
async def admin_page(request: Request):
    """Admin page"""
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "api_base_url": API_BASE_URL
    })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
