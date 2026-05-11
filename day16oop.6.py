class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited! Balance: {self.balance}")
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} withdrawn! Balance: {self.balance}")
    
    def show_balance(self):
        print(f"{self.owner}'s Balance: {self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            print(f"{amount} withdrawn! Balance: {self.balance}")
        else:
            print("Overdraft limit exceeded!")

current = CurrentAccount("Appa", 1000, 5000)
current.show_balance()
current.withdraw(4000)
current.withdraw(3000)