# # PE 0688
# January 21 2020
# Michael Hunt

# Piles of Plates

# 110941813
#runs in Python/numba() in 9.9s

function p688(N)
# total of minimum pile sizes, for all possible numbers of distinct piles, for each n<=N
    kmax=Int64((isqrt(8*N+1)-1)÷2)
    inv2=Int64(invmod(2,M))
    total=0
    for k in 1:kmax
        total+=F2(N,k,inv2)
    end
    return total%M
end

function F2(N::Int64,k::Int64,inv2::Int64)::Int64
# sum of minimum pile size given k distinct piles for all n<=N
    Nmin=k*(k+1)÷2
    d,r=divrem(N-Nmin+1,k)
    a=((k%M *d%M *inv2)%M + r)%M
    b=(d+1)%M
    return a*b %M
end

#fancy Reiner Martin way to sum over all k
# @show @time reduce(+,F2(N,k) for k in 1:kmax;init=0) % M
