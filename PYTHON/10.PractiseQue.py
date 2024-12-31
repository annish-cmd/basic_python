"""
WAP that asks the user to input a number. The program should print "Positive" if the number is greater than zero, "Negative" if
the nummber is less than zero, and "Zero" if the number is exactly zero.
"""

# num = int(input('Enter the number: \n'))
# print("You have entered:", num)

# if (num > 0):
#     print('Number is Poitive.')

# elif (num < 0):
#     print('number is Negative.')

# else :
#     print('Number exactly Zero')



"""
Q.2 Create a Python program that takes an integer input from the user representing a person's age. The program should print:
    "Child" if the age is less than 13,
    "Teenager" if the age is between 13 and 19 (inclusive),
    "Adult" if the age is between 20 and 64 (inclusive),
    "Senior" if the age is 65 or older.
"""


# age = int(input("Enter Your Age: \n"))
# print('You have entered :' , age)

# if (age < 13) :
#     print('you are Child')

# elif (age >= 13 and age <= 19):
#     print('You are Teenager')

# elif ( age >= 20 and age <= 64):
#     print('You are Adult.')

# else:
#     print('you are Senior')


"""
Q.3 Write a Python program that asks the user to input two numbers. The program should first check if both numbers are positive. 
If they are, it should then check if the first number is greater than the second number and print "First is greater". If the first
 number is not greater, it should print "Second is greater or equal". If either of the numbers is not positive, the program should 
 print "Both numbers must be positive".
"""

a = int(input("Enter first number: \n"))
print('you have entered :', a)

b = int(input("Enter second number: \n"))
print('You have entered:' , b)

if( a > 0 and b > 0):
    if( a > b):
        print(f'{a} is greater than {b}')

    elif( a < b):
        print(f'{a} is smaller than {b}')

    else:
        print('Both equals')

else:
    print('Both number are Negative')
    

    


