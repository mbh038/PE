# Michael Hunt
# 01-March -2020
# Proportionate Nim

# gradient_low=1.4777997752722001205


# 11541685709674 correct for M=10^7! in 4s


function mex(Set,minval)
    mexval = minval
    while Set[mexval+1] >=0
        mexval += 1
    end
    return mexval
end

function p665(M)

    losers=[(1,3),(2,6),(4,5),(7,10),(8,14),(9,17),(11,25),(12,28),(13,18),(15,35),(16,23),(19,31)]
    total=Int64(sum([k[1]+k[2] for k in losers]))
    nms=zeros(Int64,M).-1
    deltas=zeros(Bool,M)
    dhalfs=zeros(Bool,2*M)
    ddoubles=zeros(Bool,M)

    for i=1:length(losers)

        nms[losers[i][1]+1]=losers[i][1]
        nms[losers[i][2]+1]=losers[i][2]
        deltas[abs(losers[i][2]-losers[i][1])+1]=true
        dhalfs[abs(losers[i][1]-2*losers[i][2])+1]=true
        ddoubles[abs(2*losers[i][1]-losers[i][2])+1]=true
    end

    n=maximum(loser[1] for loser in losers)
    counthigh=5

    margin=200

    while 1>0

        n=mex(nms,n)
        nms[n+1]=n
        mcount=0

        gradient_low=1.4778
        m=max(1,floor(Int64,gradient_low*n)-margin)
        if n+m>M
            break
        end

        flag=false
        while flag==false
            mcount+=1
            if n+m>M || mcount>2*margin || m/n>1.56
                break
            end

            check=nms[m+1]>=0 ||
                + deltas[abs(m-n)+1]==true ||
                + dhalfs[abs(n-2*m)+1]==true ||
                + dhalfs[abs(m-2*n)+1]==true ||
                + ddoubles[abs(2*n-m)+1]==true
            if check==true
                m+=1
                continue
            end

            total+=n+m
            nms[m+1]=m
            deltas[abs(m-n)+1]=true
            dhalfs[abs(n-2*m)+1]=true
            ddoubles[abs(2*n-m)+1]=true
            flag=true
            break
        end

        if flag==true
            continue
        end

        counthigh+=1
        m=2*n+counthigh

        if n+m>M
            continue
        end

        total+=n+m
        nms[m+1]=m
        deltas[abs(m-n)+1]=true
        dhalfs[abs(n-2*m)+1]=true
        ddoubles[abs(2*n-m)+1]=true
    end
    println((M,total))
end


function test(M)

# s=Set(1:M)
# if a in s
#     i=1
# end
# s=Set()
s=zeros(M)
for a = 1:M
    # push!(s,a)
    s[a]=a
end

a=0
    for i=1:M
        for j=1:280
            if div(M,2) in s
                a=1
            end
        end
    end
end
