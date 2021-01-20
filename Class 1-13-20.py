# #LISTS
# myList = ["apple", "orange", "banana", ]
# for x in myList:
#     print(x, end = ' ')
# print()

# myList.append("grapes")
# myList.insert(2,"grapes")
# for x in myList:
#     print(x, end = ' ')
# print()
# print(myList.count("grapes"))
# myList2 = []
# myList2 = myList.copy()
# myList2.append("strawberries")
# print()
# print(myList2)

# #Index
# index1 = myList.index("orange")
#index1 is equal to the index of the first instance the given datatype appeared
#To find other indecies that had the given value, you need to slice the list

# print(myList[index1])
# TUPLES
# myTuple= (1,2,3,5,6)
# print(myTuple)
# if 4 not in myTuple:

    
#     #Convert to list to edit
#     tupleList = list(myTuple)
#     #add your thing
#     tupleList.insert(3,4)
# #convert back to tuple
#     myTuple=tuple(tupleList)
#     print(myTuple)
#LISTS
# mySet = {"apple", "google", "microsoft", "tesla", "amazon", 42, 53}
# def printy():
#     for x in mySet:
#         print(x, end = ' ')
#     print()
    
# printy()
# mySet.update([" meow "], [" kitty "], [" meow " ])
# printy()
# print(len(mySet))
# mySet2 = {1,2,3,4,5,42,53}
# mySet3 = mySet.difference(mySet2)
# print(mySet3)
# mySet4 = mySet.union(mySet2)
# print(mySet4)
#DICTIONARIES
myDict={"name":"Azal","Age":16, "City":"dallas"}
print("The name of the student is", myDict["name"] )