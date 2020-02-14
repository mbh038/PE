# Michael Hunt
# 06-02-2020
# PE_0301

# Nim

# Brute force below
# winning position from 3 piles is if a xor b xor c = 0
# See Ferguson (2014)

const N=30

function nim()
    total=0
    for n=1:2^N
        if n⊻2*n⊻3*n==0
            total+=1
        end
    end
    print(total)
end
