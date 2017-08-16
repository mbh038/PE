//
//  numberTheory.cpp
//  pe510
//
//  Created by Michael Hunt on 13/04/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#include <iostream>
//#include "numberTheory.hpp"
#include <cmath>
#include <cstdlib>
#include <stdint.h>
#include <vector>
#include <algorithm>    // std::count_if
#include <ctime>
#include <map>
using namespace std;

typedef long long ll;
const ll limit = 2e6;

bool isPrime(ll n){
///test for primality
    ll i=5,w=2;
    if(n==2 || n==3) return true;
    if (n%2==0 || n%3==0) return false;
    while (i*i<=n){
        if(n%i==0) return false;
        i+=w;
        w=6-w;
    }
    return true;
}

void primeFactors(int n,vector<int> &pf){
// Find prime factors of n
// Calling function would need declaration similar to
//      vector<int> pf;
//      primeFactors(n,pf);
//      Program must declare #include <vector>
    int i=2;
    while (i*i<n+1){
        if (n%i){
            i+=1;
        }
        else{
            n /=i;
            pf.push_back(i);
        }
    }
    if (n>1){
        pf.push_back(n);
    }
}

//Sieve of Eratosthenes - derived from dawghaus
void primeSieve(vector<bool> &p){
// Calling function would need declaration similar to
//      int const vectorSize = 1000000;
//      vector<bool> primes(vectorSize+1, true);
//      SieveOfEratosthenes(primes);
//      Program must declare #include <vector>
    p[0]=false;
    p[1]=false;
    for (ll i=2;i<sqrt(p.size());i++){
        if (p[i]){
            for (ll j=i*i;j<p.size();j+=i){
                p[j]=false;
            }
        }
    }
}

ll primeCount(ll n){
// Counts number of primes less than or equal to n
// 3.9s for 10^8
    vector<bool> p(n, true);
    p[0]=false;
    p[1]=false;
    for (ll i=2;i<pow(p.size()+1,0.5);i++){
        if (p[i]){
            for (ll j=i*i;j<p.size();j+=i){
                p[j]=false;
            }
        }
    }
    ll mycount=count (p.begin(), p.end(), true);
    return mycount;
}
/////////////////////////////////////////////////////
//Implementation of Meissel–Lehmer algorithm for prime counting/summing
//code by LucyHedghog in forum for p10 -page 5
//
ll MLprimeSum(ll n){
    ll i,p,sp,p2;
    ll r = sqrt(n);
    vector<ll> V;
    map<ll,ll> S;
    for (i=0;i<r;++i)
        V.push_back(n/(i+1));
    for (i=r;i<2*r-1;++i)
        V.push_back(2*r-1-i);
    for (i=0;i<2*r;++i)
        S[V[i]]=V[i]*(V[i]+1)/2-1;
    for(p=2;p<r+1;++p){
        if (S[p]>S[p-1]){ // p is prime
            sp=S[p-1]; //sum of primes smaller than p
            p2=p*p;
            for(i=0;i<2*r;++i){
                if(V[i]<p2) break;
                S[V[i]]-=p*(S[V[i]/p]-sp);
            }
        }
    }
    return S[n];
}

///////////////////////
// Segmented sieve prime counter by Kim Walisch

/// Set your CPU's L1 data cache size (in bytes) here
const int L1D_CACHE_SIZE = 30000;//32768;

/// Generate primes using the segmented sieve of Eratosthenes.
/// This algorithm uses O(n log log n) operations and O(sqrt(n)) space.
/// @param limit  Sieve primes <= limit.
///
void segmented_sieve(int64_t limit)
{
    int sqrt = (int) std::sqrt(limit);
    int segment_size = max(sqrt, L1D_CACHE_SIZE);
    
    int64_t count = (limit < 2) ? 0 : 1;
    int64_t s = 3;
    int64_t n = 3;
    
    // generate small primes <= sqrt
    vector<char> is_prime(sqrt + 1, 1);
    for (int i = 2; i * i <= sqrt; i++)
        if (is_prime[i])
            for (int j = i * i; j <= sqrt; j += i)
                is_prime[j] = 0;
    
    // vector used for sieving
    vector<char> sieve(segment_size);
    vector<int> primes;
    vector<int> next;
    
    for (int64_t low = 0; low <= limit; low += segment_size)
    {
        fill(sieve.begin(), sieve.end(), 1);
        
        // current segment = interval [low, high]
        int64_t high = min(low + segment_size - 1, limit);
        
        
        // add new sieving primes <= sqrt(high)
        for (; s * s <= high; s += 2)
        {
            if (is_prime[s])
            {
                primes.push_back((int) s);
                next.push_back((int)(s * s - low));
            }
        }
        
        
        // sieve the current segment
        for (size_t i = 0; i < primes.size(); i++)
        {
            int j = next[i];
            for (int k = primes[i] * 2; j < segment_size; j += k)
                sieve[j] = 0;
            next[i] = j - segment_size;
        }
        
        for (; n <= high; n += 2)
            if (sieve[n - low]) // n is a prime
                count++;
    }
    
    cout << count << " primes found." << endl;
}

//not yet finished
ll nextPrime(ll n){
    if (n%2==0) n+=1;
        return 0;
}


/////////////////////////////////////////////
//// test primeFactors
int main(){

    int const nmax = 100;
    vector<int > pf;
    ;
    for (int n=2;n<nmax;n++){
        primeFactors(n,pf);
        cout<<n<<": ";
        for (int j=0;j<pf.size()-1;j++){
            cout<<pf[j]<<",";
        }
        cout<<pf.back();
        cout<<endl;
        pf.clear();
    }
    return 0;
}

/////////////////////////////////////////////
//// test MLPrimeSum
//int main(){
//    cout<<MLprimeSum(limit)<<"\n";
//    return 0;
//}

/////////////////////////////////////////////
//// test isPrime
//int main(){
//    
//    int const vectorSize = 100;
//    vector<bool> primes(vectorSize, true);
//    primeSieve(primes);
//    for (int i=2;i<primes.size();i++){
//        cout<<i<<","<<primes[i]<<","<<isPrime((ll)i)<<endl;
//    }
//    return 0;
//}

/////////////////////////////////////////
// test primeCount
//int main(){
//    time_t t = clock();
//    cout<<primeCount(limit)<<endl;
//    cout << double(clock() - t) / CLOCKS_PER_SEC << " s" << endl;
//    return 0;
//}

//////////////////////////////////////////
// test segmented prime sieve
//int main(int argc, char** argv){
//    time_t t = clock();
//    cout<<"Sieving for primes less than: "<<limit<<endl;
//    cout<<"Cache size: "<<L1D_CACHE_SIZE<<endl;
//    if (argc >= 2)
//        segmented_sieve(atol(argv[1]));
//    else
//        segmented_sieve(limit);
//    cout << double(clock() - t) / CLOCKS_PER_SEC << " s" << endl;
//    return 0;
//}
