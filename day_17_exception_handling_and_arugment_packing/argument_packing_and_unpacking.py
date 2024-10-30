#Day 17: Packing and Unpacking Arguments in Python
#10/22-23/2024

countries = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'] 
countries_simple_dictionary = {"First_Name" : "FName", "Last_Name" : "LName"}


#Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

*nordic_countries, es, ru = countries
print(f"nordic_countries has {nordic_countries}, es has {es}, ru has {ru}")


#Write a function that can accept any number of arguments (using *args) and return the sum of all the arguments passed.

def sum_args(*args): 
    #*args allows you to pass a any number of arguments to a function. All arguments passed are captured as a tuple inside the function.
    return sum(args)

print(sum_args(1, 2, 3, 4, 5))

#Write a function that accepts keyword arguments using **kwargs and prints each key-value pair.

def print_keywords(**kwargs):
    #**kwargs captures keyword arguments (arguments passed as key-value pairs) as a dictionary. Inside the function, kwargs will behave like a dictionary.
    print(kwargs)
    for key_value_pair in kwargs:
        print({f"The key {key_value_pair} value is {kwargs[key_value_pair]}"})

print_keywords(name="Alice", age=25)

#Write a function that accepts both positional arguments (*args) and keyword arguments (**kwargs). The function should print both the positional and keyword arguments separately.

def print_pos_and_key(*args, **kwargs):
    print("Positional arguments: ", args)
    print("Keyword arguments: ",kwargs)

    '''
    Positional arguments (*args):
        1, 2, 3, 45 are positional arguments, captured in *args, which is treated as a tuple.
    Keyword arguments (**kwargs):
        list="numbers", head="cut" are keyword arguments, captured in **kwargs, which is treated as a dictionary.
    '''

print_pos_and_key(1, 2, 3, 45, list = "numbers", head = "cut")

#Write a function that takes three arguments and prints them. Then, use tuple/list unpacking when calling the function.

def print_three_arguments(a, b, c):
    print(a, b, c)

tuple_list = ("dog" , "cat", "mouse")
print_three_arguments(*tuple_list)
#You use the *tuple_list syntax to unpack the tuple and pass its elements as individual arguments to the function.

#Write a function that takes three keyword arguments and prints them. Then, use dictionary unpacking to call the function.

def print_three_keyword_argument(name, age, location):
    print(name, age, location)

keyword_dictionary = {"name" : "1st_value", "age" : 45, "location" : "earth"}
print_three_keyword_argument(**keyword_dictionary)

#When passing a dictionary to a function, you can use the ** operator to unpack the dictionary’s key-value pairs into individual keyword arguments.

#Write a function that accepts a mix of positional arguments, keyword arguments, and handles both using unpacking.

def print_mix_arguments(*args, **kwargs):
    print("Positional arguments: ", args)
    print("Keyword arguments: ",kwargs)

print_mix_arguments(*tuple_list, **keyword_dictionary)