# Banking System

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}, Current Balance: {self.balance}")
        else:
            print("Insufficient Funds")

class SavingAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100.00)
        self.balance += interest_amount
        print(f"Added Interest. Current Balance: {self.balance}")

class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    # overrding method
    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdraw {amount}. Current Balance: {self.balance}")
        else:
            print("Exceeds Overdraft Limit")

savings_acc = SavingAccount("SA123", 1000, 5)
savings_acc.deposite(500)
savings_acc.add_interest()
savings_acc.withdraw(200)

checking_acc = CheckingAccount("CA456", 2000, 1000)
checking_acc.deposite(300)
checking_acc.withdraw(2500)
