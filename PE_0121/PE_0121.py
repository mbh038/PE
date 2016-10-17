# -*- coding: utf-8 -*-
"""

Disk game prize fund

A bag contains one red disc and one blue disc. In a game of chance a player 
takes a disc at random and its colour is noted. After each turn the disc is 
returned to the bag, an extra red disc is added, and another disc is taken at 
random.

The player pays £1 to play and wins if they have taken more blue discs than red 
discs at the end of the game.

If the game is played for four turns, the probability of a player winning is 
exactly 11/120, and so the maximum prize fund the banker should allocate for 
winning in this game would be £10 before they would expect to incur a loss. 
Note that any payout will be a whole number of pounds and also includes the 
original £1 paid to play the game, so in the example given the player actually 
wins £9.

Find the maximum prize fund that should be allocated to a single game in which 
fifteen turns are played.

#177299/39916800
#sum upper triangle of a matrix
#[sum([x*y for x in range(1,n+1) for y in range(1,n+1) if x>y]) for n in range(1,12)]

Created on Sat Oct 15 20:44:56 2016
@author: mbh
"""
import random as rd
import time
def play(turns):    
    disks=1
    blue,red=0,0
    for n in range(1,turns+1) :
        disks+=1
        choose=rd.randint(1,disks)
        if choose==1:
            blue+=1
        else:
            red+=1
        if blue==(turns+2)//2:
            return True
    return blue>red
    
def playmany(turns,games):
    wins=0
    for i in range(1,games+1):
        if play(turns):
            wins+=1
    return wins

#this takes 40 minutes for 15,10000,10000 
def playstats(turns,games,samples):
    t=time.clock()
    winratio=[]
    for s in range(1,samples+1) :
        winratio.append(playmany(turns,games))
    print(time.clock()-t)
    return winratio


import matplotlib.pyplot as plt

# the histogram of the data
#n, bins, patches = plt.hist(a, 50, normed=1, facecolor='g', alpha=0.75)


#plt.xlabel('Smarts')
#plt.ylabel('Probability')
#plt.title('Histogram of IQ')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
#plt.grid(True)
#plt.show()  