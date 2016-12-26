#!/usr/bin/env python3

"""
Calculating Pascal's Triangle to determine Binomial Coefficients nCk % m
"""

# Calculating Pascal's Triangle until row 'n' with modulo 'mod'
# bottom-up dynamic programming approach
# runtime:	O(n**2)
# space:	O(n**2)
def pascal_triangle(n,mod):
    # prepare first row in table
    pascal = []
    pascal.append([1,0])

    for i in range(1,n+1):
        # initialize new row in table
        pascal.append([])
        pascal[i] = [0]*(i+2)
        pascal[i][0] = 1

        for j in range(1,i+1):
            # calculate current value based on neighbor values from previous row in triangle
            pascal[i][j] = (pascal[i-1][j] + pascal[i-1][j-1])%mod

    return pascal

if __name__ == '__main__':
    n = 1009 # number of rows in pascal table
    mod = 123456 # not a prime

    # calculate pascal table with mod 123456
    pascal = pascal_triangle(n,mod)

    # (950 choose 100) mod 123456
    print(pascal[950][100]) # should be 24942