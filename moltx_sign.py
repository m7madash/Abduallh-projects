import eth_account
from eth_account.messages import encode_typed_data
import json
import requests
import sys

def sign_moltx_challenge(private_key, nonce, address):
    domain_data = {
        "name": "MoltX",
        "version": "1",
        "chainId": 8453,
        "verifyingContract": "0x0000000000000000000000000000000000000000"
    }
    
    types = {
        "Challenge": [
            {"name": "address", "type": "address"},
            {"name": "nonce", "type": "string"}
        ]
    }
    
    message = {
        "address": address,
        "nonce": nonce
    }
    
    signable_message = encode_typed_data(domain_data=domain_data, message_types=types, message_data=message)
    signed_message = eth_account.Account.sign_message(signable_message, private_key=private_key)
    return signed_message.signature.hex()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 sign.py <private_key> <nonce> <address>")
        sys.exit(1)
    
    pk = sys.argv[1]
    nonce = sys.argv[2]
    addr = sys.argv[3]
    
    sig = sign_moltx_challenge(pk, nonce, addr)
    print(sig)
