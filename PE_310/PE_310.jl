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

function  p310(n)
    Gs=zeros(Int64,n+1)
    for i = 1:n+1
        Gs[i]=calculateGrundy(i-1)
    end

    selfg=Dict{Int64,Array{Tuple{Int64,Int64}}}(Gs[i]=>[] for i=1:n+1)

    for g in keys(selfg)
        for h in keys(selfg)
            gh=g⊻h
            if in(gh,keys(selfg))
                push!(selfg[g],(h,gh))
            end
        end
    end

    return selfg
end

function p310v1(n)
    Gs=zeros(Int64,n+1)
    for i = 1:n+1
        Gs[i]=calculateGrundy(i-1)
    end
    sort(Gs,rev=true)

    GsMap=countmap(Gs[1:n+1])

    # return Gs
    total=Int64(0)
    for i = n:-1:0
        c=Gs[i+1]
        for j=i:-1:0
            bc=c⊻Gs[j+1]
            # total+=length(findall(x->x==bc,Gs[1:j+1]))

            total+=get(Gs,bc,0)
            # for k=j:-1:0
            #     abc=bc⊻Gs[k+1]
            #     if abc==0
            #         if Gs[i+1]==2 && Gs[j+1] == 3 && Gs[k+1] == 1
            #             println((i,j,k),(Gs[i+1],Gs[j+1],Gs[k+1]),(ab))
            #         end
            #         total+=1
            #     end
            # end
        end
    end
    # println((total,div((n+1)*(n+2)*(n+3),6)))
    return total
    # return Gs
end

# find maximum excludant (Mex) of a set
function calculateMex(Set)
    Mex = 0
    while in(Mex,Set) == true
        Mex += 1
    end
    return Mex
end

# A function to Compute Grundy Number of 'n'
# Only this function varies according to the game
# This version is for where the player must remove a square number of stones
@memoize function calculateGrundy(n)

    if n == 0
        return 0
    # elseif n == 1
    #     return 1
    elseif n == 2
        return 0
    end

    sset=Set()

    nsqrt=isqrt(n)
    for i=1:nsqrt
        push!(sset,calculateGrundy(n-i^2))
    end

    return calculateMex(sset)
end
