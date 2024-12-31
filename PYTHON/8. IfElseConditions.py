# 1. if-else statement:

a = int(input("Enter your age:\n"))
print('Your age is:' , a)

if(a < 18):
    print("You cant Vote now.")         # used Intendation

else:
    print('You can vote now.')



# 2. elif statement

b = int(input("Enter the number: \n"))
print('You have entered number: ')

if(b == 0):
    print('Number is Zero')

elif(b <= 0):
    print('Number is Negative')

else:
    print("Number is Positive")


# Python Program to print whether the Boy can Vote or not

boy = int(input('Enter your age: \n'))
print('Your age is :' , boy)

if(boy <18):
    print('You are Minor, cant Vote')

elif(boy >= 18 and boy <=100):
    print('You can Vote.')

else:
    print("You are probably  Dead sir.")



# 3. Nested If Condtion:

c = int(input('Enter the Number to check: \n'))
print('You have entered :' , c)

if(c == 0):
    print('Zero Value')

elif (c > 0):
    if(c == 1):
        print("Greater than zero")
    
    elif(c > 1 and c <= 20):
        print("value is smaller than 20")

    else:
        print("Value greater than 20")

else:
    print("Value is Negative.")