#Day 4: Lists
#09/13/2024

empty_lists = [] #empty list
five_or_more_list = [1,2,3,4,5,6,7] #list with more than 5 items
len_list = len(five_or_more_list) #get length of the list
print("First Item: " + str(five_or_more_list[0])) #print the first index
print("Last Item: " + str(five_or_more_list[-1])) #print the last index
print("Middle Item: " + str(five_or_more_list[len_list/2])) #print the middle index

mixed_data_types = ["Name", 111, 6.2, "Married", "Address"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(mixed_data_types) #print the mixed data type list
print(it_companies) #print the IT Company list

print(len("Total Companies in List" + str(it_companies))) #print the total items in the list

print("First Item: " + str(it_companies[0])) #print the first index
print("Last Item: " + str(it_companies[-1])) #print the last index
print("Middle Item: " + str(it_companies[len(it_companies)/2])) #print the middle index

it_companies[0] = "mango" #update the first item in the company list
it_companies[3] = "apple" #update the second item in the company list

print(it_companies) #print the new list

it_companies.append("IT Company") #add a new item to the end of the list
it_companies.insert((len(it_companies) /2), "Company Example") #insert a new company to the middle of the list
print(it_companies) #print the changed list
it_companies.insert(2, it_companies[2].upper()) #reinsert the item in index 2 as all upper case
print(it_companies) #print the changed list

print("IBM" in it_companies) #determine if a company, IBM, is in the list

#print(sorted(it_companies)) #sort the list of the companies without affecting the original variable (could use it_companies.sort() to sort and save the list)

r_it_companies = reversed(it_companies) #save a new list as a reverse object of the original list
rr_it_companies = list(r_it_companies) #transform that object into a list

first_three = it_companies[0:3] #slice the first three elements
last_three = it_companies[-3:] #slice the last three elements
middle_element = it_companies[len(it_companies)/2] #slice the middle element

del it_companies[0] #remove the first element
del it_companies[len(it_companies)/2] #delete the middle element
del it_companies[-1] #remove the last element

del it_companies #delete the list

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] #create list
back_end = ['Node','Express', 'MongoDB'] #create yet another list

full_stack = front_end + back_end
full_stack.insert(full_stack.index("React") + 1, "Python") #insert element after the "React" element index
full_stack.insert(full_stack.index("Python") + 1, "SQL ") #insert element after the new "Python" element index

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] #create a age list

ages.sort() #sort the list
print("Min Age: " + str(ages[0]) + " and the Max age: " + str(ages[len(ages) - 1])) # print the smallest and largest age

ages_avg = sum(ages)/ len(ages) #using sum() find the sum of all the elements and then divide the length or number of elements to find the average
print("The average age is: " + str(ages_avg)) #print the average
print("The age range is: " + str(ages[len(ages) - 1] - ages[0])) #print the age range