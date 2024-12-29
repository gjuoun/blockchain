from typing import List, Dict, Optional
from dataclasses import dataclass
import time
import hashlib
import json
from .account import Account
from .block import Block

@dataclass
class Transaction:
    sender: Account
    receiver: Account
    value: int
    gas: int
    gas_price: int
    data: Optional[str] = None
    nonce: int = 0
    signature: Optional[str] = None

    def hash(self) -> str:
        tx_data = {
            'sender': self.sender.address,
            'receiver': self.receiver.address,
            'value': self.value,
            'gas': self.gas,
            'gas_price': self.gas_price,
            'data': self.data,
            'nonce': self.nonce
        }
        return hashlib.sha256(json.dumps(tx_data).encode()).hexdigest()

class EthBlockchain:
    def __init__(self, difficulty: int = 2):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.accounts: Dict[str, Account] = {}
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(
            index=0,
            previous_hash="0",
            timestamp=int(time.time()),
            transactions=[],
            miner="0",
            difficulty=self.difficulty,
            nonce=0
        )
        self.chain.append(genesis_block)

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def create_account(self) -> Account:
        address = hashlib.sha256(str(time.time()).encode()).hexdigest()
        account = Account(address=address, balance=0, nonce=0)
        self.accounts[address] = account
        return account

    def add_transaction(self, transaction: Transaction) -> bool:
        # Validate transaction
        sender_account = self.accounts.get(transaction.sender.address)
        if not sender_account:
            return False
            
        if sender_account.balance < transaction.value + (transaction.gas * transaction.gas_price):
            return False
            
        if sender_account.nonce != transaction.nonce:
            return False
            
        self.pending_transactions.append(transaction)
        return True

    def mine_block(self, miner_address: str) -> bool:
        if not self.pending_transactions:
            return False
            
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            previous_hash=latest_block.calculate_hash(),
            timestamp=int(time.time()),
            transactions=self.pending_transactions,
            miner=miner_address,
            difficulty=self.difficulty,
            nonce=0
        )
        
        # Proof of work
        while not new_block.calculate_hash().startswith('0' * self.difficulty):
            new_block.nonce += 1
            
        # Update accounts
        for tx in new_block.transactions:
            sender = self.accounts[tx.sender.address]
            receiver = self.accounts[tx.receiver.address]
            
            # Update balances
            sender.balance -= tx.value + (tx.gas * tx.gas_price)
            receiver.balance += tx.value
            
            # Update nonces
            sender.nonce += 1
            
        # Miner reward (block reward + gas fees)
        miner_account = self.accounts[miner_address]
        total_gas_fees = sum(tx.gas * tx.gas_price for tx in new_block.transactions)
        miner_account.balance += 5 + total_gas_fees  # Block reward + gas fees
        
        self.chain.append(new_block)
        self.pending_transactions = []
        return True

    def get_balance(self, address: str) -> int:
        account = self.accounts.get(address)
        return account.balance if account else 0
