

using Primes

function main(n=10^5)
    g=5
    total=p545(g,g)
    print("\n")
    @time p545(n,n)
end

function p545(target,m)
    n=308
    count=0
    ps=zeros(Int32,10^7)
    for n=1:10^7
        ps[n]=1+2*n
    end
    pp=0
    for p in ps
        if 0 in n*p.%[3,5,23]
            continue
        end

        # if (n*p)%3==0 || (n*p)%5==0 || (n*p)%23==0
        #     continue
        # end
        flag=true
        divs=sort(divisors(n*p)) #routine to find divisors of n*p
        if divs[1]==-1
            continue
        end
        for d in divs
            if isprime(d+1)
                if !(d+1 in [2,3,5,23,29])
                    flag=false
                    break
                end
            end
        end
        if flag
            count+=1
            if count==m
                break
            end
        end
        pp=p
    end
    return(count,pp,n*pp)

end


#miller-rabin primality check
function mr(n,k=5)
    #n must be odd and greater than three
    if  n==2 || n==3
        return true
    end
    if  n<=1 || (n & 1) == 0
        return false
    end

    # Write n-1 as d*2^s by factoring powers of 2 from n-1
    s = 0
    m=n-1
    while m&1 == 0
        s+=1
        m>>=1
    end
    d = div((n-1),(1<<s))

    for i in 1:k
        flag=true
        a=rand(2:n-2)
        x=powermod(a,d,n)

        if x ==1 || x == n-1
            continue
        end

        for r=1:s
            x=powermod(x,2,n)
            if x ==1
                return false
            end
            if x == n-1
                flag=false
                break
            end
        end
        if flag
            return false
        end
    end
    # n is *probably* prime
    return true
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
        if mr(p+1) && !(p+1 in [2,3,5,23,29])

            return [-1]
        end

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
