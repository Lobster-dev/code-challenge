from threading import Lock
from typing import Dict, Optional, Tuple

class MemoryStorage:

    def __init__(self) -> None:
        self._balances: Dict[str, int] = {}
        self._lock = Lock()

    def reset(self) -> None:
        with self._lock:
            self._balances.clear()
            

    def get_balance(self, account_id: str) -> Optional[int]:
        with self._lock:
            return self._balances.get(account_id)

    def deposit(self, destination: str | None, amount: int) -> int:
        if not destination:
            raise ValueError("destination is required for deposit")
        with self._lock:
            new_balance = self._balances.get(destination, 0) + amount
            self._balances[destination] = new_balance
            return new_balance

    def withdraw(self, origin: str | None, amount: int) -> Optional[int]:
        if not origin:
            return None
        with self._lock:
            if origin not in self._balances:
                return None
            new_balance = self._balances[origin] - amount
            self._balances[origin] = new_balance
            return new_balance

    def transfer(self, origin: str | None, destination: str | None, amount: int) -> Tuple[Optional[int], Optional[int]]:
        if not origin:
            return None, None
        if not destination:
            return None, None
        with self._lock:
            if origin not in self._balances:
                return None, None
            origin_balance = self._balances[origin] - amount
            dest_balance = self._balances.get(destination, 0) + amount
            self._balances[origin] = origin_balance
            self._balances[destination] = dest_balance
            return origin_balance, dest_balance