import uuid
import json


class Wallet:
    unique_id = ''
    balance = 0
    history = {}

    def generate_unique_id(self):
        self.unique_id = str(uuid.uuid1())

    def add_balance(self, value):
        self.balance = self.balance + value

    def sub_balance(self, value):
        self.balance = self.balance - value

    def save(self):
        file = open("content/wallets/" + self.unique_id + ".json", "a")
        file.write(json.dumps(self.__dict__))
        file.close()
