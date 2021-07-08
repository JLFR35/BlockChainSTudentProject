from classes.Wallet import Wallet


def main():
    print("Hello World!")
    #wallet = Wallet()
    #wallet.generate_unique_id()
    #wallet.save()
    #print(wallet.unique_id)
    wallet = Wallet()
    wallet.load("a7afe60a-a194-4e3a-855f-0a557e8de665")
    print(wallet.unique_id)


if __name__ == "__main__":
    main()
