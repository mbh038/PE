function test(N)
    count=0
    for i=1:N
        for j=1:N
            count+=1
        end
    end
    println(count)
end

function p665(M)

    losers=[(0,0),(1,3),(2,6),(4,5)]#,[2,6],[4,5],[3,1],[6,2],[5,4]]
    count=0

    ah,bh=2.2476,0.7486
    al,bl=1.47813,0.07693
    # for m=1:M
    for n=1:div((M-bh),(ah+1))
        # for n=1:min(m,M-m)#min(m,M-m)
        for m=floor(Int,0.95*(bh+ah*n)):floor(Int,1.05*(bh+ah*n))
            winner=false
            for loser in losers
                    # println((n,m,loser))
                if n in loser
                    winner=true
                    # println("Hello A: ",(loser,n,m))
                    break
                end
                if m in loser
                    winner=true
                    # println("Hello B: ",(loser,n,m))
                    break
                end
                if n - loser[1]==abs(m - loser[2])
                    winner=true
                    # println("Hello C: ",(loser,n,m))
                    break
                end
                # println((n,loser,n .- loser,abs.((m .- loser)/2)))
                if n - loser[1]==abs((m - loser[2])/2)
                    winner=true
                    # println("Hello D: ",(loser,n,m))
                    break
                end
                if n - loser[2]==abs((m - loser[1])/2)
                    winner=true
                    # println("Hello D: ",(loser,n,m))
                    break
                end
                if n - loser[1]==abs(2*(m - loser[2]))
                    winner=true
                    # println("Hello E: ",(loser,n,m))
                    break
                end
                if n - loser[2]==abs(2*(m - loser[1]))
                    winner=true
                    # println("Hello E: ",(loser,n,m))
                    break
                end
            end
            if winner==false
                count+=1
                push!(losers,(n,m))
                # println((n,m))
            end
        end
    end


    total=0
    for loser in losers
        println(loser)
        total+=sum(loser)
    end

    println((M,total))
    println(count)

end
