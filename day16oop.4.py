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

account = BankAccount("dharun",10000)       
account.show_balance()
account.deposit(5000)
account.withdraw(2000)
account.show_balance()