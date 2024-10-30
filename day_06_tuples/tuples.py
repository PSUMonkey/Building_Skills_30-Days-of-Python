#Day 6: Tuples
#09/17/2024

#packing tuples
empty_tuple = () #create an empty tuple
brother_tuple = ("Brother Ben" , "Brother Brian") #create a tuple
sister_tuple = ("Sister Sally", "Sister Susian") #create a tuple

sibling_tuple = brother_tuple + sister_tuple #join 2 separate tuples together
print(sibling_tuple) #print the new tuple
print("There are " + str(len(sibling_tuple)) + " siblings.") #print the total number of the joined tuple
parent_tuple = ("Fathers Frank", "Mother Mary") #create a parent tuple
family_members_tuple = sibling_tuple + parent_tuple #join separate tuples
print(family_members_tuple)

#unpacking tuples
brother_1, brother_2, sister_1, *everyone = family_members_tuple #assign all the values of the tuple to a variable, by using a *, we create a list

print(brother_1)
print(brother_2)
print(sister_1)
print(everyone)

fruits = ("apple", "pear", "orange") #create a tuple
vegetables = ("corn", "green beans", "potato") #create a tuple
animal_products = ("chicken", "beef", "pork") #create a tuple

food_stuff_tp = fruits + vegetables + animal_products #join the tuples
food_stuff_lt = list(food_stuff_tp) #change the tuple to a list
food_stuff_lt_middle_index = int(len(food_stuff_lt) / 2) #determine the nearest middle index (will round down if even number of items in list)
print(food_stuff_lt)

#save and delete the middle item
food_stuff_lt_middle_item = food_stuff_lt[food_stuff_lt_middle_index] #assign the middle item of the list to a new variable
food_stuff_lt.pop(food_stuff_lt_middle_index) #remove the last item 

#save and delete the first three items
food_stuff_lt_first_three_items = food_stuff_lt[:3] #saves the first three items to a new variable
del food_stuff_lt[:3] #deletes the first three items from the list

#save and delete the last three items
food_stuff_lt_last_three_items = food_stuff_lt[-3:] #saves the last three items to a new variable
del food_stuff_lt[-3:] #deletes the last three items from the list

del food_stuff_tp #delete the tuple

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden') #create a tuple

print("Estonia is in the country tuple: "  + str("Estonia" in nordic_countries)) #determine if a string is in the tuple and print the boolean

print("Iceland is in the country tuple: "  + str("Estonia" in nordic_countries)) #determine if a string is in the tuple and print the boolean