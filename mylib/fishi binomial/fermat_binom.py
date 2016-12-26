#!/usr/bin/env python3

"""
Using Fermat's little theorem to calculate nCk mod m, for k < m and m is prime

Two versions:
1. Pre-Compute factorials and multiplicative inverses in O(n*logn) --> later lookup in O(1)
2. Compute directly --> no lookup --> each time O(n)
"""

# modular exponentiation: b^e % mod 
def mod_exp(b,e,mod):
    r = 1
    while e > 0:
        if (e&1) == 1:
            r = (r*b)%mod
        b = (b*b)%mod
        e >>= 1

    return r

# Using Fermat's little theorem to compute nCk mod p
# Note: p must be prime and k < p
def fermat_binom(n,k,p):
    if k > n:
        return 0

    # calculate numerator
    num = 1
    for i in range(n,n-k,-1):
        num = (num*i)%p

    # calculate denominator
    denom = 1
    for i in range(1,k+1):
        denom = (denom*i)%p

    # numerator * denominator^(p-2) (mod p)
    return (num * mod_exp(denom,p-2,p))%p

# Using Fermat's little theorem to pre-compute factorials and inverses
# Note: only works when p is prime and k < p
def fermat_compute(n,p):
    facts = [0]*n
    invfacts = [0]*n

    facts[0] = 1
    invfacts[0] = 1
    for i in range(1,n):
        # calculate factorial and corresponding inverse
        facts[i] = (facts[i-1]*i)%p
        invfacts[i] = mod_exp(facts[i],p-2,p)

    return facts, invfacts

# Compute binomial coefficient from given pre-computed factorials and inverses
def binom_pre_computed(facts, invfacts, n, k, p):
    # n! / (k!^(p-2) * (n-k)!^(p-2)) (mod p)
    return (facts[n] * ((invfacts[k]*invfacts[n-k] % p))) % p

if __name__ == '__main__':
    n = 1009 # number factorials to pre-compute
    mod = 1000000007 # prime

    # pre-compute factorials and inverses
    facts, invfacts = fermat_compute(n,mod)

    # print (950 choose 100) mod 1000000007 (with pre-computing)
    print(binom_pre_computed(facts,invfacts,950,100,mod)) # should be 640644226

    # (950 choose 100) mod 1000000007 (without pre-computing)
    print(fermat_binom(950,100,mod)) # should be 640644226