#Day 9: Conditionals
#09/20/2024

def exercise_1():
    users_age = int(input("Enter your age: ")) #ask the user for their age

    if users_age >= 18: #determine if the age provided is greater or less than 18
        print("You are old enough to learn to drive") #if it is, print the following statement
    else: #anything else (which would mean it is not 18 or more, do the below)
        missing_years = str(18 - users_age) #determine the missing years by taking 18 minus the age of the user
        print("You need " + missing_years + " more years to learn to drive.") #print the following statement plus the determined amount of years until they are 18


    my_age = 30 #set my age as a int variable
    your_age = int(input("Enter your age: ")) #ask the user for their age

    print(abs(my_age - your_age)) #abs() Return the absolute value of a number, which in this scenario, allows for any negative number to be returned as as positive if my_age is larger than the your_age variable

    if your_age == my_age: #compare both ages to determine if they are the same
        print("We are the same age!!")
    elif 1 < abs(my_age - your_age): #compare if the gap is larger than 1 to determine the correct output
        print("We are " + str(abs(my_age - your_age)) + " years apart")
    elif 1 == abs(my_age - your_age): #compare if the gap is smaller than 1 to determine the correct output
        print("We are " + str(abs(my_age - your_age)) + " year apart")
    else: #add some logging to the user to allow of any mistakes or issues
        "well that didn't work"

    inputted_number_1 = input("Enter number one: ")
    inputted_number_2 = input("Enter number two: ")

    if inputted_number_1 > inputted_number_2:
        print(str(inputted_number_1) + " is greater than " + str(inputted_number_2))
    elif inputted_number_1 < inputted_number_2:
        print(str(inputted_number_1) + " is less than " + str(inputted_number_2))
    elif inputted_number_1 == inputted_number_2:
        print(str(inputted_number_1) + " is equal to " + str(inputted_number_2))

def exercise_2():
    users_grade_point = int(input("What was your grade (0 - 100): ")) #ask the user for their grade

    if users_grade_point >= 90 and users_grade_point <= 100: #determine if the grade is equal or more than the lowest point of the grade or equal to the large
        print("You got an A")
    elif users_grade_point >= 70 and users_grade_point <= 89:
        print("You got an B")
    elif users_grade_point >= 60 and users_grade_point <= 69:
        print("You got an C")
    elif users_grade_point >= 50 and users_grade_point <= 59:
        print("You got an D")
    elif users_grade_point >= 0 and users_grade_point <= 49:
        print("You got an F")
    
    # a list of the months for copying and pasting ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    month_season_dict = {"Winter" : ["December", "January", "February"], "Autumn" : ["September", "October", "November"], "Spring" : ["March", "April", "May"], "Summer" : ["June", "July", "August"]} #create a dictionary of the seasons as keys and the values as months

    user_month = input("What is your month? ") #ask the user for their month

    if user_month in month_season_dict["Winter"]: #determine if the month provided is in one of the key:value lists by calling the season's list and using the 'in' operator
        print("The season is Winter")
    elif user_month in month_season_dict["Autumn"]:
        print("The season is Autumn")
    elif user_month in month_season_dict["Spring"]:
        print("The season is Spring")
    elif user_month in month_season_dict["Summer"]:
        print("The season is Summer")
    else:
        print("TSK TSK, The provided month is not one of the 12 months of the year.") #provided some feedback if they did not provided an accurate month string
    
    fruits = ['banana', 'orange', 'mango', 'lemon']
    print("Please see my list of fruit") #show the user our fruits
    print(fruits)
    user_fruit = input("What is your fruit? ") #ask the user what fruit they want

    if user_fruit in fruits: #determine if the fruit they provided is in our list
        print("That fruit already exist in the list") 
    else: #determine if it was not add the fruit to our list
        fruits.append(user_fruit)
        print("Our new fruit list")
        print(fruits) #print the new list of fruits

def exercise_3():
    person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', "Node", 'Python', "MongoDB", "React"],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
    
    if "skills" in person:
        len_skills_list = len(person["skills"]) #determine the length of the skills value list
        middle_index_skills_list = len_skills_list // 2 #determine the nearest integer to half the length of the skills list, giving you the middle index (5 // 2 = 2)
        print(person["skills"][middle_index_skills_list]) #calling the middle index

    if "Python" in person["skills"]:
        print("Asabeneh has the 'Python' skill!")
    
    if "React" in person["skills"]:

        if "React" and "Node" and "MongoDB" in person["skills"]:
            print('He is a fullstack developer')
        
        elif "JavaScript" and "React" in person["skills"]:
            print('He is a frontend developer')

    elif "Node" and "Python" and "MongoDB" in person["skills"]:
        print('He is a backend developer')
    
    
    if person["is_marred"] == True and person["country"] == "Finland":
        print(person["first_name"] + " " + person["last_name"] + " lives in " + person["country"] + ". He is married" )
        
#exercise_1()
#exercise_2()
exercise_3()