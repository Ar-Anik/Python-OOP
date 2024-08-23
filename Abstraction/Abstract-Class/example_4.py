from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def authorize(self, amount):
        pass

    @abstractmethod
    def capture(self, amount):
        pass

    def void(self):
        if self.is_authorized and not self.is_captured:
            print("Voiding the payment...")
            self.is_authorized = False
            print("Payment voided Successfully.")
        elif self.is_captured:
            print("Payment has already been captured and cannot be voided.")
        else:
            print("Payment can't be voided.")

class CreditCardPayment(PaymentGateway):
    # cvv == Card Verification Value
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.is_authorized = False
        self.is_captured = False

    def authorize(self, amount):
        print(f"Authorizing Credit Card Payment of {amount}")
        self.is_authorized = True
        print("Payment Authorized Successfully")

    def capture(self, amount):
        if self.is_authorized:
            print(f"Capturing Authorized Payment of {amount}")
            self.is_captured = True
            print("Payment Captured Successfully")
        else:
            print("Payment is not authorized")

class PayPalPayment(PaymentGateway):
    def __init__(self, email):
        self.email = email
        self.is_authorized = False
        self.is_captured = False

    def authorize(self, amount):
        print(f"Authorizing PayPal Payment of {amount}")
        self.is_authorized = True
        print("Payment Authorized Successfully.")

    def capture(self, amount):
        if self.is_authorized:
            print(f"Capturing authorized PayPal of {amount}")
            self.is_captured = True
            print("Payment Captured Successfully.")
        else:
            print("Payment is not authorized")

credit_card_payment = CreditCardPayment("1234567890123456", "12/25", "123")
credit_card_payment.authorize(100)
credit_card_payment.capture(100)
credit_card_payment.void()
print(f"{credit_card_payment.is_authorized}---{credit_card_payment.is_captured}")

paypal_payment = PayPalPayment("anik@gmail.com")
paypal_payment.authorize(50)
paypal_payment.capture(50)
paypal_payment.void()
print(f"{paypal_payment.is_authorized}---{paypal_payment.is_captured}")
