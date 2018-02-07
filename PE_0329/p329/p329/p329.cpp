//
//  main.cpp
//  p329
//
//  Created by Michael Hunt on 26/01/2018.
//  Copyright © 2018 Michael Hunt. All rights reserved.
//

//#include <boost/utility/binary.hpp>

#include <primesieve.hpp>
#include <vector>
#include <tuple>
#include <stdint.h>
#include <iostream>
#include <stdlib.h>
#include <bitset>
#include <iomanip>
#include <cmath>
#include <ctime>

using namespace std;
typedef long long ll;

int main() {
    
    vector<ll> ps;
    primesieve::generate_primes((ll)500, &ps);
//    for(int i=0;i<ps.size();i++){
//        cout<<ps[i]<<'\n';
//    }
    
    ll probs=0;
    vector<bool> croakseq;
    string croaks_required = "PPPPNNPPPNPPNPN";

    for(int i=0;i<croaks_required.size();i++){
        cout<<croaks_required[i]<<'\n';
    }
    
    ll count=0
    for(int start=1;start<=500;start++){
        for (ll seq=1;seq<=2**(croaks_required.size()-1);seq++){
            string binseq = bitset<14>(seq).to_string(); //to binary
            
            
        }
    }
        
        for seq in it.product([1,-1],repeat=croaks-1):
            positions=[start]+[0]*(croaks-1)
            count+=1
            
            for j in range(len(seq)):
                if positions[j]+seq[j]>squares:
                    positions[j+1]=squares-1
                    elif positions[j]+seq[j]<1:
                    positions[j+1]=2
                    else:
                        positions[j+1]=positions[j]+seq[j]
                        matches=sum([primes[positions[k]] == croakseq[k] for k in range(len(croakseq))])
                        probs+=2**matches

//    int x=0b1100;
//    cout<<"x: "<<x<<endl;
//
//    string binary = bitset<15>(42).to_string(); //to binary
//    cout<<binary<<"\n";
//    cout<<binary[0]<<"\n";
//    cout<<binary[1]<<"\n";
//    cout<<binary[2]<<"\n";
//
//
//    unsigned long decimal = bitset<15>(binary).to_ulong();
//    cout<<decimal<<"\n";

    return 0;
}
