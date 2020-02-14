
function main(n=50*10^6)
    g=5
    total=p423(g)
    @time p423(n)
end

function p423(limit)
    # pps=myprimepi(limit+1)
    pps=primepi(limit+1)
    mv=10^9+7
    total=p423_sub(limit,pps,mv)
    return total
end

function p423_sub(limit,pps,mv)

    total=3
    pmk,p_mp1_k,p_mm1_km1=3,0,nothing
    k,pow5=0,1
    nstart=4
    k=pps[nstart]

    inverses=zeros(Int32,limit)
    inverses[1] = 1
    for i = 2:limit
        inverses[i] = (mv - div(mv,i) * inverses[mv%i] % mv) % mv
    end

    for n = nstart:limit
        nextk=pps[n+1]
        if k != nextk
            p_mm1_km1=pmk
            k=nextk
            continue
        elseif p_mm1_km1 != nothing
            pmk=((n-1) * inverses[k] % mv * p_mm1_km1) % mv
        end
        p_mp1_k=(n * inverses[n-k] % mv * pmk) % mv
        pow5=(pow5 * 5) % mv
        total+=(pow5 * p_mp1_k) % mv
        p_mm1_km1= nothing
        pmk=p_mp1_k
        k=nextk
    end

    # Now we are on our final row of the Pascal triangle.
    # Time to head left to the beginning of the row.
    p_mp1_kp1=p_mp1_k
    kmax=k
    for k = kmax-1:-1:0
        p_mp1_k=((k+1) * inverses[limit-k] % mv * p_mp1_kp1) % mv
        pow5=(pow5 * 5)%mv
        total+=(pow5 * p_mp1_k)  %mv
        p_mp1_kp1=p_mp1_k
    end
    return (6%mv*total%mv)%mv
end

function myprimepi(limit::Int64)
#  returns array of primepi(n) n: 2<=n<=limit
    sieve=ones(Int64,limit)
    for i =2:isqrt(n)
        if sieve[i]!=0
            for k=2i:i:limit
                sieve[k]=0
            end
        end
    end
    sieve[1]=0
    return cumsum(sieve[1:end])
end
# https://codegolf.stackexchange.com/questions/74269/calculate-the-number-of-primes-up-to-n
# Alex A
function primepi(n::Int64)
    sieve = trues(n)
    sieve[1] = false
    for p = 2:isqrt(n)
        sieve[p] || continue
        for i = 2:n÷p
            sieve[p*i] = false
        end
    end
    return cumsum(sieve)
end

# note: we did not need this in the end - and could use Mods instead.
function inverse(a, n)
# returns multiplicative inverse of a mod n. a and n must be-co-prime
    t1,t2=0,1
    r1,r2=n,a
    while r2!=0
        q = div(r1,r2)
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2
    end
    if t1 < 0
        t1 +=n
    end
    return t1 % n
end
