#Day 8: Variables
#09/20/2024

dog_dict = {} # create a empty dictionary
dog_dict['Name'] = "Dog" #add a key-value pair to the dictionary
dog_dict['Color'] = "Brown" #add a key-value pair to the dictionary
dog_dict['Legs'] = 4 #add a key-value pair to the dictionary
dog_dict['Age'] = 3 #add a key-value pair to the dictionary

student_dict = {'first_name' : "John", 'last_name' : "Johnny", 'gender' : "Male",'age' : 54, 'marital_status' : "Married", 'skills' : ["Python", "Excel", "Skate Boarding"], 'gender' : "Male",'country' : "USA", 'city ' : "New York", 'address ' : "999 New York, New York"  }

len_student_dict = len(student_dict) #get the length of the dictionary
print(type(student_dict['skills'])) #print the value of the targeted item of the dictionary

student_dict['skills'] #printing the list from the dictionary before adding more items to the list

student_dict['skills'].append("Email") #calling the list with the key, then appending 1 item to the list

student_dict['skills'].extend(["Bike Riding", "Drawing"]) #calling the list with the key, then appending more than one item to the list

print(student_dict['skills']) #print the list after adding items to the list

student_dict_keys_list = student_dict.keys() #create a variable that has the keys of the dictionary as a list
student_dict_keys_list = student_dict.values() #create a variable that has the values of the dictionary as a list

student_dict_keys_tuple = student_dict.item() #create a list of tuples from the dictionary key and values

student_dict.pop("first_name") #deletes the specific item being called from the dictionary
del student_dict #deletes the dictionary