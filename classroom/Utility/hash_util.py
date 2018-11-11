import json
import hashlib as HL

def generate_hash(string):
    return HL.sha256(string).hexdigest()

def hash_block(block):
    hashable_block= block.__dict__.copy()
    hashable_block['transactions']= [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    return generate_hash(json.dumps(hashable_block,sort_keys= True).encode())
    