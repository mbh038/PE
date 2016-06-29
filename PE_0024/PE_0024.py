# -*- coding: utf-8 -*-
"""
PE_0024

Lexicographic permutations

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Find largest index i such that array[i − 1] < array[i].
Find largest index j such that j ≥ i and array[j] > array[i − 1].
Swap array[j] and array[i − 1].
Reverse the suffix starting at array[i].

Created on Thu Jun 23 12:08:03 2016
@author: michael.hunt
"""

#	2783915460
import math as m
import time
def fastlx(sequence,which):
#    start_time = time.time()
    seq=sorted(sequence)
    lxperm=[]
    n=len(sequence)
    while n>3:
        for choose in range(n):
            poss=(choose+1)*m.factorial(n-1)
            if poss > which:
                break
        lxperm.append(seq[choose])
        which=which-choose*m.factorial(n-1)
        del(seq[choose])
        n -=1

    last3=lxperms(seq,which)
    
    for x in last3: lxperm.append(x)     
    strseq=[]
    for x in lxperm: strseq.append(str(x))
    st = ''.join(strseq)
    print st
#    print("--- %s seconds ---" % (time.time() - start_time))

def lxperms(sequence,n):
#    start_time = time.time()
    seq=sorted(sequence)
    count=1
    while True:
        count=count+1
        nextseq,flag=lxp(seq)
        if flag==True or count == n:
            break
        seq=nextseq
#    print("--- %s seconds ---" % (time.time() - start_time))
    strseq=[]
    for x in seq: strseq.append(str(x))
    s = ''.join(strseq)
    print s
    return seq 

def lxp(sequence):

    end=False
    imax=len(sequence)
    for i in range(len(sequence)-1,0,-1):
          
        if sequence[i-1]<sequence[i] :
 
            imax=i
            break
        if i==1:
            nextSequence = sequence
            end=True
            print "last permutation"
            return nextSequence,end    

    jnext=len(sequence)-1
    for j in range(len(sequence)-1,imax-1,-1):
        if sequence[j] >sequence[imax-1]:          
            jnext=j
            break
 
    temp=sequence[jnext]
    sequence[jnext]=sequence[imax-1]
    sequence[imax-1]=temp

    suffix=sequence[imax:]
    suffix.reverse()

    for i in range(len(suffix)): sequence[i+imax]=suffix[i]
    
    nextSequence = sequence
    return nextSequence,end

print 'Brute force'   
lxperms([0,1,2,3,4,5,6,7,8,9],1000000)
print 'faster...'
fastlx([0,1,2,3,4,5,6,7,8,9],1000000)



# someopne elsee
from math import factorial as fac
from time import time

goal,total_number = 1000000,10

#to calculate the time to repeat 10000times
t = time()
for counter in range(10000):
    
    rest,num_set,result_l = goal,set(range(total_number)),list()
    for i in range(1,total_number+1):
        p = fac(total_number-i)
        for j in range(len(num_set)):
            if rest-(j+1)*p <= 0:
                result_l.append(sorted(num_set)[j])
                num_set.remove(result_l[-1])
                rest -= j*p
                break


print('result:%s'%''.join(map(str,result_l)),"time:%.3f"%(time()-t))