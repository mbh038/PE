# -*- coding: utf-8 -*-
"""

PE_0098

Anagramic squares

Created on Sun Aug 21 13:47:52 2016
@author: mbh
"""
from timeit import default_timer as timer
def asq(filename='p098_words.txt'):
    start=timer()
    wdic=readWords(filename)   
    ags=anagrams(wdic)    
           
    sqs={digits:asquares(digits) for digits in range(1+max([len(k) for k,v in ags.items()]))}
    sqmax=0
    for k,v in ags.items():
        asqs=sqs[len(k)]        
        for x,y in asqs.items():
            w={v[0][i]:y[0][i] for i in range (len(v[0]))}
            nstr=''.join([w.get(v[j][kk],'X')for j in range(1,len(v)) for kk in range (len(v[j]))])
            if nstr in y and int(nstr)>sqmax:
                sqmax=int(nstr)
    print(sqmax)  
    print ('Elapsed time',timer()-start,'s')        


def readWords(filename='p098_words.txt'): 
    """returns dict of words in file, keyed by world length"""    
    with open(filename) as f:
        words= [word for line in f for word in line.split('","')]
        maxlen=max([len(word) for word in words])
        return {l:[word for word in words if len(word)==l ] for l in range(1,maxlen+1) }

            
def anagrams(wdic):
    """returns dict of anagrams in dict wdic"""
    allwords={}
    for k,v in wdic.items():
        for j in range(len(v)):
            x="".join(sorted(v[j]))
            allwords.setdefault(x,[]).append(v[j])
    return {k:v for (k,v) in allwords.items() if len(v)>1}

            
def asquares(n):
    """returns dict of all anagramic integer squares with n digits, all digits being different"""
    squares = [str(x**2) for x in range(int(10**((n-1)/2))+(n+1)%2,int(10**(n/2))+n%2)]
    allsqs={}
    for square in squares:
        if len(square)>len(set(square)): #only take those where all digits are different
            continue
        x="".join(sorted(square)) 
        allsqs.setdefault(x,[]).append(square)
    return {k:v for (k,v) in allsqs.items() if len(v)>1}

    
def test():

    wdic=readWords()   
    ags=anagrams(wdic)
    wsum={0:0,1:0}
    for k,v in ags.items():
        wsum[len(k)]=wsum.get(len(k),0)+1
    print (wsum)
    
    csum=0
    for n in range(10):
        a=asquares(n)
        
        csum+=sum([len(v) for k,v in a.items()])
        try:
            csum+=wsum[n]*sum([len(v) for k,v in a.items()])
            print(csum)
        except:
            pass
