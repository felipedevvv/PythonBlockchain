from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt

eth_k = generate_eth_key()
sk_hex = eth_k.to_hex()
pk_hex = eth_k.public_key.to_hex()