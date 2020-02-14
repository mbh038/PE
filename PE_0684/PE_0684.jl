# PE 684
# 22 January 2020
# Michael Hunt

# Inverse Digit Sum

using Memoize
const M=10^9+7
const inv2=invmod(2,M)

function S2mod(k)
    p,q=divrem(k,9)
    return (((6+(q+1) * (q+2)*inv2-1)%M * powermod(10,p,M))-6-9*p-q)%M
end

@memoize function dijkFib(n)
    #returns nth Fibonacci term mod m
    if n <=1
        return n
    end
    a=dijkFib((n-1)÷2)
    b=dijkFib((n+1)÷2)

    if n%2>0
        return (a^2+b^2)
    end
    if n%2==0
        return ((2*a+b)*b)
    end
end

fibs=(dijkFib(k) for k=2:90)
@show @time mod(sum((S2mod(fib) for fib in fibs)),M)
