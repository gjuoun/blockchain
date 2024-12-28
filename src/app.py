from blockchain.blockchain import Blockchain
from blockchain.transaction import Transaction, Input, Output

def main():
    blockchain = Blockchain()
    
    # Create sample inputs and outputs
    input1 = Input("genesis", 0)
    output1 = Output(50, "Bob")
    input2 = Input("tx1", 0)
    output2 = Output(30, "Charlie")
    input3 = Input("tx2", 0)
    output3 = Output(20, "Alice")
    
    # Create transactions
    tx1 = Transaction(1, [input1], [output1])
    tx2 = Transaction(1, [input2], [output2])
    tx3 = Transaction(1, [input3], [output3])
    
    # Add blocks with transactions
    blockchain.add_block([tx1])
    blockchain.add_block([tx2, tx3])
    
    # Print the blockchain
    for block in blockchain.chain:
        print(f"\nBlock #{block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print("Transactions:")
        if block.transactions:
            for tx in block.transactions:
                for output in tx.outputs:
                    print(f"  Transfer {output.amount} coins to {output.recipient}")
        else:
            print("  Genesis block - no transactions")

if __name__ == "__main__":
    main()
