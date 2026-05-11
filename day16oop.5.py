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
class SavingsAccount(BankAccount):  
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance) 
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest {interest} added! Balance: {self.balance}")
savings = SavingsAccount("Dharun", 10000, 4)
savings.show_balance()
savings.add_interest()
savings.show_balance()        