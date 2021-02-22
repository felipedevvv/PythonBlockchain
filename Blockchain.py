from Transaction import Transaction
from Block import Block
from datetime import date

class Blockchain:
    def __init__(self):
        self.chain = [self.createGenisisBlock()]
        self.difficulty = 2
        self.pendingTransactions = []
        self.miningReward = 100

    def __str__(self):
        chainHistory = '\nchain: \n'
        for block in self.chain:
            chainHistory += str(block)
            chainHistory += ', \n'
        return chainHistory

    def createGenisisBlock(self):
        return Block(date.today().strftime('%m/%d/%y'), {'amount' : 'Genisis Block'}, '0')

    def getLatestBlock(self):
        return self.chain[-1]

    def minePendingTransactions(self, miningRewardAddress):
        block = Block(date.today().strftime('%m/%d/%y'), self.pendingTransactions)
        block.mineBlock(self.difficulty)

        print('Block successfuly mined.')
        self.chain.append(block)

        self.pendingTransactions = [Transaction(None, miningRewardAddress, self.miningReward)];
        
    def createTransaction(self, transaction: Transaction):
        self.pendingTransactions.append(transaction)

    def getBalanceOfAddress(self, address):
        balance = 0
        for block in self.chain:
            for trans in block.transactions:
                if isinstance(trans, Transaction):
                    if trans.fromAddress == address:
                        balance -= trans.amount
                    
                    if trans.toAddress == address:
                        balance += trans.amount
        
        return balance

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


