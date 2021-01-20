myTuple= (1,2,3,5,6)
print(myTuple)
if 4 not in myTuple:

    
    #Convert to list to edit
    tupleList = list(myTuple)
    #add your thing
    tupleList.insert(3,4)
#convert back to tuple
    myTuple=tuple(tupleList)
    print(myTuple)
