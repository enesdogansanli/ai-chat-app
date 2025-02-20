from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import chat, auth, settings

app = FastAPI(title="AI Chat Backend")

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React uygulamasının adresi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route'ları ekle
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(settings.router, prefix="/api/settings", tags=["settings"])