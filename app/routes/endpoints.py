from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse
from starlette.status import (
        HTTP_200_OK, HTTP_201_CREATED,
        HTTP_404_NOT_FOUND,
        HTTP_500_INTERNAL_SERVER_ERROR
    )

from app.domain.models import EventIn
from app.domain.services import AccountService
from app.infra.storage import MemoryStorage



router   = APIRouter()
_store   = MemoryStorage()
_service = AccountService(_store)

def get_service() -> AccountService:
    return _service

def get_storage() -> MemoryStorage:
    return _store

@router.post("/reset")
def reset_state(store: MemoryStorage = Depends(get_storage)):
    try: 
        store.reset()
        return Response(
            content="OK", 
            media_type="text/plain",
            status_code=HTTP_200_OK
        )
    except Exception:
        return JSONResponse(
            content={"error": "failed to reset"},
            status_code=HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.get("/balance")
def get_balance(account_id: str, service: AccountService = Depends(get_service)):
    balance = service.get_balance(account_id)
    if balance is None:
        return Response(
            content="0",
            status_code=HTTP_404_NOT_FOUND,
            media_type="text/plain"
        )
    return Response(
        content=str(balance),
        status_code=HTTP_200_OK,
        media_type="text/plain"
    )

@router.post("/event")
def post_event(event: EventIn, service: AccountService = Depends(get_service)):
    payload, status = service.handle_event(event)
    if status == HTTP_404_NOT_FOUND:
        return Response(
            content="0",
            status_code=HTTP_404_NOT_FOUND,
            media_type="text/plain"
        )
    return JSONResponse(
        content=payload,
        status_code=HTTP_201_CREATED
    )