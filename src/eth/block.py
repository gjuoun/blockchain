from typing import List, TYPE_CHECKING
import time
import hashlib
import json
from .account import Account

class Block:
    def __init__(self, 
                 index: int, 
                 previous_hash: str, 
                 timestamp: int, 
                 transactions: List['Transaction'],
                 miner: str,
                 difficulty: int,
                 nonce: int):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.miner = miner
        self.difficulty = difficulty
        self.nonce = nonce

    def calculate_hash(self) -> str:
        block_data = {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'transactions': [tx.hash() for tx in self.transactions],
            'miner': self.miner,
            'difficulty': self.difficulty,
            'nonce': self.nonce
        }
        return hashlib.sha256(json.dumps(block_data).encode()).hexdigest()
