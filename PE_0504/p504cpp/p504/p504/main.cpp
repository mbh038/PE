//
//  main.cpp
//  p504
//
//  Created by Michael Hunt on 18/04/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#include <iostream>
using namespace std;
#include <time.h>
#include <cmath>


int gcd(int a, int b){
    int r = a % b;
    while (r>0){
        a=b;
       int tmp=b;
        b=r;
        r=tmp%r;
    }
    return b;
}

int main() {
    
    clock_t t;
    t = clock();

    int m =100;
    int issq=0;
    
    for (int p=1;p<=m;p++) for (int q=1;q<=m;q++) for (int r=1;r<=m;r++) for (int s=1;s<=m;s++){
        float res=sqrt(((p+r)*(q+s)-gcd(p,q)-gcd(q,r)-gcd(r,s)-gcd(p,s))/2+1);
        if (res==int(res)) issq+=1;
    }
    
    cout << issq << "\n";
    cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
    return 0;
}
