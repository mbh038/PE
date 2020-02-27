# Michael Hunt
# 08-02-2020
# PE_0310

# Nim Square

# Sprague-Grundy
# https://cp-algorithms.com/game_theory/sprague-grundy-nim.html

# Nim
# https://mathstrek.blog/2012/08/05/combinatorial-game-theory-iii/

using Memoize
using StatsBase

function Gzeros(n)
    Gs=[]
    for k=0:n
        a=calculateGrundy(k)
        if a==0
            push!(Gs,k)
        end
    end
    return Gs
end

# tetrahedral number = number of triplets 0<=a<=b<=c<=n
function T(n)
    return div(n*(n+1)*(n+2),6)
end

function Gs(n)
    Gs=zeros(Int64,n+1)
    for i = 1:n+1
        Gs[i]=calculateGrundy(i-1)
    end
    return Gs
end


# find maximum excludant (mex) of a set
function mex(Set)
    mexval = 0
    while in(mexval,Set) == true
        mexval += 1
    end
    return mexval
end

# A function to Compute Grundy Number of 'n'
# This version is for where the player must remove a square number of stones
@memoize function grundySquare(n)
    if n == 0
        return 0
    end

    sset=Set()
    nsqrt=isqrt(n)
    for i=1:nsqrt
        push!(sset,grundySquare(n-i^2))
    end
    return mex(sset)
end

function p310(n)
    Gs=zeros(Int64,n+1)
    for i = 1:n+1
        Gs[i]=grundySquare(i-1)
    end
    # sort(Gs,rev=false)
    Gsu=unique(Gs)
    GsMap0=Dict{Int64,Int64}(g=>0 for g in Gsu)
    total=Int128(0)
    for i = 0:n
        c=Gs[i+1]
        GsMap=deepcopy(GsMap0)
        # println((i,GsMap))
        for j=0:i

            Gsj=Gs[j+1]
            bc=c⊻Gsj
            GsMap[Gsj]+=1
            # println((i,j,GsMap))
            total+=get(GsMap,bc,0)
        end
    end
    return total
end
