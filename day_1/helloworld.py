#Day 2: Variables
#07/01/2024

#import os library to run windows command-line commands
import os

#import math to utilize 
import math

#print the current python version using the 'os' method
print(os.system('python --version'))

#print operands of '3' and '4'
print(3 + 4) #addition
print(3 - 4) #subtraction
print(3 * 4) #multiplication
print(3 % 4) #modulus
print(3 / 4) #division
print(3 ** 4) #exponential
print(3 // 4) #floor division

print("Test Name") #Print my name
print("My Family Name") #Print my family name
print("United States") #Print my Country
print("I am enjoying 30 days of python") #Print the saying

#print the type of all the below items
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh','Python','Finland']))
print(type("Test name"))
print(type("Family Name"))
print(type({9.8, 3.14, 2.7}))
print(type((9.8, 3.14, 2.7)))

print(type(3)) #print int
print(type(9.8)) #print float
print(type(7j - 3)) #print complex
print(type("string")) #print string
print(type(True)) #print boolean
print(type(["list0", "list1", "list2"])) #print list
print(type((9.8,4.3,2.6))) #print tuple
print(type({'key0':'value0','key1':'value1','key2':'value2'}))

#The Euclidean distance is essentially the length of the shortest path between two points, assuming you can only move in straight lines between dimensions.
#find the Euclidean distance between (2,3) and (10,8)

point1 = (2,3) #point 1
point2 = (10,8) #point 2

#use sqrt
#The math.sqrt function in Python is part of the math module and is used to calculate the square root of a given number.

distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1]) - point1[1]**2)
print(distance)