from Transaction import Transaction
from Block import Block
from Blockchain import Blockchain


xxuegooCoin = Blockchain()
xxuegooCoin.createTransaction(Transaction('address1', 'address2', 100))
xxuegooCoin.createTransaction(Transaction('address2', 'address1', 50))

print('\nStarting the miner...')
xxuegooCoin.minePendingTransactions('xxuegoos-address')

print('\nBalance of xxuegoo is: {}'.format(xxuegooCoin.getBalanceOfAddress('xxuegoos-address')))

print('\nStarting the miner again...')
xxuegooCoin.minePendingTransactions('xxuegoos-address')

print('\nBalance of xxuegoo is: {}'.format(xxuegooCoin.getBalanceOfAddress('xxuegoos-address')))
