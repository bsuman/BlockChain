
from Crypto.PublicKey import RSA
import Crypto.Random 
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import binascii

class Wallet:

    def __init__(self):
        self.private_key = None
        self.public_key = None


    def generate_keys(self):
        private_key = RSA.generate(1024,Crypto.Random.new().read)
        public_key = private_key.publickey()
        return (binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),(binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')))

    def create_keys(self):
        private_key, public_key = self.generate_keys()
        self.private_key = private_key
        self.public_key = public_key

    def save_keys(self):
        if self.public_key != None and self.private_key!= None:
            try:
                with open('myKeys.txt', mode ='w') as f:
                    f.write(self.public_key)
                    f.write('\n')
                    f.write(self.private_key)
            except (IOError, IndexError):
                print('The keys cannot be stored !')


    def load_keys(self):
        try:
            with open('myKeys.txt', mode ='r') as f:
                file_content = f.readlines()   
                self.public_key = file_content[0][:-1]
                self.private_key = file_content[1]

        except (IOError, IndexError):
            print('The keys cannot be found !')

    def sign_transactions(self,sender, recipient, amount):
        signer = PKCS1_v1_5.new(RSA.import_key(binascii.unhexlify(self.private_key)))
        h = SHA256.new((str(sender)+str(recipient)+str(amount)).encode('utf8'))
        signature = signer.sign(h)
        return binascii.hexlify(signature).decode('ascii')

    @staticmethod
    def verify_transaction(transaction):        
        public_key = RSA.import_key(binascii.unhexlify(transaction.sender))
        verifier = PKCS1_v1_5.new(public_key)
        h = SHA256.new((str(transaction.sender)+str(transaction.recipient)+str(transaction.amount)).encode('utf8'))

        return verifier.verify(h,binascii.unhexlify(transaction.signature))