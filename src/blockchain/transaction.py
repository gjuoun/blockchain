
import time
from typing import List, Optional

class InvalidTransactionException(Exception):
    """Exception raised when a transaction is invalid"""
    def __init__(self, total_input: int, total_output: int):
        super().__init__(f"Transaction invalid: total inputs ({total_input}) less than total outputs ({total_output})")
        self.total_input = total_input
        self.total_output = total_output
class Input:
    def __init__(self, address: str, amount: int):
        self.address = address
        self.amount = amount

class Output:
    def __init__(self, amount: int, address: str):
        self.amount = amount
        self.address = address

class Transaction:
    def __init__(self, version: int, inputs: List[Input], outputs: List[Output], locktime: int = None):
        self.version = version
        self.inputs = inputs
        self.outputs = outputs
        self.locktime = int(time.time()) if locktime is None else locktime
        self.validate_transaction()
    def validate_transaction(self):
        """
        Validate that total input amounts are >= total output amounts
        Returns the remaining balance that can be used as miner reward
        """
        total_input = sum(input.amount for input in self.inputs)
        total_output = sum(output.amount for output in self.outputs)
        
        if total_input < total_output:
            raise InvalidTransactionException(total_input, total_output)
        
        return total_input - total_output
