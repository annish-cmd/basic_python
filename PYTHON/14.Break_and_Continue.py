'''
without break statement, it cause Infinite loop in the 'while loop'.
break stops all the loop immediately once the condition matched 
Unlike 'continue' which only skips the current loop an dstarts next round.
'''

# break Statement:

print('****For the case of the BREAK*****')
for i in range(1,8) :
    if i == 5 :
        break               # Stops the loop when the i == 5
    print(i)

print ('Stopped of the program.')



# eg.1  Multiplication Table

# for i in range (12):
#     if i == 10 :
#         break
#     print("5 X" , i+1, "=", 5 * (i+1))



# continue Statement:

print('****For the case of the CONTINUE*****')
for i in range (1,8):
    if i == 5:
        continue                # Skips the 5 
    print(i)

print ('Stopped of the program.')




# Question Using both 'continue' and 'break'

print('****Question using both CONTINUE & BREAK*****')

while True :
    print ('What is Your Name ?')
    name = input()

    if name != 'anish' :
        continue                    # Go back to the start of the loop if the name is not 'anish'
    print('Hello anish, What is the Password ?')
    password = input()

    if password == 'python' :
        print('Access Granted')  
        break                      # Exit the loop after granting access

    else:
        print("Wrong Password")
    






