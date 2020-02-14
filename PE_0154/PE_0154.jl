function main(n=200000,d=12)
    total=p154bf(20,5)
    @time p154bf(n,d)
end

function p154bf(level::Int64,divisor::Int64)

    nsum=0
    nfac2,nfac5=facpfac(level,2),facpfac(level,5)
    mults=Int64[1,3,6]
    facs2=Int64[facpfac(x,2) for x in 1:level]
    facs5=Int64[facpfac(x,5) for x in 1:level]
    for p in 1:level÷2
        nf5_pf5=nfac5-facs5[p]
        nf2_pf2=nfac2-facs2[p]
        for q in 1:min(p, level-2*p)
            r=level-p-q
            if nf5_pf5-facs5[q]-facs5[r]<divisor
                continue
            end
            if nf2_pf2-facs2[q]-facs2[r]<divisor
                continue
            end
            if p==q || p==r
                nsum+=3
                continue
            end
            nsum+=6
        end
    end
    return nsum
end

function facpfac(n::Int64,prime::Int64)
# returns the exponent of prime as a factor of n!
    e=0
    power=1
    delta=10
    while delta>0
        delta=n÷prime^power
        e+=delta
        power+=1
    end
    return e
end

function test(level=200000)
    @time facs=Dict{Int64,Array{Int64,1}}(x=> facpfac(x,2) for x in 0:level)
end
