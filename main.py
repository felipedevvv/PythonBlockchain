from array import ArrayType
import hashlib as hash
from datetime import date
import json
from typing import ChainMap

class Block:
    def __init__(self, index, timestamp, data, previousHash = ''):
        self.index = index
        self.timestamp = timestamp
        self.data : dict = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def calculateHash(self):
        hashValue = hash.sha256((str(self.index) + self.timestamp + json.dumps(self.data)).encode('utf-8'))
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

class Blockchain:
    def __init__(self):
        self.chain = [self.createGenisisBlock()]

    def __str__(self):
        chainHistory = '\nchain: \n'
        for block in self.chain:
            chainHistory += str(block)
            chainHistory += ', \n'
        return chainHistory

    def createGenisisBlock(self):
        return Block(0, date.today().strftime('%m/%d/%y'), 'Genisis Block', '0')

    def getLatestBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock: Block):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock)

    def isChainValid(self):
        i = 1

        while i < len(self.chain):
            currBlock = self.chain[i]
            prevBlock = self.chain[i - 1]

            if currBlock.hash != currBlock.calculateHash():
                return False

            if currBlock.previousHash != prevBlock.hash:
                return False
            i += 1

        return True



xxuegooCoin = Blockchain()
xxuegooCoin.addBlock(Block(1, '02/01/2021', { 'amount': 4} ))
xxuegooCoin.addBlock(Block(2, '02/01/2021', { 'amount': 7} ))

print('Is blockchain valid? {}'.format(xxuegooCoin.isChainValid()))
# print(xxuegooCoin)

xxuegooCoin.chain[1].data = { 'amount' : 100 }
xxuegooCoin.chain[1].hash = xxuegooCoin.chain[1].calculateHash()
print('Is blockchain valid? {}'.format(xxuegooCoin.isChainValid()))