import uuid


class Wallet:
    unique_id = ''

    def generate_unique_id(self,unique_id=None):
        return unique_id = uuid.uuid()