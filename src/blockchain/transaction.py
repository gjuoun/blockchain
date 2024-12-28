
import time
import uuid
from typing import List, Optional

class Input:
    def __init__(self, tx_id: Optional[str] = None, output_index: int = 0):
        self.tx_id = str(uuid.uuid7()) if tx_id is None else tx_id
        self.output_index = output_index

class Output:
    # use amount in satoshis, refactor otherfiles as needed, ai!
    def __init__(self, value: float, recipient: str):
        self.value = value
        self.recipient = recipient

class Transaction:
    def __init__(self, version: int, inputs: List[Input], outputs: List[Output], locktime: int = None):
        self.version = version
        self.inputs = inputs
        self.outputs = outputs
        self.locktime = int(time.time()) if locktime is None else locktime
