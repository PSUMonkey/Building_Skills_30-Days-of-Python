#Day 18 - Regular Expressions
#10/23/2024

import re

''' Methods in re Module

re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string

'''

# re.match()
# check for a match only at the beginning of a string.
txt = "I love python!"

# syntax re.match(substring, string, re.I)
match = re.match('I love', txt, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore

#print(match) # <re.Match object; span=(0, 15), match='I love'>

# .span()
# method is used with regular expression (regex) match objects, typically obtained through the re module. It returns a tuple indicating the start and end positions of the match within the searched string.

span = match.span()
#print(span) # (0 , 6)

start, end = span
#print(start, end) # 0 6

substring = txt[start:end]
#print(substring) # I love

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
#print(match)  # None

#re.search()
#can find a match anywhere within the string.

txt = "Python is the most beautiful language that a human being has ever created. I recommend python for a first programming language"

search_match = re.search('first', txt, re.I)
#print(search_match) #<re.Match object; span=(100, 105), match='first'>

search_span = search_match.span()
#print(search_span) #(100, 105)
start, end = search_span
#print(txt[start:end]) #first

#re.findall()

txt = "I like cake, I Like sandwiches, I like icecream"
findall_match = re.findall("I like", txt, re.I)
#print(findall_match) #['I like', 'I Like', 'I like']

txt = "I like cake, I Like sandwiches, I like icecream"
findall_match = re.findall("I like", txt) #without re.I
#print(findall_match) #['I like', 'I like']

#re.sub()
# used to replace occurrences of a specified regex pattern within a string with a replacement text
# re.sub(pattern, replacement, string, count=0, flags=0)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple. 
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub("%", "", txt)
#print(matches)

#re.split()
# divides a string into a list of substrings based on a specified regex pattern.

#re.split(pattern, string, maxsplit=0, flags=0)

#print(re.split("\n", matches))

#writing Regex
'''
[] : A set of characters
- [a-c] means, a or b or c
- [a-z] means, any letter from a to z
- [A-Z] means, any character from A to Z
- [0-3] means, 0 or 1 or 2 or 3
- [0-9] means any number from 0 to 9
- [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
'''
#\ : uses to escape special characters
#- \d means: match where the string contains digits (numbers from 0-9)
#- \D means: match where the string does not contain digits
'''
. : any character except new line character(\n)

^ : starts with
- r'^substring' eg r'^love', a sentence that starts with a word love
- r'[^abc] means not a, not b, not c.

$ : ends with
- r'substring$' eg r'love$', sentence that ends with a word love

* : zero or more times
- r'[a]*' means a optional or it can occur many times.

+ : one or more times
- r'[a]+' means at least once (or more)

? : zero or one time
- r'[a]?' means zero times or once

{3} : Exactly 3 characters

{3,} : At least 3 characters

{3,8} : 3 to 8 characters

| : Either or
- r'apple|banana' means either apple or a banana

() : Capture and group
'''


# What is the most frequent word in the following paragraph?

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

paragraph_dict_counter = {}

paragraph_without_periods = re.sub(r"\.","",paragraph) #remove all the periods, with regex, to target ".", we need to use r, before the quotes, to denote a raw string, so that when we use the backslash "\" to denote a special character for regex

paragraph_without_periods = paragraph.replace(".", "") #.replace() also works but is not apart of th re module

paragraph_set = set(paragraph_without_periods.split(" ")) #now split all the words into a set that forces no repeats

for word in paragraph_set: #iterate through the paragraph_set
    paragraph_dict_counter[word] = len(re.findall(word, paragraph)) #for the current word, find all the instances of that word in the original string, find the length or total instances of that word, save the word and its amount of instances to the dictionary as a key value pair

#paragraph_dict_counter = {word: (lambda w: len(re.findall(w, paragraph, re.I)))(word) for word in paragraph_set}
#the lambda version of the for loop

sorted_paragraph_dict_counter = dict(sorted(paragraph_dict_counter.items(), key=lambda item: item[1], reverse=True))
#data.items() - returns the items of the dictionary as a list of tuples
#sorted(data.items(), key=lambda item: item[1])
# sorted() - takes two arguments, the iterable to sort, which is the data.items() and the key function
# key=lambda item: item[1] - tells sorted() to look at the second item, item[1], the value in each tuple
# The lambda here is an anonymous function that quickly defines this extraction logic.
# lambda item: item[1] is a short, inline function that takes each item and returns its value (in this case, item[1] is the second element of each tuple (key, value)).

#print(sorted_paragraph_dict_counter)

#Write a pattern which identifies if a string is a valid python variable

'''
Python Variable Name Rules

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
'''

regex_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
# ^: Asserts the start of the string.
# [a-zA-Z_]: The first character must be a letter (either lowercase or uppercase) or an underscore.
# [a-zA-Z0-9_]*: The subsequent characters can be letters, digits, or underscores, and the * quantifier allows for zero or more of these characters.
# $: Asserts the end of the string.

#print(re.match(regex_pattern, input()) is not None)
#print(re.match(regex_pattern, input()) is not None)
#print(re.match(regex_pattern, input()) is not None)

#Write a Python regex to find all four-letter words in the given string.

text = "This test will find only four letter words in this text."

#print(re.findall(r'\b\w{4}\b', text,re.I))
#\b: Asserts a word boundary at the start of each word.
#\w{4}: Matches exactly four word characters.
#\b: Asserts a word boundary at the end of each word.
#re.I: The re.I flag makes the search case-insensitive, matching both uppercase and lowercase letters.

#Write a Python regex to find all occurrences of two consecutive identical letters in words (like "letter", "bookkeeper", "committee").

text = "letter bookkeeper committee"

#print(re.findall(r'\b\w*(\w)\1\w*\b', text,re.I))
'''
\b: Word boundary to ensure you’re matching within complete words.
\w*: Matches any characters leading up to the repeated letters.
(\w)\1: The core part — a capturing group for one letter, immediately followed by a backreference \1 to match the same letter.
\w*: Matches any characters following the repeated letters within the word.
\b: Ensures the match stays within the word boundary.
'''

#Write a Python regex to match all words that start and end with the same letter.

text = "Anna went to the park with Bob to play in the noon sun."

print(re.findall(r'\b(\w).*\1\b', text , re.I))
