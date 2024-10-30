#Day 0: Stuff and Things

#This file will sever to host all the random and interesting python things I come across that I either haven't gotten to in this training or were not covered directly.

int_variable_1 = 5 #this variable has the value of 5
int_variable_2 = '' #this variable is empty

if int_variable_1: #the if *variable*: looks to see if the variable to empty or not
    print("This is True")

if int_variable_2:
    print("This is True")
else:
    print("This is False") #because the int_variable_2 is empty, it does not fullfil the if statement

string_variable_1 = "Python"
int_variable_3 = 28

print(f"My favorite code is {string_variable_1}") #the f before the "" allows for direct input of variables and removes the need to concatenate 

print(f"My favorite code is {string_variable_1} and I am {int_variable_3} old.") #you directly input many types of variables and more than one