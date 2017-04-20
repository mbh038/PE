//
//  numberTheory.hpp
//
//  Library of number theory functions
//
//  Created by Michael Hunt on 13/04/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#ifndef numberTheory_hpp
#define numberTheory_hpp

#include <stdio.h>
#include <vector>
#include <map>
#include <cmath>
//using namespace std;

//Euler gcd
int gcd(int a, int b){
    int r = a % b;
    while (r>0){
        a=b;
        int tmp=b;
        b=r;
        r=tmp%r;
    }
    return b;
}

//Euler gcd with int precision
int Gcd(int a, int b){
    int r = a % b;
    while (r>0){
        a=b;
        int64_t tmp=b;
        b=r;
        r=tmp%r;
    }
    return b;
}

//Euler gcd with long long precision
int64_t Gcd(int64_t a, int64_t b){
    int64_t r = a % b;
    while (r>0){
        a=b;
        int64_t tmp=b;
        b=r;
        r=tmp%r;
    }
    return b;
}


std::vector<int> MakePrimes2(int upperlimit)
{
    int bound = (int) floor(sqrt(upperlimit));
    std::vector<bool> primes(upperlimit, true);
    std::vector<int> outval;
    primes[0] = false;
    primes[1] = false;
    //Since 2 is a special case if we do it separately we can optimize the rest since
    //they will all be odd
    for(int i = 4; i < upperlimit; i += 2)
    {
        primes[i] = false;
    }
    outval.push_back(2);
    //Since the only ones we need to look at are odd we can step by 2
    for (int i = 3; i  <= bound; i += 2)
    {
        if (primes[i])
        {
            //Since we are looping already we might as well start filling the
            //outval vector
            outval.push_back(i);
            //Since all the even multiples are already accounted for we start
            //at the square of the number
            //and since it is odd skip to every other multiple
            for (int j = i*i; j < upperlimit; j += i * 2)
            {
                primes[j] = false;
            }
        }
    }
    //Fill the rest of the vector starting one past the square root of the upperlimit
    for(int i = bound+1;i < upperlimit; i++)
    {
        if(primes[i])
            outval.push_back(i);
    }
    return outval;
}

#define MAX_N 300

int factorial(int n)
{
    return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n;
}

void combinations (std::vector <int> vin,const int r,std::vector<std::vector <int>> &vout){
    //calling function must set up a matrix std::vector<std::vector<int>> vout;
    //on completion of this routine, vout will contain the n!/(n-r)r! combinations
    //of r elements drawn from vin, of length n.
    int n;
    n=(int)vin.size();
    std::vector<bool> v(n);
    std::fill(v.begin(), v.begin() + r, true);
    
    do {
        std::vector<int> thisComb;
        for (int i = 0; i < n; ++i) {
            if (v[i]) {
                thisComb.push_back(vin[i]);
            }
        }
        vout.push_back(thisComb);
    } while (std::prev_permutation(v.begin(), v.end()));
}



#endif /* numberTheory_hpp */

