#Day 19 - File Handling
#11/05/2024

import os

current_directory = os.getcwd() #determine the current directory with the os module and getcwd()
speech_1_file = "speech_1_file.txt"
speech_2_file = "speech_2_file.txt"
speech_3_file = "speech_3_file.txt"

print(current_directory)

#level 1 exercises
#Write a function which count number of unique lines and number of words in a text. 
#remove the empty lines
# speech_1_file

f = open(f'{current_directory}\\{speech_1_file}') #open the targeted file
lines = f.read().splitlines() 
    # f.read() reads the entire content of the file as a single string.
    # .splitlines() splits this string into a list of lines, removing the newline character \n from the end of each line.
lines = set(lines) #transform the list of lines into a set of lines to remove any duplicate lines (the empty lines)
lines.remove("") #remove the empty line
print(f"The number of lines in {speech_1_file} is " + str(len(lines)))