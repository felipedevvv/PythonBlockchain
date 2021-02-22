import json


class Transaction:
    def __init__(self, fromAddress, toAddress, amount):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount
    
    def __str__(self):
        return json.dumps(
            {
                'fromAddress' : self.fromAddress,
                'toAddress' : self.toAddress,
                'amount' : self.amount
            },
            indent = 4
        )