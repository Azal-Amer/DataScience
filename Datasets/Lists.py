#LISTS
myList = ["apple", "orange", "banana", ]
for x in myList:
    print(x, end = ' ')
print()

myList.append("grapes")
myList.insert(2,"grapes")
for x in myList:
    print(x, end = ' ')
print()
print(myList.count("grapes"))
myList2 = []
myList2 = myList.copy()
myList2.append("strawberries")
print()
print(myList2)

#Index
index1 = myList.index("orange")
# index1 is equal to the index of the first instance the given datatype appeared
# To find other indecies that had the given value, you need to slice the list

print(myList[index1])
