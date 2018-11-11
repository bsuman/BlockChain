from Utility.validation_helper import Verification
from blockchain import Blockchain
from uuid import uuid4
from wallet import Wallet

class Node:

    def __init__(self):
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)
        
        """Function to get user input  """
    def get_user_tx(self):
        """ gets the transaction value for the block"""
        tx_recipient = input('Please enter Tx recipient: ')
        tx_amount =  float(input('Please enter Tx amount: '))
        return (tx_recipient,tx_amount) 

    def get_user_choice(self):
        return input('Choice: ')

                
    def print_blockchain(self):
        for element in self.blockchain.chain:
            print('outputing block')
            print(element)
        

    def listen_for_input(self):
        waiting_for_input = True    
        while waiting_for_input:
            print('Please choose the action to perform')
            print('1: Enter 1 for adding the block')
            print('2: Mine a block')
            print('3: Enter 3 for printing the block')
            print('4: Validate transactions')
            print('5: Create Wallet')
            print('6: Load Wallet')
            print('7: Save Wallet')
            print('q: Enter Q to quit')
            user_choice=self.get_user_choice()
            
            if user_choice =='1':
                tx_data= self.get_user_tx()
                recipient, amount= tx_data 
                signature = self.wallet.sign_transactions(self.wallet.public_key,recipient,amount)
                if self.blockchain.add_Tx(self.wallet.public_key,recipient,signature,amount=amount)== True:    
                    print('Transaction added correctly!')
                else:
                    print('Transaction added failed! or got no Wallet?')
                print(self.blockchain.get_opentransactions())
            elif user_choice =='2':
                if not self.blockchain.mine_block():
                    print('Mining failed. Got no Wallet?')
            elif user_choice =='3':
                self.print_blockchain()
            elif user_choice =='4':
                if Verification.verify_transactions( self.blockchain.get_opentransactions(), self.blockchain.get_balance):
                    print('All valid transactions')
                else:
                    print('One or more transaction invalid ')
            elif user_choice =='5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice =='6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice =='7':
                self.wallet.save_keys()
            elif user_choice =='q':
                waiting_for_input = False
            else:
                print('You entered invalid input, please enter input from given options!')

            
            print('The Balance of sender {} is {}.'.format(self.wallet.public_key,self.blockchain.get_balance()))
            if not Verification.verfiy_chain(self.blockchain.chain):
                print('Block chain invalid!') 
                break

        else:
            print('User left!')

        print('Done!')


if __name__ == '__main__' :
    node = Node()
    node.listen_for_input()
