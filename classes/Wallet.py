import uuid
import json


class Wallet:

    def __init__(self):
        self.unique_id = None
        self.balance = 0
        self.history = {}

    def generate_unique_id(self):
        if self.unique_id is None:
            self.unique_id = str(uuid.uuid4())

    def add_balance(self, value):
        self.balance = self.balance + value

    def sub_balance(self, value):
        self.balance = self.balance - value

    def save(self):
        file = open("content/wallets" + self.unique_id + ".json", "a")
        file.write(json.dumps(self.__dict__))
        file.close()

    def load(self):
        file = open("content/wallets" + self.unique_id + ".json", "r")
        json_file = json.load(file)
        self.unique_id = json_file["unique_id"]
        self.balance = json_file["balance"]
        self.history = json_file["history"]


