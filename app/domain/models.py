from typing import Literal, Optional
from pydantic import BaseModel, Field

EventType = Literal["deposit", "withdraw", "transfer"]

class EventIn(BaseModel):
    type: EventType
    origin: Optional[str] = None
    destination: Optional[str] = None
    amount: int = Field(ge=0)

class AccountModel(BaseModel):
    id: str
    balance: int

class DepositResponse(BaseModel):
    destination: AccountModel

class WithdrawResponse(BaseModel):
    origin: AccountModel

class TransferResponse(BaseModel):
    origin: AccountModel
    destination: AccountModel