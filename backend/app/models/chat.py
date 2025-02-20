from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ChatMessage(BaseModel):
    id: Optional[int] = None
    content: str
    timestamp: Optional[datetime] = None
    user_id: Optional[int] = None
    is_bot: Optional[bool] = False

    class Config:
        arbitrary_types_allowed = True