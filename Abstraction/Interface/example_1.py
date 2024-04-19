from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, recipient, message):
        pass

    @abstractmethod
    def send_notifications(self, recipients, messaeg):
        pass

    @abstractmethod
    def send_notification_with_attachment(self, recipient, message, attachment):
        pass

class EmailNotification(NotificationService):
    def send_notification(self, recipient, message):
        print(f"Sending Email to {recipient} with message: {message}")

    def send_notifications(self, recipients, message):
        for recipient in recipients:
            self.send_notification(recipient, message)

    def send_notification_with_attachment(self, recipient, message, attachment):
        print(f"Sending email to {recipient} with message: {message} and attachment: {attachment}")

class SMSNotification(NotificationService):
    def send_notification(self, recipient, message):
        print(f"Sending SMS to {recipient} with message: {message}")

    def send_notifications(self, recipients, message):
        for recipient in recipients:
            self.send_notification(recipient, message)

    def send_notification_with_attachment(self, recipient, message, attachment):
        print(f"Sending SMS to {recipient} with message: {message} and attachment: {attachment}")


email_notifier = EmailNotification()
email_notifier.send_notification("example1@email.com", "Hello, this is an email notification")
email_notifier.send_notifications(["example2@email.com", "example3@email.com"], "Hello, this is a group email notification")
email_notifier.send_notification_with_attachment("example4@email.com", "Hello, this is an email notification with attachment", "attachment.txt")

sms_notifier = SMSNotification()
sms_notifier.send_notification("+1234567890", "Hello, this is an SMS notification!")
sms_notifier.send_notifications(["+1234567891", "+1234567892"], "Hello, this is a group SMS notification!")
sms_notifier.send_notification_with_attachment("+1234567893", "Hello, this is an SMS notification with attachment", "ignored_attachment.txt")