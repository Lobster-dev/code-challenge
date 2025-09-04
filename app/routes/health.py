from fastapi import APIRouter


router = APIRouter()

@router.get('/')
async def alive():
    return {"status": "ok"}