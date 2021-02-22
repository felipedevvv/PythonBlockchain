from Block import Block
from Blockchain import Blockchain


xxuegooCoin = Blockchain()

print('Mining block 1...')
xxuegooCoin.addBlock(Block(1, '02/01/2021', { 'amount': 4} ))
print('Mining block 2...')
xxuegooCoin.addBlock(Block(2, '02/01/2021', { 'amount': 7} ))

# print('Is blockchain valid? {}'.format(xxuegooCoin.isChainValid()))
# print(xxuegooCoin)
# xxuegooCoin.chain[1].data = { 'amount' : 100 }
# xxuegooCoin.chain[1].hash = xxuegooCoin.chain[1].calculateHash()
# print('Is blockchain valid? {}'.format(xxuegooCoin.isChainValid()))