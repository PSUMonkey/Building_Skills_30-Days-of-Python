#Day 16: Date Time
#10/21/2024

from datetime import datetime
from datetime import timedelta

#Get the current day, month, year, hour, minute, and timestamp from datetime module

now = datetime.now() #The datetime.now() method returns the current local date and time as a datetime object. The now variable will hold this datetime object.

print("The current day: " + str(now.day))
print("The current month: " + str(now.month))
print("The current year: " + str(now.year))
print("The current hour: " + str(now.hour))
print("The current minute: " + str(now.minute))
print("The current second: " + str(now.second))
print("The current timestamp: " + str(now.timestamp()))

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
time_one = now.strftime("%m/%d/%Y, %H:%M:%S") #The strftime() method is called on the now datetime object to create a formatted string.
print(time_one)

'''
The format string "%m/%d/%Y, %H:%M:%S" specifies how the date and time should be represented:
%m: Month as a zero-padded decimal number (01 to 12)
%d: Day of the month as a zero-padded decimal number (01 to 31)
%Y: Year with century as a decimal number (e.g., 2024)
%H: Hour (00 to 23)
%M: Minute (00 to 59)
%S: Second (00 to 59)
'''

#Calculate the time difference between now and new year.
t1 = datetime(year=2025, month=1, day=1, hour=0, second=00) #This line creates a datetime object t1
t2 = datetime(year=2024, month=10, day=21, hour=16, second=00) #This line creates another datetime object t2
t3 = t1 - t2 #This line calculates the difference between t1 and t2, resulting in a timedelta object t3
print("t3 =", t3)

#Calculate the time difference between 1 January 1970 and now.
t1 = datetime(year=1970, month=1, day=1, hour=0, second=00) #This line creates a datetime object t1
t2 = datetime(year=2024, month=10, day=21, hour=16, second=00) #This line creates another datetime object t2
t3 = t1 - t2 #This line calculates the difference between t1 and t2, resulting in a timedelta object t3
print("t3 =", t3)