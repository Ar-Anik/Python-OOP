"""
`import re` in Python to work with regular expressions (regex), which are powerful tools for searching, matching, and manipulating patterns in text.
"""

"""
regex patterns : 
1. Raw String (r'') : The r before the string makes it a raw string, which prevents Python from interpreting backslashes (\) as escape characters. 
For example:
    1. Without r: \w would be interpreted as a tab (\t) or other escape sequence.
    2. With r: \w is treated as a literal regex escape sequence.

2. ^ : The start of the string Matching.

3. [\w\.-]+ : Matches one or more (+) characters that are:
    1. \w: Any word character (letters, digits, or underscore _).
    2. . : A literal dot (.).
    3. - : A hyphen (-).

4. @ : Matches the @ symbol literally, which separates the local part and the domain part in an email.

5. \. : Matches a literal dot (.), separating the domain name from the top-level domain (TLD).

6. \w+ : Matches one or more word characters (\w), which forms the top-level domain (e.g., com, org, net).

7. $ : Matches the end of the string.
"""

import re

class Validator:
    @staticmethod
    def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(pattern, email):
            raise ValueError(f"Invalid email format: {email}")

        return True

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

        """
            The any() function in Python is used to check if any element in an iterable (such as a list, tuple, or set) is True. 
            If at least one element evaluates to True, the function returns True; otherwise, it returns False.
        """
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one number.")

        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter.")

        return True

class User:
    def __init__(self, name, email, password, validator):
        self.name = name
        self.validator = validator

        if self.validator.validate_email(email):
            self.email = email
        if self.validator.validate_password(password):
            self.password = password

    def __repr__(self):
        return f"User(name=`{self.name}`, email=`{self.email}`"

try:
    validator = Validator()
    user = User("Ar Anik", "anik13331@gmail.com", "Password123", validator)
    print(user)
except ValueError as e:
    print(f"Validation Error : {e}")

