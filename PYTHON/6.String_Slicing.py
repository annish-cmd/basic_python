# String Slicing -> Extracting specific part of the string.

print("***** String slicing *****")

name = 'Anish'
print(len(name))        # String Length

print(name[0:4])


for character in name:
    print(character)


# Hard One for the String Slicing

nameLength = 'Anish, Chauhan!'
print(len(nameLength))

print(nameLength[0:14])    #include 0 but not 14
print(nameLength[1:5])
print(nameLength[2:10])    #include 2 but not 10

for i in nameLength:
    print(i)