import hashlib

class Block:

    def __init__(self, base_hash, hash, parent_hash, transaction):
        self.base_hash = 0
        self.hash = ''
        self.parent_hash = ''
        self.transactions = {}

    def check_hash(self):
        generated_hash = hashlib.sha256(str(self.base_hash).encode()).hexdigest()
        if generated_hash == self.hash:
            return True
        else:
            return False

    def add_transaction(self, receiver_wallet, transmitter_wallet, amount ):
        transaction = {"receiver":receiver_wallet, "transmitter":transmitter_wallet,"amount":amount}
        self.transactions.update(transaction)

    def get_weight():

    def save():

    def load():


