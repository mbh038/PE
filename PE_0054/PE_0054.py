# -*- coding: utf-8 -*-
"""

PE_0054

Poker hands

How many hands does Player 1 win?

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
        values,suits=[],[]
        for i in range(2):
            score[i]=0
            values.append([cardvals[x] for x in [x[0] for x in [x for x in hand[i]]]])
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
                if len(set([x for x in values[i] if values[i].count(x) ==4]))==1:
                    print '4 of a kind'
#                    four of a kind
                    score[i]=8
                    print 'Four of a Kind for player ',i
                    continue
                #full house
                    print 'full house'
                score[i]=7
                continue
            
            #Straight: All cards are consecutive values
            if max(values[i])-min(values[i])==4 and len(set(values[i]))==5:
                score[i]=5
                continue
            
            #Three of a Kind
            if len(set([x for x in values[i] if values[i].count(x) ==3]))==1:
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
        
        #Decide winner for tied hands:
        
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
            player4s=[list(set([x for x in values[i] if values[i].count(x) ==4])) for i in [0,1]]
            if player4s[1]>player4s[0]:
                wins[1]+=1
            elif player4s[0]>player4s[1]:
                wins[0]+=1
            elif player4s[1]==player4s[0]:
                player1s=[list(set([x for x in values[i] if values[i].count(x) ==1])) for i in [0,1]]
                if player1s[1]>player1s[0]:
                    wins[1]+=1
                elif player1s[0]>player1s[1]:
                    wins[0]+=1
            continue
            
        #Full House
        if score[0]==7:
            player3s=[list(set([x for x in values[i] if values[i].count(x) ==3])) for i in [0,1]]
            if player3s[1]>player3s[0]:
                wins[1]+=1
            elif player3s[0]>player3s[1]:
                wins[0]+=1
            elif player3s[1]==player3s[0]:
                player2s=[set([x for x in values[i] if values[i].count(x) ==2]) for i in [0,1]]
                if player2s[1]>player2s[0]:
                    wins[1]+=1
                elif player2s[0]>player2s[1]:
                    wins[0]+=1
            continue

        #One pair or one trio 
        if score[0]==2 or score[0]==4:
            pairvals=[list(set([x for x in values[i] if values[i].count(x) ==2 or values[i].count(x) ==3])) for i in [0,1]]
            if pairvals[1]>pairvals[0]:
                wins[1]+=1
            elif pairvals[0]>pairvals[1]:
                wins[0]+=1             
            elif pairvals[0]==pairvals[1]:
                singles=[sorted(list(set([x for x in values[i] if values[i].count(x) ==1])),reverse=True) for i in [0,1]]
                for i in range(len(singles)):
                    if singles[1][i]>singles[0][i]:
                        wins[1]+=1
                        break
                    elif singles[0][i]>singles[1][i]:
                        wins[0]+=1
                        break
         #Two pairs 
        if score[0]==3:
            pairvals=[sorted(list(set([x for x in values[i] if values[i].count(x) ==2])),reverse=True) for i in [0,1]]
            for i in range(2):
                if pairvals[1][i]>pairvals[0][i]:
                    wins[1]+=1
                    break
                elif pairvals[0][i]>pairvals[1][i]:
                    wins[0]+=1 
                    break
                singles=[sorted(list(set([x for x in values[i] if values[i].count(x) ==1])),reverse=True) for i in [0,1]]
                print singles
                for i in range(len(singles)):
                    if singles[1][i]>singles[0][i]:
                        wins[1]+=1
                        break
                    elif singles[0][i]>singles[1][i]:
                        wins[0]+=1
                        break
                    
    print 'Wins: ',wins,' ties: ',1000-sum(wins)        
    print 'Elapsed time: ',timer()-start,'s'


                
            
            
        
        
        
        
#    print hands
#        