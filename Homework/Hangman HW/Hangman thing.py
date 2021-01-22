# input, random, time to delay
import random
import time
# ask user for information
name = input("What is your name? ")


# create a list of words
# pick a random word
# the user to guess
# wordList = ['pyhton', 'java', 'PHP', 'RAM', 'computer', 'keyboard']
wordListEasy = []
wordListMedium = []
wordListHard = []
with open('Homework\Hangman HW\Wordlist.txt', 'r') as file:
    for line in file: 
        words = 0
        wordict = 0
        # reading each word         
        for word in line.split():
            words+=1
            
            if wordict == 1:
                wordListEasy.append(word) 
            if wordict == 2:
                wordListMedium.append(word)
            if wordict == 3:
                wordListHard.append(word)  
            if word == 'LEVELONE':
                wordict = 1
            if word == 'LEVELTWO':
                wordict = 2  
            if word == 'LEVELTHREE':
                wordict = 3
          
print(name, end = '')
game = input(" , do you want to play? ")

print(wordListEasy)
print(wordListMedium)
print(wordListHard)
wordList = []

while game == 'yes':
    level = input("Easy, Medium, or Hard? (1,2,3)")
    #Level checker
    if int(level) == 1 or int(level) == 2 or int(level) == 3:
        savedLevel = int(level)
        if savedLevel == 1:
            wordList = wordListEasy.copy()
        if savedLevel == 2:
            wordList = wordListMedium.copy()
        if savedLevel == 3:
            wordList = wordListHard.copy()
    else:
        print("error, running in easy")
        wordlist = wordListEasy.copy
    word = random.choice(wordList)
    guess=''
    uniqueChar = set(word)
    turns= len(word) +5
    print (name, " ,you have " + str(turns) + " turns to guess the word", end='')
    print()
    winPoints = 0
    while turns>0 and winPoints< len(uniqueChar):
        for char in word:
            if char in guess:
                print(char, end=' ')
            else:
                print('_', end=' ')
        print()
        print(name, end=' ')
        letter= input(" please give me a letter : ")
        guess +=letter
        winPoints += 1
        turns -=1
    if winPoints == len(uniqueChar):
        print("you win yay! The word was " + word)
    else:
        print("loser. The word was " + word)
    game=input(" Do you want to play again ")
print(name, ", come back anytime!")
time.sleep(5)
# Need to add winning statement
#Need wordlist w/difficulty