//
//  main.cpp
//  p218
//
//  Created by Michael Hunt on 31/10/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#include <iostream>
using namespace std;

// Square root of limit
#define rLimit 100000000
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

int main()
{
    
    int64 count=0;
    for(int64 p=1; p<rLimit; p++){
        
        int64 p2=p*p;
        int64 p4=p2*p2;
        
        for(int64 q=1; q<p; q++){
            
            int64 q2=q*q;
            int64 r=p2+q2;
            
            if(r > rLimit)
                break;
            if(gcd(p,q) != 1)
                continue;
            if(p%2==q%2)
                continue;
            
            int64 q4=q2*q2;
            int64 a = abs(p4+q4-6*p2*q2);
            int64 b = abs(4*p*q*(p2-q2));
            
            if ((a%3==0 ||b%3==0) && (a%7==0 ||b%7==0))
                continue;
            
            count+=1;
        }
    }
    cout<<count<<'\n';
}
