from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Basit bir login endpoint'i
    return {"message": "Login endpoint"}

@router.post("/register")
async def register():
    # Basit bir kayıt endpoint'i
    return {"message": "Register endpoint"}