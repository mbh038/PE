//
//  modular.cpp
//  p381
//
//  Created by Michael Hunt on 13/05/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#include "modular.hpp"

#include <iostream>
#include <ctime>
#include <vector>

// Use this because the remainder operator % does not give the modulus
// for negative integers
int64_t mod(int64_t a, int64_t b){
    int64_t r = a % b;
    return r < 0 ? r + b : r;
}

//dawghaus uses the next two functions to calculate b where ab=1 mod p
void ExtendedEuclidean(uint64_t a, uint64_t b, int64_t &x, int64_t &y)
{
    if (a % b == 0)
    {
        x = 0;
        y = 1;
        return;
    }
    ExtendedEuclidean(b , a % b, x, y);
    int64_t temp = x;
    x = y;
    y = temp - y * (a/b);
}


int64_t ModuloInverse(int64_t a, int64_t m)
//  Returns multiplicative inverse of a mod m
//  I.E, returns inv such that a * inv mod m = 1
//  ExtendedEulidean (Extended Euclidean Algorithm function
//  does the heavy lifting)  The function does not return the
//  gcd of a and b, since all we are interested in is x value.
{
    int64_t x, y;
    ExtendedEuclidean(a, m, x, y);
    if (x < 0)
        x += m;
    return x;
}

//I used this one:

int64_t modular_inverse(int64_t a, int64_t n){
    //returns b such that ab=1 mod n
    
    int64_t t1,t2,r1,r2;
    int64_t q,temp;
    
    t1 = 0;
    t2 = 1;
    r1 = n;
    r2 = a;
    
    while(r2 != 0){
        q = (int64_t)(r1/r2);
        temp=t1;
        t1=t2;
        t2=temp-q*t2;
        temp=r1;
        r1=r2;
        r2=temp-q*r2;
    }
    if (t1<0){
        t1+=n;
    }
    return t1;
}

//Uses Wilson' theorem to return n! mod n
//don't use it in the end
int64_t fnmWilson(int64_t n,int64_t m){
    int64_t prod=-1;
    for (int64_t i=n+1;i<m;i++){
        prod=mod(prod*i,m);
    }
    return modular_inverse(prod,m);
}

