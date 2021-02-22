import hashlib as hash
import json

class Block:
    def __init__(self, index, timestamp, data, previousHash = ''):
        self.index = index
        self.timestamp = timestamp
        self.data : dict = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        hashValue = hash.sha256((str(self.index) + self.timestamp + str(self.nonce) + json.dumps(self.data)).encode('utf-8'))
        hashValue.update(str.encode('UTF-8'))
        hashValueHex = hashValue.hexdigest()
        return hashValueHex
    
    def __str__(self):
        return json.dumps(
            {
                'index' : self.index,
                'timestamp' : self.timestamp,
                'data' : self.data,
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
