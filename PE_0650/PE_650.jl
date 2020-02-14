# PE 650
# Michael Hunt
# 16 January 2020

#Answer: 538319652
# Initially solved in 5822 s (!)
# Reiner Martin does it in 16s - see code below.


using Primes
using Memoize

# n=1000 -> 1.1s
function main(n,m=10^9+7)
    compile_run=p650(5)
    @time p650(n,m)
end

# sum of binomial products up to row n
function p650(n,m=10^9+7)
    S=0
    count=0
    nextcount=0
    ps=primes(n)
    inverses=get_inverses(n,m)
    for k in 1:n
        pps=ps[ps.<=n]
        S=(S%m+D(k,pps,inverses)%m)%m
        # println(k)
    end
    return S
end

# inverses of all p-1 for all primes p up to n, mod m
function get_inverses(n,m)
    ps=primes(n)
    inverses=Dict{Int64,Int64}()
    for p in ps
        inverses[p-1]=inverse(p-1,m)
    end
    return inverses
end

# sum of divisors of product of all binomial terms in row n of Pascal triangle, mod m
function D(n,primes_from_2_to_n,inverses,m=10^9+7)

    subtotals=zeros()
    f=power_in_factorial
    total=1
    # ps=primes(n)
    # println(length(ps))
    for p in primes_from_2_to_n
        # println(p)
        pk=(n+1)*f(p, n)
        # total*=prod(p ^ (f(p, n) - f(p, k) - f(p, n - k)) for p in primes(n + 1))
        subtotal=1
        for k in 0:n
            pk = pk - f(p, k) - f(p, n - k)
        end
        # subtotal=(subtotal * (powermod(p,pk+1,m)-1)  * invmod(p-1,m)) %m
        subtotal=(subtotal * (powermod(p,pk+1,m)-1)  * inverses[p-1]) %m
        # subtotal=(subtotal % m * (powermod(p,pk+1,m)-1%m) % m * inverses[p-1] % m) % m            # subtotal=(subtotal%m * powermod(p,f(p, n) - f(p, k) - f(p, n - k),m)%m)%m

        # println(k," ",subtotal)]
        total=(total * subtotal) %m



    end
    return total%m
end

# Legendre theorem
function power_in_factorial(p, n)
    #Return the exponent of the prime p in the factorization of n!"""
    result = 0
    while true
        n =div(n,p)
        if n==0
            break
        end
        result += n
    end
    return result
end

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

function B(n,m=10^9+7)
    f=power_in_factorial
    total=1
    ps=primes(n+1)
    for k in 0:n
        # total*=prod(p ^ (f(p, n) - f(p, k) - f(p, n - k)) for p in primes(n + 1))
        subtotal=1
        for p in ps

            subtotal=(subtotal%m * powermod(p,f(p, n) - f(p, k) - f(p, n - k),m)%m)%m
        end
        # println(k," ",subtotal)
        total=(total%m * subtotal%m)%m

    end
    return total%m
end

####################################
#PE user Reiner Martin - it takes 17s or so

using Primes
using Memoize

function reiner(n)
    M = 10^9+7
    ⦿(a, b) = a * b % M
    ⊕(a, b) = (a + b) % M

    power(d::AbstractDict, n) = Dict(k => v*n for (k, v) in d)

    @memoize fact(n) = n <= 1 ? factor(1) : merge(+, fact(n-1), factor(n))

    @memoize B(n) = n ≤ 1 ? factor(1) : merge(-, merge(+, B(n-1), power(factor(n), n)), fact(n))

    @memoize D(n) = reduce(⦿, [(powermod(p, e+1, M) - 1) ⦿ invmod(p-1, M) for (p, e) in B(n)])

    S(n) = 1 + mapreduce(D, ⊕, 2:n)

    @show @time S(n)
end

# n=1000 -> 0.068s
# try Reiner without memoize
function reiner_nomem(n)
    M = 10^9+7
    ⦿(a, b) = a * b % M
    ⊕(a, b) = (a + b) % M

    power(d::AbstractDict, n) = Dict(k => v*n for (k, v) in d)

    fact(n) = n <= 1 ? factor(1) : merge(+, fact(n-1), factor(n))

    B(n) = n ≤ 1 ? factor(1) : merge(-, merge(+, B(n-1), power(factor(n), n)), fact(n))

    D(n) = reduce(⦿, [(powermod(p, e+1, M) - 1) ⦿ invmod(p-1, M) for (p, e) in B(n)])

    S(n) = 1 + mapreduce(D, ⊕, 2:n)

    @show @time S(n)
end
