class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Vloženo {amount} kč. Nový zůstatek: {self.balance} kč ")
        else:
            print("Nelze vložit zápornou částku.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Vybráno {amount} kč. Nový zůstatek: {self.balance} kč")
        elif amount > self.balance:
            print("Nedostatečný zůstatek.")
        else:
            print("Nelze vybrat zápornou částkou.")

    def print(self):
        print(f"Vlastník: {self.owner}.")
        print(f"Zůstatek: {self.balance} kč.")
    
muj_ucet = BankAccount('Jan Novák', 1000)
muj_ucet.deposit(10000)
muj_ucet.withdraw(500)
muj_ucet.print()