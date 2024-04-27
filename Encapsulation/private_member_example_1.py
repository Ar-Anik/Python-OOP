class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} units.")
        else:
            print("Invalid Amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw {amount} units.")
        else:
            print("Insufficient Funds or Invalid Amount for withdrawal.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

account = BankAccount("12345", 1000)

# access private attribute by name mangling
print(account._BankAccount__account_number)
print(account._BankAccount__balance)

# Access private attribute by public method
print("Account Number : ", account.get_account_number())
print("Initial Balance : ", account.get_balance())

# Perform transactions
account.deposit(500)
account.withdraw(200)

print("Current Balance : ", account.get_balance())
