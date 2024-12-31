'''
A function is like a mini program within a program that performs specific tasks when called.

=> reuable code.
=> smaller code & easy to update.

'''

# Program to demo use of teh 'function'

def calculateGmean (a,b):
    mean = (a*b)/(a+b)
    print (mean)

a = 3
b = 5
# function call
calculateGmean (a,b)

c = 9
d = 8
# function call
calculateGmean(c,d)


# WAP to greet user with the "Good Day" using function.

# def greet_user(name):                  #created function
#     greet = 'Good Day'
#     print(f"{greet},{name}")

# name = input("Enter your name: ")
# #function call
# greet_user(name)



'''
Question 1: Greeting Function

Write a function named personalized_greet that takes two parameters: name and time_of_day. The function should return a greeting like:

    "Good Morning, John!" if time_of_day is "Morning".
    "Good Evening, Alice!" if time_of_day is "Evening".

Call the function with different names and times of day and print the results.
'''

# def personalized_greet (name, time_of_day) :
#     if time_of_day == 'Morning' :
#         print("Good Morning," , name)
#     else :
#         print("Good Evening," , name)

# name = input("Enter Your name: \n")
# time_of_day = input("Enter time of day (Morning/Evening): \n").capitalize()         # making the input capital

# # Function call
# personalized_greet (name, time_of_day)








 


