# Michael Hunt
# 23-01-2020
# PE_0371

# License plates

function qtot(d)
total=0
for x=1:100
    total+=x*q(x-1,d)
end
println(total)
end

#

# probability that the kth integer chosen from [1,d]
# wil repeat at least one previous case =q(k-1,d)
function q(n,d)
    return 1-((d-1)/d)^n
end

# expected total number of times a selection will repeat
# a previous selection
function collision(n,d)
    return n-d+d*((d-1)/d)^n
end

function Q(M)
    Q=1
    for k=1:M
        Qterm=1
        for j=1:k
            Qterm*=1-j/M
        end
        Q+=Qterm
    end
    return Q
end

function p371sim(maxval::Int64,trials=10000000)
    cars=0
    # Seen=Dict{Int64,Bool}((k,false) for k=1:maxval)
    Seen=zeros(Int64,maxval+1)
    for i = 1:trials
        for k =1:maxval+1
            Seen[k]=0
        end
        while 1>0
            plate=rand(0:maxval-1)
            cars+=1
            if plate != 0
                sComp=maxval-plate
                # sComp=plate
                if Seen[sComp+1]>0
                    break
                end
            end
            Seen[plate+1]+=1
        end
        # for k =1:maxval
        #     Seen[k]=0
        # end
    end
    println(cars/trials)
    return Seen
end

# how many cars if win with 1 then 999
function p371simk(k,maxval::Int64,trials=10000000)
    cars=0
    # Seen=Dict{Int64,Bool}((k,false) for k=1:maxval)
    Seen=zeros(Int64,maxval+1)
    for i = 1:trials
        for j =1:maxval+1
            Seen[j]=0
        end
        while 1>0
            plate=rand(0:maxval-1)
            cars+=1
            if plate != 0
                sComp=maxval-plate
                # sComp=plate
                if Seen[k+1]>0 && Seen[maxval-k+1]>0
                    break
                end
            end
            Seen[plate+1]+=1
        end
        # for k =1:maxval
        #     Seen[k]=0
        # end
    end
    println(cars/trials)
    return Seen
end

# how many cars until see two with same plate
function p371simsame(maxval::Int64,trials=10000000)
    cars=0
    # Seen=Dict{Int64,Bool}((k,false) for k=1:maxval)
    Seen=zeros(Int64,maxval)
    for i = 1:trials
        for k =1:maxval
            Seen[k]=0
        end
        while 1>0
            plate=rand(0:maxval-1)
            cars+=1
            if Seen[plate+1]>0
                break
            end
            Seen[plate+1]+=1
        end
        # for k =1:maxval
        #     Seen[k]=0
        # end
    end
    println(cars/trials)
    return Seen
end


# give expectation value of n if maxval=2, so plates are 0 or 1
function p371b2(nmax)
    total=0
    for k in 1:nmax
        total+=k*(k-1)/2^k
        println(k," ",total)
    end
end

# give expectation value of n if maxval=3, so plates are 0, 1 or 2
function p371b3(nmax)
    total=0
    for k::Int128 in 1:nmax
        newterm=k*(2/3)^k-2*k/3^k
        total+=newterm
        println(k,"\t ",newterm,"\t",total)
    end
end

# n plates seen, k distinct plates
# this is the number of possible combinations that can have been observed so far
function nseen(n,k=1000)
    return binomial(n+k-1,k-1)
end

# of the n plates seen, given k distinct plates available, m are distinct
# this is the number of ways of seeing m distinct plates among n seen in total,
# given k available
function mdistinct(m,n,k)
    return binomial(k,m)*binomial(n-1,m-1)
end

function pNn(N,n)

    ksum=0
    for k=1:n-1
        ksum+=N^(k-1)-((N-1)^(k-1))
    end

    know=N^(n-1)-(N-1)^(n-1)

    return (know,ksum)

end
