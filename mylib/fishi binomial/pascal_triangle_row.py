#!/usr/bin/env python3

"""
Calculating a row in Pascal's Triangle to determine Binomial Coefficients
"""

# Calculating row 'n' of Pascal's Triangle with modulo 'mod' only remembering last calculated row
# bottom-up dynamic programming approach
# runtime:	O(n**2)
# space:	O(n)
def pascal_triangle_row(n,mod):
    # initialize necessary space for row 'n'
    pascal = [0]*(n+1)
    pascal[0] = 1

    for i in range(1,n+1):
        # initialize auxiliary array
        tmp = [0]*(n+1)
        tmp[0] = 1

        for j in range(1,i+1):
            # calculate current value based on neighbor values from previous row in triangle
            tmp[j] = (pascal[j] + pascal[j-1])%mod

        pascal = tmp

    return pascal

if __name__ == '__main__':
    n = 950 # row of pascal table
    mod = 123456 # not a prime

    # calculate pascal table row 950 with mod 123456
    pascal_row = pascal_triangle_row(n,mod)

    # (950 choose 100) mod 123456
    print(pascal_row[100]) # should be 24942