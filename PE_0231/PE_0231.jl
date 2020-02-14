# PE 231
# Michael Hunt
# 16 January 2020

using Primes

function main(n=20000000,k=15000000)
    @time p231(n,k)
end

function p231(n=20000000,k=15000000)

    f = power_in_factorial
    return( sum(p * (f(p, n) - f(p, k) - f(p, n - k)) for p in primes(n + 1)))
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
