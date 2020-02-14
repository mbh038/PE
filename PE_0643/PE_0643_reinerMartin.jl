# PE 643

#Reiner Martin solution

using Memoize

const M = 10^9+7
⊕(a, b) = (a + b) % M
⊗(a, b) = ((a % M) * (b % M)) % M

@memoize function g(n)::Int
    n > 1 || return 1
    mod(n ⊗ (n+1) ⊗ invmod(2, M) -
        reduce(⊕, g(div(n, k)) for k in 2:div(n,isqrt(n)+1); init=0) -
        reduce(⊕, g(m) * (div(n, m) - div(n, m+1)) for m in 1:isqrt(n); init=0), M)
end

f(n) = reduce(⊕, g(div(n,2^k)) - 1 for k in 1:ndigits(n; base=2)-1; init=0)

@show @time f(10^2)
