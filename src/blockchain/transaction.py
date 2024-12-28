
import time
import uuid
from typing import List, Optional

class Input:
    def __init__(self, address: str, tx_id: Optional[str] = None, output_index: int = 0):
        if not address:
            raise ValueError("Address cannot be empty")
        self.tx_id = str(uuid.uuid7()) if tx_id is None else tx_id
        self.output_index = output_index
        self.address = address

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
