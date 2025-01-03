import hashlib
import time
from typing import Any, List
from .transaction import Input, Output, Transaction

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: int, transactions: List[Transaction]):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}".encode()
        return hashlib.sha256(value).hexdigest()

class Blockchain:
    def __init__(self) -> None:
        self.chain: List[Block] = [self.create_genesis_block()]

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
