from dataclasses import dataclass

@dataclass
class Account:
    address: str
    balance: int
    nonce: int
