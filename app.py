"""
app.py
FastAPI server for the Customer Support Chatbot.
Run: uvicorn app:app --reload --port 8000
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from chatbot import CustomerSupportBot

app = FastAPI(title="Customer Support Chatbot API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

bot = CustomerSupportBot()


class MessageRequest(BaseModel):
    message: str
    session_id: Optional[str] = "default"


class MessageResponse(BaseModel):
    response: str
    intent: Optional[str]
    confidence: float


@app.post("/chat", response_model=MessageResponse)
def chat(req: MessageRequest):
    if not req.message.strip():
        raise HTTPException(400, "Message cannot be empty.")
    result = bot.get_response(req.message)
    return MessageResponse(**result)


@app.post("/reset")
def reset():
    bot.reset_context()
    return {"status": "context cleared"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/intents")
def get_intents():
    from knowledge_base import KNOWLEDGE_BASE
    return {"intents": [k for k in KNOWLEDGE_BASE.keys() if k != "fallback"]}