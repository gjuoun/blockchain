
import time
from typing import List

class Input:
    def __init__(self, tx_id: str, output_index: int):
        self.tx_id = tx_id
        self.output_index = output_index

class Output:
    def __init__(self, value: float, recipient: str):
        self.value = value
        self.recipient = recipient

class Transaction:
    def __init__(self, version: int, inputs: List[Input], outputs: List[Output], locktime: int = None):
        self.version = version
        self.inputs = inputs
        self.outputs = outputs
        self.locktime = int(time.time()) if locktime is None else locktime
