//
//  p501.cpp
//  
//
// Created by Michael Hunt on 15/05/2017.
//
// Uses primesieve by Kim Walisch
//
// For limit = 10^12:
//
// sum3 = 190614467420
// sum2 = 7297845280
// sum1 = 15
//
// clang++ p501.cpp -o p501 -lprimesieve -std=c++11

#include <primesieve.hpp>
#include <vector>
#include <tuple>
#include <stdint.h>
#include <iostream>
#include <cmath>
#include <ctime>

using namespace std;
typedef long long ll;

void primeSieve(vector<bool> &p){
    p[0]=p[1]=false;
    for (ll i=2;i<sqrt(p.size());i++){
        if (p[i]){
            for (ll j=i*i;j<p.size();j+=i){
                p[j]=false;
            }
        }
    }
}

void primeProd(ll limit,vector<tuple<ll,ll>> &pp){
    ll p2limit=pow(limit/2,0.5);
    vector<ll> ps,qs;
    primesieve::generate_primes((ll)sqrt(limit), &ps);
    qs=ps;
    for (ll i=0;i<ps.size();i++){
        for (ll j=i+1;j<qs.size();j++){
            ll p2 = qs[j];
            if (p2<=ps[i])
                continue;
            ll prod = ps[i]*qs[j];
            if (limit/prod <=p2)
                break;
            pp.push_back(make_tuple(p2,prod));
        }
    }
    sort(pp.begin(), pp.end(), [](const std::pair<ll,ll> &left, const std::pair<ll,ll> &right) {
        return left.first < right.first;
    });
}

ll sum1(ll limit){
    return primesieve::count_primes(0, pow(limit,0.14285714285714285));
}


ll sum2(ll limit){
    ll sumpf=0;
    vector<ll> ps;
    primesieve::generate_primes((ll)sqrt(limit), &ps);
    ll i=0;
    while(pow(ps[i],3)*ps[i+1]<=limit){
        sumpf+=primesieve::count_primes(0, (ll)(limit/pow(ps[i],3)));
        i+=1;
    }
    sumpf-=i+(ll)floor(i*(i-1)/2);
    ll j=0;
    while ((ll)(ps[j]*pow(ps[j+1],3))<=limit){
        ll count=primesieve::count_primes(0,cbrt(limit/ps[j]));
        sumpf+=primesieve::count_primes(0,cbrt(limit/ps[j]));
        j+=1;
    }
    sumpf-=j+(ll)floor(j*(j-1)/2);
    return sumpf;
}

ll sum3 (ll limit){
    vector<tuple<ll,ll>> pps;
    ll sum3=0,lastp2=0,p2pc=1;
    uint64_t count;
    primeProd(limit,pps);
    for (ll i=0;i<pps.size();i++){
        ll p2 = get<0>(pps[i]);
        if (p2>lastp2){
            lastp2=p2;
            p2pc+=1;
        }
        ll prod = (ll)get<1>(pps[i]);
        count=primesieve::count_primes(0, limit/prod);
        sum3+=count-p2pc;
    }
    return sum3;
}

int main(){
    
    clock_t t;
    t = clock();
    
    ll const limit = 1e6;
    cout<<limit<<endl;
    ll s1 = sum1(limit);
    ll s2 = sum2(limit);
    ll s3 = sum3(limit);
    cout<<s1<<endl;
    cout<<s2<<endl;
    cout<<s3<<endl;
    cout<<s1+s2+s3<<endl;
    cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
}

//int main()
//{
//    uint64_t count = primesieve::count_primes(0, 1e11);
//    std::cout << "Primes below 1000 = " << count << std::endl;
//    
//    return 0;
//}

