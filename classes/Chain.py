import hashlib
import os

from classes.Block import Block


class Chain:

    def __init__(self):
        self.blocks = []
        self.last_transaction_number = 0
        self.hash = hash

    # à refaire
    # def generate_hash(self, bloc_hashed):
    #     number = 0
    #     hash = hashlib.sha256("number".encode()).hexdigest()
    #     while not self.verify_hash(bloc_hashed):
    #         number += 1
    #         block_hashed = self.blocks

    def block_to_hash(self,number):
        return hashlib.sha256(number.encode().hexdegiest())

    @staticmethod
    def verify_hash(bloc_hashed) -> bool :
        hash = os.path.isfile("content/blocs/" + bloc_hashed + "json")
        if bloc_hashed[:4] != "0000" and hash:
            return False
        else:
            return True

    def add_block(self):
        self.generate_hash()
        block = Block()
        self.blocks.append(block)
        block.save()

    def get_block(self, v):
        for k in self.blocks:
            if k["hash"] == v:
                return k

    def add_transaction(self):
