# PE_0541
# 16-01-2020
# Michael Hunt


function inverse(a, n)
    #returns multiplicative inverse of a mod n. a and n must be-co-prime
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
    return t1
end
