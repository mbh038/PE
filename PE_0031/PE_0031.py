# -*- coding: utf-8 -*-
"""
PE_0031

Coin Sums

How many different ways can £2 be made using any number of coins

Created on Mon Jun 27 08:53:29 2016

@author: Mike
"""
import time
def coinsum(value):
    
    t=time.clock()
    
    coins=[1,2,5,10,20,50,100,200]
    ways=[0] * (value+1)
    ways[0]=1
   
    while coins[-1]>value:
        del(coins[-1])

    for i in range(len(coins)):
        for j in range (coins[i],value+1):
            ways[j]+=ways[j-coins[i]]
    
    print (ways[-1],time.clock()-t)


def dp(n):
    
    t=time.clock()
    
    denom=[1,2,5,10,20,50,100,200]
    m=len(denom)
    table = [[1 for i in range(m)] for j in range(n+1)]
            
    for i in range(1,n+1):
        for j in range(1,m):
            if i-denom[j]>=0:
                table[i][j] = table[i][j-1]+table[i-denom[j]][j]
            else:
                table[i][j] = table[i][j-1]
                
    print(table[n][m-1])
    print(time.clock()-t)
                
                


#void dp(int n)
#{
#    const int m=8;
#    int arr[n+1][m];
#    int denom[m] ={1, 2, 5, 10, 20, 50, 100, 200};
#
#    for(int a=0; a<n+1; a++)
#        for(int b=0; b<m; b++)
#            arr[a][b] = 1;
#
#    for(int i=1; i<n+1; i++)
#    {
#        for(int j=1; j<m; j++)
#        {
#            if(i-denom[j] >=0)
#                arr[i][j] = arr[i][j-1]+arr[i-denom[j]][j];
#            else
#                arr[i][j] = arr[i][j-1];
#        }
#    }
#    std::cout << arr[n][m-1] << std::endl;
#}