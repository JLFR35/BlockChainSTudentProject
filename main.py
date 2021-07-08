from classes.Wallet import Wallet


def main():
    print("Hello World!")
    wallet = Wallet()
    wallet.generate_unique_id()
    wallet.save()
    print(wallet.unique_id)
    wallet.load()


if __name__ == "__main__":
    main()
