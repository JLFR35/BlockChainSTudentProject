import hashlib
import os

from classes.Block import Block


class Chain:

    def __init__(self):
        self.blocks = []
        self.last_transaction_number = 0
        self.hash = hash
        self.first_bloc = "00"
        self.parent_bloc = "00"

    # à refaire
    def generate_hash(self):
        number = 0
        bloc_hashed = self.generate_string(number)
        while not self.verify_hash(bloc_hashed):
            number += 1
            bloc_hashed = self.generate_string(number)
            self.hash = self.blocks

    @staticmethod
    def generate_string(number):
        return hashlib.sha256(f'{number}'.encode()).hexdigest()

    @staticmethod
    def verify_hash(bloc_hashed) -> bool :
        hash = os.path.isfile("content/blocs/" + bloc_hashed + "json")
        if bloc_hashed[:4] != "0000" and hash:
            return False
        else:
            return True

    def add_block(self):
        self.generate_hash()
        block = Block(self.first_bloc, self.parent_bloc, [])
        self.blocks.append(block)
        block.save()

    def get_block(self, v):
        for k in self.blocks:
            if k["hash"] == v:
                return k

    @staticmethod
    def add_transaction():
        Chain.add_transaction()

    # A finir
    # def transaction_is_valid(self):