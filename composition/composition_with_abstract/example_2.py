from abc import ABC, abstractmethod
import random
from datetime import datetime

class PaymentMethod(ABC):
    def __init__(self):
        self.log = []

    @abstractmethod
    def process_payment(self, amount):
        pass

    def log_transaction(self, amount, success):
        """Log the transaction details"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
        status = "Success" if success else "Failure"
        self.log.append(f"{timestamp} - Amount: ${amount}, Status: {status}")

    def retry_payment(self, amount, retries=2):
        for attempt in range(retries+1):
            print(f"Try to {attempt+1} for amount ${amount}")
            success = self.process_payment(amount)
            self.log_transaction(amount, success)
            if success:
                return True
        print("Payment failed after multiple attempts.")
        return False

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        success = random.choice([True, False])
        if success:
            print(f"Credit card payment of ${amount} processed successfully.")
        else:
            print(f"Credit card payment of ${amount} failed.")

        return success

class PaypalPayment(PaymentMethod):
    def process_payment(self, amount):
        success = random.choice([True, False])
        if success:
            print(f"Paypal payment of ${amount} processed successfully.")
        else:
            print(f"Paypal payment of ${amount} failed.")

        return success

class Order:
    def __init__(self, payment_type, discount=0):
        if payment_type == 'credit':
            self.payment_method = CreditCardPayment()
        elif payment_type == 'paypal':
            self.payment_method = PaypalPayment()
        else:
            raise ValueError("Unsupported Payment Type.")

        self.discount = discount/100.00
        self.amount = 0.0

    def apply_discount(self, amount):
        discount_amount = amount * (1 - self.discount)
        print(f"Applying discount of {self.discount * 100}%. Discount Amount : ${discount_amount}")
        return discount_amount

    def checkout(self, amount):
        print("Initiating Checkout process...")
        self.amount = self.apply_discount(amount)
        success = self.payment_method.retry_payment(self.amount, 5)
        if success:
            self.generate_receipt()
        else:
            print("Transaction failed. Please try again later.")

    def generate_receipt(self):
        """Generate a receipt after successful payment"""
        receipt = f"""
RECEIPT
----------------------------------------------------------------------------------
Payment Method: {self.payment_method.__class__.__name__}
Amount: {self.amount:.2f}
Discount: {self.discount}
Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Status: Paid
----------------------------------------------------------------------------------
        """

        print(receipt)

purchase_1 = Order("credit", discount=10)
purchase_1.checkout(100)

purchase_2 = Order("paypal", discount=20)
purchase_2.checkout(200)
