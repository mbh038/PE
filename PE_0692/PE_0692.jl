# Michael Hunt
# 05-02-2020
# PE_0692

# Siegbert and Jo

# This is Fibonacci Nim
# See Ferguson (2014)

using Memoize

@memoize Fib(n)=n<=1 ? n : Fib(n-1)+Fib(n-2)

# returns indices of Fibonacci terms in Zeckendorf representation of n
function Z(n)
    Fs=[]
    ks=[]
    m=0
    while Fib(m)<=n
        m+=1
    end
    m-=1
    push!(Fs,Fib(m))
    push!(ks,m-1)
    mlast=m
    while m>0
        m-=1
        Fm=Fib(m)
        if sum(Fs)+Fm<=n && mlast-m>1
            push!(Fs,Fib(m))
            push!(ks,m-1)
            mlast=m
        else
            push!(Fs,0)
        end
    end
    if length(ks)>1
        ks=ks[1:end-1]
    end
    return ks
end

function p692(N=23416728348467685)

    n=Z(N)[1]
    fibs=[Fib(k) for k=2:n+1]
    diffs=[0,0]

    for k = 3:n-1
        push!(diffs,fibs[k-2]+diffs[k-2]+diffs[k-1])
    end

    return sum(fibs)+sum(diffs)
end
