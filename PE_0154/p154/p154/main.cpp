//
//  main.cpp
//  p154
//
//  Created by Michael Hunt on 20/10/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#include <iostream>
using namespace std;
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <ctime>
#include "p154.h"



vector<long long> facpfac(long long n){
    vector<long long> factors;
    for(int prime=2;prime<=5;prime+=3){
        long long exp=0;
        long long power=1;
        long long delta=10;
        while(delta>0){
            delta=int(n/pow(prime,power));
            exp+=delta;
            power+=1;
        }
        factors.push_back(exp);
    }
    return factors;
}

long long p154(long long level, long long divisor){
    
    long long nsum=0;
    vector <long long> nfac;
    map <long long,long long> mults;
    map <long long, vector<long long>> facs;
    set<long long> pqrSet;
    
    nfac=facpfac(level);
    mults.insert(pair<long long,long long>(1,1));
    mults.insert(pair<long long,long long>(2,3));
    mults.insert(pair<long long,long long>(3,6));
    for (int x =0;x<=level;x++){
        facs.insert(pair<long long,vector<long long>>(x,facpfac(x)));
    }
    for (long long p=level;p>level/3;p--){
        for (long long q=level-p;q>=0;q--){
            if (q>p){
                continue;
            }
            long long r=level-p-q;
            if (r>q){
                break;
            }
            if(nfac[1]-facs.at(p)[1]-facs.at(q)[1]-facs.at(r)[1]<divisor){
                continue;
            }
            if(nfac[0]-facs.at(p)[0]-facs.at(q)[0]-facs.at(r)[0]<divisor){
                continue;
            }
//            if (p==q && p==r){
//                nsum+=1;
//                continue;
//            } else if(p==q || p==r || q==r){
//                nsum+=2;
//                continue;
//            } else {
//                nsum+=3;
//            }

            pqrSet.insert(p);
            pqrSet.insert(q);
            pqrSet.insert(r);
            nsum+=mults.at(int(pqrSet.size()));
            pqrSet.clear();
        }
    }
    return nsum;
}

int main(int argc, const char * argv[]) {
    
    struct timespec start, finish;
    double elapsed;
    
    clock_gettime(CLOCK_MONOTONIC, &start);
    
    long long level =200000;
    long long divisor = 12;
    long long nsum=p154(level,divisor);
    cout << nsum << "\n";

    clock_gettime(CLOCK_MONOTONIC, &finish);
    elapsed = (finish.tv_sec - start.tv_sec);
    elapsed += (finish.tv_nsec - start.tv_nsec) / 1000000000.0;
    
    //cout << facpfac(level)[0]<<","<<facpfac(level)[1]<<"\n";
    cout << elapsed << "\n";
    
    return 0;
}
