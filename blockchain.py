import hashlib
import time
from flask import Flask, request, jsonify

# Block class to define the structure of a block
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.current_hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        while not self.current_hash.startswith('0' * difficulty):
            self.nonce += 1
            self.current_hash = self.compute_hash()

# Blockchain class to manage the chain of blocks
class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = 2  # Number of leading zeros for PoW
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), "Genesis Block", "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def add_block(self):
        if not self.pending_transactions:
            return "No transactions to add."

        previous_block = self.chain[-1]
        new_block = Block(
            len(self.chain), time.time(), self.pending_transactions, previous_block.current_hash
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.current_hash != current.compute_hash():
                return False

            if current.previous_hash != previous.current_hash:
                return False

        return True

# Flask app to dynamically interact with the blockchain
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    transaction = request.json.get('transaction')
    if not transaction:
        return jsonify({"error": "Transaction data is required"}), 400

    blockchain.add_transaction(transaction)
    return jsonify({"message": "Transaction added successfully."}), 200

@app.route('/mine_block', methods=['POST'])
def mine_block():
    new_block = blockchain.add_block()
    if isinstance(new_block, str):
        return jsonify({"message": new_block}), 200

    return jsonify({
        "message": "Block mined successfully.",
        "block": {
            "index": new_block.index,
            "timestamp": new_block.timestamp,
            "data": new_block.data,
            "previous_hash": new_block.previous_hash,
            "current_hash": new_block.current_hash,
        }
    }), 200

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [
        {
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.data,
            "previous_hash": block.previous_hash,
            "current_hash": block.current_hash,
        }
        for block in blockchain.chain
    ]
    return jsonify({"length": len(chain_data), "chain": chain_data}), 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the Blockchain API! Available endpoints:",
        "endpoints": {
            "/add_transaction": "POST - Add a new transaction (JSON payload: { 'transaction': 'Your transaction here' })",
            "/mine_block": "POST - Mine a new block with the pending transactions",
            "/chain": "GET - Retrieve the entire blockchain",
            "/validate_chain": "GET - Validate the integrity of the blockchain",
        }
    }), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
