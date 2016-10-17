# -*- coding: utf-8 -*-
"""
posted by philiplu on p88
Created on Sat Oct  8 06:02:49 2016
@author: philiplu
"""

class PrimeList:
    """
    Immutable list of primes optimized for fast access.  List of primes up to a
    limit created at initialization, after which list-style access is used,
    except that "n in prime_list" uses a set (created on demand) for faster
    access.
    
    Can be used for detecting primality for numbers up to the square of the
    initializing limit.
    """
    def __init__(self, limit = 1000000):
        self.limit = limit
        self.limit_sq = limit*limit
        self.list = [2]
        self.set = None
        multiples = set()
        sqrt = int(limit**0.5)+1
        for i in range(3, limit+1, 2):
            if i not in multiples:
                self.list.append(i)
                if i < sqrt:
                    multiples.update(range(i*i, limit+1, i))
    def __len__(self):
        return len(self.list)
    def __iter__(self):
        return iter(self.list)
    def __getitem__(self, key):
        return self.list[key]
    def __str__(self):
        return str(self.list)
    def __repl__(self):
        return str(self.list)
    def __contains__(self, item):
        try:
            result = item in self.set
        except:
            self.set = set(self.list)
            result = item in self.set
        return result

    def is_prime(self, n):
        """ Determine if n is prime.  Raises error if n > limit^2 """
        if n < self.limit:
            return n in self
        if n >= self.limit_sq:
            raise OverflowError("Can only test is_prime up to {0}".format(self.limit_sq))
        sqrt_n = int(n**0.5)+1
        for prime in self.list:
            if n % prime == 0:
                return False
            if prime > sqrt_n:
                break
        return True

def prime_factors(n, primes):
    """ Calculate prime factorization of n, given list of primes.
        Returns list of tuples, each tuple consisting of a prime
        factor and the power for that prime. """
    factors = []
    for prime in primes:
        if prime * prime > n:
            break
        count = 0
        while n % prime == 0:
            n //= prime
            count += 1
        if count > 0:
            factors.append((prime, count))
    if n > 1 or len(factors) == 0:
        factors.append((n, 1))
    return factors

def factors(n, primes):
    """ Calculate list of all factors of n, including 1 and n.
        'primes' is pre-computed list of primes.
        NOTE - the factors are not returned in sorted order, but 1 will always
        be the first factor, and n will always be the last. """
    pfs = prime_factors(n, primes)
    factors = []
    def helper(index, product):
        index -= 1
        prime, power = pfs[index]
        for i in range(power+1):
            if index > 0:
                helper(index, product)
            else:
                factors.append(product)
            product *= prime
    helper(len(pfs), 1)
    return factors

def factor_sum(n, primes):
    """ Find the sum of the proper divisors of n.  'primes' is the pre-computed
        list of primes. """
    return sum(factors(n, primes)[:-1])

def factorizations(n, primes, singleton=True):
    """ Generate all possible factorizations of n (not counting any with a 1
        as a factor).  'primes' is the pre-computed list of primes.  'singleton'
        is False if you want to suppress the factorization consisting of the
        number to factor by itself. """
    def helper(n, max_f):
        for factor in reversed(factors(n, primes)[1:]):
            if factor > max_f:
                continue
            new_n = n // factor
            if new_n > 1:
                for combo in helper(new_n, factor):
                    yield combo + [factor]
            else:
                yield [factor]
    for combo in helper(n, n if singleton else n-1):
        yield combo

def gcd(a, b):
    """ Find the greatest common divisor.  Not really prime-help, but useful. """
    while b != 0:
        a, b = b, a % b
    return a
    
import time
def ps6(nmax):
    start=time.clock()
    ns={}
    sns=set()
    primes=PrimeList(nmax)
    for p in range (2,2*nmax+1):
        az=[x for x in factorizations(p, primes)]
        ts=[(p,sum(x)-len(x)) for x in az]
        for t in ts:
            sns.add(t)               
    for sn in sns:
        p,sm=sn[0],sn[1]
        n=p-sm
        if n>=2 and n<=nmax:
            try:
                ns[n]=min(ns[n],p)
            except KeyError:
                ns[n]=p              
    print(sum(set(ns.values())),time.clock()-start)