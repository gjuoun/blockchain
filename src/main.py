import hashlib
import time
from typing import Any, List
from .transaction import Input, Output, Transaction

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: int, data: List[Transaction]):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}".encode()
        print(value)  # Print the value to see the result
        return hashlib.sha256(value).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), [])

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions: List[Transaction]):
        latest_block = self.get_latest_block()
        new_index = latest_block.index + 1
        new_timestamp = int(time.time())
        new_block = Block(new_index, latest_block.hash, new_timestamp, transactions)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

def main():
    blockchain = Blockchain()
    transactions1 = [Transaction(1, [Input("tx_id_1", 0)], [Output(10.0, "recipient_1")], 0)]
    transactions2 = [Transaction(1, [Input("tx_id_2", 0)], [Output(15.0, "recipient_2")], 0)]
    blockchain.add_block(transactions1)
    blockchain.add_block(transactions2)

    for block in blockchain.chain:
        print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}")

if __name__ == "__main__":
    main()
