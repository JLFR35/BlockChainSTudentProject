from classes.Wallet import Wallet


def main():
    print("Hello World!")
    wallet = Wallet()
    wallet.generate_unique_id()
    print(wallet.unique_id)


if __name__ == "__main__":
    main()
