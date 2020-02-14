# PE 0643
# January 18 2020
# Michael Hunt

# 2-Friendly

# n=10^10: 292126961
# n=10^11: 968274154

# I eventually (it is almost always eventually with me) realised that what we want is
#
# $$ \sum_{d=2^k: d | n}\Phi(d)=\sum_d\sum_{k=1}^d\phi(k)$$
# where $\phi(n)$ is the totient function.

using Memoize
using BenchmarkTools

const M = 10^9+7
pow10 = 11

# As used in PE512 -
#implements stack exchange 'Andy'
#http://math.stackexchange.com/questions/316376/how-to-calculate-these-totient-summation-sums-efficiently
@memoize function R2(n)::Int64
        #R2(n)+1 is the totient sum: Φ(n) = Σ ϕ(k) for k ∈ 1:n
    if n==1
        return 0
    else
        fsum = mod(mod(mod(n,M)*mod((n-1),M),M)*invmod
        (2,M),M)
        m=2
        while true
            x = div(n,m)
            nxt = div(n,x)
            if(nxt >= n)
                return mod(mod(fsum,M) - mod(mod(n-m+1,M) * mod(R2(x),M),M),M)
            end
            fsum = mod(mod(fsum,M) - mod(mod(nxt-m+1,M) * mod(R2(x),M),M),M)
            m = nxt+1
        end
    end
end

p643(n)=mod(reduce(+,R2(div(n,2^k)) for k in 1:ndigits(n; base=2)-1; init=0),M)

@show pow10
@show @benchmark p643(10^pow10)
@show p643(10^pow10)
