# -*- coding: utf-8 -*-
"""

PE_0022

Names scores

Using p022_names.txt, a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this 
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?


Created on Thu Jun 23 04:16:30 2016

@author: Mike
"""

def PE_0022(fname):
    
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'    
    
    # get sorted name list
    names=getSortedNameList(fname)
    
    #get alphabet score of each name
    scores=[]   
    for name in names:
        score=0
        for letter in name:
            score += alphabet.index(letter)+1
        scores.append(score)
    
    #get toal name score
    totalNameScore=0
    for i in range(len(names)):
        totalNameScore += (i+1)*scores[i]
        
    print totalNameScore

def getSortedNameList(fname):
    
    try:
        fhand = open(fname)
    except:
        print 'File cannot be opened:', fname
        exit() 
    names = fhand.read().split(',')    
    for i in range(len(names)):
        names[i] = names[i].translate(None, '"')
    return sorted (names)
   
