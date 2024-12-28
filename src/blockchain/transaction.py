
class Input:
    def __init__(self, tx_id: str, output_index: int):
        self.tx_id = tx_id
        self.output_index = output_index

class Output:
    def __init__(self, value: float, recipient: str):
        self.value = value
        self.recipient = recipient

class Transaction:
    def __init__(self, version, inputs, outputs, locktime):
        self.version = version
        self.inputs = inputs
        self.outputs = outputs
        self.locktime = locktime
