from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse
from app.domain.models import EventIn
from app.domain.services import AccountService
from app.infra.storage import InMemoryStore

router = APIRouter()

# Instância única do service (state in-memory), simples e suficiente para o exercício
_store = InMemoryStore()
_service = AccountService(_store)

def get_service() -> AccountService:
    return _service

@router.post("/reset")
def reset_state(service: AccountService = Depends(get_service)):
    service.reset()
    # Spec não exige corpo; 200 OK vazio é suficiente
    return Response(status_code=200)

@router.get("/balance")
def get_balance(account_id: str, service: AccountService = Depends(get_service)):
    balance = service.get_balance(account_id)
    if balance is None:
        # A suíte de testes espera 404 com corpo "0" (text/plain)
        return Response(content="0", status_code=404, media_type="text/plain")
    return Response(content=str(balance), status_code=200, media_type="text/plain")

@router.post("/event")
def post_event(event: EventIn, service: AccountService = Depends(get_service)):
    payload, status = service.handle_event(event)
    if status == 404:
        return Response(content="0", status_code=404, media_type="text/plain")
    return JSONResponse(content=payload, status_code=201)