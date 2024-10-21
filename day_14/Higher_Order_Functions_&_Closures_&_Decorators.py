#Day 14: Higher Order Functions, Closures, Decorators
#10/14/2024

from functools import reduce
from countries_data import countries_list
from countries_datadump import country_data_dump

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mixed_list = [1, 2, 3, 4, 5, "First Name", "Middle Name", "Last Name", True, False]

''' map()
- is used the apply a specific function to each item in an iterable (list, tuple, dictionary) and return a new map type iterable

Syntax:

    map(function, iterable)
function: A function that defines what to do with each element of the iterable.
iterable: The collection of elements (e.g., list, tuple) on which the function will be applied.

The result of map() is an iterator, which means it doesn't immediately return the values but instead generates them as you iterate over the result. You can convert the result to a list, tuple, or other data structures if needed.
'''
''' filter()
- is used to filter elements from an iterable based on a specified condition (i.e., a function that returns either True or False for each element). Only the elements for which the function returns True are included in the return

Syntax:
    filter(function, iterable)
function: A function that tests each element of the iterable. It should return True if the element is to be included, and False otherwise.
iterable: The collection of elements (e.g., list, tuple) to be filtered.

The result of filter() is an iterator, so to see the filtered elements all at once, you typically convert it to a list, tuple, or other data structure.

'''
'''reduce()
- is used to apply a function cumulatively to the items of an iterable reducing the iterable to a single value
- an important note: In reduce(), the first two elements are passed to the function (x and y) because reduce() needs two elements to perform the first operation.

Syntax:
    reduce(function, iterable[, initializer])

    function: A function that takes two arguments and returns a single result. This function is applied cumulatively to the elements of the iterable.
iterable: The collection of items to be reduced.
initializer (optional): A starting value for the reduction, which is used as the first argument in the first call to the function. If not provided, the first two elements of the iterable are used by default.
'''
''' Higher-Order Functions
A higher-order function is a function that either 
-- takes one or more functions as arguments, or 
-- returns a function as its result

In Python, functions are first-class objects, which means they can be passed around just like other variables (e.g., numbers, strings). Higher-order functions leverage this by accepting functions as arguments or returning them.

    def apply_twice(func, value):
        return func(func(value))

    def add_five(x):
        return x + 5

    result = apply_twice(add_five, 10)  # add_five is passed as an argument
    print(result)  # Output: 20

    Here, apply_twice is a higher-order function because it takes another function (add_five) as an argument.
'''
''' Closures
A closure is a function that remembers that values from its enclosing scope, even after the scope in which it was created has finished executing. 

    def outer_function(x):
        def inner_function(y):
            return x + y  # 'x' is remembered from the outer scope
        return inner_function

    add_ten = outer_function(10)
    print(add_ten(5))  # Output: 15

What happens:
- outer_function(10) returns inner_function, which still "remembers" the value of x = 10.
- Even though outer_function is done executing, inner_function still has access to x when it is later called with add_ten(5).
'''
''' Decorators
A decorator is a specific type of higher-order function. It is used to modify or enhance the behavior of another function without modifying the function's code. Decorators are essentially functions that wrap another function to add extra functionality before or after the execution of the original function.

In Python, decorators are typically applied using the @decorator_name syntax above the function definition.

Example of a simple decorator:

    def my_decorator(func):
        def wrapper():
            print("Something before the function")
            func()  # Call the original function
            print("Something after the function")
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")

    say_hello()

How it works:

The my_decorator function takes say_hello as an argument and returns a new function (wrapper).
When say_hello() is called, it actually runs wrapper(), which adds behavior before and after the original say_hello() function.
'''

def exercise_1():

    #Define a call function before map
    def square_MAP(x): #create a call function
        return x ** 2 
    squared_numbers = map(square_MAP, numbers) #using map, pass the created square call function and the list as parameters to the map function which squares each number in the list and returns them as a list
    print(list(squared_numbers))

    #Define a call function before filter
    def even_filter(x): #create a call function
        return x % 2 == 0
    
    even_numbers = filter(even_filter, numbers) #using filter, pass the created filter call function and the list to filter for only the even numbers are return those as a list
    print(list(even_numbers)) 

    #Define a call function before reduce
    def reduce_list(x, y): #create a call function that multiples the 2 parameters that are provided
        return x * y
    sum_of_numbers = reduce(reduce_list, numbers) #use the reduce function to use the reduce_list function, which takes two parameters. The reduce function will take each item within the passed list, through the function, starting with the first two
    print(sum_of_numbers)
    
    #Use a for loop to print each country in the countries list.
    for country in countries:
        print(country)

    #use a for loop to print each name in the names list
    for name in names:
        print(name)
    #use a for loop to print each number in the numbers list
    for number in numbers:
        print(number)
    
