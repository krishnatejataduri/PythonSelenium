class BankAccount():

    def __init__(self,name,amount):
        self.name = name
        self.amount = amount

    def deposit(self,deposit_amount):
        self.amount+=deposit_amount
        print(f"{deposit_amount}$ deposited to {self.name}'s account.")

    def withdrawal(self,withdrawal_amount):
        if self.amount>=withdrawal_amount:
            self.amount-=withdrawal_amount
            print(f"{withdrawal_amount}$ have been withdrawn from {self.name}'s account.")
        else:
            print("Funds unavailable")

    def __str__(self):
        return f"Account holder: {self.name}\nBalance: {self.amount}"