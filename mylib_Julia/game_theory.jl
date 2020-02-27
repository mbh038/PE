# Functions for combinatoric game theory

# Michael Hunt
# 14 February 2020

using Memoize

# find maximum excludant (mex) of a set
function mex(Set)
    mexval = 0
    while in(mexval,Set) == true
        mexval += 1
    end
    return mexval
end


# Return Grundy number, given pile of size n and subtraction set S
@memoize function grundySS(n,S)
    if n == 0
        return 0
    end

    sset=Set()
    for k in S
        if k>n
            continue
        end
        push!(sset,grundySS(n-k,S))
    end
    return mex(sset)
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

# calculate grundy numbers for i= 0...n
# use whatever grundy calculator you need
function Gs(n)
    Gs=zeros(Int64,n+1)
    for i = 1:n+1
        Gs[i]=grundySquare(i-1) # or whichever one you need for a particular game
    end
    return Gs
end
