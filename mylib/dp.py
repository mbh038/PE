# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:36:01 2016
@author: mbh
"""
#https://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
#minimum coin change problem
def dpMakeChange(coinValueList,change,minCoins={}):
    """gives minimum number of coins - does not keep track of which coins"""
    for cents in range(change+1):
       coinCount = cents
       for j in [c for c in coinValueList if c <= cents]:
           if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
       minCoins[cents] = coinCount
    return minCoins[change]
   
def dpMakeChange2(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin
      
def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange2(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()