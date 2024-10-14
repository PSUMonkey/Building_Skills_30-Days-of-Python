#Day 12: Modules
#10/11/2024

from random import randint #import the random and randint modules
import random

def random_user_id(): #create a function that can be called that will return a 6-digit random number
    return randint(100000, 999999) #set the return of the function as the 6-digit random number

def user_id_gen_by_user():
    id_length = int(input("Please input the length of the ids: ")) #request the character length from the user
    requested_number_of_ids = int(input("Please input the number of ids: ")) #request the number of ids from the user

    user_ids = [] #create a empty list to store the uer ids
    character_length_lower = 1 #create a base to start building the lower limit if the user id character length
    for characters in range(id_length): #iterate over the range of the request user id character length, this will be used in the below randint function to create a a random user id
        character_length_lower *= 10 #move the decimal place for every character

    #morif the lower character length into the higher limit by moving the decimal place once more than subtracting one integer value to maintain the targeted character length
    character_length_higher = character_length_lower
    character_length_higher *= 10
    character_length_higher = character_length_higher - 1


    for number_of_ids in range(requested_number_of_ids): #iterate over the range of the requested amount of user ids
        user_ids.append(randint(character_length_lower, character_length_higher)) #use randint to create a random user id

    return user_ids

def rgb_color_gen(): #create the function
    rgb_color_gen_list =[] #create a empty list to store teh rgb color 
    for i in range(3): #create a for loop that will iterate 3 times, the range of 3
        rgb_color_gen_list.append(randint(0, 255)) #create a random rgb color number 
    return rgb_color_gen_list #return the completed list

def list_of_hexa_colors(requested_number_of_colors):
    hexa_array_list = [] #create a empty array to store the hexa colors
    
    for i in range(requested_number_of_colors):
        hexa_array_list.append("#{:06x}".format(randint(0, 0xFFFFFF))) 
        #generates a random integer between 0 and 0xFFFFFF (which is the decimal equivalent of the largest possible 6-digit hexadecimal number, FFFFFF).
        #"{:06x}".format() converts the integer to a 6-digit hexadecimal string, and the # adds the standard hex color prefix.
    return hexa_array_list

def list_of_rgb_colors(requested_number_of_colors):
    rgb_color_gen_list =[] #create a empty list to store teh rgb color 
    for i in range(requested_number_of_colors): #create a for loop that will iterate 3 times, the range of 3
        rgb_color_gen_list_set = [] #create a resuable empty list to save the 3 colors of the rgb
        for i in range(3):
            rgb_color_gen_list_set.append(randint(0, 255)) #create a random rgb color number 
        rgb_color_gen_list.append(rgb_color_gen_list_set) #append the rbg list to the bigger list
    return rgb_color_gen_list

def generate_colors():
    
    type = input("What type of color do you want? hexa or rgb? ")
    requested_number_of_colors = int(input("How many different color sets do you want? "))
    
    if type == "hexa":
        hexa_array_list = [] #create a empty array to store the hexa colors
    
        for i in range(requested_number_of_colors):
            hexa_array_list.append("#{:06x}".format(randint(0, 0xFFFFFF))) 
            #generates a random integer between 0 and 0xFFFFFF (which is the decimal equivalent of the largest possible 6-digit hexadecimal number, FFFFFF).
            #"{:06x}".format() converts the integer to a 6-digit hexadecimal string, and the # adds the standard hex color prefix.
        return hexa_array_list

    elif type == "rgb":
        rgb_color_gen_list =[] #create a empty list to store teh rgb color 
        for i in range(requested_number_of_colors): #create a for loop that will iterate 3 times, the range of 3
            rgb_color_gen_list_set = [] #create a resuable empty list to save the 3 colors of the rgb
            for i in range(3):
                rgb_color_gen_list_set.append(randint(0, 255)) #create a random rgb color number 
            rgb_color_gen_list.append(rgb_color_gen_list_set) #append the rbg list to the bigger list 
        
        return rgb_color_gen_list #return the completed list
    
    else:
        print("You didnt provide hexa or rgb")
        return "Empty List"

def shuffle_list(passed_list): # create a function that takes the list
    random.shuffle(passed_list) #using the random module with the shuffle function, shuffle the list values
    return passed_list #return the shuffles list

def random_seven_array():
    set_random_seven_array = set()
    while len(set_random_seven_array) != 7:
        set_random_seven_array.add(randint(0,9))
    
    return set_random_seven_array


    


