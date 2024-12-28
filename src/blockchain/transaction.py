
import time
import uuid
from typing import List, Optional

class Input:
    def __init__(self, address: str, amount: int):
        if not address:
            raise ValueError("Address cannot be empty")
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("Amount must be a non-negative integer representing satoshis")
        self.address = address
        self.amount = amount

class Output:
    def __init__(self, amount: int, address: str):
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("Amount must be a non-negative integer representing satoshis")
        if not address:
            raise ValueError("Address cannot be empty")
        self.amount = amount
        self.address = address

class Transaction:
    def __init__(self, version: int, inputs: List[Input], outputs: List[Output], locktime: int = None):
        self.version = version
        self.inputs = inputs
        self.outputs = outputs
        self.locktime = int(time.time()) if locktime is None else locktime
