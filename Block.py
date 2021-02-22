from Transaction import Transaction
import hashlib as hash
import json

class Block:
    def __init__(self, timestamp, transactions, previousHash = ''):
        self.timestamp = timestamp
        self.transactions = transactions
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        hashValue = hash.sha256((self.timestamp + str(self.nonce) + json.dumps(str(self.transactions))).encode('utf-8'))
        hashValue.update(str.encode('UTF-8'))
        hashValueHex = hashValue.hexdigest()
        return hashValueHex
    
    def __str__(self):
        return json.dumps(
            {
                'timestamp' : self.timestamp,
                'transactions' : str(self.transactions),
                'previousHash' : self.previousHash,
                'hash' : self.hash
            },
            indent = 4
        )

    def mineBlock(self, difficulty):
        difficultyStr = '0' * (difficulty)
        while self.hash[0 : difficulty] != difficultyStr:
            self.nonce += 1
            self.hash = self.calculateHash()
        
        print('Block mined: {}'.format(self.hash))
