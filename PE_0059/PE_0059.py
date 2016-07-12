# -*- coding: utf-8 -*-
"""

PE_0059

XOR decryption

Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum 
of the ASCII values in the original text.


Created on Sat Jul 09 17:02:26 2016

@author: Mike
"""

from timeit import default_timer as timer
def PE_0059():
    
    start=timer()
    #read in cipher as list of ascii codes
    cipher=[]
    fhand = open('p059_cipher.txt')
    for number in fhand.read().split(','):
        number.rstrip()
        cipher.append(int(number))

    keylist=keys()    
    candidates={}
    target_words=common_words()
    for key in keylist:
        score=0
        keylong=key*(len(cipher)/len(key))
        message=xor_ascii(cipher, keylong)
        for word in target_words:
            if message.find(word)>-1:
                score+=1
        if score>4:
            candidates[''.join([chr(x) for x in key])]=score
            break

    key=[ord(max(candidates)[x]) for x in range(3)]
    keylong=key*(len(cipher)/len(key))
    message=xor_ascii(cipher, keylong)
    print message
    answer=sum([ord(x) for x in message])
    print answer
    print 'Elapsed time: ',timer()-start

def xor_ascii(s,t):
    '''xor corresponding elements of two lists of ascii codes'''
    return ''.join(chr(a^b) for a,b in zip(s,t))
      
def keys():
    '''
    returns list of all possible keys where each key is 3 lower case 
    letters, returned as list of 3 ascii codes
    '''
    lc='abcdefghijklmnopqrstuvwxyz'    
    return [[ord(x),ord(y),ord(z)] for x in lc for y in lc for z in lc]

def common_words():
    return ['that','have', 'the','be','to','of','and']
    
#   

def XORdecrypt():
    
    '''another attempt, using idea that most common character will be 'space' '''
    
    start=timer()
    #read in cipher as list of ascii codes
    cipher=[]
    fhand = open('p059_cipher.txt')
    for number in fhand.read().split(','):
        number.rstrip()
        cipher.append(int(number))
        
    a= [cipher[i::3] for i in range(3)]
    key=[]
    for i in range(3):
        decode=[x^32 for x in a[i] ]
        key.append(max(set(decode), key=decode.count))
    print 'The key is probably: ',key,' which is: ',''.join([chr(x) for x in key])
    
    keylong=key*(len(cipher)/len(key))
    message=''.join(chr(a^b) for a,b in zip(cipher,keylong))
    print message
    answer=sum([ord(x) for x in message])
    print answer
    
    print 'Elapsed time: ',timer()-start    

    

#
#    for number in code:
#        print binary_repr(number,width=8)