from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self._balance = balance

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    def balance(self):
        return self._balance


class SavingAccount(Account):
    def __init__(self, account_number, interest_rate, balance=0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self._balance += amount
        print(f"Successfully Deposit {amount}. Now Current Balance {self._balance}.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Successfully Withdraw {amount}. Now Current Balance {self._balance}.")
        else:
            print(f"Insufficient Balance")

    def apply_interest(self):
        self._balance += (self._balance * (self.interest_rate/100.00))
        print(f"After Add Interest, Now Current Balance {self._balance}.")

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        self._balance += amount
        print(f"Successfully Deposit {amount}. Now Current Balance {self._balance}.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Successfully Withdraw {amount}. Now Current Balance {self._balance}.")
        else:
            print(f"Insufficient Balance")

savings_account = SavingAccount("SA123", 2.5, 1000)
checking_account = CheckingAccount("CA456", 500)

savings_account.deposit(500)
savings_account.withdraw(200)
savings_account.apply_interest()

checking_account.deposit(300)
checking_account.withdraw(100)

print(f"Savings Account Balance: ${savings_account.balance()}")
print(f"Checking Account Balance: ${checking_account.balance()}")
