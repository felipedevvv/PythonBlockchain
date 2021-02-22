from Block import Block
from datetime import date

class Blockchain:
    def __init__(self):
        self.chain = [self.createGenisisBlock()]
        self.difficulty = 4

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
        newBlock.mineBlock(self.difficulty)
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


