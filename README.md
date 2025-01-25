# Blockchain Simulation

A simple blockchain simulation built with Python and Flask, showcasing the basic features of a blockchain, including block structure, hashing, chain validation, and transaction handling.

---

## Features

1. **Block Structure**  
   Each block contains the following:
   - Block index
   - Timestamp of block creation
   - List of transactions
   - Hash of the previous block
   - Current block hash

2. **Hashing**  
   - Utilizes the SHA-256 hashing algorithm to generate the block’s hash based on its data and the hash of the previous block.

3. **Blockchain Class**  
   - Manages the chain of blocks.
   - Provides methods to:
     - Add new blocks.
     - Validate the chain’s integrity to ensure hashes are correctly linked.

4. **Proof-of-Work**  
   - Implements a basic proof-of-work mechanism requiring block hashes to start with a defined number of leading zeros.

5. **Dynamic Transaction Handling**  
   - Allows users to dynamically add transactions to a list of pending transactions.
   - Mines a new block with the pending transactions.

6. **API Endpoints**  
   A Flask-based API to interact with the blockchain:
   - `POST /add_transaction`: Add a new transaction.
   - `GET /chain`: Retrieve the entire blockchain.
   - `POST /mine_block`: Mine a new block.
   - `GET /validate_chain`: Validate the blockchain.

---

## Requirements

- Python 3.10 or above
- Flask 3.1.0
- Docker (for containerization)

---

## Installation and Usage

### Clone the Repository
```bash
git clone <repository-url>
cd blockchain_simulation

Install Dependencies
pip install -r requirements.txt

Run the Application
python blockchain.py

Test API Endpoints
Use Postman or curl to interact with the following endpoints:
POST /add_transaction

Payload:
json
{
  "transaction": "Alice pays Bob 10 coins"
}
POST /mine_block
GET /chain
GET /validate_chain

Docker Setup

Build Docker Image
docker build -t blockchain-app .

Run Docker Container
docker run -p 5000:5000 blockchain-app

Demonstration
Add Transactions
Add one or more transactions using the /add_transaction endpoint.

Mine a Block
Mine a new block with the pending transactions using /mine_block.

Retrieve the Blockchain
View the blockchain details by accessing the /chain endpoint.

Validate the Blockchain
Check the integrity of the blockchain using /validate_chain.

Tampering Demonstration
Manually modify the data in a block and validate the chain using /validate_chain. The chain will detect the tampering, demonstrating its integrity validation mechanism.

Project Structure
bash
Copy
Edit
blockchain_simulation/
├── blockchain.py        # Main application code
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

Future Enhancements
Add support for persistent storage of the blockchain.
Implement a decentralized peer-to-peer network.
Add advanced proof-of-work or proof-of-stake algorithms.

License
This project is open-source and available under the MIT License.