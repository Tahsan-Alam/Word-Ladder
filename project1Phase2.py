#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:12:30 2024

@author: Tahsan
"""

#################### Project 1 Phase 1 #######################################

###############################################################################
#
# Specification: This function uses the binary search algorithm to search for 
# the given word w in the sublist L[first:last+1]. 
# It assumes that L is sorted in non-decreasing order. The function returns -1 if w is 
# not in L; otherwise it returns the index of w in L. If there are multiple occurances 
# of w in L, it just returns the index of an arbitrary occurance of w.
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

###############################################################################
#
# Specification: This function searches for the given word w in the given list L by
# calling the binarySearch function. It assumes that L is sorted in non-decreasing order.
# The function returns -1 if w is not in L; otherwise it returns the index of w in
# L. If there are multiple occurances of w in L, it just returns the index of 
# an arbitrary w.
# 
###############################################################################
def getIndex(L, w):
    return binarySearch(L, w, 0, len(L)-1)

###############################################################################
#
# Specification: This function takes two nonempty, equal-length strings w1 and w2 and 
# returns True if w2 is obtained from w1 by replacing one character
# in w1 by another (different) character; otherwise the function returns False. 
#
# Note: The replacement character cannot be identical to the character being replaced.
#
# Examples:
# >>> areNeighbors("Hello", "cello")
# True
# >>> areNeighbors("Hello", "cells")
# False
# >>> areNeighbors("Hello", "hello")
# True
# >>> areNeighbors("Hello", "belto")
# False
# >>> areNeighbors("Hello", "Hello")
# False
#
###############################################################################
def areNeighbors(w1, w2):
    isFalse = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            isFalse += 1
    if isFalse > 1 or isFalse == 0:
        return False
    else:
        return True
                

###############################################################################
#
# Specification: The function reads words from the file "words.txt" and creates and
# returns a list with these words. The words should in the same order in the list
# as they appear in the file. Each string in the list of words should be exactly
# 5 characters long.
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
    list = []
    word = ''
    with open("words.txt","r") as wordList:
        for words in wordList:
            word = words.rstrip()
            list.append(word)
    return list
    
######################################################################
#
# Specification: You are given a list L of distinct, equal-length strings. We 
# define two distinct strings w1 and w2 to be neighbors if w2 can be obtained from 
# w1 by replacing one character in w1 by another (different) character. In other words, w1 and w2 
# are neighbors if areNeighbors(w1, w2) is True. The function is required to return 
# the list of neighbor lists of each word in L. 
#
# EXAMPLE 1
# L = ['added', 'aider', 'aides', 'ailed', 'aimed', 'aired', 'anded', 'bided', 
#      'sided', 'tided']
#
# makeNeighborLists(L) returns
#
# [['anded'],
# ['aides'],
# ['aider'],
# ['aimed', 'aired'],
# ['ailed', 'aired'],
# ['ailed', 'aimed'],
# ['added'],
# ['sided', 'tided'],
# ['bided', 'tided'],
# ['bided', 'sided']]
#
# In this example, "added" is the first word in L and it has one neighbor
# in L, which is "anded". So ["anded"] is the first item in the returned list.
# The 4th word in L is "ailed" and it has two neighbors "aimed" and "aired".
# So the 4th item in the returned list is ["aimed", "aired"].
#
# EXAMPLE 2
# L = ['joked', 'poked', 'toked', 'yokel', 'yokes', 'yodel', 
#      'yoked', 'cokes', 'jokes', 'pokes', 'tokes', 'yikes', 
#      'yores', 'folks', 'yolky', 'folky', 'yolks']
#
# makeNeighborLists(L) returns
#
# [['poked', 'toked', 'yoked', 'jokes'],
# ['joked', 'toked', 'yoked', 'pokes'],
# ['joked', 'poked', 'yoked', 'tokes'],
# ['yokes', 'yodel', 'yoked'],
# ['yokel', 'yoked', 'cokes', 'jokes', 'pokes', 'tokes', 'yikes', 'yores'],
# ['yokel'],
# ['joked', 'poked', 'toked', 'yokel', 'yokes'],
# ['yokes', 'jokes', 'pokes', 'tokes'],
# ['joked', 'yokes', 'cokes', 'pokes', 'tokes'],
# ['poked', 'yokes', 'cokes', 'jokes', 'tokes'],
# ['toked', 'yokes', 'cokes', 'jokes', 'pokes'],
# ['yokes'],
# ['yokes'],
# ['folky', 'yolks'],
# ['folky', 'yolks'],
# ['folks', 'yolky'],
# ['folks', 'yolky']]
#
#
# NOTES
# (i) The neighbor lists should appear in the order corresponding to words in L. In 
# other words if we call the returned list nbrList, then the list of neighbors of
# the word L[0] should appear as nbrList[0].
# (ii) Each list of neighbors should contain words in the same order as in L. For
# example, the neighbor list of "ailed" should be ["aimed", "aired"] rather than
# ["aired", "aimed"].
# (iii) The neighbor relationship is only defined for distinct words. So a word
# cannot be its own neighbor.
#
# ADDITIONAL EXAMPLES:
# >>> L1 = ['added', 'aided', 'bided']
# >>> makeNeighborLists(L1)
# [['aided'], ['added', 'bided'], ['aided']]
# >>> L2 = ['joked', 'jokes', 'yikes', 'yokel', 'yokes']
# >>> makeNeighborLists(L2)
# [['jokes'],
#  ['joked', 'yokes'],
#  ['yokes'],
#  ['yokes'],
#  ['jokes', 'yikes', 'yokel']]
# 
######################################################################
def makeNeighborLists(wordList):
    nbrList = []
    for word in range(len(wordList)):
        List = []
        for nextWord in range(len(wordList)):
            if areNeighbors(wordList[word], wordList[nextWord]):
                List.append(wordList[nextWord])     
        nbrList.append(List)
        
    return nbrList         
     
            

###############################################################################
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. In addition, it takes
# a word w in wordList and returns the list of neighbors of this word in wordList.
# The returned list of neighbors is sorted (in increasing alphabetical order). 
#
# EXAMPLES:
# >>> L1 = ['added', 'aided', 'bided']
# >>> nL1 = makeNeighborLists(L1)
# >>> getNeighbors(L1, nL1, 'aided')
# ['added', 'bided']
# >>> getNeighbors(L1, nL1, 'added')
# ['aided']
# >>> getNeighbors(L1, nL1, 'bided')
# ['aided']
# >>> L2 = ['joked', 'jokes', 'yikes', 'yokel', 'yokes']
# >>> nL2 = makeNeighborLists(L2)
# >>> getNeighbors(L2, nL2, 'yokes')
# ['jokes', 'yikes', 'yokel']
# >>> getNeighbors(L2, nL2, 'joked')
# ['jokes']
# >>> getNeighbors(L2, nL2, 'jokes')
# ['joked', 'yokes']
#
###############################################################################
def getNeighbors(wordList, nbrsList, w):
    for i in range(len(nbrsList)):
        if wordList[i] == w:
            return nbrsList[i]

###############################################################################
# 
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It returns all words 
# with 0 neighbors, i.e., isolated nodes.
#
# EXAMPLES:
# >>> L = ['abbey', 'added', 'aided', 'audio', 'audit', 'bided', 'young']
# >>> nL = makeNeighborLists(L)
# >>> getIsolatedNodes(L, nL)
# ['abbey', 'young']    
# >>> L = ['aargh',
#          'abaft',
#          'abbey',
#          'abbot',
#          'abeam',
#          'abhor',
#          'absit',
#          'abuzz',
#          'abyss',
#          'achoo',
#          'acids',
#          'acrid',
#          'actin',
#          'actor',
#          'acute',
#          'adage',
#          'addle',
#          'adieu',
#          'adios',
#          'adlib']
# >>> nL = makeNeighborLists(L)
# >>> getIsolatedNodes(L, nL)
# ['aargh',
#  'abaft',
#  'abbey',
#  'abbot',
#  'abeam',
#  'abhor',
#  'absit',
#  'abuzz',
#  'abyss',
#  'achoo',
#  'acids',
#  'acrid',
#  'actin',
#  'actor',
#  'acute',
#  'adage',
#  'addle',
#  'adieu',
#  'adios',
#  'adlib']  
#
###############################################################################
def getIsolatedNodes(wordList, nbrsList):
    isolatednodes = []
    for i in range(len(wordList)):
        if nbrsList[i] == []:
            isolatednodes.append(wordList[i])
    return isolatednodes


###############################################################################
# 
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It returns all pairs of 
# nodes that are connected to each other, but to no other node.
# 
# EXAMPLES:
# >>> L = ['abbey', 'added', 'aided', 'audio', 'audit', 'bided', 'young']
# >>> nL = makeNeighborLists(L)
# >>> getIsolatedEdges(L, nL)
# [['audio', 'audit']]
# >>> L.extend(['joked', 'jokes'])
# >>> L.sort()
# >>> nL = makeNeighborLists(L)
# >>> getIsolatedEdges(L, nL)
# [['audio', 'audit'], ['joked', 'jokes']]
# >>> L = ['aided', 'bided', 'sided', 'tided']
# >>> nL = makeNeighborLists(L)
# >>> getIsolatedEdges(L, nL)
# []
#
###############################################################################
def getIsolatedEdges(wordList, nbrsList):
    isolatedEdges = []
    for i in range(len(wordList) - 1):
        temp = []
        if len(nbrsList[i])== 1 and len(nbrsList[i+1]) == 1:
                if wordList[i] == nbrsList[i+1][0] and nbrsList[i][0] == wordList[i+1]:
                  temp.append(wordList[i])
                  temp.append(wordList[i+1])
                  isolatedEdges.append(temp)
    return isolatedEdges              

###############################################################################
# 
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It returns the list 
# of words in wordList but in non-decreasing order of degree. Remember that the 
# degree of a node in the network is the number of neighbors it has. Two words 
# with the same degree appear in alphabetical order.
#
# EXAMPLES:
# >>> L1 = ['added', 'aided', 'bided']
# >>> sortByDegree(L1, makeNeighborLists(L1))
# ['added', 'bided', 'aided']
# >>> L2 = ['joked', 'jokes', 'yikes', 'yokel', 'yokes']
# >>> sortByDegree(L2, makeNeighborLists(L2))
# ['joked', 'yikes', 'yokel', 'jokes', 'yokes']  
# >>> L3 = ['added', 'aider', 'aides', 'ailed', 'aimed', 'aired', 'anded', 'bided', 'sided', 'tided']
# >>> sortByDegree(L3, makeNeighborLists(L3))
# ['added',
#  'aider',
#  'aides',
#  'anded',
#  'ailed',
#  'aimed',
#  'aired',
#  'bided',
#  'sided',
#  'tided']
#
###############################################################################
def sortByDegree(wordList, nbrsList):
    sortedList = []
    
    for lenNum in range(len(wordList)):
        for j in range(len(wordList)):
            if len(nbrsList[j]) == lenNum:
                sortedList.append(wordList[j])
    return sortedList
                
        
###############################################################################
# 
# Specification: This function returns the distributions of the degrees of the nodes
# in the word network specified by wordList and nbrsList. wordList is a non-empty, 
# sorted (in increasing alphabetical order) list of words  and nbrsList is the word 
# network of wordList represented as the corresponding list of neighbor lists. The
# function returns a list of nonnegative integers, where the integer at index i is the
# number of nodes in the word network with degree i. The length of the returned list
# is 1 plus the maximum degree of the word network.
#
# EXAMPLES:
# >>> L1 = ['added', 'aided', 'bided']
# >>> degreeDistribution(L1, makeNeighborLists(L1))
# [0, 2, 1]
# >>> L2 = ['joked', 'jokes', 'yikes', 'yokel', 'yokes']
# >>> degreeDistribution(L2, makeNeighborLists(L2))
# [0, 3, 1, 1]
# >>> L3 = ['added', 'aider', 'aides', 'ailed', 'aimed', 'aired', 'anded', 'bided', 'sided', 'tided']
# >>> degreeDistribution(L3, makeNeighborLists(L3))
# [0, 4, 6]
#
###############################################################################
def degreeDistribution(wordList, nbrsList):
    degreeOfNodes = []
    maxLen = 0
    
    for i in range(len(nbrsList)):
        if len(nbrsList[i]) > maxLen:
            maxLen = len(nbrsList[i])
    maxLen = maxLen + 1
    degreeOfNodes = [0] * maxLen
    
    for j in range(len(nbrsList)):
        n = len(nbrsList[j])
        degreeOfNodes[n] += 1 
    
        
    return degreeOfNodes




##################### Project 1 Phase 2 ######################################


###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It also take a word
# called source and it performs a breadth first search of the word network starting from
# the word source. It returns a list containing two lists: (i) the parents of all words 
# reached by the search and (ii) the distances of these words from the source word.    
#
# Examples: 
# >>> L1 = ['added', 'aided', 'bided']
# >>> nL1 = makeNeighborLists(L1)
# >>> searchWordNetwork(L1, nL1, "aided")
# [['aided', '', 'aided'], [1, 0, 1]]
# >>> searchWordNetwork(L1, nL1, "added")
# [['', 'added', 'aided'], [0, 1, 2]]
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
# Two more examples: 
# >>> L2 = ["bided", "bides", "sided", "sides", "tided", "tides"]
# >>> nL2 = makeNeighborLists(L2)
# >>> searchWordNetwork(L2, nL2, "tides")
# [['bides', 'tides', 'sides', 'tides', 'tides', ''], [2, 1, 2, 1, 1, 0]]
#
###############################################################################
def searchWordNetwork(wordList, nbrsList, source):
    n = len(wordList) 
    parentList = ['']*n
    processedList = []
    reachedList = [source]
    distanceList = [0]*n
    
    
    while reachedList != []:
        m = reachedList.pop(0)
        ind = wordList.index(m)
        
            
        for i in range(len(nbrsList[ind])):
            if nbrsList[ind][i] not in processedList and nbrsList[ind][i] not in reachedList:
                reachedList.append(nbrsList[ind][i])
                ind1 = wordList.index(nbrsList[ind][i])
                parentList[ind1] = wordList[ind]
                if wordList[ind] != source:
                    distanceList[ind1] += distanceList[ind] + 1
                else:
                    distanceList[ind1] = 1  
        processedList.append(wordList[ind])
        
    for j in range(len(parentList)):
        if wordList[j] != source and parentList[j] == '':
            distanceList[j] = -1
                    
    return [parentList, distanceList]
               
    
    

###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It also take a word
# called source and a word called target. The function returns a shortest path
# from the source word to the target word, if there is a path between these two
# words. Otherwise, the function returns []. This function calls searchWordNetwork
# to compute the parent list and then follows the parent pointers from target 
# to source to compute a path; this path is then reversed and returned.
#
# Examples: 
# >>> L2 = ["bided", "bides", "sided", "sides", "tided", "tides"]
# >>> nL2 = makeNeighborLists(L2)
# >>> findPath(L2, nL2, "tides", "sided")
# ['tides', 'sides', 'sided']
# >>> L3 = ["curse", "curve", "nurse", "parse", "passe", "paste", "purse", "taste"]
# >>> nL3 = makeNeighborLists(L3)
# >>> findPath(L3, nL3, "curve", "taste")
# ['curve', 'curse', 'purse', 'parse', 'passe', 'paste', 'taste']
#
###############################################################################
def findPath(wordList, nbrsList, source, target):
    List1 = searchWordNetwork(wordList, nbrsList, source)
    path = []
    currentWord = ""
    
    if target not in wordList:
        return path
    targetInd = wordList.index(target)
    
    if List1[0][targetInd] == "":
       return path
    
    path.append(target)
    while currentWord != source:
       path.append(List1[0][targetInd])
       currentWord = List1[0][targetInd]
       targetInd = wordList.index(List1[0][targetInd])
    
    path.reverse()
    return path
                
            
        
###############################################################################     
#
# Specification:  This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It returns the list of
# connected components in the word network.
#
# Definition: A connected component of a network is the set of all nodes that can
# be reached from each other via paths in the network.
#
# Examples: 
# >>> L3 = ["curse", "curve", "nurse", "parse", "passe", "paste", "purse", "taste"]
# >>> nL3 = makeNeighborLists(L3)
# >>> findComponents(L3, nL3)
# [['curse', 'curve', 'nurse', 'parse', 'passe', 'paste', 'purse', 'taste']]   
# >>> L4 = L3 +["sided", "tided", "bided"]
# >>> L4.sort()
# >>> nL4 = makeNeighborLists(L4)
# >>> findComponents(L4, nL4)
#  [['bided', 'sided', 'tided'],
#   ['curse', 'curve', 'nurse', 'parse', 'passe', 'paste', 'purse', 'taste']]
# >>> L5 = ["abhor"] + L4
# >>> nL5 = makeNeighborLists(L5)
# >>> findComponents(L5, nL5)
# [['abhor'],
#  ['bided', 'sided', 'tided'],
#  ['curse', 'curve', 'nurse', 'parse', 'passe', 'paste', 'purse', 'taste']]
#
# Notes: 
# (a) The nodes in each connected component should appear in the same order
# as they appear in wordList. 
# (b) The components themselves should be sorted by the first word in the component.
#
###############################################################################            
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


 