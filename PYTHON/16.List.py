# Storing Multiple value in one name ---> List
# List are changeable, meaning we can add new items in the list
# Tuple are not changeable meaning we can not add new items in the tuple.


# Simple list example:
list1 = ["Aple", "Orange", "Grapes"]
print(list1)
print(type(list1))
print(list1[1])
print(list1[2])
print(list1[0])

# negative Indexing
print(list1[-1] )             # Total item - 1  =>  (3 - 1)
print(list1[-3])
print(list1[-2], "\n")


if "Orange" in list1:
    print ("orange is present \n")
else :
    print("Orange is not present")


# RANGE in list:     list Slicing

listName = ['Candy', 'Choco', 'Bar' , 'Pie', 'Bean']
print(listName[:])
print(listName[1:3])
print(listName[1:4], '\n')


# list Comprehension
# => purano list ma new Rule apply garera n NEW List Banako.....

# Square of each numbers from ( 0- 4)

numbers = [1,2,3,4,5,6,7,8,9,0]
print(numbers)

numnber1 = [ x**2 for x in range(5)]
print(numnber1,'\n')

number2 = [ x**3 for x in range(10) if x % 2 == 0]
print(number2)


# append() use in the list => add the new item in the last position

listAni = [1,2,3,4,5]
listAni.append(6)
print(listAni, '\n')

# insert() use in the List => add the new item in the any posiiton of the list

listAni.insert(0 , 0)
print(listAni)