#Day 13: List Comprehension & Lambda
#10/14/2024

#filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6] #create the list of numbers
list = [i for i in numbers if i % 2 == 0 ] #Iterates over each element i in the numbers list., i % 2 == 0 to ensure the number is divisible by 2
print(list) #print the list

#flatten the following list of lists to a one dimensional list
list_of_lists = [[1, 2, 3], [4, 5, 6] , [7,8,9]]
list = [item for sublist in list_of_lists for item in sublist]
#for sublist in list_of_lists: Iterates over each sublist in the list_of_lists.
#for item in sublist: Iterates over each element (item) in the sublist.
print(list)

numbers = [(i * 1 , 1, i, i * i, i ** 3,i ** 4,i ** 5  ) for i in range(11)] #applying powers of the row index to generate each element in the tuple.
print(numbers)

#flatten the following list of lists into 1 new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

list = [[country[0].upper(), country[0][:3].upper(),country[1].upper()] for country_sub_list in countries for country in country_sub_list]
print(list)

#Change the following list to a list of dictionaries:
list = [{'countries' : country[0].upper(), 'city': country[1].upper()} for country_sub_list in countries for country in country_sub_list]
print(list) 

#Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
list = [item[1] + " " + item[0] for sublist in names for item in sublist]
print(list)

#Write a lambda function which can solve a slope or y-intercept of linear functions.

slope_and_intercept = lambda p1, p2: (
    (p2[1] - p1[1]) / (p2[0] - p1[0]),  # Slope
    p1[1] - ((p2[1] - p1[1]) / (p2[0] - p1[0])) * p1[0]  # Y-Intercept
)

point1 = (5, 3)
point2 = (1, 7)

m, a = slope_and_intercept(point1, point2)
print("Slope: " + str(m) + ", Y-Intercept: " + str(a))

#In Python, {m} is typically used in formatted strings, specifically in the context of f-strings (formatted string literals) or the str.format() method. It acts as a placeholder for a variable named m, which gets replaced by its value when the string is evaluated.