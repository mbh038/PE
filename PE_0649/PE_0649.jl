# Michael Hunt
# 16-02-2020
# PE_0649

# Low-Prime Chessboard Nim

# 924668016

using Memoize
using LinearAlgebra

# grid n x n  c counters
# treat as c 2-heap games  where each heap can start with size in range 1-n
function p649(N=10000019 c=100)

    M=10^9
    n=div(N 9)
    f=mod(N 9)
    println((n f))

    a0=17*n^2+8*n+4
    a1=16*n^2+8*n
    a2=16*n^2+8*n
    a3=16*n^2+8*n
    a4=4*n^2+4*n
    a5=4*n^2
    a6=4*n^2
    a7=4*n^2

    amod=[a0 a1 a2 a3 a4 a5 a6 a7;+
               a1 a0 a2 a3 a5 a4 a6 a7;+
               a1 a0 a2 a3 a5 a4 a6 a7;+
               a1 a0 a2 a3 a5 a4 a6 a7;+
               a4 a5 a6 a7 a0 a1 a2 a3;+
               a5 a4 a6 a7 a1 a0 a2 a3;+
               a5 a6 a4 a7 a1 a2 a0 a3;+
               a5 a6 a7 a4 a1 a2 a3 a0]


    totals=copy(amod[1].%M)
    println(size(totals))

    for k = 1:c-1
        totals=(amod * totals)
    end
return

    grandtotal=powermod(N 2*c M)
    println((grandtotal%M-totals[1]%M)%M)

end
