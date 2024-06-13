#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 07:23:03 2024

@author: Tahsan
"""

###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList. It takes the 
# word network of all the words in wordList, represented as the corresponding 
# list of neighbor lists. It also takes a word called source in wordList and 
# it performs a breadth first search of the word network starting from
# the word source. In addition, it takes a list of words called easyWordList,
# all of which belong to wordList. These words have weight 0, whereas the remaining
# words have weight given by the non-negative integer parameter w.
# It returns a list containing two lists: (i) the parents of all words 
# reached by the search and (ii) the distances of these words from the source word.    
#
# Definition: The length of a path is the sum of the number of edges in the path
# plus the sum of the weights of all the nodes in the path.
#
# Definition: The distance between a pair of nodes u and v is the length of the
# shortest path betwwen them.
#
# Notes: 
# (a) If the length of wordList is n, then the returned list contains two lists,
# each of length n.
# (b) If the returned list is [L1, L2] and a word w has index i in wordList, then
# the parent information of w is stored in L1[i] and the distance information of
# w is stored in L2[i].
# (c) The parent information of a word is "" if it is the source word or if it
# is not reachable from the source word.
# (d) The distance information for any word that is not reachable from the source
# word is -1.
#
###############################################################################
def binarySearch(L, w, first, last):
    if (first > last):
        return -1
    
    mid = (first + last) // 2
    if (w == L[mid]):
        return mid
    elif (w < L[mid]):
        return binarySearch(L, w, first, mid-1)
    else:
        return binarySearch(L, w, mid+1, last)
    
def getIndex(L, w):
    return binarySearch(L, w, 0, len(L)-1)


def searchWeightedWordNetwork(wordList, nbrsList, source, easyWordList, w):
    processed = []
    
    if source not in easyWordList:    
     reached = [[source,w]]
    else:
      reached = [[source,0]]
     
     
     # Initialization: parent lists
    parents = [""]*len(wordList)
    distances = [-1]*len(wordList)
     
    sourceIndex = getIndex(wordList, source)
    distances[sourceIndex] = 0

     # Repeat until reached set becomes empty or target is reached 
    while reached:
         currentWord = reached[0][0]
         weight = reached[0][1]
         reached.pop(0)
         if weight == 0:
          currentWordIndex = getIndex(wordList, currentWord)
          currentNeighbors = nbrsList[currentWordIndex]
          for neighbor in currentNeighbors:
             if (neighbor not in reached) and (neighbor not in processed):
                
                 if neighbor in easyWordList:
                    reached.append([neighbor,0])
                    neighborIndex = getIndex(wordList, neighbor)
                    if parents[neighborIndex] == "":
                      parents[neighborIndex] = currentWord
                      distances[neighborIndex] = distances[currentWordIndex] + 1
                 else:
                    reached.append([neighbor,w])
                    neighborIndex = getIndex(wordList, neighbor)
                    if parents[neighborIndex] == "":
                      parents[neighborIndex] = currentWord
                      distances[neighborIndex] = distances[currentWordIndex] + 1 + w
                    
         if weight > 0:
              reached.append([currentWord, weight - 1])         
                 
         processed.append(currentWord)

    return [parents, distances]
###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList. It also takes a word 
# called source in wordList and a list of distances of all nodes in wordList
# from this network. It returns a list of words, in aphabetical order,
# that are between distance d1 and d2 from source (inclusive of d1 and d2).
# You can assume that d1 and d2 are non-negative integers and d1 <= d2. 
#
# You can assume that distanceList has been produced by a call to searchWordNetwork
# or searchWeightedWordNetwork. 
#
###############################################################################
def wordsAtDistanceRange(wordList, source, distanceList, d1, d2):
    distanceWordList = []
    for i in range(len(wordList)):
        if distanceList[i] >= d1 and d2 >= distanceList[i]:
        
            distanceWordList.append(wordList[i])
    
    distanceWordList.sort()
    return distanceWordList       

###############################################################################
# Main program

# Read parameters.txt; use default values if parameters.txt is missing
# The paremeters.txt file has the format:
#   p = value1
#   w = value2
#   ed1 = value3, ed2 = value4
#   hd1 = value5, hd2 = value6
#   eh = value7, hh = value8
#   r = value9
# ADD CODE HERE. Ideally, this should be a fuction call

def parameterFileRead():
   try: 
     f = open("parameters.txt","r")
     allNumList = []
     
     for line in f:
       string = "".join(line.split("="))
       string = string.rstrip()
       if line.count(",") > 0:
           string = string.replace(","," ")
       NumList = string.split("  ")
       allNumList.append(NumList)
       NumList = []
       string = ""
    
        
     p = int(allNumList[0][1])
     w = int(allNumList[1][1])
     ed1 = int(allNumList[2][1])
     ed2 = int(allNumList[2][3])
     hd1 = int(allNumList[3][1])
     hd2 = int(allNumList[3][3])
     eh = int(allNumList[4][1])
     hh = int(allNumList[4][3])
     r = float(allNumList[5][1])
    
     List = [p,w,ed1,ed2,hd1,hd2,eh,hh,r]
    
     return List
     
     f.close()

   except:
       p = 30
       w = 3
       ed1 = 5
       ed2 = 10
       hd1 = 8
       hd2 = 13
       eh = 2
       hh = 2
       r = 0.2
       List = [p,w,ed1,ed2,hd1,hd2,eh,hh,r]
       return List

# Functions for handling gameInformation file missing

def readWords():
    try:
        list = []
        word = ''
        with open("words.txt","r") as wordList:
            for words in wordList:
                word = words.rstrip()
                list.append(word)
        return list
    except:
        return []
            
def computeFrequencies(smallerWordList, fileNameList):
    n = len(smallerWordList)
    wordFrequencyList = [0]*n
    
    for eachFile in fileNameList:
            try:
               with open(eachFile,'r') as file:
                for eachSentence in file:
                    for eachCharacter in eachSentence:
                       if eachCharacter.isalpha() == False:
                           eachSentence = eachSentence.replace(eachCharacter,' ')
                    eachWord = eachSentence.split()
                    for i in range(len(smallerWordList)):
                       m = eachWord.count(smallerWordList[i])
                       wordFrequencyList[i] += m
            except:
                continue
           
    return wordFrequencyList

def areNeighbors(w1, w2):
     count = 0
     for i in range(len(w1)):
         count = count + (w1[i] != w2[i])

     return (count == 1)

def fastMakeNeighborLists(wordList):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    possibleWord = ""
   
    nbrsList = []
    
    for i in range(len(wordList)):
        tempList = []
        for j in range(len(wordList[i])):
            for k in range(len(alphabets)):
                    possibleWord += wordList[i][0:j]
                    possibleWord += alphabets[k]
                    possibleWord += wordList[i][j+1:]
                    if (getIndex(wordList, possibleWord) != -1) and (possibleWord != wordList[i]):
                        tempList.append(possibleWord)
                    possibleWord = ""
                       
        tempList.sort()
        nbrsList.append(tempList)            
                        
    return nbrsList


def findComponents(wordList, nbrsList):
     processedList = []
     compList = []
     
     for i in range(len(wordList)):
         if wordList[i] not in processedList:
             reachedList = [wordList[i]]
             currentComp = []
             while reachedList != []:
                 currentWord = reachedList.pop()
                 if currentWord not in processedList:
                     processedList.append(currentWord)
                     currentComp.append(currentWord)
                     for word in nbrsList[getIndex(wordList,currentWord)]:
                         if word not in processedList:
                             reachedList.append(word)
             compList.append(currentComp)
             
     for j in range(len(compList)):
         compList[j].sort()
     
      
     return compList

def largestComponent():
     wordList = readWords()
     nbrsList = fastMakeNeighborLists(wordList)
     CompList = findComponents(wordList, nbrsList)
     maxLen = len(CompList[0])
     ind = 0
     largestCompList = [] 
     for i in range(len(CompList)):
         if len(CompList[i]) > maxLen:
             maxLen = len(CompList[i])
             ind = i

     for j in range(len(CompList[ind])):
         largestCompList.append(CompList[ind][j])
     
     return largestCompList          
def frequencyList():
   
    str = ''
    with open('parameters.txt','r') as file:
       for eachLine in file:
           for i in range(len(eachLine)):
            if eachLine[i].isdigit():
               str += eachLine[i]
           break
       p = int(str)
       
    
    filesList = ['pg1342.txt','pg2641.txt','pg2701.txt','pg37106.txt','pg64317.txt','pg84.txt']
    largestCompList = largestComponent()
    freqList = computeFrequencies(largestCompList, filesList)
    List1 = []
    sortedDegreeList = []
    
        

    for i in range(len(freqList)):
        temp = []
        temp.append(freqList[i])
        temp.append(largestCompList[i])
        List1.append(temp)
    List1.sort()


    
    for i in range(len(largestCompList)):
        sortedDegreeList.append(List1[i][1])
    
     
    
    hardWordLen = int(len(sortedDegreeList) * (1-(0.01 * p)))
    
    easyWordList = []
    hardWordList = []
    
    for i in range(hardWordLen):
        hardWordList.append(sortedDegreeList[i])

  
    
    ind = hardWordLen
   
    for k in range(ind,len(sortedDegreeList)):
        easyWordList.append(sortedDegreeList[k])

   
  
    easyWordList.sort()
    hardWordList.sort()
    
    return easyWordList, hardWordList
    

# Read gameInformation.txt 
# Create easyWordList, hardWordList, wordList, nbrsList
# if gameInformation.txt is missing, provide a message to the user and construct all these lists
# from scratch.
# ADD CODE HERE. Ideally, this should be a function call


def readGameFile():
   try:
    f = open("gameInformation.txt",'r')
    easyWordList = []
    hardWordList = []
    nbrsList = []
    easyWordLen = int(f.readline())

    i = 0
    wordList = []
    for line in f:
           line = line.rstrip()  
           
           if i < easyWordLen:
               easyWordList.append(line)
           elif i == easyWordLen:
               hardWordLen = int(line)
           elif i > easyWordLen and i < easyWordLen + hardWordLen:
               hardWordList.append(line)    
           elif i == easyWordLen + hardWordLen + 1:
               wordListLen = int(line)
           elif i > easyWordLen + hardWordLen + 1:
               if i < easyWordLen + hardWordLen + wordListLen + 2:
                  wordList.append(line)
               else:
                 line = line.split(",")
                 nbrsList.append(line) 
   
           i += 1
    return easyWordList, hardWordList, nbrsList, wordList
    f.close() 
 
   except:
       print("Game File missing. Please wait while we retrieve all the data for the game") 
       easyWordList, hardWordList = frequencyList()
       largestComp = largestComponent()
       nbrsList = fastMakeNeighborLists(largestComp)
       return easyWordList, hardWordList, nbrsList, largestComp 

        

# Start initial user interaction
# Welcome them to the game and ask them to pick game playing mode.
# E for "easy mode" and H for "hard mode"
# ADD CODE HERE

print("Welcome to word ladder!!!")



# Once user has picked a mode, initialize parameter values for the game.
# (a) [d1, d2] = [ed1, ed2] for easy mode, [d1, d2] = [hd1, hd2] for hard mode
# (b) numWordHints = eh for easy mode, numWordHints = hh for hard mode 
# (c) distanceHintRate = r
# In the easy mode, pick a random word from easyWordList
# In the hard mode, pick a random word from wordList
# This is your target word.
# ADD CODE HERE

import random
valueList = parameterFileRead()
easyWordList, hardWordList, nbrsList, wordList = readGameFile()

while True:
 mode = input("Pree E for 'Easy Mode' and H for 'Hard Mode': ")
 if mode.upper() == 'E':
    target = random.choice(easyWordList)
    d1 = valueList[2]
    d2 = valueList[3]
    numWordHints = valueList[6]
    break
 elif mode.upper() == 'H':
    target = random.choice(hardWordList)
    d1 = valueList[4]
    d2 = valueList[5]
    numWordHints = valueList[7]
    break
 else:
    print("Invalid mode selection. Please select either 'E' for Easy Mode or 'H' for Hard Mode.")

distanceHintRate = valueList[8]



# (a) Call searchWeightedWordNetwork(wordList, nbrsList, target, easyWordList, w) 
# to get parentList and distanceList
# (b) Call wordsAtDistanceRange(wordList, target, distanceList, d1, d2)
# to obtain all words at distance in the range [d1, d2] from target.
# Pick a word at random from this list; this is your source word
# ADD CODE HERE

w = valueList[1]

Lists1 = searchWeightedWordNetwork(wordList, nbrsList, target, easyWordList, w)
parentList = Lists1[0]

distanceList = Lists1[1]

distanceWordList = wordsAtDistanceRange(wordList, target, distanceList, d1, d2)
source = random.choice(distanceWordList)



# Start main user interaction
# Provide the source word and target word. Ask the user to complete the word ladder
# from source word to target word. Let them know if they need to type the source word 
# and target word also. Inform them that they can type "Q" to quit the game at any 
# point and "H" if they want a next word hint.
# MAke sure messsages are clear. For example, you could use:
# "Excellent!" if the next word they type is a valid word in the ladder
# "Not a word in my dictionary!" if the next word they typs is not a word in wordList
# "The ladder can't go from xxxxx to yyyyy!" if the current word yyyyy is not a neighbor 
# of the previous word "xxxxx"
# ADD CODE HERE
print("Here is the target word: ", target)
print("                                   ")
print("Here is the source Word: ",source)
print("                                    ")
print("1. Complete the word ladder by typing words that are between source to target")
print("2. Do not type source and target word")
print("3. Type Q at any time if you want to quit the game")
print("4. Type H if you need next word hint")
print("                                      ")
print("             !!!Good Luck!!!             ")

currentWord = source
count = 0
coin = ''
while True:
    if random.random() <= distanceHintRate:
        coin = 'Heads'
    else:
        coin = 'Tails'
    ans = input("Enter Word: ")
    if ans == source:
        print("The word is already accepted in the ladder!!!")
        continue
    if ans == target:
        print("You can't enter the target word!!!")
        continue
    if ans.upper() == 'Q':
        print("Game Over")
        break
    if ans.upper() == 'H':
        if count == numWordHints:
            print("Limit reached!!!")
            count += 1
            continue
        elif count >= 0 and count < numWordHints:
            count += 1
            ind = getIndex(wordList, currentWord)
            print("The first 3 letters of each words that are connected to previous word ")
            print("are given as hint")
            print("One or more than one is correct")
            print("Number of hints remaining: ", numWordHints - count)
            for i in range(len(nbrsList[ind])):
                    print(nbrsList[ind][i][0:3])               
         
        continue 
    if ans not in wordList:
      print("Not a word in my dictionary!")
    else:
        ind = getIndex(wordList, currentWord)
        if ans in nbrsList[ind]:
            print("Excellent!")
            previousWord = currentWord
            currentWord = ans
            ind2 = getIndex(distanceWordList, target)
            if currentWord == distanceWordList[ind2 - 1]:
                print("                           ")
                print("Congratulations you won!!!")
                break
            if coin == 'Heads':
                ind3 = getIndex(distanceWordList, target)
                ind1 = getIndex(distanceWordList, currentWord)
                print(abs(ind3 - ind1)," words remaining")
        else:
            print("The ladder can't go from ", currentWord, "to ", ans)
    

