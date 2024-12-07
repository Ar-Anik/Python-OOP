from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def has_sufficient_balance(self, amount):
        pass

    @abstractmethod
    def process_payment(self, amount, transaction_type):
        pass

    @abstractmethod
    def get_details(self):
        pass


class CreditCard(PaymentMethod):
    def __init__(self, card_number, card_holder, balance):
        self.card_number = card_number
        self.card_holder = card_holder
        self.balance = balance

    def has_sufficient_balance(self, amount):
        return self.balance >= amount

    def process_payment(self, amount, transaction_type):
        if transaction_type == 'debit':
            if not self.has_sufficient_balance(amount):
                return "Transaction Failed: Insufficient Funds on Credit Card."
            self.balance -= amount
            return f"Debit ${amount:.2f} from Credit Card. Remaining Balance: ${self.balance:.2f}"

        elif transaction_type == 'credit':
            self.balance += amount
            return f"Credited ${amount:.2f} to Credit Card. Updated Balance: ${self.balance:.2f}"

        return "Invalid transaction type. Use 'debit' or 'credit'."

    def get_details(self):
        return f"Credit Card - Holder: {self.card_holder}, Number: **** **** **** {self.card_number[-4:]}, Balance: ${self.balance:.2f}"


class Paypal(PaymentMethod):
    def __init__(self, email, balance):
        self.email = email
        self.balance = balance

    def has_sufficient_balance(self, amount):
        return self.balance >= amount

    def process_payment(self, amount, transaction_type):
        if transaction_type == 'debit':
            if not self.has_sufficient_balance(amount):
                return "Transaction failed: Insufficient funds in PayPal account."
            self.balance -= amount
            return f"Debited ${amount:.2f} from Paypal. Remaining Balance: ${self.balance}"

        elif transaction_type == 'credit':
            self.balance += amount
            return f"Credited ${amount:.2f} to Paypal. Updated Balance: ${self.balance:.2f}"

        return "Invalid transaction type. Use 'debit' or 'credit'."

    def get_details(self):
        return f"Paypal - Email: {self.email}, Balance: ${self.balance:.2f}"


class PaymentProcessor:
    def __init__(self):
        self.payment_methods = {}

    def add_payment_method(self, method_name, method):
        self.payment_methods[method_name] = method

    def list_payment_methods(self):
        for name, method in self.payment_methods.items():
            print(method.get_details())

    def process_payment(self, method_name, amount, transaction_type):
        method = self.payment_methods.get(method_name)
        if not method:
            return f"Error: Payement method `{method_name}` not found."
        return method.process_payment(amount, transaction_type)

processor = PaymentProcessor()

processor.add_payment_method("CreditCard", CreditCard("1234567891122334", "Ar Anik", 500.00))
processor.add_payment_method("Paypal", Paypal("anik13331@gmail.com", 200.00))

print("Available Payment Methods:")
processor.list_payment_methods()

print("\nAttempting a transaction...")
print(processor.process_payment("Paypal", 150.00, "debit"))

print("\nAttempting a refund...")
print(processor.process_payment("CreditCard", 50.00, "credit"))

print("\nInsufficient funds example:")
print(processor.process_payment("Paypal", 100.00, "debit"))
