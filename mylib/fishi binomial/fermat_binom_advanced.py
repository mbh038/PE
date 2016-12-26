#!/usr/bin/env python3

"""
Using Fermat's little theorem to calculate nCk mod m, m is prime
Computation O(n)
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

# get degree of p in n! (exponent of p in the factorization of n!)
def fact_exp(n,p):
    e = 0
    u = p
    t = n
    while u <= t:
        e += t//u
        u *= p

    return e

# Using Fermat's little theorem to compute nCk mod p
# considering cancelation of p in numerator and denominator
# Note: p must be prime
def fermat_binom_advanced(n,k,p):
    # check if degrees work out
    num_degree = fact_exp(n,p) - fact_exp(n-k,p)
    den_degree = fact_exp(k,p)
    if num_degree > den_degree:
        return 0

    if k > n:
        return 0

    # calculate numerator and cancel out occurrences of p
    num = 1
    for i in range(n,n-k,-1):
        cur = i
        while cur%p == 0:
            cur //= p
        num = (num*cur)%p

    # calculate denominator and cancel out occurrences of p
    denom = 1
    for i in range(1,k+1):
        cur = i
        while cur%p == 0:
            cur //= p
        denom = (denom*cur)%p

    # numerator * denominator^(p-2) (mod p)
    return (num * mod_exp(denom,p-2,p))%p

if __name__ == '__main__':
    mod = 1000000007 # prime

    # (950 choose 100) mod 1000000007
    print(fermat_binom_advanced(950,100,mod)) # should be 640644226