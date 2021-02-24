from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
from hashlib import sha256
import json

###
###
### Unfinished code - switched over to javascript to finish the project and further with Angular frontend
###
###

class Transaction:
    def __init__(self, fromAddress, toAddress, amount):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount
        self.signature = None
    
    def __str__(self):
        return json.dumps(
            {
                'fromAddress' : self.fromAddress,
                'toAddress' : self.toAddress,
                'amount' : self.amount
            },
            indent = 4
        )

    def calculateHash(self):
        return str(sha256(self.fromAddress + self.toAddress + self.amount))

    def signTransaction(self, signingKey: generate_eth_key):
        if signingKey.public_key.to_hex() != self.fromAddress:
            print("You cannot sign for other wallets!")
        else:
            hashTx = self.calculateHash()
            # self.signature = signingKey.sign(hashTx, 'base64')

    def isValid(self):
        if self.fromAddress == None:
            return True
        
        if self.signature == None or len(self.signature) == 0:
            print('No signature in this transaction')
            return False
        
        # unfinsihed code