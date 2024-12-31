'''
Q.1) WAP for a loop  that iterates over the numbers from 1 to 10. Use a break statement to exit the 
    loop  when the number is 5.
'''

# print('**** Question 1 BREAK ****')

# for num in range (1,10):
#     if num == 5 :
#         break               # terminates once condition matched
#     print(num)
# print("these are the outputs")


'''
Q. 2) Use continue statement incase of break in the Q. 1)  (1 to 10)
'''
# print('**** Question 2 CONTINUE ****')

# for i in range (1,10):
#     if i == 5 :
#         continue         # skips the 5
#     print(i)
# print('End of the program')



'''
Q 3) WAP while loop that starts wit a variable n = 0 and increments n by 1 in each iteration.
'''

# print('**** Question 3 combination of both ****')

# n = 0
# while n < 10:
#         n = n + 1
#         if  n % 2 == 0 :
#               continue       
#         print(n)
#         if n == 10 :
#             break
       

'''
Q 3) Write a nested loop where the outer loop iterates over the numbers 1 to 3, and the inner loop iterates 
over the numbers 1 to 5. Use a break statement in the inner loop to exit when the number 3 is encountered
'''

for i in range(1,4) :             # Outer Loop which iterates (1,2,3)
      for j in range (1,6):       # Inner Loop which iterates (1,2,3,4,5)
            if j == 3:
                  print(j)
                  break
            print(i)






