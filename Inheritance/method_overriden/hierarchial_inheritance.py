class Account:
    def __init__(self, balance):
        self.balance = balance

    def calculateInterest(self):
        return self.balance * 0.01

class SavingsAccount(Account):
    def calculateInterest(self):
        return self.balance * 0.02

class CheckingAccount(Account):
    def calculateInterest(self):
        return self.balance * 0.005

class InvestmentAccount(Account):
    def calculateInterest(self):
        return self.balance * 0.05

savings_account = SavingsAccount(5000)
checking_account = CheckingAccount(5000)
investment_account = InvestmentAccount(5000)

print("Interest For Savings Account : ", savings_account.calculateInterest())
print("Interest For Checking Account : ", checking_account.calculateInterest())
print("Interest For Investment Account : ", investment_account.calculateInterest())

