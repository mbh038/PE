//
//  main.cpp
//  p540
//
//  Created by Michael Hunt on 20/11/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#include <iostream>
using namespace std;

// Limit
//#define limit 3141592653589793
//#define LSQ 56049912

#define limit 10000000000
#define LSQ 100000

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

//a^2 +b^2 =c^2
//c<limit
//need m and n  coprime, different parity
int64 primitiveTriples(){
    int64 valid=0;
    int64 c;
    for(int64 n=1; n<=LSQ; n++){
        for(int64 m=1; m<n; m++){
            if(gcd(m,n) != 1) continue;
            if(m%2==n%2) continue;
//            a = n*n-m*m;
//            b = 2*m*n;
            c = n*n+m*m;
            
            if(c > limit) break;
//            cout<<c<<'\n';
            valid += 1;
        }
    }
    return valid;
}

int main() {
    int64 np=primitiveTriples();
    cout<<np<<'\n';
    return 0;
}
