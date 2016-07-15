# -*- coding: utf-8 -*-
"""

PE_0079

Passcode derivation

A common security method used for online banking is to ask the user for three
 random characters from a passcode. For example, if the passcode was 531278,
 they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
 be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file
 so as to determine the shortest possible secret passcode of unknown length.
 
Created on Thu Jul 14 05:34:36 2016

@author: Mike
"""
from timeit import default_timer as timer
def PE_0079(filename):
    start=timer()
    with open(filename, 'r') as fh:
        logins=set([number[0:3] for number in fh])

    pos={x:[set(),set()] for x in '0123456789'}
    
    for login in logins:

        pos[login[0]][0].add(login[1])
        pos[login[0]][0].add(login[2])        
        pos[login[1]][0].add(login[2])        
        pos[login[2]][1].add(login[0])
    
    for digit in pos.keys():
        if len(pos[digit][0])==0 and len(pos[digit][1])==0:
            del(pos[digit])
    
    passcode=[0]*len(pos)
    for digit in pos:
        passcode[len(pos)-len(pos[digit][0])-1]=digit
    
    print ''.join(x for x in passcode)
    print 'Elapsed time: ',timer()-start,'s'
        
        
    
    
#solved by hand!
    
def parse_log(fname):
    with open(fname) as f:
        xs = f.read()
    return xs.split()

def run(fname):
    start=timer()
    logs = parse_log(fname)
    befors = dict()            #dictionary mapping a char to the chars that appear before it
    password = [None] * 10     #guess that the password will be at most 10 digits long
    for s in logs:              
        for i, c in enumerate(s):
            if c not in befors:
                befors[c] = set()    #use set to avoid counting duplicates
            befors[c].update(s[:i])
    for k, v in befors.items():      #the index of a char in pwd is the num of chars before it 
        password[len(v)] = k
    code = ''.join(list(filter(lambda x: x is not None, password)))
    print 'Elapsed time: ',timer()-start,'s'#removes digits never used
    return code                       #i think i spelled befors wrong