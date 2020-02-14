function primeSieve(n)
    #return array of primes p: 2<=p<=n
    # slower than the numpy() version
    sieve=ones(Int32,n+1)
    for i =2:floor(Int32,(n+1)^0.5+1)
        if sieve[i] != 0
            for k=2i:i:n
                sieve[k]=0
            end
        end
    end
    sieve[1]=0
    result = eltype(sieve)[]
    for i=1:n
        if sieve[i] != 0
            push!(result,i)
        end
    end
    return result
end

# Legendre theorem
function power_in_factorial(p, n)
    """Return the exponent of the prime p in the factorization of n!"""
    result = 0
    while true
        n =div(n,p)
        if n==0
            break
        end
        result += n
    end
    return result
end

# Sieve of Eratosthenes, based on Alex A code from
# https://codegolf.stackexchange.com/questions/74269/calculate-the-number-of-primes-up-to-n
# Alex A
function primepi(n::Int64)
    # returns array of primepi(n) n: 2<=n<=limit
    sieve = trues(n)
    sieve[1] = false
    for p = 2:isqrt(n)
        sieve[p] || continue
        for i = 2:n÷p
            sieve[p*i] = false
        end
    end
    return sum(sieve) # replace with sum(... ) if ust want #primes < n
end

# translation from my numpy() code
# is 3 x slower than primepi
function myprimepi(n::Int64)
    # returns array of primepi(n) n: 2<=n<=limit
    sieve=ones(n)
    # for i =2:floor(Int64,(n+1)^0.5+1)
    for i =2:isqrt(n)
        if sieve[i]!=0
            for k=2i:i:n
                sieve[k]=0
            end
        end
    end
    sieve[1]=0
    return cumsum(sieve)
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

function test(n=500*10^6)
    @time primepi(n)
    @time myprimepi(n)
end
