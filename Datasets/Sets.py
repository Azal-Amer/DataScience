

mySet = {"apple", "google", "microsoft", "tesla", "amazon", 42, 53}
def printy():
    for x in mySet:
        print(x, end = ' ')
    print()
    
printy()
mySet.update([" meow "], [" kitty "], [" meow " ])
printy()
print(len(mySet))
mySet2 = {1,2,3,4,5,42,53}
mySet3 = mySet.difference(mySet2)
print(mySet3)
mySet4 = mySet.union(mySet2)
print(mySet4)
