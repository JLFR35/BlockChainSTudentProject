import uuid
import json
import os


class Wallet:

    def __init__(self):
        self.unique_id = None
        self.balance = 0
        self.history = {}

    def generate_unique_id(self):
        if os.path.isfile(self.unique_id):
            print('file already exist')
        else:
            self.unique_id = str(uuid.uuid4())

    def add_balance(self, value):
        self.balance = self.balance + value

    def sub_balance(self, value):
        self.balance = self.balance - value

    def save(self):
        file = open("content/wallets" + self.unique_id + ".json", "w")
        file.write(json.dumps(self.__dict__))
        file.close()

    def load(self, wallet_uuid):
        file = open("content/wallets" + wallet_uuid + ".json", "r")
        json_file = json.load(file)
        self.unique_id = json_file["unique_id"]
        self.balance = json_file["balance"]
        self.history = json_file["history"]
        file.close()


