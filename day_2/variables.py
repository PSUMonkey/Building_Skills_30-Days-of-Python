#Day 1: Variables
#08/30/2024

#Level 1 Exercises
first_name = "First Name" #Declare First Name Variable
last_name = "Last Name" #Declare Last Name Variable
full_name = "Full Name" #Declare Full Name Variable
country_name = "Country Name" #Declare Country Name Variable
city_name = "City Name" #Declare City Name Variable
Age_Variable = 99 #Declare Age Variable
Year_Variable = 1999 #Declare Year Variable
is_married = True #Declare is_married variable
is_true = True #Declare is_true variable
is_light_on = True #Declare is_light_on variable
one_variable, two_variable, three_variable = 0,1,2 #Declare multiple variables in a single line

#Level 2 Exercises

#print the type of all the bellow variables 
print("first_name variable is: " + str(type(first_name)))
print("last_name variable is: " + str(type(last_name)))
print("full_name variable is: " + str(type(full_name)))
print("country_name variable is: " + str(type(country_name)))
print("city_name variable is: " + str(type(city_name)))
print("Age_Variable variable is: " + str(type(Age_Variable)))
print("Year_Variable variable is: " + str(type(Year_Variable)))
print("is_married variable is: " + str(type(is_married)))
print("is_true variable is: " + str(type(is_true)))
print("is_light_on variable is: " + str(type(is_light_on)))
print("one_variable variable is: " + str(type(one_variable)))
print("two_variable variable is: " + str(type(two_variable)))
print("three_variable variable is: " + str(type(three_variable)))

#print the length of the First Name Variable
print("Length of the First Name Variable: " + str(len(first_name)))

num_one, num_two = 5, 4 #set num_one and num_two variables
total = num_one + num_two #create a new variable that is the sum of num_one and num_two
diff = num_one - num_two #create a new variable that is the diff of num_one and num_two
product = num_one * num_two #create a new variable that is the multiple of num_one and num_two
division = num_one / num_two #create a new variable that is the divided of num_one and num_two
remainder = num_one % num_two #create a new variable that is the modulus of num_one and num_two
exp = num_one ** num_two #create a new variable that is the exponential of num_one and num_two
floor_division = num_one // num_two #create a new variable that is the floor division of num_one and num_two

radius_of_circle = 30 #setting the value of the radius_of_circle variable
#to determine the area, 3.14 * r squared, r being the radius of the circle
area_of_circle = 3.14 * radius_of_circle ** 2

#to determine the circumference of a circle, 2 * 3.14 * r
circum_of_circle = 2 * 3.14 * 30

radius_of_circle = input(" What is the radius of your circle? ") #ask the user for the radius of their circle
area_of_circle = 3.14 * radius_of_circle ** 2 #calculate the area of the users circle
print("The area of your circle is :" + str(area_of_circle)) #return the area to the user

user_first_name = ("What is your first name? ") #ask the user for their first name
user_last_name = ("What is your last name? ") #ask the user for their last name
user_country_name = ("What is your country name? ") #ask the user for their country name
user_age = ("What is your age? ") #ask the user for their age