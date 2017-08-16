//
//  divisors.cpp
//  
//
//  Created by Michael Hunt on 14/05/2017.
//
//

#include <iostream>
using namespace std;
#include <map>


int nDivisors(ll n){
    //returns number of divisors of n
    //  requires #include <map>
    ll i=2;
    map <ll,int> factors;
    while (i*i<=n){
        if (n%i){
            i+=1;
        }
        else {
            n = (ll)(n/i);
            factors[i]+=1;
        }
    }
    if (n>1){
        factors[n]+=1;
    }
    int divisors=1;
    for ( const auto &myPair : factors ) {
        divisors*=(myPair.second+1);
    }
    return divisors;
}
