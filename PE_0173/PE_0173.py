# -*- coding: utf-8 -*-
"""

PE_0173():

Using up to one million tiles how many different "hollow" square laminae can be 
formed?

We shall define a square lamina to be a square outline with a square "hole" so 
that the shape possesses vertical and horizontal symmetry. For example, using 
exactly thirty-two square tiles we can form two different square laminae:

With one-hundred tiles, and not necessarily using all of the tiles at one time, 
it is possible to form forty-one different square laminae.

Using up to one million tiles how many different square laminae can be formed?
Created on Sun Nov 20 14:47:38 2016

@author: mbh
"""

import math
import time

def p173(n):
    t=time.clock()
    amin=3
    amax=(n+4)//4
    total=0
    for a in range(amin,amax+1):
        bsqmin=a**2-n
        b=2-a%2
        if bsqmin>1:
            b=max(b,math.ceil((bsqmin)**.5))
        total+=(a-b)//2
    print(total,time.clock()-t)
