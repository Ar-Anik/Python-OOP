class EmailNotificationMixin:
    @staticmethod
    def send_email(sender, receiver, subject, body):
        email_str = f"""
Email
-------------------------------------------------
From : {sender}
To : {receiver}
Subject : {subject}
body: {body}
-------------------------------------------------   
        """
        print(email_str)
        return True

class SMSNotificationMixin:
    @staticmethod
    def send_sms(sender, receiver, message):
        sms_str = f"""
SMS
-------------------------------------------------
Sender : {sender}
Receiver : {receiver}
Message : {message}
-------------------------------------------------
        """
        print(sms_str)
        return True

class NotificationSender:
    def __init__(self):
        self.email_sender = EmailNotificationMixin()
        self.sms_sender = SMSNotificationMixin()

    def send_notification(self, method, **kwargs):
        if method == 'email':
            sender = kwargs.get('sender')
            receiver = kwargs.get('receiver')
            subject = kwargs.get('subject', 'No Subject')
            body = kwargs.get('body', 'No Body')
            return self.email_sender.send_email(sender, receiver, subject, body)

        elif method == 'sms':
            sender = kwargs.get('sender')
            receiver = kwargs.get('receiver')
            message = kwargs.get('message')
            return self.sms_sender.send_sms(sender, receiver,message)

        else:
            print(f"Notification method `{method}` is not supported.")
            return False

notifier = NotificationSender()

notifier.send_notification(
    method='email',
    sender='anik@gmail.com',
    receiver='oni@gmail.com',
    subject='Welcome',
    body='Thank you for singing up'
)

notifier.send_notification(
    method='sms',
    sender='+8801685946475',
    receiver='+8801312244544',
    message='Your OTP is 66543'
)

notifier.send_notification(
    method='push',
    sender='user'
)
