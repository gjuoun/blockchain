from blockchain.blockchain import Blockchain
from blockchain.transaction import Transaction

def main():
    blockchain = Blockchain()
    
    # Create some sample transactions
    tx1 = Transaction("Alice", "Bob", 50)
    tx2 = Transaction("Bob", "Charlie", 30)
    tx3 = Transaction("Charlie", "Alice", 20)
    
    # Add blocks with transactions
    blockchain.add_block([tx1])
    blockchain.add_block([tx2, tx3])
    
    # Print the blockchain
    for block in blockchain.chain:
        print(f"\nBlock #{block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print("Transactions:")
        for tx in block.transactions:
            print(f"  {tx.sender} sent {tx.amount} to {tx.recipient}")

if __name__ == "__main__":
    main()
