
import time
import uuid
from typing import List, Optional
class Input:
    def __init__(self, address: str, amount: int):
        self.address = address
        self.amount = amount

class Output:
    def __init__(self, amount: int, address: str):
        self.amount = amount
        self.address = address

# in each transaction, create a method that make sure amounts in inputs are greater than amounts in outputs, ai!
class Transaction:
    def __init__(self, version: int, inputs: List[Input], outputs: List[Output], locktime: int = None):
        self.version = version
        self.inputs = inputs
        self.outputs = outputs
        self.locktime = int(time.time()) if locktime is None else locktime
