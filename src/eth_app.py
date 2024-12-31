from eth.eth_blockchain import EthBlockchain, Transaction

def main():
    # Initialize blockchain
    blockchain = EthBlockchain(difficulty=2)
    
    # Create accounts
    alice = blockchain.create_account()
    bob = blockchain.create_account()
    miner = blockchain.create_account()
    
    # Fund Alice's account (special case for genesis)
    blockchain.accounts[alice.address].balance = 1000
    
    print(f"Alice's balance: {blockchain.get_balance(alice.address)}")
    print(f"Bob's balance: {blockchain.get_balance(bob.address)}")
    
    # Create transactions
    tx1 = Transaction(
        sender=alice,
        receiver=bob,
        value=100,
        gas=10,
        gas_price=1
    )
    
    tx2 = Transaction(
        sender=alice,
        receiver=bob,
        value=50,
        gas=10,
        gas_price=1
    )
    
    # Add transactions
    blockchain.add_transaction(tx1)
    blockchain.add_transaction(tx2)
    
    # Mine block
    if blockchain.mine_block(miner.address):
        print("\nBlock mined successfully!")
        print(f"Alice's new balance: {blockchain.get_balance(alice.address)}")
        print(f"Bob's new balance: {blockchain.get_balance(bob.address)}")
        print(f"Miner's balance: {blockchain.get_balance(miner.address)}")
    else:
        print("Failed to mine block")

if __name__ == "__main__":
    main()
