#Day 11: Functions
#10/07-08/2024

passed_list_only_int = [4,1,7,23,90,54,47,2,24]
passed_list_only_int_uneven = [4,1,7,23,90,54,47,2,24,34]
passed_list_only_int_same_numbers = [4,1,7,23,4,24,24,90,47,47,54,47,47,4,2,34,24,34]
passed_list_first = [2,"string", "bar", "plane"] #create a mixed type list
passed_list_second = [2,2,2] #create a list of only integers 
passed_list_third = ["string", "bus", "gear", "hat"]
empty = ""

def add_two_numbers(first_number, second_number): #create a function that takes two parameters
    add_two_numbers_sum = first_number + second_number #take the passed parameters and add them together into a new variable
    return add_two_numbers_sum #return that variable create above

def area_of_circle_calc(radius): #create a function that takes one variable
    area_of_circle = 3.14 * radius ** 2 #determine the area of a circle given the radius variable
    return area_of_circle #return the variable 

def add_all_nums(passed_list): #create a function that passes a list variable
    sum = 0 #create a local function variable
    for item in passed_list: #iterate through the list
        if type(item) != int: #determine if each item of that list is a integer 
            print("One of your items is not a integer") #if the item was not a integer, return a printed statement to the user
            return #due to one of the items not being a integer, break the function and return
        else:
            sum = sum + item #take all the items, and add them to the variable
    print(sum) #print the total sum of all the integers in the list
    return

def convert_celsius_to_fahrenheit(celsius): #create a function that passes one variable
    fahrenheit = (celsius * 9 / 5)  + 32 #create a variable that is the sum of the conversion 
    return fahrenheit #return the variable

def check_season(provided_month):
    # a list of the months for copying and pasting ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    month_season_dict = {"Winter" : ["December", "January", "February"], "Autumn" : ["September", "October", "November"], "Spring" : ["March", "April", "May"], "Summer" : ["June", "July", "August"]} #create a dictionary of the seasons as keys and the values as months

    if provided_month in month_season_dict["Winter"]: #determine if the month provided is in one of the key:value lists by calling the season's list and using the 'in' operator
        return("The season is Winter")
    elif provided_month in month_season_dict["Autumn"]:
        return("The season is Autumn")
    elif provided_month in month_season_dict["Spring"]:
        return("The season is Spring")
    elif provided_month in month_season_dict["Summer"]:
        return("The season is Summer")
    else:
        return("TSK TSK, The provided month is not one of the 12 months of the year.") #provided some feedback if they did not provided an accurate month string

def calculate_slope(x1, y1, x2, y2):
    # Check if the line is vertical to avoid division by zero
    if x1 == x2:
        raise ValueError("Slope is undefined for vertical lines.")
    
    # Calculate the slope
    slope = (y2 - y1) / (x2 - x1)
    return slope

def print_each_item(passed_list): #create a function that passes a list variable
    for item in passed_list: #iterate through each item of the list
        print(item) #print each item

def reverse_list(passed_list): #create a function that passes a list variable
    reverse_list = passed_list.reverse() #create a new variable that is the reverse of the variable that was passed through the function
    return reverse_list #return that new reversed variable

def capitalize_list(passed_list): #create a function that passes a list variable
    passed_list = list(map(str.capitalize, passed_list)) #use map() to apply a str.capitalize function to each element of an iterable
    return passed_list

def add_item(passed_list, item): #create a function that passes a list and one string
    passed_list.append(item) #append the string to the list
    return passed_list #return the modified list

def remove_item(passed_list, item): #create a function that passes a list and one string
    passed_list.remove(item) #remove the string from the list
    return passed_list #return the modified list

def sum_of_numbers(passed_integer): #create a function that passes a integer
    sum = 0 #create a 0 int variable
    while passed_integer != 0: #create logic that will perform the loop if the passed integer value is not 0
        sum = sum + passed_integer #add the current value of the passed integer to the sum 
        passed_integer = passed_integer - 1 #deduct 1 value from the passed integer
    return sum #return the sum

def sum_of_odds(passed_integer): #create a function that passes a integer
    passed_integer_list = list(range(1,passed_integer,2)) #take the integer and create a ranged list from 1 to the integer, skipping every other number to only get the odds
    sum = 0 #create a 0 sum variable
    for integer in passed_integer_list: #iterate through the list 
        sum = sum + integer #sum each item of the list 
    return sum #return the sum

