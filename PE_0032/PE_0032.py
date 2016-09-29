# -*- coding: utf-8 -*-
"""

PE_0032

Pandigital products

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.
 
 
Created on Tue Jun 28 09:24:17 2016

@author: Mike
"""
    
from itertools import permutations
from time import time

def p32():
    t0=time()
    digits='123456789'
    sums=set()
    
    rs=[]
    lens=[2,3,1,4]
    for i in range(2):
        rs.append([])
        for j in range(2):
            rs[i].append([])
            r=permutations('123456789',lens[2*i+j])
            for x in r:
                newr=''
                for k in range(lens[2*i+j]):
                    newr+=x[k]
                if newr[-1]!='5' and newr[-1]!='1':   
                    rs[i][j].append(newr)
    
#    print rs
    count=0
#    flag=False
    for r in rs:       
        for multiplicand in r[0]:
            for multiplier in r[1]:
                if multiplier[-1] in '248'  and multiplicand[-1]=='6':
                    continue
                if multiplicand[-1] in '248'  and multiplier[-1]=='6':
                    continue               
                flag=False
                for digit in multiplicand:
                    if digit in multiplier :
                        flag=True
                        count+=1
                        continue
                if flag==False:
                    product=int(multiplicand)*int(multiplier )      
                    test=multiplicand+multiplier+str(product)
                    
                    if len(test)==9 and digits.strip(test)=='':
#                    if sorted(test)==digits:
                        sums.add(product)
    #                print multiplicand,multiplier,product
    
#    print (count,sums)          
    print (sum(sums))
    
    print('Elapsed time:',time()-t0)


#from FJ_Sevilla
def prob32():
    res=set()
    for n in range(2,99):
        sn = str(n)
        for dig in sn:
            if dig=='0' or sn.count(dig)!=1: break
        else:
            for m in range(1234//n,9876//n+1):
                    r=n*m
                    st=sn+str(m)+str(r)
                    if len(st)==9:
                        for dig in st:
                            if dig=='0' or st.count(dig)!=1: break
                        else: res.add(r)
    print ('Sol:',sum(res))

#if __name__=='__main__':
def FJSevilla():
    t0=time()
    prob32()
    print('Elapsed time:',time()-t0)
#    input()


def alligator():

    import time
    start_time = time.time()

    product_sum = 0
    check_pandigital = False
    set_of_products = set()
    
    def pandigital(l):
            seen = set() # Start with an empty set
            for i in l:
                    if i in seen:
                            return False
                    seen.add(i) # If it is not in the seen set, then add it.
            return True
     
    for x in range(1, 2000):
            for y in range(x+1, 2000):
                    z = x * y
                    digits = str(x) + str(y) + str(z) # This takes all three numbers and joins them into one long number
                    if (len(digits) == 9 and "0" not in (digits) and pandigital(digits)):
                            if z not in set_of_products:
                                    set_of_products.add(z)
                                    product_sum = product_sum + z
    
    print ("The sum of the pandigital products is: ", product_sum)
    print("--- %s seconds ---" % (time.time() - start_time))
    
#alligator()
    
def pan(n): return len(n)==9 and "123456789".strip(n)==""

def tzaman():
    import time
    start_time = time.time()
    prod = set()
    for i in range(1,10):
        for j in range(1234,9877):
            if pan(str(i)+str(j)+str(i*j)): prod.add(i*j)
    
    for i in range(12,99):
        for j in range(123,988):
            if pan(str(i)+str(j)+str(i*j)): prod.add(i*j)
    
    print (sum(prod))
    print("--- %s seconds ---" % (time.time() - start_time))
