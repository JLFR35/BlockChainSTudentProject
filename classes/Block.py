import hashlib
import json


class Block:

    def __init__(self, base_hash, hash, parent_hash):
        self.base_hash = base_hash
        self.hash = hash
        self.parent_hash = parent_hash
        self.transactions = []

    def check_hash(self):
        generated_hash = hashlib.sha256(str(self.base_hash).encode('utf-8')).hexdigest()
        if generated_hash == self.hash:
            return True
        else:
            return False

    def add_transaction(self, receiver_wallet, transmitter_wallet, amount):
        transaction = {"receiver": receiver_wallet, "transmitter": transmitter_wallet, "amount": amount}
        self.transactions.append(transaction)

    def get_weight(self):
        length = len("content/blocs/" + self.hash + ".json")
        print(str(length))

    def save(self):
        file = open("content/blocs" + self.hash + ".json", "w")
        file.write(json.dumps(self.__dict__))
        file.close()

    def load(self, hash):
        file = open("content/blocs" + hash + ".json", "r")
        json_file = json.load(file)
        self.hash = json_file["hash"]
        self.base_hash = json_file["base_hash"]
        self.parent_hash = json_file["parent"]
        self.transactions = json_file["transactions"]
        file.close()
