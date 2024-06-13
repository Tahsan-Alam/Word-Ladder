#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:12:30 2024

@author: Tahsan 
"""

###############################################################################
#
# Specification: The function reads words from the file "words.txt" and creates and
# returns a list with these words. The words should in the same order in the list
# as they appear in the file. Each string in the list of words should be exactly
# 5 characters long.
#
# NEW: if the file word.txt is missing, this function should just return [] instead
# of causing the program to cause an exception.
#
# Examples:
# >>> L = readWords()
# >>> len(L)
# 5757
# >>> L[len(L)-1]
# 'zowie'
# >>> L[0:10]
# ['aargh',
#  'abaca',
#  'abaci',
#  'aback',
#  'abaft',
#  'abase',
#  'abash',
#  'abate',
#  'abbey',
#  'abbot']
# >>> L[1000]
# 'coney'
# >>> sorted(L)==L
# True
#
###############################################################################
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
            
            
    
###############################################################################     
#
# Specification:  This function takes a list of words and a list of file names.
# It reads from each file in the given list of file names and extracts words from
# the file. For each word in the list of words, it computes the frequency of this
# word in all the files in the given list of file names. The function returns
# the list of frequencies. The order in which frequencies appear in the frequency
# list should match the order in which words appear in the given word list. In other
# words, the frequency in slot 0 should be the frequency of smallerWordList[0],
# the frequency in slot 1 should be the frequency of smallerWordList[1], etc.
# The function should use "try and except" to gracefully deal with missing files.
# If a file is missing, it should just skip over to the next file. If all files
# are missing, then the frequency list returned should contain all 0's.
#
###############################################################################   
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

            
        

############################################################################### 
# You can add as many other functions as you want to make your code streamlined,
# readable, and efficient
############################################################################### 


############################################################################### 
# main program starts here
############################################################################### 

# STEP 1: Identify the list of words in the largest connected component
# (a) Read the list of all words in words.txt. Make sure that the 
# program exits gracefully if words.txt is not available
# (b) Build the adjacency list representation of the word network of this list of 
# words
# (c) Find all connected components of this word network
# (d) Identify the largest connected component and create a list with the words 
# in the largest connected component in sorted order
#
# Code for STEP 1 goes here
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

def areNeighbors(w1, w2):
    # Algorithm: Walk down both strings w1 and w2 and count the number of indices 
    # at which w1 and w2 have distinct characters. If this count <= 1, then the function
    # should return True; otherwise False
    # This algorithm can be implemented using a single for-loop
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
   
    


# STEP 2: Compute the frequencies of all the words in the largest connected component
# and designate the p % of the words with highest frequency as "easy" words  
# (a) Create a list containing all the names of text files downloaded from Project Gutenberg
# (b) Call the function computeFrequencies to read from these files, extract words, and
# update the frequencies of the words in the largest connected component  
# (c) Read from the file parameters.txt to get the value of parameter p
# (d) Designate the most frequent  p % of these words as "easy" words and the rest
# as "hard" words 
#
# Code for STEP 2 goes here


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

   
    List2 = []
    easyWordList.sort()
    hardWordList.sort()
   
    List2.append(easyWordList)
    List2.append(hardWordList)
    
    return List2

    
    
    
            
# STEP 3: Write into the file gameInformation.txt
# (a) Open the file "gameInformation.txt" for writing
# (b) Write the number of easy words, followed by the easy words themselves in alphabetical order
# (c) Write the number of hard words, followed by the hard words themselves in alphabetical order
# (d) Write the adjacency list representation of the word network of the largest connected component
#
# Code for STEP 3 goes here

def writeFile():
  
  f = open("gameInformation.txt","w")
  freqList = frequencyList()
  largestComp = largestComponent()
  nbrsList = fastMakeNeighborLists(largestComp)
  
  f.write(str(len(freqList[0])) + "\n")
  
  
  for i in range(len(freqList[0])):
      f.write(freqList[0][i] + "\n")
      
  f.write(str(len(freqList[1])) + "\n")
  
  for j in range(len(freqList[1])):
      f.write(freqList[1][j] + "\n")
  
  f.write(str(len(largestComp)) + "\n")
  
  for i in range(len(largestComp)):
      f.write(largestComp[i] + "\n")
      
  for i in range(len(nbrsList)):
       f.write(",".join(nbrsList[i]) + "\n")
  
  f.close()
 
