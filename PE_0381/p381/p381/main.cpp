//
//  main.cpp
//  p381
//
//  Created by Michael Hunt on 12/05/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//
//  Ans: 139602943319822

#include <iostream>
using namespace std;
typedef long long ll;
#include <ctime>
#include <vector>
#include <cmath>

const ll limit = 100000000;
vector<bool> primes(limit+1, true);

// Use this because the remainder operator % does not give the modulus
// for negative integers
ll mod(ll a, ll b){
    ll r = a % b;
    return r < 0 ? r + b : r;
}

void primeSieve(vector<bool> &p){
// Calling function would need declaration similar to
//      int const vectorSize = 1000000;
//      vector<bool> primes(vectorSize, true);
//      SieveOfEratosthenes(primes);
//      Program must declare #include <vector>
    p[0]=false;
    p[1]=false;
    for (int i=2;i<sqrt(p.size());i++){
        if (p[i]){
            for (int j=i*i;j<p.size();j+=i){
                p[j]=false;
            }
        }
    }
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

ll modular_inverse(ll a, ll n){
//returns b such that ab=1 mod n
    
    ll t1=0,t2=1,r1=n,r2=a;
    ll q,temp;
    
    while(r2 != 0){
        q = (ll)(r1/r2);
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
ll fnmWilson(ll n,ll m){
    ll prod=-1;
    for (ll i=n+1;i<m;i++){
        prod=mod(prod*i,m);
    }
    return ModuloInverse(prod,m);
}

// S = (p-1)! + (p-2)! + (p-3)! + (p-4)! + (p-5)! mod p as defined in problem intro.
// given Wilson's theorem : (p-1)! = -1 mod p we can show that
// S = -3/8 mod p = -3 * modular inverse of 8 mod p
// very neat
ll S (ll p){
    return mod((-3*modular_inverse(8,p)),p);
}

int main(){
    time_t t = clock();
    ll sum=0;
    primeSieve(primes);
    for (ll p=5;p<limit;p++){
        if (primes[p]){
            sum+=S(p);
        }
    }
    cout << sum << endl;
    cout << double(clock() - t) / CLOCKS_PER_SEC << " s" << endl;
}

