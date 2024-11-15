"""
A mixin class is a type of class in Python that’s used to add specific functionality to other classes, without being a core part of their main behavior.
Think of it as a "helper" that gives extra abilities to other classes without making them fundamentally different.

# Key Characteristics of Mixin Classes
1. Single Responsibility: A mixin usually has one clear, specific responsibility (such as adding logging, access control, or a utility function).
2. No Instantiation: Mixins are generally not instantiated on their own. They’re used as "helper" classes to be inherited by other classes.
3. Modular and Reusable: Since they add only specific functionality, they’re modular and can be reused across multiple classes without coupling deeply.
4. Multiple Inheritance: Mixins rely on Python's support for multiple inheritance. When mixed into other classes, they become part of the class hierarchy,
   adding their methods and properties.
"""

class LoggingMixin:
    def log(self, message):
        print(f"[Log] : {message}")

class EmailNotification(LoggingMixin):
    def send(self, recipient, subject):
        self.log(f"Email sent to {recipient} with subject `{subject}`")

class SMSNotification(LoggingMixin):
    def send(self, phone_number, message):
        self.log(f"SMS sent to {phone_number} with message `{message}`")

email_notification = EmailNotification()
email_notification.send("anik@gmail.com", "Thank you for everything.")

sms_notification = SMSNotification()
sms_notification.send('01654372829', "Your varification code is 223344")


"""
# When to Use Mixins
1. Avoid Code Duplication: When we need to add the same functionality to multiple classes without duplicating code.
2. Flexible and Modular Design: When designing a class that could benefit from additional optional behaviors that don’t fit a strict inheritance model.
"""

"""
# Rules for Designing a Mixin
1. Do not use __init__ unless necessary: Mixins shouldn't assume other classes will call their __init__ method. If initialization is needed, document it carefully.
2. Single Responsibility Principle: A mixin should ideally focus on one area, keeping functionality simple and specific.
3. Do not define state: Mixins should avoid defining attributes that would introduce dependencies or assumptions about the classes that use them.

---> Using mixin classes keeps our code DRY (Don't Repeat Yourself) and allows for modular functionality.
"""
