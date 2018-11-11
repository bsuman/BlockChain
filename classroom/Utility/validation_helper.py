""" Adds verification helper functions"""

from wallet import Wallet
from Utility.hash_util import generate_hash, hash_block

class Verification:
    @staticmethod
    def valid_proof(transactions, last_hash, proof_num):
        guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) +str(proof_num)).encode()   
        guess_hash = generate_hash(guess)
        return guess_hash[0:2] == '00'

    @staticmethod
    def verify_transaction(transaction,get_balance, check_funds =True):
        if check_funds:
            sender_balance = get_balance()
            return sender_balance >= transaction.amount and Wallet.verify_transaction(transaction)
        else:
            return Wallet.verify_transaction(transaction)

    @classmethod
    def verify_transactions(cls,open_transaction,get_balance):
        return (all([Verification.verify_transaction(tx,get_balance,False) for tx in open_transaction]))

    @classmethod
    def verfiy_chain(cls,blockchain):
        is_valid= True
        for (index,block) in enumerate(blockchain):
            if index == 0:
                continue
            if block.previous_hash != hash_block(blockchain[index -1]):
                return False
            if not Verification.valid_proof(block.transactions[:-1],block.previous_hash, block.proof):
                return False  

        return is_valid