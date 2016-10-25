# -*- coding: utf-8 -*-
"""

PE_0145

How many reversible numbers are there below one-billion?

Created on Mon Oct 24 06:09:00 2016
@author: mbh
"""

def p145(nmin,nmax):
    rev=0
    solns={}
    for n in range (nmin,nmax):
        flag=True
        nstr=str(n)
        if nstr[-1]=='0':
            continue
        if (int(nstr[0])+int(nstr[-1]))%2==0:
            continue
        nrevstr=str(n)[::-1]
        if nrevstr[0]=='0':
            continue
        ns=n+int(nrevstr)
        rev+=1
        while ns//10>0:
            if ns%10%2==0:
                rev-=1
                flag=False
                break
            ns=ns//10
        if flag:
            solns.setdefault(n+int(nrevstr),[]).append(n)
            print(n,n+int(nrevstr))
    print (rev)
    print (solns)
    print(len(solns))
    print(sum([len(v) for k,v in solns.items()]))
    return[k for k,v in solns.items()]
        
            