//
//  main.cpp
//  p141
//
//  Created by Michael Hunt on 31/10/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#include <cmath>
#include <iostream>
using namespace std;

#define Limit 1000000000000
#define Limit3Root 10000
typedef long long int int64;

int64 gcd(int64 a, int64 b)
{
    int64 c = a % b;
    while(c != 0)
    {
        a = b;
        b = c;
        c = a % b;
    }
    return b;
}

int main() {

    int64 nsum=0;
    double precision=.1/sqrt(Limit);
    for (int64 a=1;a<=Limit3Root;a++){
        for(int64 b=1;b<a;b++){
            if (a*a*a*b+b >= Limit) break;
            if (gcd(a,b)!=1) continue;
            int64 c=1;
            for(c=1;;c++){
                int64 n=a*a*a*b*c*c+c*b*b;
                if (n>=Limit)
                    break;
                double nroot=sqrt(double(n));
                if (abs(nroot-int64(nroot))<precision){
                        nsum+=n;
                }
            }
        }
    }
                
    cout << nsum<<"\n";
    return 0;
}
            

