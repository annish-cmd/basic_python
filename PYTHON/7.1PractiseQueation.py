# Q.1) WAP that takes a string input from the user and prints the string in both Upper and Lower case

print('***** PYTHON ****')

# print('Enter your name: \n')
# a = input()

# print("UpperCase is:", a.upper())
# print('LowerCase is :', a.lower())


#Q.2) Remove all Trailing exclamation marks from the String.

a = 'Hello World !!!'
print("Removed word is :", a.rstrip("!"))

# Q.3) Replace Word "Jave" with the "Python".

b = 'I Love Java'
print("New Replace Word is :", b.replace("Java","Python"))


#Q.4) Split the Strings into a list of fruits.

s = "apple,banana,cherry"
print("Fruit List is :", s.split(" ")) 


#Q.5) Ceters the String wit the Width = 20.

c = 'PYTHON'
print('Centering hte string :', c.center(20))

#Q.6) Python program to check if "Hello, Anish" is ending with the "Anish".

d = 'Hello, Anish'
print('Checking :', d.endswith('Anish'))

# Q.7) Python program to print the substring "World" from the "Hello, World". (SLICING)

e = 'Hello, World'
print('Slicing then Result is :', e[7:12])

# Q.8) Program that asks the user for their first and last name then prints a greeting message.

# f = input('Enter your First name: \n')
# g = input('Enter your Last name: \n')
 
# print('Hello,', f, g)


'''
Q.9) Python Program that takes a number input from the user as a string, then converts it to an integer
     and then prints the square of the number.
'''

h = input("Enter number ")
i = int(h)

print('Square of the number is :' , i*i)