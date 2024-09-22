def fetch_wallets():
    with open("data/wallets.txt", "r") as file:
        wallets = file.readlines()
        wallets = map(lambda x: x.strip(), wallets)
        wallets = filter(lambda x: x != "", wallets)
        return wallets
