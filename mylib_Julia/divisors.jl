function ndivisors(n)
    # find number of divisors of n from prime factor exponents"""

    i = 2
    factors = Dict()
    while i * i <= n
        if n % i !=0
            i += 1
        else
            n =div(n,i)
            factors[i]=get(factors,i,0)+1
        end
    end
    if n > 1
        factors[n]=get(factors,n,0)+1
    end

    divisors=1
    vs=[value for value in values(factors)]
    for v in vs
        divisors*=(v+1)
    end

    return divisors
end

function pfdic(n)
    # returns the distinct prime factors of n as {prime1:exponent1,...}
    i = 2
    factors = Dict{Int64,Int64}()
    while i * i <= n
        if n % i>0
            i += 1
        else
            n = div(n,i)
            factors[i]=get(factors,i,0)+1
        end
    end
    if n > 1
        factors[n]=get(factors,n,0)+1
    end
    return factors
end

#Euler sigma is sum of divisors of n, including 1 and n
#fastest
function eulersigma(n)

    pfs=pfdic(n)
    es=1
    for (p,e) in pfs
        es*=div((p^(e+1)-1),(p-1))
    end
    return es
end

function divisors(n)
    #returns the divisors of n"""
    #first get the prime factors
    i = 2
    fs = Dict()
    while i * i <= n
        if n % i != 0
            i += 1
        else
            n =div(n,i)
            fs[i]=get(fs, i, 0)+1
        end
    end
    if n > 1
        fs[n]=get(fs, n, 0)+1
    end

    ps=[key for key in keys(fs)] #prime factors
    es=[value for value in values(fs)] #exponents

    divs=Array{Int32}(undef,0)
    nfactors = length(ps)
    f = zeros(Int32,nfactors)
    while true
        p=1
        pfs=[x^y for (x,y) in zip(ps,f)]
        for i in 1:length(ps)
            p*=pfs[i]
        end
        append!(divs,p)

        i = 1
        while true
            f[i] += 1
            if f[i] <= es[i]
                break
            end
            f[i] = 0
            i += 1
            if i > nfactors
                return divs
            end
        end
    end
end
