"""
A unit test is a type of software testing that focuses on testing individual units or components of a software application in isolation.
A unit is the smallest testable part of an application, such as a single function, method, or class.

The primary purpose of unit testing is to ensure that each unit of the software performs as expected. Unit tests are typically written by
developers during or after the development of a piece of code to verify its correctness.
"""

"""
--> Key Characteristics of Unit Tests:
1. Small Scope:
    1. They focus on testing a single function, method, or class.
    2. They are narrow and specific, ensuring that the unit works as intended.

2. Isolated:
    1. They test the unit independently of other parts of the application.
    2. Mocking or stubbing is often used to replace dependencies (e.g., databases, APIs).

3. Fast and Repeatable:
    1. They execute quickly and can be run multiple times without significant overhead.
    2. They are part of continuous integration pipelines to catch regressions.

4. Automated:
    1. They are automated tests written in code and integrated into the development process.

"""

"""
--> Benefits of Unit Testing:
    1. Error Detection: Detect bugs early in the development cycle.
    2. Code Quality: Encourage writing modular, reusable, and maintainable code.
    3. Refactoring Safety: Ensure that changes in the code do not break functionality.
    4. Documentation: Serve as documentation for the expected behavior of code.
"""

""" Python's built-in unittest module to test a function that calculates the square of a number. """

from test_code import square
import unittest

class TestSquareFunction(unittest.TestCase):
    def test_square_positve_number(self):
        self.assertEqual(square(5), 25)

    def test_square_negative_number(self):
        self.assertEqual(square(-4), 16)

    def test_squre_zero(self):
        self.assertEqual(square(0), 0)

if __name__ == "__main__":
    unittest.main()                 # Run this code by command : python -m unittest introduction.py

"""
When we run a Python file containing unit tests, unittest.main() is responsible for discovering and running the test cases.

Q : How unittest.main() Works ?
1. Discovery of Test Cases:
    1. The unittest framework scans the file for any classes that inherit from unittest.TestCase.
    2. These classes (like TestSquareFunction in this example) are considered test case containers.

2. Collecting Test Methods:
    1. Within the discovered classes, unittest looks for methods whose names start with test_.
    2. These methods are treated as individual test cases.

3. Execution:
    1. unittest.main() automatically executes all the test methods it discovers in the unittest.TestCase subclasses.
"""

"""
Q : Why is the Class Not Explicitly Called?

1. The unittest framework dynamically instantiates the TestSquareFunction class for each test method. Here's what happens behind the scenes:
    test_case = TestSquareFunction('test_square_positive_number')
    test_case.run()
This process is handled internally by the unittest framework.

2. Separation of Methods: Each test method (test_square_positive_number, etc.) is treated as an independent unit, so the framework creates a new 
instance of TestSquareFunction for each one. This ensures that the tests are isolated and do not share state.
"""

"""
Best Practices:
    1. Test one thing at a time in each unit test.
    2. Write tests for edge cases and normal scenarios.
    3. Keep tests isolated; avoid dependencies on external systems.
    4. Run unit tests frequently to catch issues early.
"""

"""
Tools for Unit Testing in Python: unittest, pytest, nose
"""
