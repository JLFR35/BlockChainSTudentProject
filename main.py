from classes.Chain import Chain
from classes.Wallet import Wallet
from classes.Block import Block
#from classes.Chain import Chain


def main():
    # test main
    print("Hello World!")

    # test creation objet wallet
    # wallet0 = Wallet()
    # wallet0.generate_unique_id()
    # wallet0.save()
    # print(wallet0.unique_id)
    # wallet0.balance = 200

    # test methode load()
    wallet = Wallet()
    wallet.load("a7afe60a-a194-4e3a-855f-0a557e8de665")
    print(wallet.unique_id)

    # test bloc generate_hash to implement !!!
    # bloc = Block()
    # bloc.load()
    # print(bloc.get_weight)

    #test verify_hash
    chain = Chain()
    chain.add_block()
    print(chain)


if __name__ == "__main__":
    main()
