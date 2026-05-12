class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited! Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance-= amount
            print(f"{amount} withdrawn! Balance: {self.__balance}")
        else:
            print("Insufficient funds!")
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Dharun", 10000)
account.deposit(5000)
account.withdraw(2000)
print(account.get_balance())
 