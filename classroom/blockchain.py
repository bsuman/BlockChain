from functools import reduce
import hashlib as HL
import json
from Utility.hash_util import hash_block, generate_hash
from Utility.validation_helper import Verification
from block import Block
from transaction import Transaction
from wallet import Wallet

MINIG_REWARD= 10

class Blockchain:

        def __init__(self,hosting_node_id):
            genesis_block = Block('0','',[],100,0)
            self.chain =[genesis_block] 
            self.__open_transaction=[]
            self.load_data()
            self.hosting_node=hosting_node_id

        @property
        def chain(self):
            return self.__chain[:]
        
        @chain.setter
        def chain(self,val):
            self.__chain =  val


        def get_opentransactions(self):
            return self.__open_transaction.copy()

        def load_data(self):
            try:
                with open('blockchain.txt', mode = 'r') as f:
                    file_content = f.readlines()   
                    blockchain = json.loads(file_content[0][:-1])
                    updated_blockchain= []
                    for block in blockchain:
                        converted_tx  = [Transaction(tx['sender'],tx['recipient'],tx['signature'],tx['amount']) for tx in block['transactions']]
                        updated_block = Block(block['index'],block['previous_hash'],converted_tx,block['proof'],block['timestamp'])
                        updated_blockchain.append(updated_block)
                    self.chain = updated_blockchain
                    
                    open_transaction =json.loads(file_content[1])
                    updated_transactions = []
                    for tx1 in open_transaction:
                        updated_tx =Transaction(tx1['sender'],tx1['recipient'],tx1['signature'],tx1['amount'])
                        updated_transactions.append(updated_tx)
                    self.__open_transaction = updated_transactions 
            
            except (IOError, IndexError):
                    pass
            finally:
                print('Clean up!')        
        

        def save_data(self):
            try:
                with open('blockchain.txt', mode = 'w') as f:
                    saveable_chain = [block.__dict__ for block in
                    [Block(block_el.index,block_el.previous_hash,
                    [tx.__dict__ for tx in block_el.transactions],
                    block_el.proof,block_el.timestamp) for block_el in self.__chain]]
                    f.write(json.dumps(saveable_chain))
                    f.write('\n')
                    saveable_Tx = [tx.__dict__ for tx in self.__open_transaction]
                    f.write(json.dumps(saveable_Tx))
            except IOError:
                print('Saving blockchain to disk failed!!')

        def proof_of_work(self):
            last_block = self.__chain[-1]
            last_hash = hash_block(last_block)
            proof = 0
            while not Verification.valid_proof(self.__open_transaction,last_hash, proof):
                proof = proof + 1
            return proof

        def get_balance(self):
            participant = self.hosting_node
            tx_sender =[[tx.amount for tx in block.transactions if tx.sender== participant] for block in self.__chain]
            open_sender_tx = [tx.amount for tx in self.__open_transaction if tx.sender== participant]
            tx_sender.append(open_sender_tx)
            total_sent= reduce(lambda x,y:x + sum(y) if len(y) >0 else x+ 0, tx_sender,0)
            
            tx_recipient =[[tx.amount for tx in block.transactions  if tx.recipient== participant] for block in self.__chain]
            total_received= reduce(lambda x,y: x + sum(y) if len(y) >0 else x + 0,tx_recipient,0)
            return total_received - total_sent


        def get_last_blockchainvalue(self):
            """ returns last value of the block chain """
            if len(self.__chain) < 1:
                return None
            return self.__chain[-1]

    
        def mine_block(self):
            if(self.hosting_node == None):
                 return False
            last_block = self.__chain[-1]
            hashed_block = hash_block(last_block)
            work_proof = self.proof_of_work()
            reward_tx = Transaction ('MINING',self.hosting_node,'',MINIG_REWARD)
            copied_transactions = self.__open_transaction[:]
            for tx in copied_transactions:
                if not Wallet.verify_transaction(tx):
                        return False
            copied_transactions.append(reward_tx)
            print(self.__open_transaction)
            block = Block(len(self.__chain),hashed_block,copied_transactions,work_proof)
            self.__chain.append(block)

            self.__open_transaction = []
            self.save_data()
            return True
        

        def add_Tx(self,sender,recipient,signature, amount =1.0):
            """ 
            Arguments: 
                : sender: sender of the coin
                : recipient: recipient of the coin
                : amount: amount of coins sent with transaction ( default = 1.0)

            """
            if(self.hosting_node == None):
                 return False
            transaction = Transaction(sender,recipient,signature,amount)
            if Verification.verify_transaction(transaction,self.get_balance) == True:
                self.__open_transaction.append(transaction)
                self.save_data()
                return True    
            return False 
