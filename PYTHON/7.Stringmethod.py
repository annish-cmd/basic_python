# Strings are Immutable, cant change. But we can create new one.

a = "i love python"
print(len(a))

# upper() & lower()
print(a.upper())
print(a.lower())

# rstrip()
b = "Anish likes Python !!!"
print(b.rstrip("!"))
               
# replace()
c = 'Anish is Happy'
print(c.replace("Anish","Manish"))

# split() -> Split string into seperate string as list items.
d = 'Honey Moon'
print(d.split(' '))    # sapce must be used

# capitalize()
e = 'anish is working hard'
print(e.capitalize())

# center()
f = 'Anish likes Anime'
print(f.center(120))

# count()
g = 'I like Japan, Japan is good.'
print(g.count('Japan'))

# endsWith()
h = 'Ends with dot .'
print(h.endswith("."))    #True

# find()     ---> Output is given in the index, if not found then displays (-1).
i = 'What is inside my head ?'
print(i.find("is"))

# isalnum()
j = 'I am Anish1'
print(j.isalnum())   # if space is used then output displays 'False' automatically.

# istitle()
k = 'Hello I Am Python'
print(k.istitle())

# swapcase()
l = 'Testing Of The SwapCase'
print(l.swapcase())