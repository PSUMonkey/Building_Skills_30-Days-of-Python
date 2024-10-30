#Day 4: Operators
#07/04/2024

string_Thirty, string_Days, string_of, string_python = "Thirty", "Days", "of", "Python" #create the sub string variables
string_Thirty_Days_Of_Python = string_Thirty + " " + string_Days + " " + string_of + " " + string_python #create a Concatenate variable of all the minor string variables
print(string_Thirty_Days_Of_Python)

string_Coding, string_For, string_All = "Coding", "For", "All" #create the sub string variables
string_Coding_For_All = string_Coding + " " + string_For + " " + string_All #create a Concatenate variable of all the minor string variables
print(string_Coding_For_All)

company_variable = 'Coding For All'
company_variable_Python = "Python For Everyone"
print(company_variable)
print(str(len(company_variable))) #print the length of the variable

print("Upper(): " + company_variable.upper()) #change all the character to upper case
print("Lower(): " + company_variable.lower()) #change all the characters to lower case
print("capitalized(): " + company_variable.capitalize()) #Upper case the first letter in this sentence
print("Titled(): " + company_variable.title()) #Make the first letter in each word upper case
print("Swapcase(): " + company_variable.swapcase()) #Swapcase the lower and upper cases of the string

print(company_variable[0:6]) #slicing a string

print(company_variable.index("For")) #using .index(), determine if the string is in the variable string
print("Coding" in company_variable) #method finds the first occurrence of the specified value
print(company_variable.find("Coding")) #method finds the first occurrence of the specified value
print(company_variable.rfind("Coding")) #method finds the first occurrence of the specified value

print(company_variable.replace("Coding", "Python")) #replace one word for another

print(company_variable.split(" ")) #using the split method, turns the 1 string variable into a list of all the different strings once split

tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(",")) #using the split method, turns the 1 string variable into a list of all the different strings once split

print(company_variable[0]) #Returns the letter at the indicated number position at the string
print(company_variable[5]) #Returns the letter at the indicated number position at the string
print(company_variable[len(company_variable) - 1]) #using length - 1, we can return the last character of the string
print(company_variable[10]) #Returns the letter at the indicated number position at the string

company_variable_Python = "Python For Everyone"
company_variable_Python_list = company_variable_Python.split() #split the string into a list
company_variable_Python_ACR = "" #create the final variable you want at the end
for item in company_variable_Python_list: #iterate through the list so we can pull the first letter of each word
    company_variable_Python_ACR = company_variable_Python_ACR + item[0] #take the first letter, and append it to the string
print(company_variable_Python_ACR)


company_variable_ = "Coding For All"
company_variable_list = company_variable_.split() #split the string into a list
company_variable_ACR = "" #create the final variable you want at the end
for item in company_variable_list: #iterate through the list so we can pull the first letter of each word
    company_variable_ACR = company_variable_ACR + item[0] #take the first letter, and append it to the string
print(company_variable_ACR)

print(company_variable_.index("C")) #use the index method to determine the character location of the first "C"
print(company_variable_.index("F")) #use the index method to determine the character location of the first "F"

Coding_For_All_People_var = "Coding For All People"
print(Coding_For_All_People_var.rfind("i")) #use the index method to determine the character location of the first "i"

provided_sent = 'You cannot end a sentence with because because because is a conjunction'
print(provided_sent.find("because")) #find the position of the string "because"
print(provided_sent.rindex("because")) #method finds the last occurrence of the specified value.
print(provided_sent.replace("because ","")) #using the replace function, remove all the instances of "because"

print(company_variable_.startswith("Coding")) #return a true or false if the string starts with the targeted string
print(company_variable_.endswith("Coding")) #return a true or false if the string ends with the targeted string


trailing_substrings = '   Coding For All      '
print(trailing_substrings.strip()) #using strip() strip all the whitespace away

list_32 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
list_32_string = "# ".join(list_32) #join the list into one string
print(list_32_string)

string_33 = "I am enjoying this challenge.I just wonder what is next."
string_33_period_location = string_33.index('.') + 1 #find the location of the period and add 1 space to determine where we need to split the sentence  
print(string_33[:string_33_period_location] + "\n" + string_33[string_33_period_location:]) #print the string with the added new line character

print("Name\tAge\tCountry\tCity") #use the \t to tab the string items
print("Asabeneh\t250\tFinland\tHelsinki") #use the \t to tab the string items

print("8 + 6 = 14")
print("8 - 6 = 2")
print("8 * 6 = 48")
print("8 / 6 = 1.33")
print("8 % 6 = 2")
print("8 // 6 = 1")
print("8 ** 6 = 262144")