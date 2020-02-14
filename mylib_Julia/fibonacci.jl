
using Memoize

# from Reiner Martin
@memoize fib(n) = ([1 1; 1 0]^n)[1,2]

@memoize Fib(n)=n<=1 ? n : Fib(n-1)+Fib(n-2)

# Fibonacci mod m: 0.2 micro s - but unstable with large n
@memoize fibMod(n,m)=n<=1 ? n : (fibMod(n-1,m)%m+fibMod(n-2,m)%m)%m

#Dijkstra algorithm: 4 micro s
@memoize function dijkFibMod(n::Int64,m::Int64)::Int64
    #returns nth Fibonacci term mod m
    if n <=1
        return n
    end
    a=dijkFibMod((n-1)÷2,m)
    b=dijkFibMod((n+1)÷2,m)

    if n%2>0
        return (a^2+b^2)%m
    end
    if n%2==0
        return ((2*a+b)*b)%m
    end
end

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
