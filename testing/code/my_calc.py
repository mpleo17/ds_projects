# What is unit testing - Unit testing is a set of code written to test a unit, which may be a function,
# or a method or a piece of a code that we refer to as a unit. It is a good way to test if our code
# functions as expected.

# Assert statement generates an AssertionError when it is true.

# We have unittest module - This module is a good framework for testing. We have a base class named TestCase,
# that can be inherited to write Test cases. Each case is called a test case and ends with an assert statment.
# Common examples are assertEqual - to compare two values for equality, assertTrue - to compare a value with
# True, assertFalse, etc. Need to look at documentation to find all statements. There also exists assertRaises
# that need to be dealed with a context manager for the function to be called. This special syntax is to
# prevent the exception/error to be raised when the instance is called.

# basic calculator example done! Now run the testcases!!
# the syntax is python -m unittest module.class.testcase

# if there is a need to skip any test use the decorator syntax @unittest.skip("reason for skipping")
# if there is an expectation of any faiilure then the decorator syntax @unittest.expectedFailure
# view those cases in the output upon running the tests

# setUp and tearDown methods - gets run each time for an individual test case
# setUpClass and tearDown Class methods - run once upon running the test

# mocking - mocking as the name suggests is used to mock or substitute a part of the code usually
# external dependencies like database calls, API calls, hardware devices etc.
# This helps ensure speed - API calls are time consuming, isolation, control and simplicity
# unittest.mock module helps with mocking!!!

import requests

class Calculations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b

    def get_diff(self):
        return self.a - self.b

    def get_product(self):
        return self.a * self.b

    def get_quotient(self):
        if self.b ==0:
            raise ValueError('Denominator cannot be zero!')
        return self.a / self.b

class Employee:
    raise_factor = 0.04

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def email(self):
        return r'{}@eexample.com'.format(self.name)

    def raise_amt(self):
        return self.salary * self.raise_factor

    def monthly_schedule(self, month):
        response = requests.get('http:/example.com/{}/{}'.format(self.name, month))
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'