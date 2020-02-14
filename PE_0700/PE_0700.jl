# Michael Hunt
# 05-02-2020
# PE_0700
# Eulercoin

const a = Int128(1504170715041707)
const b = Int128(4503599627370517)

function p700()
    eulermin=mod(a,b)
    eulermax,eulersum=eulermin,eulermin
    while eulermin>=1
        coin=(eulermin+eulermax)%b
        if coin>eulermax
            eulermax=coin
        elseif coin<eulermin
            eulermin=coin
            eulersum+=coin
        end
    end
    println(eulersum)
end
