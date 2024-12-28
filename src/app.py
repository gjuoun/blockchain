from blockchain.blockchain import Blockchain
from blockchain.transaction import Transaction, Input, Output

def create_sample_transactions(blockchain):
    # Create sample inputs and outputs
    input1 = Input("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "genesis", 0)
    output1 = Output(5000000000, "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2")  # 50 BTC in satoshis
    input2 = Input("1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2", "tx1", 0)
    output2 = Output(3000000000, "1CounterpartyXXXXXXXXXXXXXXXUWLpVr")  # 30 BTC in satoshis
    input3 = Input("1CounterpartyXXXXXXXXXXXXXXXUWLpVr", "tx2", 0)
    output3 = Output(2000000000, "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")  # 20 BTC in satoshis
    
    # Create transactions
    tx1 = Transaction(1, [input1], [output1])
    tx2 = Transaction(1, [input2], [output2])
    tx3 = Transaction(1, [input3], [output3])
    
    # Add blocks with transactions
    blockchain.add_block([tx1])
    blockchain.add_block([tx2, tx3])

def main():
    blockchain = Blockchain()
    create_sample_transactions(blockchain)
    
    # Print the blockchain
    for block in blockchain.chain:
        print(f"\nBlock #{block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print("Transactions:")
        if block.transactions:
            for tx in block.transactions:
                for output in tx.outputs:
                    print(f"  Transfer {output.amount} coins to {output.address}")
        else:
            print("  Genesis block - no transactions")

if __name__ == "__main__":
    main()
