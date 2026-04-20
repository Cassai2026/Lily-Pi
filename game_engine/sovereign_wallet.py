class SovereignWallet:
    def __init__(self, owner="Node_29_Mentee"):
        self.balance = 0.0
        self.owner = owner

    def add_credit(self, amount):
        self.balance += amount
        print(f"[HUD] 💰 WALLET UPDATED: +{amount} VT. New Balance: {self.balance} VT")

if __name__ == "__main__":
    wallet = SovereignWallet()
    wallet.add_credit(15.0)