def exercise_2():
    
    upper_lambda = lambda string: string.upper() #create a lambda function that upper cases the passed parameter
    
    #use the map function to create a new list by changing each country to uppercase in the countries list

    def upper(country): #create a function that will accept a parameter and return the upper cased version of that variable
        return country.upper()
    
    upper_country_list = list(map(upper, countries)) #use the map function to iterate over the countries and apply the upper function to them
    print(upper_country_list)
    
    #Use map to create a new list by changing each number to its square in the numbers list
    def new_square(x):
        return x ** 2
    
    new_square_list = list(map(new_square, numbers)) #use the map function to iterate over the countries and apply the new_square function to them
    print(new_square_list)

    #Use map to change each name to uppercase in the names list
    upper_name_list = list(map(upper_lambda, names)) #use the upper_lambda lambda function within the map function to pass the names in the name list through a function that upper cases each name in the list
    print(upper_name_list)

    #Use filter to filter out countries containing 'land'
    def filter_out_land(country): #create a function that returns True if the string "land" is in the passed parameter, return false if the string "land" is not in the passed parameter
        if "land" not in country:
            return True
        return False
    
    no_land_country_list = filter(filter_out_land, countries) #used the filter function to create a new list dependent on the True or False returned
    print(list(no_land_country_list))

    #Use filter to filter for countries having exactly six characters.
    def filter_for_6_character(country): #create a function that returns True if the country has 6 characters, return false if the country does not have 6 characters
        if len(country) == 6:
            return True
        return False
    
    no_6_character_country_list = filter(filter_for_6_character, countries) #used the filter function to create a new list dependent on the True or False returned
    print(list(no_6_character_country_list))

    #we could also use a lambda function instead of a call function to call for countries with only 6 characters

    result = filter(lambda country: len(country) == 6, countries)
    print(list(result))

    #Use filter to filter out countries having exactly more than 5 characters.
    def filter_out_6_character(country): #create a function that returns True if the country has 6 characters, return false if the country does not have 6 characters
        if len(country) < 5:
            return True
        return False
    
    not_6_character_country_list = filter(filter_out_6_character, countries) #used the filter function to create a new list dependent on the True or False returned
    print(list(not_6_character_country_list))
    
    #again, we could use a lambda function instead of a call function
    not_6_character_country_list = filter(lambda x: len(x) < 5, countries)
    print(list(not_6_character_country_list))

    #Use filter to filter out countries starting with an 'E'
    starts_with_a_E = filter(lambda country: country[0] == "E", countries)
    print(list(starts_with_a_E))

    #Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
    country_starts_with_a_N_and_upper_case = filter(lambda country: country[0] == "N", map(lambda country: country.upper(), countries))
    print(list(country_starts_with_a_N_and_upper_case))

    even_numbers_times_2 = filter(lambda number: number % 2 == 0, map(lambda number: number * 3, numbers)) #times each number in the numbers list by 3 then filter for only the even results
    print(list(even_numbers_times_2))

    #Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
    def get_string_list(item):
        if type(item) == str:
            return True
        return False
    
    new_string_list = filter(get_string_list, mixed_list)
    print(list(new_string_list))

    #accomplishing the same but with a lambda function
    new_string_list = filter(lambda item: type(item) == str, mixed_list)
    print(list(new_string_list))

    #Use reduce to sum all the numbers in the numbers list.
    ## using a call function
    def sum_of_all_numbers(x, y):
        return x + y
    
    sum_of_all_the_numbers = reduce(sum_of_all_numbers, numbers)
    print(int(sum_of_all_the_numbers))

    #using a lambda function
    sum_numbers = reduce(lambda x, y: x + y , numbers)
    print(sum_numbers)

    #Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
    def reduce_countries_to_a_sentence(x, y):
        if y == "Iceland":
            return x + ", and " + y + " are north European countries."
        else:
            return x + ", " + y
        
    new_country_string = reduce(reduce_countries_to_a_sentence, countries)
    print(new_country_string)

    #Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

    def categorize_countries():
        country_land_list = list(filter(lambda country: "ia" in country, countries_list))
        print(country_land_list)

        country_land_list = list(filter(lambda country: "island" in country, countries_list))
        print(country_land_list)

        country_land_list = list(filter(lambda country: "stan" in country, countries_list))
        print(country_land_list)

        country_land_list = list(filter(lambda country: len(country) == 6, countries_list))
        print(country_land_list)

    categorize_countries()

    #Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

    def count_countries_by_letter(countries_list):
        """        
        Parameters: countries (list): A list of country names (strings).
        Returns: dict: A dictionary with letters as keys and counts as values.
        """
        # Using reduce to build a dictionary of counts based on the first letter of each country
        return reduce(
            # The lambda function is called for each country in the list
            lambda acc, country: {**acc, country[0]: acc.get(country[0], 0) + 1}, countries_list,{})

            # Spread the existing accumulator dictionary (acc) into the new dictionary
                # acc is the accumulator dictionary that reduce() passes along as it iterates through the list. When you use **acc, it unpacks all the key-value pairs from acc into a new dictionary.
            
            # The key is the first letter of the current country (country[0])
            
            # The value is the current count of this letter in the dictionary (acc.get(country[0], 0))
                #The get() method in Python dictionaries is used to retrieve the value associated with a specified key. If the key is not found, it returns a default value, which is None if not specified
            
            # We add 1 to that count to reflect the new occurrence of the letter

            # The empty brackets {} in the context of the reduce() function represent an initial value for the accumulator.

    # Calling the function with the list of countries
    result = count_countries_by_letter(countries_list)

    # Printing the resulting dictionary
    print(result)

    #Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

    def get_last_ten_countries():
        return countries_list[-10:]
    print(get_last_ten_countries())

#exercise_1()
#exercise_2()