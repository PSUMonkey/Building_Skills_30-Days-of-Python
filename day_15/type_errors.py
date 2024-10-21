#Day 15: Type Errors
#10/21/2024

# Syntax Error
'''
SyntaxError in python occur when the code violates the language's grammar rules, making it impossible for the interpreter to parse or execute it. These errors are typically detected during the parsing stage and prevent the code from running.

Common causes of syntax errors in Python include:

1. Missing Colons
2. Indentation Errors
3. Mitchmatched Parentheses, brackets, or braces
4. Incorrect use of keywords or reserved words
5. Missing or extra quotation marks
6. Misplaced or missing commas
7. Invalid function definitions
'''

#Name Error
'''
A NameError in Python occurs when you try to use a variable, function, or object that hasn't been defined or is not accessible within the current scope. This happens when the interpreter encounters a name that is not yet recognized.

Common causes of Name errors in Python include:

1. Using a variable before its defined
2. Misspelled variable or function names
3. Calling a function that hasn't been defined
4. Out of scope variables
5. Unimported module or object
'''

#Index Error
'''
An IndexError in Python occur when you try to access an element from a list, tuple, or other sequence types using an index that is out of the valid range. In other words, your're trying to access an element that doesn't exist at the specified position. 

Common causes of an Index Errors include:

1. Accessing an index that is too high
2. Negative indexing beyond the start of the sequence
3. Empty lists or sequences
4. Using an index in a loop that exceeds the sequence length
'''

#ModuleNotFound Error
'''
A ModuleNotFoundError in Python occurs when you attempt to import a module that cannot be found by the Python interpreter. This error is raised when the module your're trying to load does not exist or isn't installed in your environment.

Common causes of an ModuleNotFound Error included:

1. Module not installed
2. Typo in the module name
3. Module in a different directory
4. Virtual Environment issues
5. Missing init.py in package directories
'''

#AttributeError
'''
An AttributeError in Python occurs when you try to access an attribute or method that doesn't exist for a particular object or when the object is of a type that doesn't support the requested attribute. This usually happens if the object does not have the property or method you're trying to use, or if you misrefereneced it. 

Common causes of an Attribute Error include:

1. Accessing a non-existent method or attribute
2. Misnaming or misspelling a method or attribute
3. NoneType object has no attribute
4. Incorrect use of a method on the wrong type of object
5. Incorrect class hierarchy
'''

#KeyError
'''
A KeyError in Python occurs when you try to access a key in a dictionary (or other mapping types) that doesn't exist. This is similar to an IndexError in lists, but with keys instead of indexes.

Common causes of an Key Error include:


1. Accessing a non-existent key in a dictionary
2. Incorrect use of dictionary methods
3. Key misspelling
4. Accessing deleted keys
5. Incorrectly using nested dictionaries
'''

#TypeError
'''
A TypeError in python occurs when a operation or function is applied to an object of inappropriate type. This error is typically raised when Python encounters an invalid type for a particular operation or when the number of arguments passed to a function is incorrect.

Common causes of a TypeError include:

1. Performing operation on incompatible types
2. Calling a function with the wrong number of arguments
3. Using the wrong type of object in a function
4. Attempting to iterate over a non-iterable object
5. Using unsupported operand types of operations
6. Using mutable vs. immutable types incorrectly
'''

#ImportError
'''
An ImportError in Python occurs when there's an issue with importing a module or a specific object from a module. This can happen for several reasons, such as if the module isn't found, or if you're trying to import something that doesn't exist in the module.

Common causes of an ImportError:
1. Module not installed
2. Typo in the module or object name
3. Importing a module from the wrong directory
4. Trying to import something that doesn't exist in the module
5. Circular imports
6. Environment or virtual environment issues
'''

#ValueError
'''
A ValueError in Python occurs when a function receives an argument of the correct type but with an inappropriate or invalid value. In other words, the type of the data is correct, but the value is outside the expected range or format for that function.

Common Causes of an ValueError:
1. Incorrect value for type conversion
2. Invalid value passed to a function
3. Unpacking the wrong number of values
4. Using the wrong range of values for certain operations
5. Invalid format for a built-in function
'''

#ZeroDivisionError
'''
A ZeroDivisionError in Python occurs when you attempt to divide a number by zero, which is mathematically undefined. This error is raised during operations involving division (/, //, or %) when the denominator is zero. 

Common causes of ZeroDivisionError:
1. Dividing by zero
2. Modulo by zero
3. Integer division by zero
'''