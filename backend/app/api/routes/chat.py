from fastapi import APIRouter, HTTPException
from app.models.chat import ChatMessage
from typing import Dict

router = APIRouter()

@router.post("/message")
async def send_message(message: ChatMessage) -> Dict:
    try:
        # Şimdilik basit bir yanıt döndürelim
        return {
            "response": f"Mesajınız alındı: {message.content}",
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )