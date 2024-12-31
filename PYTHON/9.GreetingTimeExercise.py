"""
Python Program capable of greeting you with "Good Morning", "Good Afternoon" or 
"Good Evening" depending on the time of the day. Use the datetime module to get the current time.
"""

# Importing the time module
import time

a = time.strftime("%H:%M:%S")
print(a)


if(a >= '5:00:00' and a <= '12:00:00'):
    print("Good Morning")

elif(a >= '12:00:00' and a <= '17:00:00'):
    print("Good Afternoon")

elif(a >= '17:00:00' and a <= '21:00:00'):
    print("Good Evening")

else:
    print("Good Night") 



