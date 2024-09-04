#Day 3: Operators
#07/01/2024

#Variable Creation
my_age = 28 #integer variable
my_height = 6.4 #floating variable
complex_variable = 1 + 1j #complex number

#String evaluation and manipulation 
python_string = "Python"
dragon_string = "Dragon"

python_string_length = len("python_string") #save the int length of the string 'python'
dragon_string_length = len("dragon_string") #save the int length of the string 'dragon'
print(dragon_string_length < python_string_length) #print a non-true statement

print('on' in dragon_string and 'on' not in python_string) #Use and operator to check if 'on' is found in both 'python' and 'dragon'

jargon_string = "I hope this course is not full of jargon. "
print('jargon' in jargon_string) #Use in operator to check if jargon is in the sentence.

python_string_length_float = float(python_string_length) #create a variable that is the float of the length of the word python

user_number = int(input("Please provide a number and I will determine if it is divisible by 2: ")) #prompt the user for a number to determine if it divisible by 2
user_number_remainder = user_number % 2 == 0 #determine the remainder of the user number once divided by two
print("The number you provided is divisible by 2: " + str(user_number_remainder)) #return a true or false statement about the user's provided number

print((7 // 3) == int(2.7)) #this will print true, fllor division will round the result as will the int() of 2.7

print('10' == 10) #a string does not equal a integer 

print(int(9.8) == 10) #rounds down

#Print out a table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
print("2 1 2 4 8")

#User Input Script
def determine_users_triangle_area(): #create a function to determine the area of a triangle
    user_inputted_base = input("Please enter the base of your triangle: " ) #ask the user for the measurement of the base
    user_inputted_height = input("Please enter the height of your triangle: " ) #ask the user for the measurement of the height
    user_triangle_area = .5 * int(user_inputted_base) * int(user_inputted_height) #multiply the base, height, and .5 to get the area
    print("The area of your triangle is: " + str(user_triangle_area)) #provide the user the area of the triangle

def determine_users_triangle_perimeter(): #create a function to determine the perimeter of a triangle
    user_inputted_triangle_side_A = input("Please enter the length of side A: " ) #ask the user for the measurement of side A
    user_inputted_triangle_side_B = input("Please enter the length of side B: " ) #ask the user for the measurement of side B
    user_inputted_triangle_side_C = input("Please enter the length of side C: " ) #ask the user for the measurement of side C
    user_triangle_perimeter = int(user_inputted_triangle_side_A) + int(user_inputted_triangle_side_B) + int(user_inputted_triangle_side_C) #determine the triangle's perimeter
    print("The perimeter of your triangle is :" + str(user_triangle_perimeter)) #provide the user the perimeter of the triangle

def determine_users_rectangle_area(): #create a function to determine the area of a rectangle
    user_inputted_rectangle_length = input("Please enter the length of rectangle: " ) #ask the user for the length
    user_inputted_rectangle_width = input("Please enter the width of rectangle: " ) #ask the user for the width
    user_rectangle_area = int(user_inputted_rectangle_length) + int(user_inputted_rectangle_width)  #determine the rectangle's area
    print("The area of your rectangle is: " + str(user_rectangle_area)) #provide the user the area of the rectangle 

def determine_users_circles_area_and_circumference(): #create a function to determine the area and circumference of a circle
    user_inputted_circles_radius = input("Please enter the radius of circle: " ) #ask the user for the radius of circle
    user_circles_area = 3.14 * (int(user_inputted_circles_radius) ** 2)  #determine the circle's area
    user_rectangle_circumference = 2 * 3.14 * int(user_inputted_circles_radius)  #determine the circle's circumference
    print("The area of your rectangle is: " + str(user_circles_area)) #provide the user the circle's area
    print("The area of your rectangle is: " + str(user_rectangle_circumference)) #provide the user the circle's circumference

def determine_salary():
    users_hours = int(input("Enter Hours: ")) #ask the user for their work hours per week
    users_rate_per_hour = int(input("Enter rate per hour: ")) #ask the the user their pay per hour
    print("Your weekly earnings is " + str((users_hours * users_rate_per_hour))) #return their total week pay by multiplying the rate by the hours, transform the integer into a string to allow for printing with the string

def determine_secs_in_age():
    users_age_in_years = int(input("How old are you in years? ")) #ask the user for their age in years, also ensure we transform the provided string into a integer
    users_age_in_secs = users_age_in_years * 31622400 #take the years, multiply by the total seconds in a year
    print("You have been alive for a total of " + str(users_age_in_secs) + " seconds!")

determine_users_triangle_area()
determine_users_triangle_perimeter()
determine_users_rectangle_area()
determine_users_circles_area_and_circumference()
determine_salary()
determine_secs_in_age()