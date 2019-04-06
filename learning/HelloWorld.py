#Hello world print
print("Hello World")



#Mutliple assignment
Name, Age = "Kishore", 24
print(Name, Age)



#Placeholders
placehloder = "%s is my name and my age is %d"
print(placehloder % (Name, Age))



#Lists
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
#Max Min
ListNum = [10, 200, 100, 1000, 45000]
print(max(ListNum))



#Dictionaries (Should use clury braces)
Students = {"Bob": 15, "Mike": 20, "Ben": 10}
print(Students)
print(Students["Bob"])
Students["Bob"] = 20
print(Students["Bob"])
del Students["Mike"]
print(Students)
len(Students)












