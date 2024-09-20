#Day 7: Variables
#09/20/2024

#create a series of sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

it_companies.add("Twitter") #add an item to the set
it_companies.update(["Facebook", "Google", "Oracle","Palo Alto"]) #update/add more than one item to the set
it_companies.remove("Facebook") #remove a specific item
it_companies.discard("Friendz") #this name is not in the set, but the discard method does not throw an error
it_companies.pop() #remove a random item from the set

print(it_companies)

a_and_b = A.union(B) #join the A and B sets together

print(A.intersection(B)) #print the same items or 'intersections' in both A and B sets

print("Is A set a subset of B: " + str(A.issubset(B))) #determine if A set is a subset of set B

print("Are A and B sets disjointed (do not have any of the same items): " + str(A.isdisjoint(B))) #determine if the two sets have any items in common

print(A.symmetric_difference(B)) #print the symmetric difference of the two sets before joining them

A.update(B) #updating set A with the items in B
B.update(A) #updating set B with the items in A

print(A.symmetric_difference(B)) #print the symmetric difference of the two sets after joining them

del A, B #delete both sets

age_set = set(age) #create a set from the list
age_list_length = len(age) #get the length of the age list
age_set_length = len(age_set)

print("Is the age list shorter the age set? " + str(age_list_length < age_set_length))
print("Is the age list longer the age set? " + str(age_list_length > age_set_length))

string = "I am a teacher and I love to inspire and teach people." #create the string
string_list = string.split(" ") #split the string into a list by the spaces to get 1 word per list item
string_set = set(string_list) #transform the list into a set with only unique items or words
len_string_set = len(string_set) #get the length of the set
print("The amount of unique words are: " + str(len_string_set))
