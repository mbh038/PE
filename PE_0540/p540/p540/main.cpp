//
//  main.cpp
//  p540
//
//  Created by Michael Hunt on 20/11/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//
//// clang++ main.cpp -o p540 -lprimesieve -std=c++11

#include <iostream>
#include <cmath>
#include<vector>
#include <primesieve.hpp>
using namespace std;

#define N 3141592653589793

typedef long long int int64;

void moebius(int64 n, vector <int> &L){
    vector<int64 > ps;
    primesieve::generate_primes(n, &ps);
    
    for (int64 i=0;i<n;i++){
        L.push_back(1);
    }
    
    for (int i=0;i<ps.size();i++){
        for (int64 j=ps[i];j<L.size();j+=ps[i]){
            L[j]*=-1;
        }
        for (int64 j=ps[i]*ps[i];j<L.size();j+=ps[i]*ps[i]){
            L[j]=0;
        }
    }
}

int64 C_oe(int64 n){
    int64 c=0;
    for (int64 q=2;q*q<=n;q+=2){
        c+=int64(((pow(n-q*q,0.5))+1)/2);
    }
    return c;
}

int64 cntPPT(int64 n){
    
    vector <int> L;
    moebius(int64(pow(n,0.5))+1,L);
    int64 c = 0;
    int64 c5=0;
    for (int64 d = 1; d<=L.size(); d += 2){
        if (n/d/d<5) break;
        if (n/d/d==5){
            c5+=1;
            c+=L[d];
            continue;
        }
        if (L[d]==0) continue;
        int64 dc=L[d] * C_oe(n/d/d);
        c += dc;
//        cout<<dc<<'\n';;
    }
    cout<<"c5: "<<c5<<'\n';
    return c;
}

int main() {
    cout<<cntPPT(N)<<'\n';
}

/////////////////////////////////////////////////////////////////////////

int64 cAll(int64 n){
    int64 c = 0;
    for (int64 q = 1;q < pow(n/2,0.5); q++)
        c += int64(pow(n - q*q,0.5)) - q;
    return c;
}

int64 C_odd(int64 n){
    int64 c=0;
    for(int64 q=1;q<pow(n/2,0.5);q+=2){
        c += int64((pow(n - q*q,0.5)+1)/2) - (q+1)/2;
    }
    return c;
}
