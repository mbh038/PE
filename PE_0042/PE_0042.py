# -*- coding: utf-8 -*-
"""

PE_0042

Coded triangle numbers

Created on Fri Jul 01 14:34:37 2016

@author: michael.hunt
"""

import time as t
start_time = t.time()

triangleNumbers=[int(((n/float(2))*(n+1))) for n in range(1,21)]
alphabet='"ABCDEFGHIJKLMNOPQRSTUVWXYZ'
codes=dict()
for i in range(len(alphabet)): codes[alphabet[i]]=i
    
twords=0
fhand = open('p042_words.txt')
for word in fhand.read().split(','):
    wordVal=sum([codes[letter] for letter in word])
    if wordVal in triangleNumbers: twords+=1
print twords
print("--- %s s ---" % (t.time() - start_time))



