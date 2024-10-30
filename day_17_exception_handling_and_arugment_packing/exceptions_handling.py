#Day 17: Exception Handling
#10/22/2024

'''
In Python, exceptions are events that occur during the execution of a program that disrupt its normal flow. Exception handling allows you to respond to these events gracefully, ensuring that your program can handle errors without crashing unexpectedly.

Key Concepts:
- Exception: An error that occurs during execution. Examples include ZeroDivisionError, FileNotFoundError, TypeError, etc.
- Handling Exceptions: Catching and responding to errors in a controlled manner
- Raising Exceptions: Manually triggering exceptions to indicate an error condition
'''

#The try-except Block
'''
The try block lets you a block of code for errors, while the except block lets you handle the error.
Catching Multiple Exceptions
You can catch multiple types of exceptions by using multiple except blocks or by grouping them


Syntax
try:
    # code that might raise an exception
except SomeException as e:
    #code to handle the exception
'''

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a valid number.")

'''
If the user inputs 0, a ZeroDivisionError will occur
if the input is non-numeric, a ValueError will occur
'''

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")

#The else Clause
'''
The else block will run if no exception occurs in the try block
If no exception is raised, the else block executes

Syntax
try:
    # Code that might raise an exception
except SomeException:
    # Code to handle the exception
else:
    # Code that runs if no exception occurs
'''

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("The result is:", result)


# The finally Block
'''
The finally block will always execute, whether an exception occurs or not. it's typically used for cleanup actions like closing files or databases connections.

Syntax
try:
    # Code that might raise an exception
except SomeException:
    # Code to handle the exception
finally:
    # Code that always runs (cleanup, etc.)

Even if an exception occurs, the finally block executes
'''

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This will run no matter what.")

# Raising Exceptions
'''
You can raise exceptions manually using the raise keyword. This is useful for custom handling or when certain conditions should result in an exception.

This raises a ValueError if a negative age is passed

Syntax
raise SomeException("Error message")
'''
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        print("Age is valid")

try:
    check_age(-5)
except ValueError as e:
    print(e)

#Custom Exceptions
''' 
You can create own exception classes by subclassing the built-in Exception class.

Syntax
class MyCustomError(Exception):
    pass
'''

class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError(num)
except NegativeNumberError as e:
    print(f"Error: {e.value} is not a positive number.")

# Best Practices for Exception Handling
'''
- Use specific exceptions: Catch specific exceptions rather than catching all exceptions with a generic except block
- Handle exceptions minimally: Only catch exceptions that you can handle or log. Don't suppress errors unnecessarily/
-  Use finally for cleanup: Always release resources such as file handles, database connections, etc., in a finally block
'''

# Summary of Key Python Exceptions
'''
Here’s a brief overview of some common exceptions you might encounter:

ZeroDivisionError: Raised when dividing by zero.
ValueError: Raised when a function gets an argument of the right type but inappropriate value.
TypeError: Raised when an operation is applied to an object of inappropriate type.
IndexError: Raised when accessing an out-of-range index in a list.
KeyError: Raised when accessing a non-existent key in a dictionary.
FileNotFoundError: Raised when trying to access a file that does not exist.
AttributeError: Raised when an invalid attribute is accessed on an object.
ModuleNotFoundError: Raised when a module import fails.
'''