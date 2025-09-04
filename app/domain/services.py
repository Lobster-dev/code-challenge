from typing import Any, Dict, Tuple

from app.domain.models import EventIn
from app.infra.storage import MemoryStorage

from starlette.status import (
        HTTP_201_CREATED, HTTP_404_NOT_FOUND
    )


class AccountService:

    def __init__(self, store: MemoryStorage):
        self.store = store

    def reset(self) -> None:
        self.store.reset()

    def get_balance(self, account_id: str):
        return self.store.get_balance(account_id)

    def handle_event(self, event: EventIn) -> Tuple[Any, int]:
        if event.type == "deposit":
            new_balance = self.store.deposit(event.destination, event.amount)
            return {"destination": {"id": event.destination, "balance": new_balance}}, HTTP_201_CREATED

        if event.type == "withdraw":
            new_balance = self.store.withdraw(event.origin, event.amount)
            if new_balance is None:
                return "0", HTTP_404_NOT_FOUND
            return {"origin": {"id": event.origin, "balance": new_balance}}, HTTP_201_CREATED

        if event.type == "transfer":
            origin_balance, dest_balance = self.store.transfer(event.origin, event.destination, event.amount)
            if origin_balance is None:
                return "0", HTTP_404_NOT_FOUND
            return {
                "origin": {"id": event.origin, "balance": origin_balance},
                "destination": {"id": event.destination, "balance": dest_balance},
            }, HTTP_201_CREATED


        return "0", HTTP_404_NOT_FOUND