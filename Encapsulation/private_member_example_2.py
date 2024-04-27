from datetime import datetime

class Account:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance
        self.__transactions = []

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_transaction_history(self):
        return self.__transactions

    def __record_transaction(self, transaction_type, amount):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date": datetime.now()
        }
        self.__transactions.append(transaction)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__record_transaction("Deposit", amount)
            print(f"Successfully Deposit {amount} at Account {self.__account_number}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__record_transaction("Withdraw", -amount)
            print(f"Successfully Withdraw {amount} at Account {self.__account_number}")

class Bank:
    def __init__(self, bank_name):
        self.__bank_name = bank_name
        self.__accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number not in self.__accounts:
            self.__accounts[account_number] = Account(account_number, initial_balance)
        else:
            print(f"Account {account_number} already exists.")

    def get_account_balance(self, account_number):
        if account_number in self.__accounts:
            return self.__accounts[account_number].get_balance()
        else:
            print(f"Account {account_number} does not exist.")
            return None

    def deposit(self, account_number, amount):
        if account_number in self.__accounts:
            self.__accounts[account_number].deposit(amount)
        else:
            print(f"Account {account_number} does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.__accounts:
            self.__accounts[account_number].withdraw(amount)
        else:
            print(f"Account {account_number} does not exist.")

    def get_transaction_history(self, account_number):
        if account_number in self.__accounts:
            return self.__accounts[account_number].get_transaction_history()
        else:
            print(f"Account {account_number} does not exist.")

bank = Bank("OneBank")
bank.create_account("123456", 1000)
bank.deposit("123456", 500)
bank.withdraw("123456", 200)
print("Account Balance:", bank.get_account_balance("123456"))
print("Transaction History:", bank.get_transaction_history("123456"))
