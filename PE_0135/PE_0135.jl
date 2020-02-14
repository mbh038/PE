function main(n=10,limit=1000000)
    dummy=p135(10,100)
    @time p135(n,limit)
end

function p135(n=10,limit=1000000)
    solutions=zeros(limit)
    for c in 1:limit+1
        b=4-c%4
        while b*c<limit && b < 3*c
            solutions[b*c-1]+=1
            b+=4
        end
    end
    println(length(solutions[solutions.==n]))
end

function p135v2(n=10,limit=1000000)
    solutions=Dict{Int64,Int64}()
    for x=1:10*limit
        for a=div(x,5):div(x,2)+1
            nn=-(x-5a)*(x-a)
            if nn<limit
                solutions[nn]=get(solutions,nn,0)+1
            end
        end
    end

    count=0
    for (key, value) in solutions
        if value==10
            count+=1
            # println(key," ",value)
        end
    end

    return count
end




function p135v(n,limit)
    found=[]
    for i in 1:limit-1
        if ndivisors(i)>=2
            push!(found,i)
        end
    end
    nn=0
    for d in found
        j=0
        aset=[]
        ds=sort!(divisors(d))
        for i in 1:div(length(ds)+1,2)
            d1,d2=ds[i],ds[end-i+1]
            if (d1+d2)%4>0
                continue
            end
            delta=div(d1+d2,4)
            a1=delta+d1
            a2=delta+d2
            if a1>2*delta && a1<5*delta
                j+=1
                # aset[j]=[a1,delta]
                push!(aset,(a1,delta))
            end
            j+=1
            # aset[j]=[a2,delta]
            push!(aset,(a2,delta))
        end
        if length(unique(aset))==n
            nn+=1
        end
    end
    println(nn)
end



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
