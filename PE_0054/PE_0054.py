# -*- coding: utf-8 -*-
"""

PE_0054

Poker hands

Created on Mon Jul 11 12:10:03 2016

@author: Mike
"""
from collections import Counter
from timeit import default_timer as timer

def poker():
    start=timer()
    hands=[]
    fhand = open('p054_poker.txt')
    for line in fhand.read().split('\n'):
        hands.append(line)
         
    hands=zip([x[0:14].split() for x in hands],[x[15:30].split() for x in hands])
    cardvals={x:y for (x,y) in zip('23456789TJQKA',range(13))}
   
    wins=[0,0]
    for hand in hands:
        score=[0,0]
        valCounts,values,suits=[],[],[]
        for i in range(2):
            score[i]=0
            values.append([cardvals[x] for x in [x[0] for x in [x for x in hand[i]]]])
            valCounts.append(Counter(values[i]))
            suits.append([x[1] for x in [x for x in hand[i]]])
            
            #Flushes
            if len(set(suits[i]))==1:
                #Royal Flush
                if set(values[i])==set([8,9,10,11,12]):
                    score[i]=10
                    continue
                #Straight Flush
                if max(values[i])-min(values[i])==4:
                    score[i]=9
                    continue
                #Flush
                score[i]=6
                continue
            
            #Four of a kind or Full house
            if len(set(values[i]))==2:
                if max(valCounts[i].values())==4:
#                    four of a kind
                    score[i]=8
                    print 'Four of a Kind for player ',i
                    continue
                #full house
                score[i]=7
                continue
            
            #Straight: All cards are consecutive values
            if max(values[i])-min(values[i])==4 and len(set(values[i]))==5:
                score[i]=5
                continue
            
            #Three of a Kind
            if max(valCounts[i].values())==3:
                score[i]=4 
                continue
            
            #Two pairs
            if len(set(values[i]))==3:
                score[i]=3
                continue
            
            #One Pair
            if len(set(values[i]))==4:
                score[i]=2
                continue
            
            #High card
            score[i]=1

        if score[0]>score[1]:
            wins[0]+=1
            continue
        if score[1]>score[0]:
            wins[1]+=1
            continue
        
        #Ties        
        #Royal Flush - noone would win - there cannot be any of these.
        
        #Straight Flush or Straight or High card
        if score[0]==9 or score[0]==5 or score[0]==1:
            if max(values[1])>max(values[0]):
                wins[1]+=1
            if max(values[0])>max(values[1]):
                wins[0]+=1
            continue
                
        #flush
        if score[0]==6:
            for i in range(5):
                nexts=[sorted(values[0],reverse=True)[i] for i in [0,1]]
                if nexts[1]>nexts[0]:
                    wins[1]+=1
                    continue
                elif nexts[0]>nexts[1]:
                    wins[0]+=1
                    continue
            continue
                
        #Four of a Kind
        if score[0]==8:
            player4s=[valCounts[i].keys()[valCounts[i].values().index(4)]for i in [0,1]]
            if player4s[1]>player4s[0]:
                wins[1]+=1
            elif player4s[0]>player4s[1]:
                wins[0]+=1
            elif player4s[1]==player4s[0]:
                player1s=[valCounts[i].keys()[valCounts[i].values().index(1)] for i in [0,1]]
                if player1s[1]>player1s[0]:
                    wins[1]+=1
                elif player1s[0]>player1s[1]:
                    wins[0]+=1
            continue
            
        #Full House
        if score[0]==7:
            player3s=[valCounts[i].keys()[valCounts[i].values().index(3)] for i in [0,1]]
            if player3s[1]>player3s[0]:
                wins[1]+=1
            elif player3s[0]>player3s[1]:
                wins[0]+=1
            elif player3s[1]==player3s[0]:
                player2s=[valCounts[i].keys()[valCounts[i].values().index(2)]for i in [0,1]]
                if player2s[1]>player2s[0]:
                    wins[1]+=1
                elif player2s[0]>player2s[1]:
                    wins[0]+=1
            continue
            
#        #Three of a Kind

        #One pair
        if score[0]==2:

            pairvals=[valCounts[i].keys()[valCounts[i].values().index(2)] for i in[0,1]]
            if pairvals[1]>pairvals[0]:
                wins[1]+=1
            elif pairvals[0]>pairvals[1]:
                wins[0]+=1             
            elif pairvals[0]==pairvals[1]:
                counts = [{key: value for key, value in valCounts[i].items() if value is not 2} for i in [0,1]]
                while len(counts[0])>0:
                    if max(counts[1])>max(counts[0]):
                        wins[1]+=1
                        break
                    if max(counts[0])>max(counts[1]):
                        wins[0]+=1
                        break 
                    counts = [{key: value for key, value in counts[i].items() if value is not max(counts[i].values())} for i in [0,1]]
    print 'Wins: ',wins,' ties: ',1000-sum(wins)        
    print 'Elapsed time: ',timer()-start,'s'


                
            
            
        
        
        
        
#    print hands
#        