def sum_of_evens(passed_integer): #create a function that passes a integer
    passed_integer_list = list(range(0,passed_integer,2)) #take the integer and create a ranged list from 0 to the integer, skipping every other number to only get the evens
    sum = 0 #create a 0 sum variable
    for integer in passed_integer_list: #iterate through the list 
        sum = sum + integer #sum each item of the list 
    return sum #return the sum

def evens_and_odds(passed_integer):
    passed_integer_list_odds = list(range(1,passed_integer,2)) #take the integer and create a ranged list from 1 to the integer, skipping every other number to only get the odds
    
    passed_integer_list_evens = list(range(0,passed_integer,2)) #take the integer and create a ranged list from 0 to the integer, skipping every other number to only get the evens

    return len(passed_integer_list_odds), len(passed_integer_list_evens) #return the length of both lists to determine the total evens and odds between 0 and the passed integer

def factorial(whole_number):
    factorial_range_list = list(range(1, whole_number + 1)) #create a ranged list to capture all the intergers before the given whole number, we had 1 value to account for the 0 index
    sum = 1 #create a variable with the value of 1 to ensure we do not multiple by 0 further in the function
    for number in factorial_range_list: #iterate through the list to multiply and get the factorial
        sum = number * sum
    return sum

def is_empty(passed_parameter): 
    if not passed_parameter: #check of the parameter was empty
        print("The passed parameter was empty")

def calculate_mean(passed_list):
    
    return sum(passed_list)/len(passed_list) #using sum() and len() determine mean

def calculate_median(passed_list):
    passed_list.sort() #sort the list smallest to largest

    if len(passed_list) % 2 != 0: #determine if the list has an even amount of numbers
        print(passed_list)
        return(passed_list[int(len(passed_list)/2)]) # if it didnt have an even amount of numbers, then the list can be safely divided to a non-whole number, which is then rounded up to determine the middle index
    
    elif len(passed_list) % 2 == 0: #if there are a even amount of numbers, the middle two numbers are taken as the median
        return(passed_list[int(len(passed_list)/2 - 1): int(len(passed_list)/2 + 1)]) #take the length of the list, and determine the middle indexs by adding and subtracting 1 to the middle index

def calculate_mode(passed_list):
    passed_list_dict = {} #create an empty dictionary

    for item in passed_list: #iterate through all the numbers of the list
        passed_list_dict[item] = passed_list.count(item) #when iterating through the list, add the number to the dictionary as the key and using the .count to add the total times that number appears in the list to the dictionary as the value

    sorted_passed = sorted(passed_list_dict, key=passed_list_dict.get, reverse=True) # the sorted() method sorts the keys based on their values using the key=language_dict.get
    #The key parameter of the sorted() function expects a function that returns a value to sort by. In this case, language_dict.get is passed directly as the sorting function.
    #When sorted() iterates through the keys of the dictionary, it calls language_dict.get(key) for each key to get its associated value. This value is what sorted() uses to determine the order of the keys.

    return(sorted_passed[0])

def calculate_range(passed_list):
    passed_list.sort() #sort the unsorted list
    return passed_list[0],passed_list[int(len(passed_list) - 1)] #return the first and last index item

def exercise_1():
    print(add_two_numbers(5,5))
    print(area_of_circle_calc(5))
    add_all_nums(passed_list_first)
    add_all_nums(passed_list_second)
    print(convert_celsius_to_fahrenheit(56))
    print(check_season("June"))
    print(calculate_slope(5, 6, 1, 2))
    print_each_item(passed_list_first)
    print(reverse_list(passed_list_first))
    print(capitalize_list(passed_list_third))
    print(add_item(passed_list_third, "Meat"))
    print(remove_item(passed_list_third, "Meat"))
    print(sum_of_numbers(5))
    print(sum_of_numbers(10))
    print(sum_of_numbers(100))
    print(sum_of_odds(10))
    print(sum_of_evens(10))

def exercise_2():
    print(evens_and_odds(43))
    print(factorial(5))
    is_empty(empty)
    print(calculate_mean(passed_list_only_int))
    print(calculate_median(passed_list_only_int))
    print(calculate_median(passed_list_only_int_uneven))
    print(calculate_mode(passed_list_only_int_same_numbers))
    print(calculate_range(passed_list_only_int))


exercise_1()
exercise_2()