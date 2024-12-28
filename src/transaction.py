from typing import List
# remove all docstrings in this file, AI!
class Input:
    """Represents a transaction input that references a previous transaction's output.
    
    Attributes:
        tx_id (str): The transaction ID of the referenced output
        output_index (int): The index of the output in the referenced transaction
    """
    def __init__(self, tx_id: str, output_index: int):
        self.tx_id = tx_id
        self.output_index = output_index

class Output:
    """Represents a transaction output that specifies value and recipient.
    
    Attributes:
        value (float): The amount of cryptocurrency to transfer
        recipient (str): The address of the recipient
    """
    def __init__(self, value: float, recipient: str):
        self.value = value
        self.recipient = recipient

class Transaction:
    """Represents a complete cryptocurrency transaction.
    
    Attributes:
        version (int): Transaction format version
        inputs (List[Input]): List of transaction inputs
        outputs (List[Output]): List of transaction outputs
        locktime (int): Block height or timestamp when transaction becomes valid
    """
    def __init__(self, version: int, inputs: List[Input], outputs: List[Output], locktime: int):
        self.version = version
        self.inputs = inputs
        self.outputs = outputs
        self.locktime = locktime
