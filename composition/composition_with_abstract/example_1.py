"""
Composition is a design principle where a class is composed of one or more objects of other classes, creating a "has-a" relationship.
When combined with abstract base classes, it provides a powerful way to create flexible and extensible code structures.
"""

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message, recipient):
        """send a notification with a message to the recipient."""
        pass


class EmailNotification(Notification):
    def send(self, message, recipient):
        print(f"Sending Email to {recipient}: {message}")


class SMSNotification(Notification):
    def send(self, message, recipient):
        print(f"Sending SMS to {recipient}: {message}")


class NotificationService:
    def __init__(self, channel):
        if channel == 'email':
            self.notification = EmailNotification()
        elif channel == 'sms':
            self.notification = SMSNotification()
        else:
            self.ValueError("Unsupported Notification Channel.")

    def notify(self, message, recipient):
        self.notification.send(message, recipient)

email_service = NotificationService('email')
email_service.notify('Your order has been shipped.', 'anik13331@gmail.com')

sms_service = NotificationService('sms')
email_service.notify('Your order is out for delivery', '+01675946475')


"""
This approach provides flexibility and reusability by separating the notify behavior from the NotificationService itself. The NotificationService can change its behavior at runtime, 
and channel change without modifying existing NotificationService code.
"""