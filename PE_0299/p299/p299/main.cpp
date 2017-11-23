//
//  main.cpp
//  p299
//
//  Created by Michael Hunt on 28/10/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#include <iostream>
using namespace std;

// Limit
#define limit 100000000
typedef long long int int64;

int64 gcd(int64 a, int64 b){
    int64 r = a % b;
    while (r>0){
        a=b;
        b=r;
        r=a%b;
    }
    return b;
}

int64 nonParallel(){
    int64 nonParallels=0;
    int64 b,d;
    for(int64 n=1; n<limit/2; n++){
        for(int64 m=1; m<n; m++){
            if(gcd(m,n) != 1) continue;
            if(m%2==n%2) continue;
            b = n*n-m*m;
            d = 2*m*n;
            if(b+d >= limit) break;
            nonParallels += 2*int(limit/(b+d));
        }
    }
    return nonParallels;
}

int64 parallel(){
    int64 parallels=0;
    int64 y,c;
    for(int64 n=1; n<limit; n+=2){
        for(int64 m=1; m<limit; m++){
            if(gcd(m,n) != 1) continue;
            y = 2*m*n;
            c=n*n+2*m*m;
            if(2*(y+c) > limit) break;
            parallels += int((limit-1)/(2*(y+c)));
        }
    }
    return parallels;
}

int main() {
    int64 np=nonParallel();
    cout<<np<<'\n';
    int64 p=parallel();
    cout<<p<<'\n';
    cout<<np+p<<'\n';
    return 0;
}
