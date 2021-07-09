import hashlib
import os

class Chain:

    def __init__(self):
        self.blocks = []
        self.last_transaction_number = 0

    def generate_hash(self, bloc_hashed=None):
        number = 0
        hash = hashlib.sha256("number".encode()).hexdigest()
        while self.verify_hash(bloc_hashed):
            number += 1
            block_hash = self.blocks


    @staticmethod
    def verify_hash(bloc_hashed) -> bool :
        hash = os.path.isfile("content/blocs/" + bloc_hashed + "json")
        if bloc_hashed[:4] != "0000" and hash:
            return False
        else:
            return True

    def add_block(self):

    def get_block(self):

    def add_transaction(self):
