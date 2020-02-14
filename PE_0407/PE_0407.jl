# -*- coding: utf-8 -*-
"""

PE_0407

Idempotents

Created on Tue Jan 10 04:49:44 2017
@author: mbh
"""


using Mods
using Primes
using Combinatorics

function test(idem=[1,2,3])
    # for a in Iterators.product(fill(idem,2)...)
    for a in combinations(idem,2)
        println(a)
    end
end

function main(limit=10^7)
    a=p407(10)
    @time p407(limit)
end


function p407(limit)
    misum=0
    for n in 2:limit
        nsum=max_idempotent(n)
        misum+=nsum
    end
    return(misum)
end


function max_idempotent(n)
    #returns maximum idempotent a < n: a^2=a mod n"""
    pfs=pflist(n)
    pfnum=length(pfs)
    if pfnum==1
        return 1 #idempotent=1 for primes or powers of primes
    end

    #Use the CRT to find m 'base' idempotent solutions from m prime factors p_i^a_i
    idems=Int64[]
    for i in 1:pfnum
        allButOnePfs=vcat(pfs[1:i-1],pfs[i+1:end])
        xsum=0
        for i in 1:pfnum-1
            Ni=div(n,allButOnePfs[i])
            xsum+=inverse(Ni,allButOnePfs[i])*Ni # faster
        end
        push!(idems,xsum % n)
    end
    #generate all other idempotents from these, and return the maximum
    maxval=maximum(idems)
    for i in 2:length(idems)-1
        for a in combinations(idems,i)
            aprod=1
            for x in a
                aprod = (aprod * x) % n
            end
            if aprod>maxval
                maxval=aprod
            end
        end
    end
    return maxval
end

#from Wikipedia
function inverse(a, n)
    #returns multiplicative inverse of a mod n. a and n must be-co-prime
    t1,t2=0,1
    r1,r2=n,a
    while r2!=0
        q = div(r1,r2)
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2
    end
    if t1 < 0
        t1 +=n
    end
    return t1
end

function pflist(n)
    # returns the distinct prime factors of n as [2^a,3^b.....]
    i = 2
    factors = Int64[]
    while i * i <= n
        if n % i>0
            i += 1
        else
            push!(factors,1)
            while n %i ==0
                n =div(n,i)
                factors[end]*=i
            end
        end
    end
    if n > 1
        push!(factors,n)
    end
    return factors
end
