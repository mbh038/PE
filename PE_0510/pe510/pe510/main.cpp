//
//  main.cpp
//  pe510
//
//  Created by Michael Hunt on 12/04/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#include<iostream>
using namespace std;
#include<time.h>
#include<cmath>
#include<tuple>
#include<vector>
#include "numberTheory.hpp"

void p510 (int64_t limit){
    clock_t t;
    t = clock();
    int64_t a,b,c,p,q;
    vector<tuple<int64_t, int64_t, int64_t>> abc;
    for (q=1;q<=floor(sqrt(limit));q++){
        for (p=1;p<=q;p++){
            if ((p*q)%(p+q)==0){
                a=p*p;
                b=q*q;
                c=floor(p*q/(p+q))*floor(p*q/(p+q));
                abc.push_back( tuple<int64_t, int64_t, int64_t>(a,b,c) );
            }
        }
    }
    
    vector<tuple<int64_t, int64_t, int64_t>> abcfund;
    for (int64_t i=0;i<abc.size();i++){
        int64_t div=longGcd(get<0>(abc[i]),longGcd(get<1>(abc[i]),get<2>(abc[i])));
        a=floor(get<0>(abc[i])/div);
        b=floor(get<1>(abc[i])/div);
        c=floor(get<2>(abc[i])/div);
        
        tuple<int64_t,int64_t,int64_t> next_abc;
        
        next_abc=make_tuple(a,b,c);
        
        if(find(abcfund.begin(), abcfund.end(), next_abc) == abcfund.end()) {
            abcfund.push_back( next_abc );
            }
        }
    //cout <<abcfund.size() << endl;
    
    int64_t S=0;
    int64_t L;
    
    for(int64_t k=0;k<abcfund.size();k++){
        int64_t aa=get<0>(abcfund[k]);
        int64_t bb=get<1>(abcfund[k]);
        int64_t cc=get<2>(abcfund[k]);
        L=(int64_t)floor((long double)(limit/bb));
        S +=(int64_t)floor((long double)(aa+bb+cc)*L*(L+1)/2.0);

    }
    cout << S << endl;
    cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<endl;

}

int main(){
    int64_t limit;
    cout << "Type limit : "<< endl;;
    cin >> limit;
    p510(limit);
    return 0;
 }
 

