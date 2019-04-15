# Hello world print
print("Hello World")

# Mutliple assignment
Name, Age = "Kishore", 24
print(Name, Age)

# Placeholders
placehloder = "%s is my name and my age is %d"
print(placehloder % (Name, Age))

# Lists
Shoplist = ["Apple", "Orange", "grapes"]
print(Shoplist)
Shoplist[0] = "Cheese"
print(Shoplist[0])
del Shoplist[2]
print(Shoplist)
Shoplist.append("appended Fruit")
print(len(Shoplist))
Shoplist2 = ["Hershey's", "Dairy milk", "Kitkat"]
print(Shoplist + Shoplist2)
# Max Min
ListNum = [10, 200, 100, 1000, 45000]
print(max(ListNum))

# Dictionaries (Should use clury braces)
Students = {"Bob": 15, "Mike": 20, "Ben": 10}
print(Students)
print(Students["Bob"])
Students["Bob"] = 20
print(Students["Bob"])
del Students["Mike"]
print(Students)
len(Students)

# Tuples (Similar to list but cannot modify or remove specific item values)
tup = ("Orange", "Apple", "Grapes")
print(tup)
print(tup[0])

# Conditional statements(if, else, elif, and, or)
if (5 > 5):
    print("It's true ")
    print("So we say Hello")
else:
    print("It's false and so we say bye")
age = 13
if (age < 13):
    print("You are young")
elif (age >= 13 and age < 18):
    print("You are a teenager")
else:
    print("You are an adult")

# For Loops(range,increments, nested for loops)
list1 = ["Apple", "Bananas", "Cherries"]
tupp1 = (13, 2, 5)
for item in list1:
    print(item)
for item in tupp1:
    print(item)
for i in range(0, 10):
    print(i)
for i in range(0, 11):
    print(i)
# i++ incremental way
for i in range(0, 11, 2):
    print(i)
for i in range(20, 26):
    for j in range(26, 31):
        print(i + j)

# While loops(runs until condition becomes false) and Control statements(break, continue and pass)
c = 0
while c < 5:
    print(c)
    c = c + 1
c = 0
# Stops after 2
while c < 5:
    print(c)
    if c == 2:
        break
    c = c + 1
c = 0
# Skips to print 2 and continue
while c < 5:
    c = c + 1
    if c == 2:
        continue
    print(c)

# Try and Except case
try:
    if name > 3:
        print("It's 3")
except:
    print("There is something wrong with the code")


# Functions
def first_function():
    print("hello first function")


first_function()


def greeting(name):
    print("Hi " + name + "!")


greeting("Kishore")


def add(num1, num2):
    print(4 + num1 + num2)


add(4, 2)


def return_add(num1, num2):
    return num1 + num2


summation = return_add(5, 4)
print(summation)

"""InBuilt functions:
abs(-100): absolute function is used to print any number in positive
bool(0): Boolean 0 always returns false and for all other values returns true
dir("String"): Dir function is used to indentify the usages of that practicular value based on data types
"""
sent = "Hello"
print(dir(sent))
help(sent.upper)
help(sent.__init__())
help(sent.splitlines())
sent = 'Print("Hi")'
# eval(sent)
