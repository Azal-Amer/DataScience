import collections
# 1
myList = [1,2,3,4,5,5,2,3,4,5,6,'a', 'a']
sumList = 0
for x in myList:
    if isinstance(x,int):
        sumList += (myList[x-1])
    else:
        sumList += 0
print(sumList)
# 2
keyString = 'lkseropewdssafsdfafkpwe'
print(collections.Counter(keyString).most_common(3))
# the collections library has a counter function that takes in a given string as an array, and can sort through it for the most frequent charecters. Result is printed as an object
#3
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dicsum = dict(dic1)
dicsum.update(dic2)
dicsum.update(dic3)
print(dicsum)
#4
myList4 = ['abc', 'xyz', 'aba', '1221']
conditionCount = 0
for x in myList4:
    if len(x) >=2 and x[0] == x[len(x)-1]:
        conditionCount+=1
print(conditionCount)
#5
myWords = ['red', 'grEEn', 'bLue', 'black', 'white', '5 1 1 1 1 1']
#Words to accept are RGB
myWordsKey = {'red':0, "green":0, "blue":0}
for x in myWords:
    if x.lower() == 'red':
        myWordsKey['red']+=1
    if x.lower() == 'green':
        myWordsKey['green']+=1
    if x.lower() == 'blue':
        myWordsKey['blue']+=1
print(myWordsKey)
#6
dupliList = []
for x in myList:
    if x not in dupliList:
        dupliList.append(x)
print(dupliList)