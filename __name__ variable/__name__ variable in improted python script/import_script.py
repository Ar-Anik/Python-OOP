"""
when python import a script as module and when executes function from imported script, the __name__ value of the imported script will be script name.
suppose,
in main_script import import_script as module, in netdown function we call greet function of import_script this time import_script __name__
value will be __name__ == 'import_script'.
"""

def greet():
    return "Hello, world"

if __name__ == "__main__":
    print("This script is being run directly")
    print(greet())
else:
    print("Name : ", __name__)
    print("This script has been imported as a module.")