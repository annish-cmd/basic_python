'''
Basic Questions

    Write a function add_numbers that takes two numbers as arguments, adds them, and returns the result.

    Define a function greet_user that takes a name as an argument and prints a greeting message.

    Write a function calculate_area to calculate the area of a rectangle using length and breadth. Use the return keyword to return the area.

    Create a function double_number that takes an integer as an input, doubles it, and prints the result without using return.

Intermediate Questions

    Explain the difference between global and local scope by writing a function that modifies a global variable and a local variable. Print both before and after calling the function.

    Write a function update_score that uses a global variable score. Increment the score by 10 whenever the function is called.

    Create a function factorial to calculate the factorial of a number using recursion.

    Write a function find_max that takes a list of numbers and returns the largest number in the list.

Advanced Questions

    Define a function nested_scope_example where:
        A local variable is defined inside the function.
        Another function inside it modifies that local variable using a nested function.

    Write a function is_palindrome that takes a string and checks whether it is a palindrome. Return True if it is, otherwise return False.

    Write a program where:
        A global variable counter is initialized to 0.
        A function increment_counter is defined to increment the counter by 1.
        Another function reset_counter resets the counter to 0.
        Use the functions and demonstrate how the global variable changes.

    Write a function fibonacci_sequence that takes an integer n and returns the first n terms of the Fibonacci series.

Logic-Building Challenges

    Create a function calculate_total_price that takes a list of item prices and a discount percentage as inputs. Return the total price after applying the discount.

    Write a function swap_variables that takes two arguments and returns them swapped.

    Write a function count_vowels that takes a string and returns the number of vowels in it.

    Write a function number_summary that takes a list of numbers and returns a dictionary with keys:
        "sum": Sum of all numbers
        "average": Average of the numbers
        "maximum": Largest number
        "minimum": Smallest number

Bonus Question

    Write a program to demonstrate the use of nonlocal inside a nested function. For example:
        A function outer_function defines a variable count.
        A nested inner_function modifies count using nonlocal.
'''

# -----------------------------------BASIC QUESTION----------------------------------------------

# 1. Write a function add_numbers that takes two numbers as arguments, adds them, and returns the result.

def add_numbers(a, b):
    add = a + b
    return add  # Return the result instead of printing it for reusing again.

# Use the function
a = 5
b = 4
result = add_numbers(a, b)
print(f"Add of {a} and {b} is: {result}")


# 2.Define a function greet_user that takes a name as an argument and prints a greeting message.

def greet_user(name):
    message = 'GoodMorning ' + name
    return message

name = 'Anish'
result = greet_user(name)
print(result) 


# 3. Write a function calculate_area to calculate the area of a rectangle using length and breadth. Use the return keyword to return the area.

def calculate_area (l,b):
    area = l * b
    return area

# Assign values to length and breadth
l = 5
b = 5

# Call the function
result = calculate_area(l, b)

# Print the result with proper formatting
print(f"The Length is {l} and the Breadth is {b}. Now, the Area is: {result}")



# 4.Create a function double_number that takes an integer as an input, doubles it, and prints the result without using return.

def double_number(num):
    doubles = num * 2  # Corrected formula for doubling
    print(doubles)  # Prints the doubled value

# Call the function
num = 2
double_number(num)  # Directly call the function

# If you need a formatted message:
print(f"The number {num} doubled is printed above. \n")




# -----------------------------------INTERMEDIATE QUESTION----------------------------------------------

# 1. Explain the difference between global and local scope by writing a function that modifies a global variable and a local variable.
#  Print both before and after calling the function.

'''
Global scope is declared outside of the function.  AND Local Scope is declared inside of the function.
Global scope can be accessed anywhere in the program. WHEREAS Local Scope can't accessed outside of the function.
'''
                                # GLOBAL SCOPE
global_variable = 100

def demo():
    print("Global variable inside of the function is :" , global_variable)
#method call
demo()
print("Global variable outside of the function is :" , global_variable ,'\n')


                                # LOCAL SCOPE
def anotherDemo():
    local_variable = 200
    print("Local variable inside of the function is :", local_variable)
#method call
anotherDemo()
print("Local variable outside of the function is cause error \n" )



# 2.Write a function update_score that uses a global variable score. Increment the score by 10 whenever the function is called.

score = 100
def update_score():
    global score                        # use  of the 'global' keyword when inside of the function
    score = score + 10
    return score

# function call
result = update_score()
print(f"The Updated score is: {result}")

# function call again
result = update_score()
print(f"The Updated score after another update is : {result}, \n ")



# 3. Create a function factorial to calculate the factorial of a number using recursion.

def factorial(num):
    if num == 0 or num == 1 :
        return 1
    else :
        return num * factorial( num -1)                         # recursion -> Function calling itself

#Function call
num = 4
result = factorial(num)
print(f"The Factorial of the number is : {result}, \n")


# 4. Write a function find_max that takes a list of numbers and returns the largest number in the list.

def find_max(numbers):
    return max(numbers)  # Use the built-in max() function

# Test the function
numbers = [1, 2, 3, 4, 5, 6]
result = find_max(numbers)
print(f"The largest number in the list is: {result}")



# 5.  Write a function find_max that takes a list of numbers and returns the largest number in the list.

